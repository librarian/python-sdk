"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import google.type.timeofday_pb2
import sys
import typing
import yandex.cloud.mdb.greenplum.v1.config_pb2
import yandex.cloud.mdb.greenplum.v1.maintenance_pb2
import yandex.cloud.mdb.greenplum.v1.pxf_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Cluster(google.protobuf.message.Message):
    """A Greenplum® cluster resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Environment:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnvironmentEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Environment.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ENVIRONMENT_UNSPECIFIED: Cluster._Environment.ValueType  # 0
        PRODUCTION: Cluster._Environment.ValueType  # 1
        """Stable environment with a conservative update policy: only hotfixes are applied during regular maintenance."""
        PRESTABLE: Cluster._Environment.ValueType  # 2
        """Environment with more aggressive update policy: new versions are rolled out irrespective of backward compatibility."""

    class Environment(_Environment, metaclass=_EnvironmentEnumTypeWrapper): ...
    ENVIRONMENT_UNSPECIFIED: Cluster.Environment.ValueType  # 0
    PRODUCTION: Cluster.Environment.ValueType  # 1
    """Stable environment with a conservative update policy: only hotfixes are applied during regular maintenance."""
    PRESTABLE: Cluster.Environment.ValueType  # 2
    """Environment with more aggressive update policy: new versions are rolled out irrespective of backward compatibility."""

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Cluster._Health.ValueType  # 0
        """Health of the cluster is unknown ([Host.health] for every host in the cluster is UNKNOWN)."""
        ALIVE: Cluster._Health.ValueType  # 1
        """Cluster is working normally ([Host.health] for every host in the cluster is ALIVE)."""
        DEAD: Cluster._Health.ValueType  # 2
        """Cluster is inoperable ([Host.health] for every host in the cluster is DEAD)."""
        DEGRADED: Cluster._Health.ValueType  # 3
        """Cluster is working below capacity ([Host.health] for at least one host in the cluster is not ALIVE)."""
        UNBALANCED: Cluster._Health.ValueType  # 4
        """Cluster is working below capacity ([Host.health] for at least one host in the cluster is UNBALANCED)."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNKNOWN: Cluster.Health.ValueType  # 0
    """Health of the cluster is unknown ([Host.health] for every host in the cluster is UNKNOWN)."""
    ALIVE: Cluster.Health.ValueType  # 1
    """Cluster is working normally ([Host.health] for every host in the cluster is ALIVE)."""
    DEAD: Cluster.Health.ValueType  # 2
    """Cluster is inoperable ([Host.health] for every host in the cluster is DEAD)."""
    DEGRADED: Cluster.Health.ValueType  # 3
    """Cluster is working below capacity ([Host.health] for at least one host in the cluster is not ALIVE)."""
    UNBALANCED: Cluster.Health.ValueType  # 4
    """Cluster is working below capacity ([Host.health] for at least one host in the cluster is UNBALANCED)."""

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: Cluster._Status.ValueType  # 0
        """Cluster state is unknown."""
        CREATING: Cluster._Status.ValueType  # 1
        """Cluster is being created."""
        RUNNING: Cluster._Status.ValueType  # 2
        """Cluster is running normally."""
        ERROR: Cluster._Status.ValueType  # 3
        """Cluster has encountered a problem and cannot operate."""
        UPDATING: Cluster._Status.ValueType  # 4
        """Cluster is being updated."""
        STOPPING: Cluster._Status.ValueType  # 5
        """Cluster is stopping."""
        STOPPED: Cluster._Status.ValueType  # 6
        """Cluster has stopped."""
        STARTING: Cluster._Status.ValueType  # 7
        """Cluster is starting."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """Current state of the cluster."""

    STATUS_UNKNOWN: Cluster.Status.ValueType  # 0
    """Cluster state is unknown."""
    CREATING: Cluster.Status.ValueType  # 1
    """Cluster is being created."""
    RUNNING: Cluster.Status.ValueType  # 2
    """Cluster is running normally."""
    ERROR: Cluster.Status.ValueType  # 3
    """Cluster has encountered a problem and cannot operate."""
    UPDATING: Cluster.Status.ValueType  # 4
    """Cluster is being updated."""
    STOPPING: Cluster.Status.ValueType  # 5
    """Cluster is stopping."""
    STOPPED: Cluster.Status.ValueType  # 6
    """Cluster has stopped."""
    STARTING: Cluster.Status.ValueType  # 7
    """Cluster is starting."""

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    MONITORING_FIELD_NUMBER: builtins.int
    MASTER_CONFIG_FIELD_NUMBER: builtins.int
    SEGMENT_CONFIG_FIELD_NUMBER: builtins.int
    MASTER_HOST_COUNT_FIELD_NUMBER: builtins.int
    SEGMENT_HOST_COUNT_FIELD_NUMBER: builtins.int
    SEGMENT_IN_HOST_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    PLANNED_OPERATION_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    HOST_GROUP_IDS_FIELD_NUMBER: builtins.int
    CLUSTER_CONFIG_FIELD_NUMBER: builtins.int
    CLOUD_STORAGE_FIELD_NUMBER: builtins.int
    MASTER_HOST_GROUP_IDS_FIELD_NUMBER: builtins.int
    SEGMENT_HOST_GROUP_IDS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the Greenplum® cluster.
    This ID is assigned by the platform at the moment of cluster creation.
    """
    folder_id: builtins.str
    """ID of the folder that the Greenplum® cluster belongs to."""
    name: builtins.str
    """Name of the Greenplum® cluster.
    The name is unique within the folder.
    """
    description: builtins.str
    """Description of the Greenplum® cluster."""
    environment: global___Cluster.Environment.ValueType
    """Deployment environment of the Greenplum® cluster."""
    master_host_count: builtins.int
    """Number of hosts in the master subcluster."""
    segment_host_count: builtins.int
    """Number of hosts in the segment subcluster."""
    segment_in_host: builtins.int
    """Number of segments per host."""
    network_id: builtins.str
    """ID of the cloud network that the cluster belongs to."""
    health: global___Cluster.Health.ValueType
    """Aggregated cluster health."""
    status: global___Cluster.Status.ValueType
    """Current state of the cluster."""
    user_name: builtins.str
    """Owner user name."""
    deletion_protection: builtins.bool
    """Determines whether the cluster is protected from being deleted."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the cluster was created."""

    @property
    def config(self) -> global___GreenplumConfig:
        """Greenplum® cluster configuration."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels for the Greenplum® cluster as `key:value` pairs. Maximum 64 labels per resource."""

    @property
    def monitoring(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Monitoring]:
        """Description of monitoring systems relevant to the Greenplum® cluster."""

    @property
    def master_config(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.MasterSubclusterConfig:
        """Configuration of the Greenplum® master subcluster."""

    @property
    def segment_config(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.SegmentSubclusterConfig:
        """Configuration of the Greenplum® segment subcluster."""

    @property
    def maintenance_window(self) -> yandex.cloud.mdb.greenplum.v1.maintenance_pb2.MaintenanceWindow:
        """A Greenplum® cluster maintenance window. Should be defined by either one of the two options."""

    @property
    def planned_operation(self) -> yandex.cloud.mdb.greenplum.v1.maintenance_pb2.MaintenanceOperation:
        """Maintenance operation planned at nearest [maintenance_window]."""

    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """User security groups."""

    @property
    def host_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Host groups hosting VMs of the cluster."""

    @property
    def cluster_config(self) -> global___ClusterConfigSet:
        """Greenplum® and Odyssey® configuration."""

    @property
    def cloud_storage(self) -> global___CloudStorage:
        """Cloud storage settings"""

    @property
    def master_host_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Host groups hosting VMs of the master subcluster."""

    @property
    def segment_host_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Host groups hosting VMs of the segment subcluster."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        config: global___GreenplumConfig | None = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        environment: global___Cluster.Environment.ValueType = ...,
        monitoring: collections.abc.Iterable[global___Monitoring] | None = ...,
        master_config: yandex.cloud.mdb.greenplum.v1.config_pb2.MasterSubclusterConfig | None = ...,
        segment_config: yandex.cloud.mdb.greenplum.v1.config_pb2.SegmentSubclusterConfig | None = ...,
        master_host_count: builtins.int = ...,
        segment_host_count: builtins.int = ...,
        segment_in_host: builtins.int = ...,
        network_id: builtins.str = ...,
        health: global___Cluster.Health.ValueType = ...,
        status: global___Cluster.Status.ValueType = ...,
        maintenance_window: yandex.cloud.mdb.greenplum.v1.maintenance_pb2.MaintenanceWindow | None = ...,
        planned_operation: yandex.cloud.mdb.greenplum.v1.maintenance_pb2.MaintenanceOperation | None = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        user_name: builtins.str = ...,
        deletion_protection: builtins.bool = ...,
        host_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        cluster_config: global___ClusterConfigSet | None = ...,
        cloud_storage: global___CloudStorage | None = ...,
        master_host_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        segment_host_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cloud_storage", b"cloud_storage", "cluster_config", b"cluster_config", "config", b"config", "created_at", b"created_at", "maintenance_window", b"maintenance_window", "master_config", b"master_config", "planned_operation", b"planned_operation", "segment_config", b"segment_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_storage", b"cloud_storage", "cluster_config", b"cluster_config", "config", b"config", "created_at", b"created_at", "deletion_protection", b"deletion_protection", "description", b"description", "environment", b"environment", "folder_id", b"folder_id", "health", b"health", "host_group_ids", b"host_group_ids", "id", b"id", "labels", b"labels", "maintenance_window", b"maintenance_window", "master_config", b"master_config", "master_host_count", b"master_host_count", "master_host_group_ids", b"master_host_group_ids", "monitoring", b"monitoring", "name", b"name", "network_id", b"network_id", "planned_operation", b"planned_operation", "security_group_ids", b"security_group_ids", "segment_config", b"segment_config", "segment_host_count", b"segment_host_count", "segment_host_group_ids", b"segment_host_group_ids", "segment_in_host", b"segment_in_host", "status", b"status", "user_name", b"user_name"]) -> None: ...

global___Cluster = Cluster

@typing.final
class ClusterConfigSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GREENPLUM_CONFIG_SET_6_17_FIELD_NUMBER: builtins.int
    GREENPLUM_CONFIG_SET_6_19_FIELD_NUMBER: builtins.int
    GREENPLUM_CONFIG_SET_6_21_FIELD_NUMBER: builtins.int
    GREENPLUM_CONFIG_SET_6_22_FIELD_NUMBER: builtins.int
    GREENPLUM_CONFIG_SET_6_FIELD_NUMBER: builtins.int
    POOL_FIELD_NUMBER: builtins.int
    BACKGROUND_ACTIVITIES_FIELD_NUMBER: builtins.int
    PXF_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def greenplum_config_set_6_17(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6_17: ...
    @property
    def greenplum_config_set_6_19(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6_19: ...
    @property
    def greenplum_config_set_6_21(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6_21: ...
    @property
    def greenplum_config_set_6_22(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6_22: ...
    @property
    def greenplum_config_set_6(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6: ...
    @property
    def pool(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.ConnectionPoolerConfigSet:
        """Odyssey® pool settings."""

    @property
    def background_activities(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.BackgroundActivitiesConfig:
        """Managed Greenplum® background tasks configuration."""

    @property
    def pxf_config(self) -> yandex.cloud.mdb.greenplum.v1.pxf_pb2.PXFConfigSet: ...
    def __init__(
        self,
        *,
        greenplum_config_set_6_17: yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6_17 | None = ...,
        greenplum_config_set_6_19: yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6_19 | None = ...,
        greenplum_config_set_6_21: yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6_21 | None = ...,
        greenplum_config_set_6_22: yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6_22 | None = ...,
        greenplum_config_set_6: yandex.cloud.mdb.greenplum.v1.config_pb2.GreenplumConfigSet6 | None = ...,
        pool: yandex.cloud.mdb.greenplum.v1.config_pb2.ConnectionPoolerConfigSet | None = ...,
        background_activities: yandex.cloud.mdb.greenplum.v1.config_pb2.BackgroundActivitiesConfig | None = ...,
        pxf_config: yandex.cloud.mdb.greenplum.v1.pxf_pb2.PXFConfigSet | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["background_activities", b"background_activities", "greenplum_config", b"greenplum_config", "greenplum_config_set_6", b"greenplum_config_set_6", "greenplum_config_set_6_17", b"greenplum_config_set_6_17", "greenplum_config_set_6_19", b"greenplum_config_set_6_19", "greenplum_config_set_6_21", b"greenplum_config_set_6_21", "greenplum_config_set_6_22", b"greenplum_config_set_6_22", "pool", b"pool", "pxf_config", b"pxf_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["background_activities", b"background_activities", "greenplum_config", b"greenplum_config", "greenplum_config_set_6", b"greenplum_config_set_6", "greenplum_config_set_6_17", b"greenplum_config_set_6_17", "greenplum_config_set_6_19", b"greenplum_config_set_6_19", "greenplum_config_set_6_21", b"greenplum_config_set_6_21", "greenplum_config_set_6_22", b"greenplum_config_set_6_22", "pool", b"pool", "pxf_config", b"pxf_config"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["greenplum_config", b"greenplum_config"]) -> typing.Literal["greenplum_config_set_6_17", "greenplum_config_set_6_19", "greenplum_config_set_6_21", "greenplum_config_set_6_22", "greenplum_config_set_6"] | None: ...

global___ClusterConfigSet = ClusterConfigSet

@typing.final
class Monitoring(google.protobuf.message.Message):
    """Monitoring system metadata."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LINK_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the monitoring system."""
    description: builtins.str
    """Description of the monitoring system."""
    link: builtins.str
    """Link to the monitoring system charts for the Greenplum® cluster."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        link: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "link", b"link", "name", b"name"]) -> None: ...

global___Monitoring = Monitoring

@typing.final
class GreenplumConfig(google.protobuf.message.Message):
    """Greenplum® cluster configuration."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    BACKUP_WINDOW_START_FIELD_NUMBER: builtins.int
    BACKUP_RETAIN_PERIOD_DAYS_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    version: builtins.str
    """Version of the Greenplum® server software."""
    zone_id: builtins.str
    """ID of the availability zone the cluster belongs to.
    To get a list of available zones, use the [yandex.cloud.compute.v1.ZoneService.List] request.
    """
    subnet_id: builtins.str
    """ID of the subnet the cluster belongs to. This subnet should be a part of the cloud network the cluster belongs to (see [Cluster.network_id])."""
    assign_public_ip: builtins.bool
    """Determines whether the cluster has a public IP address.

    After the cluster has been created, this setting cannot be changed.
    """
    @property
    def backup_window_start(self) -> google.type.timeofday_pb2.TimeOfDay:
        """Time to start the daily backup, in the UTC timezone."""

    @property
    def backup_retain_period_days(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Retention policy of automated backups."""

    @property
    def access(self) -> global___Access:
        """Access policy for external services."""

    def __init__(
        self,
        *,
        version: builtins.str = ...,
        backup_window_start: google.type.timeofday_pb2.TimeOfDay | None = ...,
        backup_retain_period_days: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        access: global___Access | None = ...,
        zone_id: builtins.str = ...,
        subnet_id: builtins.str = ...,
        assign_public_ip: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["access", b"access", "backup_retain_period_days", b"backup_retain_period_days", "backup_window_start", b"backup_window_start"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access", b"access", "assign_public_ip", b"assign_public_ip", "backup_retain_period_days", b"backup_retain_period_days", "backup_window_start", b"backup_window_start", "subnet_id", b"subnet_id", "version", b"version", "zone_id", b"zone_id"]) -> None: ...

global___GreenplumConfig = GreenplumConfig

@typing.final
class Access(google.protobuf.message.Message):
    """Greenplum® cluster access options."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_LENS_FIELD_NUMBER: builtins.int
    WEB_SQL_FIELD_NUMBER: builtins.int
    DATA_TRANSFER_FIELD_NUMBER: builtins.int
    YANDEX_QUERY_FIELD_NUMBER: builtins.int
    data_lens: builtins.bool
    """Allows data export from the cluster to DataLens."""
    web_sql: builtins.bool
    """Allows SQL queries to the cluster databases from the management console."""
    data_transfer: builtins.bool
    """Allows access for DataTransfer."""
    yandex_query: builtins.bool
    """Allow access for YandexQuery."""
    def __init__(
        self,
        *,
        data_lens: builtins.bool = ...,
        web_sql: builtins.bool = ...,
        data_transfer: builtins.bool = ...,
        yandex_query: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_lens", b"data_lens", "data_transfer", b"data_transfer", "web_sql", b"web_sql", "yandex_query", b"yandex_query"]) -> None: ...

global___Access = Access

@typing.final
class GreenplumRestoreConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUP_WINDOW_START_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    zone_id: builtins.str
    """ID of the availability zone where the host resides.

    To get a list of available zones, use the [yandex.cloud.compute.v1.ZoneService.List] request.
    """
    subnet_id: builtins.str
    """ID of the subnet that the host should belong to. This subnet should be a part of the network that the cluster belongs to.
    The ID of the network is set in the field [Cluster.network_id].
    """
    assign_public_ip: builtins.bool
    """Determines whether the host should get a public IP address on creation.

    After a host has been created, this setting cannot be changed.

    To remove an assigned public IP, or to assign a public IP to a host without one, recreate the host with [assign_public_ip] set as needed.

    Possible values:
    * `false` - do not assign a public IP to the master host.
    * `true` - assign a public IP to the master host.
    """
    @property
    def backup_window_start(self) -> google.type.timeofday_pb2.TimeOfDay:
        """Time to start the daily backup, in the UTC timezone."""

    @property
    def access(self) -> global___Access:
        """Access policy for external services."""

    def __init__(
        self,
        *,
        backup_window_start: google.type.timeofday_pb2.TimeOfDay | None = ...,
        access: global___Access | None = ...,
        zone_id: builtins.str = ...,
        subnet_id: builtins.str = ...,
        assign_public_ip: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["access", b"access", "backup_window_start", b"backup_window_start"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access", b"access", "assign_public_ip", b"assign_public_ip", "backup_window_start", b"backup_window_start", "subnet_id", b"subnet_id", "zone_id", b"zone_id"]) -> None: ...

global___GreenplumRestoreConfig = GreenplumRestoreConfig

@typing.final
class RestoreResources(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    DISK_SIZE_FIELD_NUMBER: builtins.int
    resource_preset_id: builtins.str
    """ID of the preset for computational resources available to a host (CPU, memory, etc.)."""
    disk_size: builtins.int
    """Volume of the storage available to a host."""
    def __init__(
        self,
        *,
        resource_preset_id: builtins.str = ...,
        disk_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["disk_size", b"disk_size", "resource_preset_id", b"resource_preset_id"]) -> None: ...

global___RestoreResources = RestoreResources

@typing.final
class CloudStorage(google.protobuf.message.Message):
    """Cloud Storage Settings"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLE_FIELD_NUMBER: builtins.int
    enable: builtins.bool
    """enable Cloud Storage for cluster"""
    def __init__(
        self,
        *,
        enable: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["enable", b"enable"]) -> None: ...

global___CloudStorage = CloudStorage
