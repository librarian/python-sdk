"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.mysql.v1alpha.cluster_pb2
import yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ClusterServiceStub:
    """A set of methods for managing MySQL clusters."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_pb2.Cluster,
    ]
    """Returns the specified MySQL cluster.

    To get the list of available MySQL clusters, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of MySQL clusters that belong to the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a MySQL cluster in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Modifies the specified MySQL cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified MySQL cluster."""

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified MySQL cluster."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified MySQL cluster."""

    Backup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a backup for the specified MySQL cluster."""

    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new MySQL cluster using the specified backup."""

    ListLogs: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified MySQL cluster."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of operations for the specified MySQL cluster."""

    ListBackups: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Retrieves the list of available backups for the specified MySQL cluster."""

    ListHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified MySQL cluster."""

    AddHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates new hosts for a cluster."""

    DeleteHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified hosts for a cluster."""

class ClusterServiceAsyncStub:
    """A set of methods for managing MySQL clusters."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_pb2.Cluster,
    ]
    """Returns the specified MySQL cluster.

    To get the list of available MySQL clusters, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of MySQL clusters that belong to the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a MySQL cluster in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Modifies the specified MySQL cluster."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified MySQL cluster."""

    Start: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified MySQL cluster."""

    Stop: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified MySQL cluster."""

    Backup: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a backup for the specified MySQL cluster."""

    Restore: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new MySQL cluster using the specified backup."""

    ListLogs: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified MySQL cluster."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of operations for the specified MySQL cluster."""

    ListBackups: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Retrieves the list of available backups for the specified MySQL cluster."""

    ListHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified MySQL cluster."""

    AddHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates new hosts for a cluster."""

    DeleteHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified hosts for a cluster."""

class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing MySQL clusters."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.GetClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1alpha.cluster_pb2.Cluster, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1alpha.cluster_pb2.Cluster]]:
        """Returns the specified MySQL cluster.

        To get the list of available MySQL clusters, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClustersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClustersResponse, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClustersResponse]]:
        """Retrieves the list of MySQL clusters that belong to the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.CreateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a MySQL cluster in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.UpdateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Modifies the specified MySQL cluster."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.DeleteClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified MySQL cluster."""

    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.StartClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Starts the specified MySQL cluster."""

    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.StopClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Stops the specified MySQL cluster."""

    @abc.abstractmethod
    def Backup(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.BackupClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a backup for the specified MySQL cluster."""

    @abc.abstractmethod
    def Restore(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.RestoreClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new MySQL cluster using the specified backup."""

    @abc.abstractmethod
    def ListLogs(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterLogsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterLogsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterLogsResponse]]:
        """Retrieves logs for the specified MySQL cluster."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterOperationsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterOperationsResponse]]:
        """Retrieves the list of operations for the specified MySQL cluster."""

    @abc.abstractmethod
    def ListBackups(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterBackupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterBackupsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterBackupsResponse]]:
        """Retrieves the list of available backups for the specified MySQL cluster."""

    @abc.abstractmethod
    def ListHosts(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterHostsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.ListClusterHostsResponse]]:
        """Retrieves a list of hosts for the specified MySQL cluster."""

    @abc.abstractmethod
    def AddHosts(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.AddClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates new hosts for a cluster."""

    @abc.abstractmethod
    def DeleteHosts(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2.DeleteClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified hosts for a cluster."""

def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
