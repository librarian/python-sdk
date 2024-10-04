"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import nebius.vpc.v1.subnet_pb2
import nebius.vpc.v1.subnet_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class SubnetServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        nebius.vpc.v1.subnet_service_pb2.GetSubnetRequest,
        nebius.vpc.v1.subnet_pb2.Subnet,
    ]

    GetByName: grpc.UnaryUnaryMultiCallable[
        nebius.vpc.v1.subnet_service_pb2.GetSubnetByNameRequest,
        nebius.vpc.v1.subnet_pb2.Subnet,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        nebius.vpc.v1.subnet_service_pb2.ListSubnetsRequest,
        nebius.vpc.v1.subnet_service_pb2.ListSubnetsResponse,
    ]

class SubnetServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.vpc.v1.subnet_service_pb2.GetSubnetRequest,
        nebius.vpc.v1.subnet_pb2.Subnet,
    ]

    GetByName: grpc.aio.UnaryUnaryMultiCallable[
        nebius.vpc.v1.subnet_service_pb2.GetSubnetByNameRequest,
        nebius.vpc.v1.subnet_pb2.Subnet,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        nebius.vpc.v1.subnet_service_pb2.ListSubnetsRequest,
        nebius.vpc.v1.subnet_service_pb2.ListSubnetsResponse,
    ]

class SubnetServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: nebius.vpc.v1.subnet_service_pb2.GetSubnetRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.vpc.v1.subnet_pb2.Subnet, collections.abc.Awaitable[nebius.vpc.v1.subnet_pb2.Subnet]]: ...

    @abc.abstractmethod
    def GetByName(
        self,
        request: nebius.vpc.v1.subnet_service_pb2.GetSubnetByNameRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.vpc.v1.subnet_pb2.Subnet, collections.abc.Awaitable[nebius.vpc.v1.subnet_pb2.Subnet]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: nebius.vpc.v1.subnet_service_pb2.ListSubnetsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.vpc.v1.subnet_service_pb2.ListSubnetsResponse, collections.abc.Awaitable[nebius.vpc.v1.subnet_service_pb2.ListSubnetsResponse]]: ...

def add_SubnetServiceServicer_to_server(servicer: SubnetServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...