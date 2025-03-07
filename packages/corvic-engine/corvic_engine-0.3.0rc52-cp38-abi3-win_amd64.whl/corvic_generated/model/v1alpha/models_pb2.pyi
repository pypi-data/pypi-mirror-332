from corvic_generated.orm.v1 import agent_pb2 as _agent_pb2
from corvic_generated.orm.v1 import completion_model_pb2 as _completion_model_pb2
from corvic_generated.orm.v1 import feature_view_pb2 as _feature_view_pb2
from corvic_generated.orm.v1 import pipeline_pb2 as _pipeline_pb2
from corvic_generated.orm.v1 import space_pb2 as _space_pb2
from corvic_generated.orm.v1 import table_pb2 as _table_pb2
from corvic_generated.status.v1 import event_pb2 as _event_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Room(_message.Message):
    __slots__ = ("id", "name", "org_id", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    org_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., org_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Resource(_message.Message):
    __slots__ = ("id", "name", "description", "mime_type", "url", "size", "md5", "original_path", "room_id", "org_id", "pipeline_id", "recent_events", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_PATH_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    RECENT_EVENTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    mime_type: str
    url: str
    size: int
    md5: str
    original_path: str
    room_id: str
    org_id: str
    pipeline_id: str
    recent_events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., mime_type: _Optional[str] = ..., url: _Optional[str] = ..., size: _Optional[int] = ..., md5: _Optional[str] = ..., original_path: _Optional[str] = ..., room_id: _Optional[str] = ..., org_id: _Optional[str] = ..., pipeline_id: _Optional[str] = ..., recent_events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ("id", "name", "table_op_graph", "room_id", "org_id", "pipeline_id", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_OP_GRAPH_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    table_op_graph: _table_pb2.TableComputeOp
    room_id: str
    org_id: str
    pipeline_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., table_op_graph: _Optional[_Union[_table_pb2.TableComputeOp, _Mapping]] = ..., room_id: _Optional[str] = ..., org_id: _Optional[str] = ..., pipeline_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Pipeline(_message.Message):
    __slots__ = ("id", "name", "description", "room_id", "resource_inputs", "source_outputs", "pipeline_transformation", "org_id", "created_at")
    class ResourceInputsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Resource
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Resource, _Mapping]] = ...) -> None: ...
    class SourceOutputsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Source
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Source, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_INPUTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_TRANSFORMATION_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    room_id: str
    resource_inputs: _containers.MessageMap[str, Resource]
    source_outputs: _containers.MessageMap[str, Source]
    pipeline_transformation: _pipeline_pb2.PipelineTransformation
    org_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., room_id: _Optional[str] = ..., resource_inputs: _Optional[_Mapping[str, Resource]] = ..., source_outputs: _Optional[_Mapping[str, Source]] = ..., pipeline_transformation: _Optional[_Union[_pipeline_pb2.PipelineTransformation, _Mapping]] = ..., org_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FeatureViewSource(_message.Message):
    __slots__ = ("id", "source", "table_op_graph", "drop_disconnected", "org_id", "created_at", "room_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TABLE_OP_GRAPH_FIELD_NUMBER: _ClassVar[int]
    DROP_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    source: Source
    table_op_graph: _table_pb2.TableComputeOp
    drop_disconnected: bool
    org_id: str
    created_at: _timestamp_pb2.Timestamp
    room_id: str
    def __init__(self, id: _Optional[str] = ..., source: _Optional[_Union[Source, _Mapping]] = ..., table_op_graph: _Optional[_Union[_table_pb2.TableComputeOp, _Mapping]] = ..., drop_disconnected: bool = ..., org_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., room_id: _Optional[str] = ...) -> None: ...

class FeatureView(_message.Message):
    __slots__ = ("id", "name", "description", "room_id", "feature_view_output", "feature_view_sources", "space_ids", "org_id", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_VIEW_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_VIEW_SOURCES_FIELD_NUMBER: _ClassVar[int]
    SPACE_IDS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    room_id: str
    feature_view_output: _feature_view_pb2.FeatureViewOutput
    feature_view_sources: _containers.RepeatedCompositeFieldContainer[FeatureViewSource]
    space_ids: _containers.RepeatedScalarFieldContainer[str]
    org_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., room_id: _Optional[str] = ..., feature_view_output: _Optional[_Union[_feature_view_pb2.FeatureViewOutput, _Mapping]] = ..., feature_view_sources: _Optional[_Iterable[_Union[FeatureViewSource, _Mapping]]] = ..., space_ids: _Optional[_Iterable[str]] = ..., org_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Space(_message.Message):
    __slots__ = ("id", "name", "description", "room_id", "space_parameters", "feature_view", "auto_sync", "org_id", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_VIEW_FIELD_NUMBER: _ClassVar[int]
    AUTO_SYNC_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    room_id: str
    space_parameters: _space_pb2.SpaceParameters
    feature_view: FeatureView
    auto_sync: bool
    org_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., room_id: _Optional[str] = ..., space_parameters: _Optional[_Union[_space_pb2.SpaceParameters, _Mapping]] = ..., feature_view: _Optional[_Union[FeatureView, _Mapping]] = ..., auto_sync: bool = ..., org_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Agent(_message.Message):
    __slots__ = ("id", "name", "room_id", "agent_parameters", "org_id", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    room_id: str
    agent_parameters: _agent_pb2.AgentParameters
    org_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., room_id: _Optional[str] = ..., agent_parameters: _Optional[_Union[_agent_pb2.AgentParameters, _Mapping]] = ..., org_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CompletionModel(_message.Message):
    __slots__ = ("id", "name", "description", "org_id", "parameters", "secret_api_key", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SECRET_API_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    org_id: str
    parameters: _completion_model_pb2.CompletionModelParameters
    secret_api_key: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., org_id: _Optional[str] = ..., parameters: _Optional[_Union[_completion_model_pb2.CompletionModelParameters, _Mapping]] = ..., secret_api_key: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
