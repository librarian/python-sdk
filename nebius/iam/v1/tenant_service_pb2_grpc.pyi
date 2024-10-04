"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import nebius.iam.v1.container_pb2
import nebius.iam.v1.tenant_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class TenantServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        nebius.iam.v1.tenant_service_pb2.GetTenantRequest,
        nebius.iam.v1.container_pb2.Container,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        nebius.iam.v1.tenant_service_pb2.ListTenantsRequest,
        nebius.iam.v1.tenant_service_pb2.ListTenantsResponse,
    ]

class TenantServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.iam.v1.tenant_service_pb2.GetTenantRequest,
        nebius.iam.v1.container_pb2.Container,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        nebius.iam.v1.tenant_service_pb2.ListTenantsRequest,
        nebius.iam.v1.tenant_service_pb2.ListTenantsResponse,
    ]

class TenantServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: nebius.iam.v1.tenant_service_pb2.GetTenantRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.iam.v1.container_pb2.Container, collections.abc.Awaitable[nebius.iam.v1.container_pb2.Container]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: nebius.iam.v1.tenant_service_pb2.ListTenantsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.iam.v1.tenant_service_pb2.ListTenantsResponse, collections.abc.Awaitable[nebius.iam.v1.tenant_service_pb2.ListTenantsResponse]]: ...

def add_TenantServiceServicer_to_server(servicer: TenantServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...