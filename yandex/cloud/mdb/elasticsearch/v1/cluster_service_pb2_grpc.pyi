"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.elasticsearch.v1.cluster_pb2
import yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ClusterServiceStub:
    """A set of methods for managing Elasticsearch clusters."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified Elasticsearch cluster.

    To get the list of available Elasticsearch clusters, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of Elasticsearch clusters that belong to the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new Elasticsearch cluster in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified Elasticsearch cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified Elasticsearch cluster."""

    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Moves the specified Elasticsearch cluster to the specified folder."""

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified Elasticsearch cluster."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified Elasticsearch cluster."""

    Backup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create a backup for the specified ElasticSearch cluster."""

    ListBackups: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Returns the list of available backups for the specified Elasticsearch cluster."""

    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new ElasticSearch cluster from the specified backup."""

    ListLogs: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified Elasticsearch cluster.

    For more information about logs, see the [Logs](/docs/managed-elasticsearch/operations/cluster-logs) section in the documentation.
    """

    StreamLogs: grpc.UnaryStreamMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StreamClusterLogsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StreamLogRecord,
    ]
    """Same as [ListLogs] but using server-side streaming. Also supports `tail -f` semantics."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of operations for the specified Elasticsearch cluster."""

    ListHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified Elasticsearch cluster."""

    AddHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds new hosts to the specified Elasticsearch cluster."""

    DeleteHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes specified hosts from the specified Elasticsearch cluster."""

    RescheduleMaintenance: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Reschedule planned maintenance operation."""

class ClusterServiceAsyncStub:
    """A set of methods for managing Elasticsearch clusters."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified Elasticsearch cluster.

    To get the list of available Elasticsearch clusters, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of Elasticsearch clusters that belong to the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new Elasticsearch cluster in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified Elasticsearch cluster."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified Elasticsearch cluster."""

    Move: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Moves the specified Elasticsearch cluster to the specified folder."""

    Start: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified Elasticsearch cluster."""

    Stop: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified Elasticsearch cluster."""

    Backup: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create a backup for the specified ElasticSearch cluster."""

    ListBackups: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Returns the list of available backups for the specified Elasticsearch cluster."""

    Restore: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new ElasticSearch cluster from the specified backup."""

    ListLogs: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified Elasticsearch cluster.

    For more information about logs, see the [Logs](/docs/managed-elasticsearch/operations/cluster-logs) section in the documentation.
    """

    StreamLogs: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StreamClusterLogsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StreamLogRecord,
    ]
    """Same as [ListLogs] but using server-side streaming. Also supports `tail -f` semantics."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of operations for the specified Elasticsearch cluster."""

    ListHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified Elasticsearch cluster."""

    AddHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds new hosts to the specified Elasticsearch cluster."""

    DeleteHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes specified hosts from the specified Elasticsearch cluster."""

    RescheduleMaintenance: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Reschedule planned maintenance operation."""

class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Elasticsearch clusters."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.GetClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.elasticsearch.v1.cluster_pb2.Cluster, collections.abc.Awaitable[yandex.cloud.mdb.elasticsearch.v1.cluster_pb2.Cluster]]:
        """Returns the specified Elasticsearch cluster.

        To get the list of available Elasticsearch clusters, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClustersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClustersResponse, collections.abc.Awaitable[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClustersResponse]]:
        """Retrieves the list of Elasticsearch clusters that belong to the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.CreateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new Elasticsearch cluster in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.UpdateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified Elasticsearch cluster."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.DeleteClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified Elasticsearch cluster."""

    @abc.abstractmethod
    def Move(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.MoveClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Moves the specified Elasticsearch cluster to the specified folder."""

    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StartClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Starts the specified Elasticsearch cluster."""

    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StopClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Stops the specified Elasticsearch cluster."""

    @abc.abstractmethod
    def Backup(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.BackupClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Create a backup for the specified ElasticSearch cluster."""

    @abc.abstractmethod
    def ListBackups(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterBackupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterBackupsResponse, collections.abc.Awaitable[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterBackupsResponse]]:
        """Returns the list of available backups for the specified Elasticsearch cluster."""

    @abc.abstractmethod
    def Restore(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.RestoreClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new ElasticSearch cluster from the specified backup."""

    @abc.abstractmethod
    def ListLogs(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterLogsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterLogsResponse, collections.abc.Awaitable[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterLogsResponse]]:
        """Retrieves logs for the specified Elasticsearch cluster.

        For more information about logs, see the [Logs](/docs/managed-elasticsearch/operations/cluster-logs) section in the documentation.
        """

    @abc.abstractmethod
    def StreamLogs(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StreamClusterLogsRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StreamLogRecord], collections.abc.AsyncIterator[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.StreamLogRecord]]:
        """Same as [ListLogs] but using server-side streaming. Also supports `tail -f` semantics."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterOperationsResponse, collections.abc.Awaitable[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterOperationsResponse]]:
        """Retrieves the list of operations for the specified Elasticsearch cluster."""

    @abc.abstractmethod
    def ListHosts(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterHostsResponse, collections.abc.Awaitable[yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.ListClusterHostsResponse]]:
        """Retrieves a list of hosts for the specified Elasticsearch cluster."""

    @abc.abstractmethod
    def AddHosts(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.AddClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Adds new hosts to the specified Elasticsearch cluster."""

    @abc.abstractmethod
    def DeleteHosts(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes specified hosts from the specified Elasticsearch cluster."""

    @abc.abstractmethod
    def RescheduleMaintenance(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Reschedule planned maintenance operation."""

def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
