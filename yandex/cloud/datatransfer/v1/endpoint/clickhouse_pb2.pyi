"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.empty_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing
import yandex.cloud.datatransfer.v1.endpoint.common_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ClickhouseCleanupPolicy:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ClickhouseCleanupPolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ClickhouseCleanupPolicy.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    CLICKHOUSE_CLEANUP_POLICY_UNSPECIFIED: _ClickhouseCleanupPolicy.ValueType  # 0
    CLICKHOUSE_CLEANUP_POLICY_DISABLED: _ClickhouseCleanupPolicy.ValueType  # 1
    CLICKHOUSE_CLEANUP_POLICY_DROP: _ClickhouseCleanupPolicy.ValueType  # 2
    CLICKHOUSE_CLEANUP_POLICY_TRUNCATE: _ClickhouseCleanupPolicy.ValueType  # 3

class ClickhouseCleanupPolicy(_ClickhouseCleanupPolicy, metaclass=_ClickhouseCleanupPolicyEnumTypeWrapper): ...

CLICKHOUSE_CLEANUP_POLICY_UNSPECIFIED: ClickhouseCleanupPolicy.ValueType  # 0
CLICKHOUSE_CLEANUP_POLICY_DISABLED: ClickhouseCleanupPolicy.ValueType  # 1
CLICKHOUSE_CLEANUP_POLICY_DROP: ClickhouseCleanupPolicy.ValueType  # 2
CLICKHOUSE_CLEANUP_POLICY_TRUNCATE: ClickhouseCleanupPolicy.ValueType  # 3
global___ClickhouseCleanupPolicy = ClickhouseCleanupPolicy

@typing.final
class ClickhouseShard(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    HOSTS_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def hosts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        hosts: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["hosts", b"hosts", "name", b"name"]) -> None: ...

global___ClickhouseShard = ClickhouseShard

@typing.final
class OnPremiseClickhouse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHARDS_FIELD_NUMBER: builtins.int
    HTTP_PORT_FIELD_NUMBER: builtins.int
    NATIVE_PORT_FIELD_NUMBER: builtins.int
    TLS_MODE_FIELD_NUMBER: builtins.int
    http_port: builtins.int
    native_port: builtins.int
    @property
    def shards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClickhouseShard]: ...
    @property
    def tls_mode(self) -> yandex.cloud.datatransfer.v1.endpoint.common_pb2.TLSMode: ...
    def __init__(
        self,
        *,
        shards: collections.abc.Iterable[global___ClickhouseShard] | None = ...,
        http_port: builtins.int = ...,
        native_port: builtins.int = ...,
        tls_mode: yandex.cloud.datatransfer.v1.endpoint.common_pb2.TLSMode | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tls_mode", b"tls_mode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["http_port", b"http_port", "native_port", b"native_port", "shards", b"shards", "tls_mode", b"tls_mode"]) -> None: ...

global___OnPremiseClickhouse = OnPremiseClickhouse

