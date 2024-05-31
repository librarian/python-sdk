"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.compute.v1.zone_pb2
import yandex.cloud.compute.v1.zone_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ZoneServiceStub:
    """A set of methods to retrieve information about availability zones."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.zone_service_pb2.GetZoneRequest,
        yandex.cloud.compute.v1.zone_pb2.Zone,
    ]
    """Returns the information about the specified availability zone.

    To get the list of availability zones, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.zone_service_pb2.ListZonesRequest,
        yandex.cloud.compute.v1.zone_service_pb2.ListZonesResponse,
    ]
    """Retrieves the list of availability zones."""

class ZoneServiceAsyncStub:
    """A set of methods to retrieve information about availability zones."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.zone_service_pb2.GetZoneRequest,
        yandex.cloud.compute.v1.zone_pb2.Zone,
    ]
    """Returns the information about the specified availability zone.

    To get the list of availability zones, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.zone_service_pb2.ListZonesRequest,
        yandex.cloud.compute.v1.zone_service_pb2.ListZonesResponse,
    ]
    """Retrieves the list of availability zones."""

class ZoneServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods to retrieve information about availability zones."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.compute.v1.zone_service_pb2.GetZoneRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.zone_pb2.Zone, collections.abc.Awaitable[yandex.cloud.compute.v1.zone_pb2.Zone]]:
        """Returns the information about the specified availability zone.

        To get the list of availability zones, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.compute.v1.zone_service_pb2.ListZonesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.zone_service_pb2.ListZonesResponse, collections.abc.Awaitable[yandex.cloud.compute.v1.zone_service_pb2.ListZonesResponse]]:
        """Retrieves the list of availability zones."""

def add_ZoneServiceServicer_to_server(servicer: ZoneServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
