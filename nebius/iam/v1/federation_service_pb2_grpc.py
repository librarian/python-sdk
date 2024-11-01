# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius.common.v1 import operation_pb2 as nebius_dot_common_dot_v1_dot_operation__pb2
from nebius.iam.v1 import federation_pb2 as nebius_dot_iam_dot_v1_dot_federation__pb2
from nebius.iam.v1 import federation_service_pb2 as nebius_dot_iam_dot_v1_dot_federation__service__pb2


class FederationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/nebius.iam.v1.FederationService/Create',
                request_serializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.CreateFederationRequest.SerializeToString,
                response_deserializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
                )
        self.Get = channel.unary_unary(
                '/nebius.iam.v1.FederationService/Get',
                request_serializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.GetFederationRequest.SerializeToString,
                response_deserializer=nebius_dot_iam_dot_v1_dot_federation__pb2.Federation.FromString,
                )
        self.GetByName = channel.unary_unary(
                '/nebius.iam.v1.FederationService/GetByName',
                request_serializer=nebius_dot_common_dot_v1_dot_metadata__pb2.GetByNameRequest.SerializeToString,
                response_deserializer=nebius_dot_iam_dot_v1_dot_federation__pb2.Federation.FromString,
                )
        self.List = channel.unary_unary(
                '/nebius.iam.v1.FederationService/List',
                request_serializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.ListFederationsRequest.SerializeToString,
                response_deserializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.ListFederationsResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/nebius.iam.v1.FederationService/Update',
                request_serializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.UpdateFederationRequest.SerializeToString,
                response_deserializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/nebius.iam.v1.FederationService/Delete',
                request_serializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.DeleteFederationRequest.SerializeToString,
                response_deserializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
                )


class FederationServiceServicer(object):
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


def add_FederationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.CreateFederationRequest.FromString,
                    response_serializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.GetFederationRequest.FromString,
                    response_serializer=nebius_dot_iam_dot_v1_dot_federation__pb2.Federation.SerializeToString,
            ),
            'GetByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByName,
                    request_deserializer=nebius_dot_common_dot_v1_dot_metadata__pb2.GetByNameRequest.FromString,
                    response_serializer=nebius_dot_iam_dot_v1_dot_federation__pb2.Federation.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.ListFederationsRequest.FromString,
                    response_serializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.ListFederationsResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.UpdateFederationRequest.FromString,
                    response_serializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=nebius_dot_iam_dot_v1_dot_federation__service__pb2.DeleteFederationRequest.FromString,
                    response_serializer=nebius_dot_common_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nebius.iam.v1.FederationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FederationService(object):
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.FederationService/Create',
            nebius_dot_iam_dot_v1_dot_federation__service__pb2.CreateFederationRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.FederationService/Get',
            nebius_dot_iam_dot_v1_dot_federation__service__pb2.GetFederationRequest.SerializeToString,
            nebius_dot_iam_dot_v1_dot_federation__pb2.Federation.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.FederationService/GetByName',
            nebius_dot_common_dot_v1_dot_metadata__pb2.GetByNameRequest.SerializeToString,
            nebius_dot_iam_dot_v1_dot_federation__pb2.Federation.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.FederationService/List',
            nebius_dot_iam_dot_v1_dot_federation__service__pb2.ListFederationsRequest.SerializeToString,
            nebius_dot_iam_dot_v1_dot_federation__service__pb2.ListFederationsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.FederationService/Update',
            nebius_dot_iam_dot_v1_dot_federation__service__pb2.UpdateFederationRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.iam.v1.FederationService/Delete',
            nebius_dot_iam_dot_v1_dot_federation__service__pb2.DeleteFederationRequest.SerializeToString,
            nebius_dot_common_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)