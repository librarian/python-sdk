"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.billing.v1.sku_pb2
import yandex.cloud.billing.v1.sku_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class SkuServiceStub:
    """A set of methods for managing Sku resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.sku_service_pb2.GetSkuRequest,
        yandex.cloud.billing.v1.sku_pb2.Sku,
    ]
    """Returns the specified SKU."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.sku_service_pb2.ListSkusRequest,
        yandex.cloud.billing.v1.sku_service_pb2.ListSkusResponse,
    ]
    """Retrieves the list of SKUs."""

class SkuServiceAsyncStub:
    """A set of methods for managing Sku resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.sku_service_pb2.GetSkuRequest,
        yandex.cloud.billing.v1.sku_pb2.Sku,
    ]
    """Returns the specified SKU."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.sku_service_pb2.ListSkusRequest,
        yandex.cloud.billing.v1.sku_service_pb2.ListSkusResponse,
    ]
    """Retrieves the list of SKUs."""

class SkuServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Sku resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.billing.v1.sku_service_pb2.GetSkuRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.billing.v1.sku_pb2.Sku, collections.abc.Awaitable[yandex.cloud.billing.v1.sku_pb2.Sku]]:
        """Returns the specified SKU."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.billing.v1.sku_service_pb2.ListSkusRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.billing.v1.sku_service_pb2.ListSkusResponse, collections.abc.Awaitable[yandex.cloud.billing.v1.sku_service_pb2.ListSkusResponse]]:
        """Retrieves the list of SKUs."""

def add_SkuServiceServicer_to_server(servicer: SkuServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
