"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.sqlserver.v1.database_pb2
import yandex.cloud.mdb.sqlserver.v1.database_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DatabaseServiceStub:
    """A set of methods for managing SQL Server databases."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.GetDatabaseRequest,
        yandex.cloud.mdb.sqlserver.v1.database_pb2.Database,
    ]
    """Returns the specified SQL Server database.

    To get the list of available SQL Server databases, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ListDatabasesRequest,
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ListDatabasesResponse,
    ]
    """Retrieves the list of SQL Server databases in the specified cluster."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.CreateDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SQL Server database in the specified cluster."""

    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.RestoreDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SQL Server database in the specified cluster from a backup."""

    ImportBackup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ImportDatabaseBackupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Imports a new SQL Server database from an external backup."""

    ExportBackup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ExportDatabaseBackupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Exports the last database backup to an external backup."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.DeleteDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified SQL Server database."""

class DatabaseServiceAsyncStub:
    """A set of methods for managing SQL Server databases."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.GetDatabaseRequest,
        yandex.cloud.mdb.sqlserver.v1.database_pb2.Database,
    ]
    """Returns the specified SQL Server database.

    To get the list of available SQL Server databases, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ListDatabasesRequest,
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ListDatabasesResponse,
    ]
    """Retrieves the list of SQL Server databases in the specified cluster."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.CreateDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SQL Server database in the specified cluster."""

    Restore: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.RestoreDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SQL Server database in the specified cluster from a backup."""

    ImportBackup: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ImportDatabaseBackupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Imports a new SQL Server database from an external backup."""

    ExportBackup: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ExportDatabaseBackupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Exports the last database backup to an external backup."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.database_service_pb2.DeleteDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified SQL Server database."""

class DatabaseServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing SQL Server databases."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.database_service_pb2.GetDatabaseRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.sqlserver.v1.database_pb2.Database, collections.abc.Awaitable[yandex.cloud.mdb.sqlserver.v1.database_pb2.Database]]:
        """Returns the specified SQL Server database.

        To get the list of available SQL Server databases, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ListDatabasesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ListDatabasesResponse, collections.abc.Awaitable[yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ListDatabasesResponse]]:
        """Retrieves the list of SQL Server databases in the specified cluster."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.database_service_pb2.CreateDatabaseRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new SQL Server database in the specified cluster."""

    @abc.abstractmethod
    def Restore(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.database_service_pb2.RestoreDatabaseRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new SQL Server database in the specified cluster from a backup."""

    @abc.abstractmethod
    def ImportBackup(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ImportDatabaseBackupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Imports a new SQL Server database from an external backup."""

    @abc.abstractmethod
    def ExportBackup(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.database_service_pb2.ExportDatabaseBackupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Exports the last database backup to an external backup."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.database_service_pb2.DeleteDatabaseRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified SQL Server database."""

def add_DatabaseServiceServicer_to_server(servicer: DatabaseServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
