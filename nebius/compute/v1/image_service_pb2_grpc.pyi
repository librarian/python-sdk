"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import nebius.common.v1.metadata_pb2
import nebius.common.v1.operation_service_pb2
import nebius.compute.v1.image_pb2
import nebius.compute.v1.image_service_pb2
import nebius.compute.v1.operation_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ImageServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.image_service_pb2.GetImageRequest,
        nebius.compute.v1.image_pb2.Image,
    ]

    GetByName: grpc.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.compute.v1.image_pb2.Image,
    ]

    GetLatestByFamily: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.image_service_pb2.GetImageLatestByFamilyRequest,
        nebius.compute.v1.image_pb2.Image,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.image_service_pb2.ListImagesRequest,
        nebius.compute.v1.image_service_pb2.ListImagesResponse,
    ]

    ListOperationsByParent: grpc.UnaryUnaryMultiCallable[
        nebius.compute.v1.operation_service_pb2.ListOperationsByParentRequest,
        nebius.common.v1.operation_service_pb2.ListOperationsResponse,
    ]

class ImageServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.image_service_pb2.GetImageRequest,
        nebius.compute.v1.image_pb2.Image,
    ]

    GetByName: grpc.aio.UnaryUnaryMultiCallable[
        nebius.common.v1.metadata_pb2.GetByNameRequest,
        nebius.compute.v1.image_pb2.Image,
    ]

    GetLatestByFamily: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.image_service_pb2.GetImageLatestByFamilyRequest,
        nebius.compute.v1.image_pb2.Image,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.image_service_pb2.ListImagesRequest,
        nebius.compute.v1.image_service_pb2.ListImagesResponse,
    ]

    ListOperationsByParent: grpc.aio.UnaryUnaryMultiCallable[
        nebius.compute.v1.operation_service_pb2.ListOperationsByParentRequest,
        nebius.common.v1.operation_service_pb2.ListOperationsResponse,
    ]

class ImageServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: nebius.compute.v1.image_service_pb2.GetImageRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.image_pb2.Image, collections.abc.Awaitable[nebius.compute.v1.image_pb2.Image]]: ...

    @abc.abstractmethod
    def GetByName(
        self,
        request: nebius.common.v1.metadata_pb2.GetByNameRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.image_pb2.Image, collections.abc.Awaitable[nebius.compute.v1.image_pb2.Image]]: ...

    @abc.abstractmethod
    def GetLatestByFamily(
        self,
        request: nebius.compute.v1.image_service_pb2.GetImageLatestByFamilyRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.image_pb2.Image, collections.abc.Awaitable[nebius.compute.v1.image_pb2.Image]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: nebius.compute.v1.image_service_pb2.ListImagesRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.compute.v1.image_service_pb2.ListImagesResponse, collections.abc.Awaitable[nebius.compute.v1.image_service_pb2.ListImagesResponse]]: ...

    @abc.abstractmethod
    def ListOperationsByParent(
        self,
        request: nebius.compute.v1.operation_service_pb2.ListOperationsByParentRequest,
        context: _ServicerContext,
    ) -> typing.Union[nebius.common.v1.operation_service_pb2.ListOperationsResponse, collections.abc.Awaitable[nebius.common.v1.operation_service_pb2.ListOperationsResponse]]: ...

def add_ImageServiceServicer_to_server(servicer: ImageServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
