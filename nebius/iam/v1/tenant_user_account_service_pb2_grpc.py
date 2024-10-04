# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nebius.common.v1 import operation_pb2 as nebius_dot_common_dot_v1_dot_operation__pb2
from nebius.iam.v1 import tenant_user_account_pb2 as nebius_dot_iam_dot_v1_dot_tenant__user__account__pb2
from nebius.iam.v1 import tenant_user_account_service_pb2 as nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2


class TenantUserAccountServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/nebius.iam.v1.TenantUserAccountService/Get',
                request_serializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.GetTenantUserAccountRequest.SerializeToString,
                response_deserializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__pb2.TenantUserAccount.FromString,
                )
        self.List = channel.unary_unary(
                '/nebius.iam.v1.TenantUserAccountService/List',
                request_serializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.ListTenantUserAccountsRequest.SerializeToString,
                response_deserializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.ListTenantUserAccountsResponse.FromString,
                )
        self.Block = channel.unary_unary(
                '/nebius.iam.v1.TenantUserAccountService/Block',
                request_serializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.BlockTenantUserAccountRequest.SerializeToString,
                response_deserializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
                )
        self.Unblock = channel.unary_unary(
                '/nebius.iam.v1.TenantUserAccountService/Unblock',
                request_serializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.UnblockTenantUserAccountRequest.SerializeToString,
                response_deserializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
                )


class TenantUserAccountServiceServicer(object):
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

    def Block(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unblock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TenantUserAccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.GetTenantUserAccountRequest.FromString,
                    response_serializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__pb2.TenantUserAccount.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.ListTenantUserAccountsRequest.FromString,
                    response_serializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.ListTenantUserAccountsResponse.SerializeToString,
            ),
            'Block': grpc.unary_unary_rpc_method_handler(
                    servicer.Block,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.BlockTenantUserAccountRequest.FromString,
                    response_serializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Unblock': grpc.unary_unary_rpc_method_handler(
                    servicer.Unblock,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.UnblockTenantUserAccountRequest.FromString,
                    response_serializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nebius.iam.v1.TenantUserAccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TenantUserAccountService(object):
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.TenantUserAccountService/Get',
            nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.GetTenantUserAccountRequest.SerializeToString,
            nebius_dot_iam_dot_v1_dot_tenant__user__account__pb2.TenantUserAccount.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.TenantUserAccountService/List',
            nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.ListTenantUserAccountsRequest.SerializeToString,
            nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.ListTenantUserAccountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Block(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.TenantUserAccountService/Block',
            nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.BlockTenantUserAccountRequest.SerializeToString,
            nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unblock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.TenantUserAccountService/Unblock',
            nebius_dot_iam_dot_v1_dot_tenant__user__account__service__pb2.UnblockTenantUserAccountRequest.SerializeToString,
            nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
