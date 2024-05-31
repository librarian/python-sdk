"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.datasphere.v1.project_data_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ProjectDataServiceStub:
    """A set of methods for managing data of the Project resource."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    UploadFile: grpc.StreamUnaryMultiCallable[
        yandex.cloud.datasphere.v1.project_data_service_pb2.UploadFileRequest,
        yandex.cloud.datasphere.v1.project_data_service_pb2.UploadFileResponse,
    ]
    """Uploads a file to the specified project."""

    DownloadFile: grpc.UnaryStreamMultiCallable[
        yandex.cloud.datasphere.v1.project_data_service_pb2.DownloadFileRequest,
        yandex.cloud.datasphere.v1.project_data_service_pb2.DownloadFileResponse,
    ]
    """Downloads the specified file from the specified project."""

class ProjectDataServiceAsyncStub:
    """A set of methods for managing data of the Project resource."""

    UploadFile: grpc.aio.StreamUnaryMultiCallable[
        yandex.cloud.datasphere.v1.project_data_service_pb2.UploadFileRequest,
        yandex.cloud.datasphere.v1.project_data_service_pb2.UploadFileResponse,
    ]
    """Uploads a file to the specified project."""

    DownloadFile: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.datasphere.v1.project_data_service_pb2.DownloadFileRequest,
        yandex.cloud.datasphere.v1.project_data_service_pb2.DownloadFileResponse,
    ]
    """Downloads the specified file from the specified project."""

class ProjectDataServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing data of the Project resource."""

    @abc.abstractmethod
    def UploadFile(
        self,
        request_iterator: _MaybeAsyncIterator[yandex.cloud.datasphere.v1.project_data_service_pb2.UploadFileRequest],
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.datasphere.v1.project_data_service_pb2.UploadFileResponse, collections.abc.Awaitable[yandex.cloud.datasphere.v1.project_data_service_pb2.UploadFileResponse]]:
        """Uploads a file to the specified project."""

    @abc.abstractmethod
    def DownloadFile(
        self,
        request: yandex.cloud.datasphere.v1.project_data_service_pb2.DownloadFileRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.datasphere.v1.project_data_service_pb2.DownloadFileResponse], collections.abc.AsyncIterator[yandex.cloud.datasphere.v1.project_data_service_pb2.DownloadFileResponse]]:
        """Downloads the specified file from the specified project."""

def add_ProjectDataServiceServicer_to_server(servicer: ProjectDataServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
