# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.serverless.containers.v1 import container_pb2 as yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__pb2
from yandex.cloud.serverless.containers.v1 import container_service_pb2 as yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2


class ContainerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/Get',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.GetContainerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__pb2.Container.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/List',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/Create',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.CreateContainerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/Update',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.UpdateContainerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/Delete',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.DeleteContainerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeployRevision = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/DeployRevision',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.DeployContainerRevisionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Rollback = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/Rollback',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.RollbackContainerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetRevision = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/GetRevision',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.GetContainerRevisionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__pb2.Revision.FromString,
                )
        self.ListRevisions = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/ListRevisions',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersRevisionsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersRevisionsResponse.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainerOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainerOperationsResponse.FromString,
                )
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                )
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.serverless.containers.v1.ContainerService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ContainerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeployRevision(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Rollback(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRevision(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRevisions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContainerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.GetContainerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__pb2.Container.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.CreateContainerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.UpdateContainerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.DeleteContainerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeployRevision': grpc.unary_unary_rpc_method_handler(
                    servicer.DeployRevision,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.DeployContainerRevisionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Rollback': grpc.unary_unary_rpc_method_handler(
                    servicer.Rollback,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.RollbackContainerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetRevision': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRevision,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.GetContainerRevisionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__pb2.Revision.SerializeToString,
            ),
            'ListRevisions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRevisions,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersRevisionsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersRevisionsResponse.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainerOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainerOperationsResponse.SerializeToString,
            ),
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
            'SetAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.serverless.containers.v1.ContainerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ContainerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/Get',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.GetContainerRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__pb2.Container.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/List',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/Create',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.CreateContainerRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/Update',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.UpdateContainerRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/Delete',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.DeleteContainerRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeployRevision(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/DeployRevision',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.DeployContainerRevisionRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Rollback(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/Rollback',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.RollbackContainerRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRevision(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/GetRevision',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.GetContainerRevisionRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__pb2.Revision.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRevisions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/ListRevisions',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersRevisionsRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainersRevisionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/ListOperations',
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainerOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__service__pb2.ListContainerOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/ListAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/SetAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.containers.v1.ContainerService/UpdateAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
