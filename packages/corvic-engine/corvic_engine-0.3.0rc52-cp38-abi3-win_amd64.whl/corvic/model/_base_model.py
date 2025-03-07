import abc
import contextlib
import copy
import datetime
import functools
import uuid
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Final, Generic, Protocol, TypeVar

import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
import structlog
from google.protobuf import timestamp_pb2
from typing_extensions import Self

from corvic import orm, system
from corvic.model._proto_orm_convert import ID, UNCOMMITTED_ID_PREFIX, OrmObj
from corvic.result import InvalidArgumentError, NotFoundError, Ok

_logger = structlog.get_logger()


class _ModelProto(Protocol):
    id: str
    created_at: timestamp_pb2.Timestamp


_ProtoObj = TypeVar("_ProtoObj", bound=_ModelProto)


def _generate_uncommitted_id_str():
    return f"{UNCOMMITTED_ID_PREFIX}{uuid.uuid4()}"


@contextlib.contextmanager
def _create_or_join_session(
    client: system.Client, existing_session: sa_orm.Session | None
) -> Iterator[sa_orm.Session]:
    if existing_session:
        yield existing_session
    else:
        with orm.Session(client.sa_engine) as session:
            yield session


class HasProtoSelf(Generic[_ProtoObj], abc.ABC):
    client: Final[system.Client]
    proto_self: Final[_ProtoObj]

    def __init__(self, client: system.Client, proto_self: _ProtoObj):
        self.proto_self = proto_self
        self.client = client

    @property
    def created_at(self) -> datetime.datetime | None:
        if self.proto_self.created_at:
            return self.proto_self.created_at.ToDatetime(tzinfo=datetime.timezone.utc)
        return None


class UsesOrmID(Generic[ID, _ProtoObj], HasProtoSelf[_ProtoObj]):
    def __init__(self, client: system.Client, proto_self: _ProtoObj):
        if not proto_self.id:
            proto_self.id = _generate_uncommitted_id_str()
        super().__init__(client, proto_self)

    @classmethod
    @abc.abstractmethod
    def id_class(cls) -> type[ID]: ...

    @functools.cached_property
    def id(self) -> ID:
        return self.id_class().from_str(self.proto_self.id)


class BaseModel(Generic[ID, _ProtoObj, OrmObj], UsesOrmID[ID, _ProtoObj]):
    """Base for orm wrappers providing a unified update mechanism."""

    @classmethod
    @abc.abstractmethod
    def orm_class(cls) -> type[OrmObj]: ...

    @classmethod
    @abc.abstractmethod
    def orm_to_proto(cls, orm_obj: OrmObj) -> _ProtoObj: ...

    @classmethod
    @abc.abstractmethod
    def proto_to_orm(
        cls, proto_obj: _ProtoObj, session: orm.Session
    ) -> Ok[OrmObj] | InvalidArgumentError: ...

    @classmethod
    @abc.abstractmethod
    def delete_by_ids(
        cls, ids: Sequence[ID], session: orm.Session
    ) -> Ok[None] | InvalidArgumentError: ...

    @classmethod
    def load_proto_for(
        cls,
        obj_id: ID,
        client: system.Client,
        existing_session: sa_orm.Session | None = None,
    ) -> Ok[_ProtoObj] | NotFoundError:
        """Create a model object by loading it from the database."""
        with _create_or_join_session(client, existing_session) as session:
            orm_self = session.get(cls.orm_class(), obj_id)
            if orm_self is None:
                return NotFoundError("object with given id does not exist", id=obj_id)
            proto_self = cls.orm_to_proto(orm_self)
        return Ok(proto_self)

    @classmethod
    def _generate_query_results(
        cls, query: sa.Select[tuple[OrmObj]], session: sa_orm.Session
    ) -> Iterator[OrmObj]:
        it = iter(session.scalars(query))
        while True:
            try:
                yield from it
            except Exception:  # noqa: PERF203
                _logger.exception(
                    "omitting source from list: "
                    + "failed to parse source from database entry",
                )
            else:
                break

    @classmethod
    def orm_load_options(cls) -> list[sa_orm.interfaces.LoaderOption]:
        """Overridable method to pass extra orm specific transformations."""
        return []

    @classmethod
    def list_as_proto(
        cls,
        client: system.Client,
        *,
        limit: int | None = None,
        room_id: orm.RoomID | None = None,
        created_before: datetime.datetime | None = None,
        ids: Iterable[ID] | None = None,
        additional_query_transform: Callable[
            [sa.Select[tuple[OrmObj]]], sa.Select[tuple[OrmObj]]
        ]
        | None = None,
        existing_session: sa_orm.Session | None = None,
    ) -> Ok[list[_ProtoObj]] | NotFoundError | InvalidArgumentError:
        """List sources that exist in storage."""
        orm_class = cls.orm_class()
        with _create_or_join_session(client, existing_session) as session:
            query = sa.select(orm_class).order_by(sa.desc(orm_class.created_at))
            if limit is not None:
                if limit < 0:
                    return InvalidArgumentError("limit cannot be negative")
                query = query.limit(limit)
            if room_id:
                if session.get(orm.Room, room_id) is None:
                    return NotFoundError("room not found", room_id=room_id)
                query = query.filter_by(room_id=room_id)
            if created_before:
                query = query.filter(orm_class.created_at < created_before)
            if ids:
                query = query.filter(orm_class.id.in_(ids))
            if additional_query_transform:
                query = additional_query_transform(query)
            extra_orm_loaders = cls.orm_load_options()
            if extra_orm_loaders:
                query = query.options(*extra_orm_loaders)
            return Ok(
                [
                    cls.orm_to_proto(val)
                    for val in cls._generate_query_results(query, session)
                ]
            )

    def commit(self) -> Ok[Self] | InvalidArgumentError:
        """Store this object in the database at its id or a newly allocated id.

        This overwrites the entry at id in the database so that future readers will see
        this object. One of `id` or `derived_from_id` cannot be empty or None.
        """
        with orm.Session(self.client.sa_engine) as session:
            try:
                new_orm_self = self.proto_to_orm(
                    self.proto_self, session
                ).unwrap_or_raise()
                session.commit()
            except sa.exc.DatabaseError as err:
                return InvalidArgumentError.from_(err)
            return Ok(
                self.__class__(
                    client=self.client,
                    proto_self=self.orm_to_proto(new_orm_self),
                )
            )

    def add_to_session(self, session: orm.Session) -> Ok[None] | InvalidArgumentError:
        """Like commit, but just calls session.flush to check for database errors.

        This adds the updated object to a transaction in session. Unlike commit
        this will not return the updated object because some values may not be known
        until the wrapped transaction commits.
        """
        try:
            _ = self.proto_to_orm(self.proto_self, session).unwrap_or_raise()
            session.flush()
        # TODO(thunt): Possibly separate out DatabaseError into a precondition error
        except (sa.exc.DatabaseError, sa.exc.StatementError) as err:
            return InvalidArgumentError.from_(err)
        return Ok(None)

    def delete(self) -> Ok[Self] | NotFoundError | InvalidArgumentError:
        with orm.Session(
            self.client.sa_engine, expire_on_commit=False, autoflush=False
        ) as session:
            match self.delete_by_ids([self.id], session):
                case InvalidArgumentError() as err:
                    return err
                case Ok(None):
                    pass
            session.commit()

            new_proto_self = copy.copy(self.proto_self)
            new_proto_self.id = ""

            return Ok(
                self.__class__(
                    client=self.client,
                    proto_self=new_proto_self,
                )
            )
