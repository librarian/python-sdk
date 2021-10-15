# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.vpc.v1 import subnet_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__pb2
from yandex.cloud.vpc.v1 import subnet_service_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2


class SubnetServiceStub(object):
    """A set of methods for managing Subnet resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/Get',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/List',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/Create',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.CreateSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/Update',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.UpdateSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.AddCidrBlocks = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/AddCidrBlocks',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.AddSubnetCidrBlocksRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.RemoveCidrBlocks = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/RemoveCidrBlocks',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.RemoveSubnetCidrBlocksRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/Delete',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.DeleteSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsResponse.FromString,
                )
        self.Move = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/Move',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.MoveSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListUsedAddresses = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SubnetService/ListUsedAddresses',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListUsedAddressesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListUsedAddressesResponse.FromString,
                )


class SubnetServiceServicer(object):
    """A set of methods for managing Subnet resources.
    """

    def Get(self, request, context):
        """Returns the specified Subnet resource.

        To get the list of available Subnet resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Subnet resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a subnet in the specified folder and network.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified subnet.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCidrBlocks(self, request, context):
        """Adds CIDR blocks to the specified subnet.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveCidrBlocks(self, request, context):
        """Removes CIDR blocks from the specified subnet.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified subnet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """List operations for the specified subnet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Move(self, request, context):
        """Move subnet to another folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsedAddresses(self, request, context):
        """List used addresses in specified subnet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubnetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.CreateSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.UpdateSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'AddCidrBlocks': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCidrBlocks,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.AddSubnetCidrBlocksRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'RemoveCidrBlocks': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveCidrBlocks,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.RemoveSubnetCidrBlocksRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.DeleteSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsResponse.SerializeToString,
            ),
            'Move': grpc.unary_unary_rpc_method_handler(
                    servicer.Move,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.MoveSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListUsedAddresses': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsedAddresses,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListUsedAddressesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListUsedAddressesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.vpc.v1.SubnetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SubnetService(object):
    """A set of methods for managing Subnet resources.
    """

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/Get',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/List',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/Create',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.CreateSubnetRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/Update',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.UpdateSubnetRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCidrBlocks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/AddCidrBlocks',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.AddSubnetCidrBlocksRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveCidrBlocks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/RemoveCidrBlocks',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.RemoveSubnetCidrBlocksRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/Delete',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.DeleteSubnetRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/ListOperations',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Move(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/Move',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.MoveSubnetRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsedAddresses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.vpc.v1.SubnetService/ListUsedAddresses',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListUsedAddressesRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListUsedAddressesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
