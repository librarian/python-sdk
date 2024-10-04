# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nebius.vpc.v1 import subnet_pb2 as nebius_dot_vpc_dot_v1_dot_subnet__pb2
from nebius.vpc.v1 import subnet_service_pb2 as nebius_dot_vpc_dot_v1_dot_subnet__service__pb2


class SubnetServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/nebius.vpc.v1.SubnetService/Get',
                request_serializer=nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetRequest.SerializeToString,
                response_deserializer=nebius_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.FromString,
                )
        self.GetByName = channel.unary_unary(
                '/nebius.vpc.v1.SubnetService/GetByName',
                request_serializer=nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetByNameRequest.SerializeToString,
                response_deserializer=nebius_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.FromString,
                )
        self.List = channel.unary_unary(
                '/nebius.vpc.v1.SubnetService/List',
                request_serializer=nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsRequest.SerializeToString,
                response_deserializer=nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsResponse.FromString,
                )


class SubnetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

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


def add_SubnetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetRequest.FromString,
                    response_serializer=nebius_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.SerializeToString,
            ),
            'GetByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByName,
                    request_deserializer=nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetByNameRequest.FromString,
                    response_serializer=nebius_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsRequest.FromString,
                    response_serializer=nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nebius.vpc.v1.SubnetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SubnetService(object):
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
        return grpc.experimental.unary_unary(request, target, '/nebius.vpc.v1.SubnetService/Get',
            nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetRequest.SerializeToString,
            nebius_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.vpc.v1.SubnetService/GetByName',
            nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetByNameRequest.SerializeToString,
            nebius_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nebius.vpc.v1.SubnetService/List',
            nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsRequest.SerializeToString,
            nebius_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)