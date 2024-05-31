"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.access.access_pb2
import yandex.cloud.compute.v1.image_pb2
import yandex.cloud.compute.v1.image_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ImageServiceStub:
    """A set of methods for managing Image resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.GetImageRequest,
        yandex.cloud.compute.v1.image_pb2.Image,
    ]
    """Returns the specified Image resource.

    To get the list of available Image resources, make a [List] request.
    """

    GetLatestByFamily: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.GetImageLatestByFamilyRequest,
        yandex.cloud.compute.v1.image_pb2.Image,
    ]
    """Returns the latest image that is part of an image family."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.ListImagesRequest,
        yandex.cloud.compute.v1.image_service_pb2.ListImagesResponse,
    ]
    """Retrieves the list of Image resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.CreateImageRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates an image in the specified folder.

    You can create an image from a disk, snapshot, other image or URI.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.UpdateImageRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified image."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.DeleteImageRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified image.

    Deleting an image removes its data permanently and is irreversible.
    """

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.ListImageOperationsRequest,
        yandex.cloud.compute.v1.image_service_pb2.ListImageOperationsResponse,
    ]
    """Lists operations for the specified image."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """access

    Lists access bindings for the image.
    """

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the image."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the image."""

class ImageServiceAsyncStub:
    """A set of methods for managing Image resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.GetImageRequest,
        yandex.cloud.compute.v1.image_pb2.Image,
    ]
    """Returns the specified Image resource.

    To get the list of available Image resources, make a [List] request.
    """

    GetLatestByFamily: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.GetImageLatestByFamilyRequest,
        yandex.cloud.compute.v1.image_pb2.Image,
    ]
    """Returns the latest image that is part of an image family."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.ListImagesRequest,
        yandex.cloud.compute.v1.image_service_pb2.ListImagesResponse,
    ]
    """Retrieves the list of Image resources in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.CreateImageRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates an image in the specified folder.

    You can create an image from a disk, snapshot, other image or URI.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.UpdateImageRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified image."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.DeleteImageRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified image.

    Deleting an image removes its data permanently and is irreversible.
    """

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.image_service_pb2.ListImageOperationsRequest,
        yandex.cloud.compute.v1.image_service_pb2.ListImageOperationsResponse,
    ]
    """Lists operations for the specified image."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """access

    Lists access bindings for the image.
    """

    SetAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the image."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the image."""

class ImageServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Image resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.compute.v1.image_service_pb2.GetImageRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.image_pb2.Image, collections.abc.Awaitable[yandex.cloud.compute.v1.image_pb2.Image]]:
        """Returns the specified Image resource.

        To get the list of available Image resources, make a [List] request.
        """

    @abc.abstractmethod
    def GetLatestByFamily(
        self,
        request: yandex.cloud.compute.v1.image_service_pb2.GetImageLatestByFamilyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.image_pb2.Image, collections.abc.Awaitable[yandex.cloud.compute.v1.image_pb2.Image]]:
        """Returns the latest image that is part of an image family."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.compute.v1.image_service_pb2.ListImagesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.image_service_pb2.ListImagesResponse, collections.abc.Awaitable[yandex.cloud.compute.v1.image_service_pb2.ListImagesResponse]]:
        """Retrieves the list of Image resources in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.compute.v1.image_service_pb2.CreateImageRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates an image in the specified folder.

        You can create an image from a disk, snapshot, other image or URI.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.compute.v1.image_service_pb2.UpdateImageRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified image."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.compute.v1.image_service_pb2.DeleteImageRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified image.

        Deleting an image removes its data permanently and is irreversible.
        """

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.compute.v1.image_service_pb2.ListImageOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.image_service_pb2.ListImageOperationsResponse, collections.abc.Awaitable[yandex.cloud.compute.v1.image_service_pb2.ListImageOperationsResponse]]:
        """Lists operations for the specified image."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """access

        Lists access bindings for the image.
        """

    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets access bindings for the image."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the image."""

def add_ImageServiceServicer_to_server(servicer: ImageServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...