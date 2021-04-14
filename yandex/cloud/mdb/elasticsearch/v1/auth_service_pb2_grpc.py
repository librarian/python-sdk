# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.mdb.elasticsearch.v1 import auth_pb2 as yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2
from yandex.cloud.mdb.elasticsearch.v1 import auth_service_pb2 as yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class AuthServiceStub(object):
    """A set of methods for managing Elasticsearch Authentication resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListProviders = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.AuthService/ListProviders',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.ListAuthProvidersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.ListAuthProvidersResponse.FromString,
                )
        self.GetProvider = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.AuthService/GetProvider',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.GetAuthProviderRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2.AuthProvider.FromString,
                )
        self.AddProviders = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.AuthService/AddProviders',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.AddAuthProvidersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateProviders = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.AuthService/UpdateProviders',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.UpdateAuthProvidersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteProviders = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.AuthService/DeleteProviders',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.DeleteAuthProvidersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateProvider = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.AuthService/UpdateProvider',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.UpdateAuthProviderRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteProvider = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.AuthService/DeleteProvider',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.DeleteAuthProviderRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class AuthServiceServicer(object):
    """A set of methods for managing Elasticsearch Authentication resources.
    """

    def ListProviders(self, request, context):
        """Retrieves the list of registered auth providers for Elasticsearch cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProvider(self, request, context):
        """Returns registered auth provider by name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddProviders(self, request, context):
        """Adds new auth providers to Elasticsearch cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProviders(self, request, context):
        """Replase the list of auth providers.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProviders(self, request, context):
        """Removes auth providers from Elasticsearch cluster by name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProvider(self, request, context):
        """Updates registered auth provider.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProvider(self, request, context):
        """Removes auth provider from Elasticsearch cluster by name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProviders,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.ListAuthProvidersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.ListAuthProvidersResponse.SerializeToString,
            ),
            'GetProvider': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProvider,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.GetAuthProviderRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2.AuthProvider.SerializeToString,
            ),
            'AddProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.AddProviders,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.AddAuthProvidersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProviders,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.UpdateAuthProvidersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProviders,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.DeleteAuthProvidersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateProvider': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProvider,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.UpdateAuthProviderRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteProvider': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProvider,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.DeleteAuthProviderRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.elasticsearch.v1.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """A set of methods for managing Elasticsearch Authentication resources.
    """

    @staticmethod
    def ListProviders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.AuthService/ListProviders',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.ListAuthProvidersRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.ListAuthProvidersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProvider(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.AuthService/GetProvider',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.GetAuthProviderRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2.AuthProvider.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddProviders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.AuthService/AddProviders',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.AddAuthProvidersRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProviders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.AuthService/UpdateProviders',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.UpdateAuthProvidersRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProviders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.AuthService/DeleteProviders',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.DeleteAuthProvidersRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProvider(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.AuthService/UpdateProvider',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.UpdateAuthProviderRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProvider(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.AuthService/DeleteProvider',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__service__pb2.DeleteAuthProviderRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)