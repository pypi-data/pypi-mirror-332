# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from corvic_generated.ingest.v2 import resource_pb2 as corvic_dot_ingest_dot_v2_dot_resource__pb2


class ResourceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUploadURL = channel.unary_unary(
                '/corvic.ingest.v2.ResourceService/CreateUploadURL',
                request_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateUploadURLRequest.SerializeToString,
                response_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateUploadURLResponse.FromString,
                )
        self.FinalizeUploadURL = channel.unary_unary(
                '/corvic.ingest.v2.ResourceService/FinalizeUploadURL',
                request_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.FinalizeUploadURLRequest.SerializeToString,
                response_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.FinalizeUploadURLResponse.FromString,
                )
        self.DeleteResource = channel.unary_unary(
                '/corvic.ingest.v2.ResourceService/DeleteResource',
                request_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.DeleteResourceRequest.SerializeToString,
                response_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.DeleteResourceResponse.FromString,
                )
        self.GetResource = channel.unary_unary(
                '/corvic.ingest.v2.ResourceService/GetResource',
                request_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.GetResourceRequest.SerializeToString,
                response_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.GetResourceResponse.FromString,
                )
        self.ListResources = channel.unary_stream(
                '/corvic.ingest.v2.ResourceService/ListResources',
                request_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesRequest.SerializeToString,
                response_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesResponse.FromString,
                )
        self.ListResourcesPaginated = channel.unary_unary(
                '/corvic.ingest.v2.ResourceService/ListResourcesPaginated',
                request_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesPaginatedRequest.SerializeToString,
                response_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesPaginatedResponse.FromString,
                )
        self.WatchResources = channel.unary_stream(
                '/corvic.ingest.v2.ResourceService/WatchResources',
                request_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.WatchResourcesRequest.SerializeToString,
                response_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.WatchResourcesResponse.FromString,
                )
        self.CreateResourceDownloadURL = channel.unary_unary(
                '/corvic.ingest.v2.ResourceService/CreateResourceDownloadURL',
                request_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateResourceDownloadURLRequest.SerializeToString,
                response_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateResourceDownloadURLResponse.FromString,
                )


class ResourceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUploadURL(self, request, context):
        """CreateUploadURL returns a limited-time duration URL that can be used to upload
        a resource to a room.
        
        Callers should perform a PUT request on the returned URL to upload data and then
        call FinalizeUploadURL.
        
        This is an alternative to UploadResource when uploads are large as clients
        directly write to the bucket room location.
        
        For more details on how to use the returned URL:
        https://cloud.google.com/storage/docs/performing-resumable-uploads
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinalizeUploadURL(self, request, context):
        """FinalizeUploadURL completes an upload created with CreateUploadURL.
        
        Callers should perform a PUT request on the returned URL to complete the
        upload.
        
        This is an alternative to UploadResource when uploads are large as clients
        directly write to the bucket room location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteResource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetResource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListResources(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListResourcesPaginated(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchResources(self, request, context):
        """Open a stream that notifies the caller about changes to the resources.
        
        This is useful for detecting changes to a resources digest status. Callers
        may continue to watch this stream to be notified about updated resources.
        
        The current status of all matching resources is always returned first
        regardless of how recently they were updated.
        
        Similar to ListResources with the difference being that ListResources terminates
        after resporting each requested resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateResourceDownloadURL(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResourceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUploadURL': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUploadURL,
                    request_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateUploadURLRequest.FromString,
                    response_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateUploadURLResponse.SerializeToString,
            ),
            'FinalizeUploadURL': grpc.unary_unary_rpc_method_handler(
                    servicer.FinalizeUploadURL,
                    request_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.FinalizeUploadURLRequest.FromString,
                    response_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.FinalizeUploadURLResponse.SerializeToString,
            ),
            'DeleteResource': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteResource,
                    request_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.DeleteResourceRequest.FromString,
                    response_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.DeleteResourceResponse.SerializeToString,
            ),
            'GetResource': grpc.unary_unary_rpc_method_handler(
                    servicer.GetResource,
                    request_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.GetResourceRequest.FromString,
                    response_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.GetResourceResponse.SerializeToString,
            ),
            'ListResources': grpc.unary_stream_rpc_method_handler(
                    servicer.ListResources,
                    request_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesRequest.FromString,
                    response_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesResponse.SerializeToString,
            ),
            'ListResourcesPaginated': grpc.unary_unary_rpc_method_handler(
                    servicer.ListResourcesPaginated,
                    request_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesPaginatedRequest.FromString,
                    response_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesPaginatedResponse.SerializeToString,
            ),
            'WatchResources': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchResources,
                    request_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.WatchResourcesRequest.FromString,
                    response_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.WatchResourcesResponse.SerializeToString,
            ),
            'CreateResourceDownloadURL': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateResourceDownloadURL,
                    request_deserializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateResourceDownloadURLRequest.FromString,
                    response_serializer=corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateResourceDownloadURLResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'corvic.ingest.v2.ResourceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ResourceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUploadURL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.ingest.v2.ResourceService/CreateUploadURL',
            corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateUploadURLRequest.SerializeToString,
            corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateUploadURLResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinalizeUploadURL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.ingest.v2.ResourceService/FinalizeUploadURL',
            corvic_dot_ingest_dot_v2_dot_resource__pb2.FinalizeUploadURLRequest.SerializeToString,
            corvic_dot_ingest_dot_v2_dot_resource__pb2.FinalizeUploadURLResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.ingest.v2.ResourceService/DeleteResource',
            corvic_dot_ingest_dot_v2_dot_resource__pb2.DeleteResourceRequest.SerializeToString,
            corvic_dot_ingest_dot_v2_dot_resource__pb2.DeleteResourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.ingest.v2.ResourceService/GetResource',
            corvic_dot_ingest_dot_v2_dot_resource__pb2.GetResourceRequest.SerializeToString,
            corvic_dot_ingest_dot_v2_dot_resource__pb2.GetResourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/corvic.ingest.v2.ResourceService/ListResources',
            corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesRequest.SerializeToString,
            corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListResourcesPaginated(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.ingest.v2.ResourceService/ListResourcesPaginated',
            corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesPaginatedRequest.SerializeToString,
            corvic_dot_ingest_dot_v2_dot_resource__pb2.ListResourcesPaginatedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WatchResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/corvic.ingest.v2.ResourceService/WatchResources',
            corvic_dot_ingest_dot_v2_dot_resource__pb2.WatchResourcesRequest.SerializeToString,
            corvic_dot_ingest_dot_v2_dot_resource__pb2.WatchResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateResourceDownloadURL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/corvic.ingest.v2.ResourceService/CreateResourceDownloadURL',
            corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateResourceDownloadURLRequest.SerializeToString,
            corvic_dot_ingest_dot_v2_dot_resource__pb2.CreateResourceDownloadURLResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