@typing.final
class ClickhouseConnectionOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ON_PREMISE_FIELD_NUMBER: builtins.int
    MDB_CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    mdb_cluster_id: builtins.str
    user: builtins.str
    database: builtins.str
    """Database"""
    @property
    def on_premise(self) -> global___OnPremiseClickhouse: ...
    @property
    def password(self) -> yandex.cloud.datatransfer.v1.endpoint.common_pb2.Secret: ...
    def __init__(
        self,
        *,
        on_premise: global___OnPremiseClickhouse | None = ...,
        mdb_cluster_id: builtins.str = ...,
        user: builtins.str = ...,
        password: yandex.cloud.datatransfer.v1.endpoint.common_pb2.Secret | None = ...,
        database: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["address", b"address", "mdb_cluster_id", b"mdb_cluster_id", "on_premise", b"on_premise", "password", b"password"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "database", b"database", "mdb_cluster_id", b"mdb_cluster_id", "on_premise", b"on_premise", "password", b"password", "user", b"user"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["address", b"address"]) -> typing.Literal["on_premise", "mdb_cluster_id"] | None: ...

global___ClickhouseConnectionOptions = ClickhouseConnectionOptions

@typing.final
class ClickhouseConnection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTION_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def connection_options(self) -> global___ClickhouseConnectionOptions: ...
    def __init__(
        self,
        *,
        connection_options: global___ClickhouseConnectionOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["connection", b"connection", "connection_options", b"connection_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["connection", b"connection", "connection_options", b"connection_options"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["connection", b"connection"]) -> typing.Literal["connection_options"] | None: ...

global___ClickhouseConnection = ClickhouseConnection

@typing.final
class ClickhouseSharding(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class ColumnValueHash(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        COLUMN_NAME_FIELD_NUMBER: builtins.int
        column_name: builtins.str
        def __init__(
            self,
            *,
            column_name: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["column_name", b"column_name"]) -> None: ...

    @typing.final
    class ColumnValueMapping(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing.final
        class ValueToShard(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            COLUMN_VALUE_FIELD_NUMBER: builtins.int
            SHARD_NAME_FIELD_NUMBER: builtins.int
            shard_name: builtins.str
            @property
            def column_value(self) -> yandex.cloud.datatransfer.v1.endpoint.common_pb2.ColumnValue: ...
            def __init__(
                self,
                *,
                column_value: yandex.cloud.datatransfer.v1.endpoint.common_pb2.ColumnValue | None = ...,
                shard_name: builtins.str = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["column_value", b"column_value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["column_value", b"column_value", "shard_name", b"shard_name"]) -> None: ...

        COLUMN_NAME_FIELD_NUMBER: builtins.int
        MAPPING_FIELD_NUMBER: builtins.int
        column_name: builtins.str
        @property
        def mapping(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClickhouseSharding.ColumnValueMapping.ValueToShard]: ...
        def __init__(
            self,
            *,
            column_name: builtins.str = ...,
            mapping: collections.abc.Iterable[global___ClickhouseSharding.ColumnValueMapping.ValueToShard] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["column_name", b"column_name", "mapping", b"mapping"]) -> None: ...

    COLUMN_VALUE_HASH_FIELD_NUMBER: builtins.int
    CUSTOM_MAPPING_FIELD_NUMBER: builtins.int
    TRANSFER_ID_FIELD_NUMBER: builtins.int
    ROUND_ROBIN_FIELD_NUMBER: builtins.int
    @property
    def column_value_hash(self) -> global___ClickhouseSharding.ColumnValueHash: ...
    @property
    def custom_mapping(self) -> global___ClickhouseSharding.ColumnValueMapping: ...
    @property
    def transfer_id(self) -> google.protobuf.empty_pb2.Empty: ...
    @property
    def round_robin(self) -> google.protobuf.empty_pb2.Empty: ...
    def __init__(
        self,
        *,
        column_value_hash: global___ClickhouseSharding.ColumnValueHash | None = ...,
        custom_mapping: global___ClickhouseSharding.ColumnValueMapping | None = ...,
        transfer_id: google.protobuf.empty_pb2.Empty | None = ...,
        round_robin: google.protobuf.empty_pb2.Empty | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["column_value_hash", b"column_value_hash", "custom_mapping", b"custom_mapping", "round_robin", b"round_robin", "sharding", b"sharding", "transfer_id", b"transfer_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["column_value_hash", b"column_value_hash", "custom_mapping", b"custom_mapping", "round_robin", b"round_robin", "sharding", b"sharding", "transfer_id", b"transfer_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["sharding", b"sharding"]) -> typing.Literal["column_value_hash", "custom_mapping", "transfer_id", "round_robin"] | None: ...

global___ClickhouseSharding = ClickhouseSharding

@typing.final
class ClickhouseSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTION_FIELD_NUMBER: builtins.int
    INCLUDE_TABLES_FIELD_NUMBER: builtins.int
    EXCLUDE_TABLES_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    SECURITY_GROUPS_FIELD_NUMBER: builtins.int
    CLICKHOUSE_CLUSTER_NAME_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    clickhouse_cluster_name: builtins.str
    """Name of the ClickHouse cluster. For Managed ClickHouse that is name of
    ShardGroup.
    """
    @property
    def connection(self) -> global___ClickhouseConnection: ...
    @property
    def include_tables(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """While list of tables for replication. If none or empty list is presented - will
        replicate all tables. Can contain * patterns.
        """

    @property
    def exclude_tables(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Exclude list of tables for replication. If none or empty list is presented -
        will replicate all tables. Can contain * patterns.
        """

    @property
    def security_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        connection: global___ClickhouseConnection | None = ...,
        include_tables: collections.abc.Iterable[builtins.str] | None = ...,
        exclude_tables: collections.abc.Iterable[builtins.str] | None = ...,
        subnet_id: builtins.str = ...,
        security_groups: collections.abc.Iterable[builtins.str] | None = ...,
        clickhouse_cluster_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["connection", b"connection"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["clickhouse_cluster_name", b"clickhouse_cluster_name", "connection", b"connection", "exclude_tables", b"exclude_tables", "include_tables", b"include_tables", "security_groups", b"security_groups", "subnet_id", b"subnet_id"]) -> None: ...

global___ClickhouseSource = ClickhouseSource

@typing.final
class ClickhouseTarget(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTION_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ALT_NAMES_FIELD_NUMBER: builtins.int
    CLEANUP_POLICY_FIELD_NUMBER: builtins.int
    SHARDING_FIELD_NUMBER: builtins.int
    CLICKHOUSE_CLUSTER_NAME_FIELD_NUMBER: builtins.int
    SECURITY_GROUPS_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    cleanup_policy: global___ClickhouseCleanupPolicy.ValueType
    clickhouse_cluster_name: builtins.str
    """Name of the ClickHouse cluster. For Managed ClickHouse that is name of
    ShardGroup.
    """
    @property
    def connection(self) -> global___ClickhouseConnection: ...
    @property
    def alt_names(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datatransfer.v1.endpoint.common_pb2.AltName]:
        """Alternative table names in target"""

    @property
    def sharding(self) -> global___ClickhouseSharding: ...
    @property
    def security_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        connection: global___ClickhouseConnection | None = ...,
        subnet_id: builtins.str = ...,
        alt_names: collections.abc.Iterable[yandex.cloud.datatransfer.v1.endpoint.common_pb2.AltName] | None = ...,
        cleanup_policy: global___ClickhouseCleanupPolicy.ValueType = ...,
        sharding: global___ClickhouseSharding | None = ...,
        clickhouse_cluster_name: builtins.str = ...,
        security_groups: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["connection", b"connection", "sharding", b"sharding"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["alt_names", b"alt_names", "cleanup_policy", b"cleanup_policy", "clickhouse_cluster_name", b"clickhouse_cluster_name", "connection", b"connection", "security_groups", b"security_groups", "sharding", b"sharding", "subnet_id", b"subnet_id"]) -> None: ...

global___ClickhouseTarget = ClickhouseTarget
