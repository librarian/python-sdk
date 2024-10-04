# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nebius.common.v1 import operation_pb2 as nebius_dot_common_dot_v1_dot_operation__pb2
from nebius.iam.v1 import service_account_pb2 as nebius_dot_iam_dot_v1_dot_service__account__pb2
from nebius.iam.v1 import service_account_service_pb2 as nebius_dot_iam_dot_v1_dot_service__account__service__pb2


class ServiceAccountServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/nebius.iam.v1.ServiceAccountService/Create',
                request_serializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.SerializeToString,
                response_deserializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
                )
        self.Get = channel.unary_unary(
                '/nebius.iam.v1.ServiceAccountService/Get',
                request_serializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.GetServiceAccountRequest.SerializeToString,
                response_deserializer=nebius_dot_iam_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
                )
        self.GetByName = channel.unary_unary(
                '/nebius.iam.v1.ServiceAccountService/GetByName',
                request_serializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.GetServiceAccountByNameRequest.SerializeToString,
                response_deserializer=nebius_dot_iam_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
                )
        self.List = channel.unary_unary(
                '/nebius.iam.v1.ServiceAccountService/List',
                request_serializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountRequest.SerializeToString,
                response_deserializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/nebius.iam.v1.ServiceAccountService/Update',
                request_serializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountRequest.SerializeToString,
                response_deserializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/nebius.iam.v1.ServiceAccountService/Delete',
                request_serializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.SerializeToString,
                response_deserializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
                )


class ServiceAccountServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
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


def add_ServiceAccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.FromString,
                    response_serializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.GetServiceAccountRequest.FromString,
                    response_serializer=nebius_dot_iam_dot_v1_dot_service__account__pb2.ServiceAccount.SerializeToString,
            ),
            'GetByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByName,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.GetServiceAccountByNameRequest.FromString,
                    response_serializer=nebius_dot_iam_dot_v1_dot_service__account__pb2.ServiceAccount.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountRequest.FromString,
                    response_serializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountRequest.FromString,
                    response_serializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.FromString,
                    response_serializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nebius.iam.v1.ServiceAccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServiceAccountService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.ServiceAccountService/Create',
            nebius_dot_iam_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.SerializeToString,
            nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.ServiceAccountService/Get',
            nebius_dot_iam_dot_v1_dot_service__account__service__pb2.GetServiceAccountRequest.SerializeToString,
            nebius_dot_iam_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.ServiceAccountService/GetByName',
            nebius_dot_iam_dot_v1_dot_service__account__service__pb2.GetServiceAccountByNameRequest.SerializeToString,
            nebius_dot_iam_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.ServiceAccountService/List',
            nebius_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountRequest.SerializeToString,
            nebius_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.ServiceAccountService/Update',
            nebius_dot_iam_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountRequest.SerializeToString,
            nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.ServiceAccountService/Delete',
            nebius_dot_iam_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.SerializeToString,
            nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)