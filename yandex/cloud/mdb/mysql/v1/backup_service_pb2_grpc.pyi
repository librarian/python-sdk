"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.mysql.v1.backup_pb2
import yandex.cloud.mdb.mysql.v1.backup_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class BackupServiceStub:
    """A set of methods for managing MySQL backups.

    See [the documentation](/docs/managed-mysql/operations/cluster-backups) for details.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.backup_service_pb2.GetBackupRequest,
        yandex.cloud.mdb.mysql.v1.backup_pb2.Backup,
    ]
    """Retrieves information about the specified backup."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.backup_service_pb2.ListBackupsRequest,
        yandex.cloud.mdb.mysql.v1.backup_service_pb2.ListBackupsResponse,
    ]
    """Retrieves the list of backups in a folder.

    To list backups for an existing cluster, make a [ClusterService.ListBackups] request.
    """

class BackupServiceAsyncStub:
    """A set of methods for managing MySQL backups.

    See [the documentation](/docs/managed-mysql/operations/cluster-backups) for details.
    """

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.backup_service_pb2.GetBackupRequest,
        yandex.cloud.mdb.mysql.v1.backup_pb2.Backup,
    ]
    """Retrieves information about the specified backup."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1.backup_service_pb2.ListBackupsRequest,
        yandex.cloud.mdb.mysql.v1.backup_service_pb2.ListBackupsResponse,
    ]
    """Retrieves the list of backups in a folder.

    To list backups for an existing cluster, make a [ClusterService.ListBackups] request.
    """

class BackupServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing MySQL backups.

    See [the documentation](/docs/managed-mysql/operations/cluster-backups) for details.
    """

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.mysql.v1.backup_service_pb2.GetBackupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1.backup_pb2.Backup, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1.backup_pb2.Backup]]:
        """Retrieves information about the specified backup."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.mysql.v1.backup_service_pb2.ListBackupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1.backup_service_pb2.ListBackupsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1.backup_service_pb2.ListBackupsResponse]]:
        """Retrieves the list of backups in a folder.

        To list backups for an existing cluster, make a [ClusterService.ListBackups] request.
        """

def add_BackupServiceServicer_to_server(servicer: BackupServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
