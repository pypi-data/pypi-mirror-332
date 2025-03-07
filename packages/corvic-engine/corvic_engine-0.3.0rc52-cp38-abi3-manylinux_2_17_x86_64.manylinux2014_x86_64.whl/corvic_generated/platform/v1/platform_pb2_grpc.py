# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from corvic_generated.platform.v1 import platform_pb2 as corvic_dot_platform_dot_v1_dot_platform__pb2


class OrgServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOrg = channel.unary_unary(
                '/corvic.platform.v1.OrgService/GetOrg',
                request_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgRequest.SerializeToString,
                response_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgResponse.FromString,
                )
        self.CreateOrg = channel.unary_unary(
                '/corvic.platform.v1.OrgService/CreateOrg',
                request_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.CreateOrgRequest.SerializeToString,
                response_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.CreateOrgResponse.FromString,
                )
        self.ListOrgs = channel.unary_unary(
                '/corvic.platform.v1.OrgService/ListOrgs',
                request_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgsRequest.SerializeToString,
                response_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgsResponse.FromString,
                )
        self.GetOrgUser = channel.unary_unary(
                '/corvic.platform.v1.OrgService/GetOrgUser',
                request_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgUserRequest.SerializeToString,
                response_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgUserResponse.FromString,
                )
        self.AddOrgUser = channel.unary_unary(
                '/corvic.platform.v1.OrgService/AddOrgUser',
                request_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.AddOrgUserRequest.SerializeToString,
                response_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.AddOrgUserResponse.FromString,
                )
        self.ListOrgUsers = channel.unary_unary(
                '/corvic.platform.v1.OrgService/ListOrgUsers',
                request_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgUsersRequest.SerializeToString,
                response_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgUsersResponse.FromString,
                )
        self.DeactivateOrgUser = channel.unary_unary(
                '/corvic.platform.v1.OrgService/DeactivateOrgUser',
                request_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateOrgUserRequest.SerializeToString,
                response_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateOrgUserResponse.FromString,
                )
        self.PurgeOrg = channel.unary_unary(
                '/corvic.platform.v1.OrgService/PurgeOrg',
                request_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.PurgeOrgRequest.SerializeToString,
                response_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.PurgeOrgResponse.FromString,
                )
        self.DeactivateAllOrgUsers = channel.unary_unary(
                '/corvic.platform.v1.OrgService/DeactivateAllOrgUsers',
                request_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateAllOrgUsersRequest.SerializeToString,
                response_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateAllOrgUsersResponse.FromString,
                )


class OrgServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOrg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOrg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOrgs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrgUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddOrgUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOrgUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeactivateOrgUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PurgeOrg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeactivateAllOrgUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOrg': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrg,
                    request_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgRequest.FromString,
                    response_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgResponse.SerializeToString,
            ),
            'CreateOrg': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrg,
                    request_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.CreateOrgRequest.FromString,
                    response_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.CreateOrgResponse.SerializeToString,
            ),
            'ListOrgs': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOrgs,
                    request_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgsRequest.FromString,
                    response_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgsResponse.SerializeToString,
            ),
            'GetOrgUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrgUser,
                    request_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgUserRequest.FromString,
                    response_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgUserResponse.SerializeToString,
            ),
            'AddOrgUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddOrgUser,
                    request_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.AddOrgUserRequest.FromString,
                    response_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.AddOrgUserResponse.SerializeToString,
            ),
            'ListOrgUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOrgUsers,
                    request_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgUsersRequest.FromString,
                    response_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgUsersResponse.SerializeToString,
            ),
            'DeactivateOrgUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeactivateOrgUser,
                    request_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateOrgUserRequest.FromString,
                    response_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateOrgUserResponse.SerializeToString,
            ),
            'PurgeOrg': grpc.unary_unary_rpc_method_handler(
                    servicer.PurgeOrg,
                    request_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.PurgeOrgRequest.FromString,
                    response_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.PurgeOrgResponse.SerializeToString,
            ),
            'DeactivateAllOrgUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.DeactivateAllOrgUsers,
                    request_deserializer=corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateAllOrgUsersRequest.FromString,
                    response_serializer=corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateAllOrgUsersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'corvic.platform.v1.OrgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrgService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOrg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.platform.v1.OrgService/GetOrg',
            corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgRequest.SerializeToString,
            corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateOrg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.platform.v1.OrgService/CreateOrg',
            corvic_dot_platform_dot_v1_dot_platform__pb2.CreateOrgRequest.SerializeToString,
            corvic_dot_platform_dot_v1_dot_platform__pb2.CreateOrgResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOrgs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.platform.v1.OrgService/ListOrgs',
            corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgsRequest.SerializeToString,
            corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrgUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.platform.v1.OrgService/GetOrgUser',
            corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgUserRequest.SerializeToString,
            corvic_dot_platform_dot_v1_dot_platform__pb2.GetOrgUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddOrgUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.platform.v1.OrgService/AddOrgUser',
            corvic_dot_platform_dot_v1_dot_platform__pb2.AddOrgUserRequest.SerializeToString,
            corvic_dot_platform_dot_v1_dot_platform__pb2.AddOrgUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOrgUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.platform.v1.OrgService/ListOrgUsers',
            corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgUsersRequest.SerializeToString,
            corvic_dot_platform_dot_v1_dot_platform__pb2.ListOrgUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeactivateOrgUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.platform.v1.OrgService/DeactivateOrgUser',
            corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateOrgUserRequest.SerializeToString,
            corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateOrgUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PurgeOrg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.platform.v1.OrgService/PurgeOrg',
            corvic_dot_platform_dot_v1_dot_platform__pb2.PurgeOrgRequest.SerializeToString,
            corvic_dot_platform_dot_v1_dot_platform__pb2.PurgeOrgResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeactivateAllOrgUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.platform.v1.OrgService/DeactivateAllOrgUsers',
            corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateAllOrgUsersRequest.SerializeToString,
            corvic_dot_platform_dot_v1_dot_platform__pb2.DeactivateAllOrgUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
