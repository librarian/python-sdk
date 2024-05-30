"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MongodConfig3_6(google.protobuf.message.Message):
    """Configuration of a mongod daemon. Supported options are a limited subset of all
    options described in [MongoDB documentation](https://docs.mongodb.com/v3.6/reference/configuration-options/).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Storage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing.final
        class WiredTiger(google.protobuf.message.Message):
            """Configuration of WiredTiger storage engine."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            @typing.final
            class EngineConfig(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                CACHE_SIZE_GB_FIELD_NUMBER: builtins.int
                @property
                def cache_size_gb(self) -> google.protobuf.wrappers_pb2.DoubleValue:
                    """The maximum size of the internal cache that WiredTiger will use for all data."""

                def __init__(
                    self,
                    *,
                    cache_size_gb: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
                ) -> None: ...
                def HasField(self, field_name: typing.Literal["cache_size_gb", b"cache_size_gb"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing.Literal["cache_size_gb", b"cache_size_gb"]) -> None: ...

            @typing.final
            class CollectionConfig(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                class _Compressor:
                    ValueType = typing.NewType("ValueType", builtins.int)
                    V: typing_extensions.TypeAlias = ValueType

                class _CompressorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongodConfig3_6.Storage.WiredTiger.CollectionConfig._Compressor.ValueType], builtins.type):
                    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
                    COMPRESSOR_UNSPECIFIED: MongodConfig3_6.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 0
                    NONE: MongodConfig3_6.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 1
                    """No compression."""
                    SNAPPY: MongodConfig3_6.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 2
                    """The [Snappy](https://docs.mongodb.com/v3.6/reference/glossary/#term-snappy) compression."""
                    ZLIB: MongodConfig3_6.Storage.WiredTiger.CollectionConfig._Compressor.ValueType  # 3
                    """The [zlib](https://docs.mongodb.com/v3.6/reference/glossary/#term-zlib) compression."""

                class Compressor(_Compressor, metaclass=_CompressorEnumTypeWrapper): ...
                COMPRESSOR_UNSPECIFIED: MongodConfig3_6.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 0
                NONE: MongodConfig3_6.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 1
                """No compression."""
                SNAPPY: MongodConfig3_6.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 2
                """The [Snappy](https://docs.mongodb.com/v3.6/reference/glossary/#term-snappy) compression."""
                ZLIB: MongodConfig3_6.Storage.WiredTiger.CollectionConfig.Compressor.ValueType  # 3
                """The [zlib](https://docs.mongodb.com/v3.6/reference/glossary/#term-zlib) compression."""

                BLOCK_COMPRESSOR_FIELD_NUMBER: builtins.int
                block_compressor: global___MongodConfig3_6.Storage.WiredTiger.CollectionConfig.Compressor.ValueType
                """Default type of compression to use for collection data."""
                def __init__(
                    self,
                    *,
                    block_compressor: global___MongodConfig3_6.Storage.WiredTiger.CollectionConfig.Compressor.ValueType = ...,
                ) -> None: ...
                def ClearField(self, field_name: typing.Literal["block_compressor", b"block_compressor"]) -> None: ...

            ENGINE_CONFIG_FIELD_NUMBER: builtins.int
            COLLECTION_CONFIG_FIELD_NUMBER: builtins.int
            @property
            def engine_config(self) -> global___MongodConfig3_6.Storage.WiredTiger.EngineConfig:
                """Engine configuration for WiredTiger."""

            @property
            def collection_config(self) -> global___MongodConfig3_6.Storage.WiredTiger.CollectionConfig:
                """Collection configuration for WiredTiger."""

            def __init__(
                self,
                *,
                engine_config: global___MongodConfig3_6.Storage.WiredTiger.EngineConfig | None = ...,
                collection_config: global___MongodConfig3_6.Storage.WiredTiger.CollectionConfig | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["collection_config", b"collection_config", "engine_config", b"engine_config"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["collection_config", b"collection_config", "engine_config", b"engine_config"]) -> None: ...

        @typing.final
        class Journal(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            ENABLED_FIELD_NUMBER: builtins.int
            COMMIT_INTERVAL_FIELD_NUMBER: builtins.int
            @property
            def enabled(self) -> google.protobuf.wrappers_pb2.BoolValue:
                """Whether the journal is enabled or disabled.
                Possible values:
                * true (default) - the journal is enabled.
                * false - the journal is disabled.
                """

            @property
            def commit_interval(self) -> google.protobuf.wrappers_pb2.Int64Value:
                """Commit interval between journal operations, in milliseconds.
                Default: 100.
                """

            def __init__(
                self,
                *,
                enabled: google.protobuf.wrappers_pb2.BoolValue | None = ...,
                commit_interval: google.protobuf.wrappers_pb2.Int64Value | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["commit_interval", b"commit_interval", "enabled", b"enabled"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["commit_interval", b"commit_interval", "enabled", b"enabled"]) -> None: ...

        WIRED_TIGER_FIELD_NUMBER: builtins.int
        JOURNAL_FIELD_NUMBER: builtins.int
        @property
        def wired_tiger(self) -> global___MongodConfig3_6.Storage.WiredTiger:
            """Configuration of the WiredTiger storage engine."""

        @property
        def journal(self) -> global___MongodConfig3_6.Storage.Journal:
            """Configuration of the MongoDB [journal](https://docs.mongodb.com/v3.6/reference/glossary/#term-journal)."""

        def __init__(
            self,
            *,
            wired_tiger: global___MongodConfig3_6.Storage.WiredTiger | None = ...,
            journal: global___MongodConfig3_6.Storage.Journal | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["journal", b"journal", "wired_tiger", b"wired_tiger"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["journal", b"journal", "wired_tiger", b"wired_tiger"]) -> None: ...

    @typing.final
    class OperationProfiling(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _Mode:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongodConfig3_6.OperationProfiling._Mode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            MODE_UNSPECIFIED: MongodConfig3_6.OperationProfiling._Mode.ValueType  # 0
            OFF: MongodConfig3_6.OperationProfiling._Mode.ValueType  # 1
            """The profiler is off and does not collect any data."""
            SLOW_OP: MongodConfig3_6.OperationProfiling._Mode.ValueType  # 2
            """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""
            ALL: MongodConfig3_6.OperationProfiling._Mode.ValueType  # 3
            """The profiler collects data for all operations."""

        class Mode(_Mode, metaclass=_ModeEnumTypeWrapper): ...
        MODE_UNSPECIFIED: MongodConfig3_6.OperationProfiling.Mode.ValueType  # 0
        OFF: MongodConfig3_6.OperationProfiling.Mode.ValueType  # 1
        """The profiler is off and does not collect any data."""
        SLOW_OP: MongodConfig3_6.OperationProfiling.Mode.ValueType  # 2
        """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""
        ALL: MongodConfig3_6.OperationProfiling.Mode.ValueType  # 3
        """The profiler collects data for all operations."""

        MODE_FIELD_NUMBER: builtins.int
        SLOW_OP_THRESHOLD_FIELD_NUMBER: builtins.int
        mode: global___MongodConfig3_6.OperationProfiling.Mode.ValueType
        """Mode which specifies operations that should be profiled."""
        @property
        def slow_op_threshold(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The slow operation time threshold, in milliseconds. Operations that run
            for longer than this threshold are considered slow, and are processed by the profiler
            running in the SLOW_OP mode.
            """

        def __init__(
            self,
            *,
            mode: global___MongodConfig3_6.OperationProfiling.Mode.ValueType = ...,
            slow_op_threshold: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["slow_op_threshold", b"slow_op_threshold"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["mode", b"mode", "slow_op_threshold", b"slow_op_threshold"]) -> None: ...

    @typing.final
    class Network(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MAX_INCOMING_CONNECTIONS_FIELD_NUMBER: builtins.int
        @property
        def max_incoming_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The maximum number of simultaneous connections that mongod will accept."""

        def __init__(
            self,
            *,
            max_incoming_connections: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["max_incoming_connections", b"max_incoming_connections"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["max_incoming_connections", b"max_incoming_connections"]) -> None: ...

    STORAGE_FIELD_NUMBER: builtins.int
    OPERATION_PROFILING_FIELD_NUMBER: builtins.int
    NET_FIELD_NUMBER: builtins.int
    @property
    def storage(self) -> global___MongodConfig3_6.Storage:
        """`storage` section of mongod configuration."""

    @property
    def operation_profiling(self) -> global___MongodConfig3_6.OperationProfiling:
        """`operationProfiling` section of mongod configuration."""

    @property
    def net(self) -> global___MongodConfig3_6.Network:
        """`net` section of mongod configuration."""

    def __init__(
        self,
        *,
        storage: global___MongodConfig3_6.Storage | None = ...,
        operation_profiling: global___MongodConfig3_6.OperationProfiling | None = ...,
        net: global___MongodConfig3_6.Network | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["net", b"net", "operation_profiling", b"operation_profiling", "storage", b"storage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["net", b"net", "operation_profiling", b"operation_profiling", "storage", b"storage"]) -> None: ...

global___MongodConfig3_6 = MongodConfig3_6

@typing.final
class MongoCfgConfig3_6(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Storage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing.final
        class WiredTiger(google.protobuf.message.Message):
            """Configuration of WiredTiger storage engine."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            @typing.final
            class EngineConfig(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                CACHE_SIZE_GB_FIELD_NUMBER: builtins.int
                @property
                def cache_size_gb(self) -> google.protobuf.wrappers_pb2.DoubleValue:
                    """The maximum size of the internal cache that WiredTiger will use for all data."""

                def __init__(
                    self,
                    *,
                    cache_size_gb: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
                ) -> None: ...
                def HasField(self, field_name: typing.Literal["cache_size_gb", b"cache_size_gb"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing.Literal["cache_size_gb", b"cache_size_gb"]) -> None: ...

            ENGINE_CONFIG_FIELD_NUMBER: builtins.int
            @property
            def engine_config(self) -> global___MongoCfgConfig3_6.Storage.WiredTiger.EngineConfig:
                """Engine configuration for WiredTiger."""

            def __init__(
                self,
                *,
                engine_config: global___MongoCfgConfig3_6.Storage.WiredTiger.EngineConfig | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["engine_config", b"engine_config"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["engine_config", b"engine_config"]) -> None: ...

        WIRED_TIGER_FIELD_NUMBER: builtins.int
        @property
        def wired_tiger(self) -> global___MongoCfgConfig3_6.Storage.WiredTiger:
            """Configuration of the WiredTiger storage engine."""

        def __init__(
            self,
            *,
            wired_tiger: global___MongoCfgConfig3_6.Storage.WiredTiger | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["wired_tiger", b"wired_tiger"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["wired_tiger", b"wired_tiger"]) -> None: ...

    @typing.final
    class OperationProfiling(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _Mode:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongoCfgConfig3_6.OperationProfiling._Mode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            MODE_UNSPECIFIED: MongoCfgConfig3_6.OperationProfiling._Mode.ValueType  # 0
            OFF: MongoCfgConfig3_6.OperationProfiling._Mode.ValueType  # 1
            """The profiler is off and does not collect any data. This is the default
            profiler level.
            """
            SLOW_OP: MongoCfgConfig3_6.OperationProfiling._Mode.ValueType  # 2
            """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""
            ALL: MongoCfgConfig3_6.OperationProfiling._Mode.ValueType  # 3
            """The profiler collects data for all operations."""

        class Mode(_Mode, metaclass=_ModeEnumTypeWrapper): ...
        MODE_UNSPECIFIED: MongoCfgConfig3_6.OperationProfiling.Mode.ValueType  # 0
        OFF: MongoCfgConfig3_6.OperationProfiling.Mode.ValueType  # 1
        """The profiler is off and does not collect any data. This is the default
        profiler level.
        """
        SLOW_OP: MongoCfgConfig3_6.OperationProfiling.Mode.ValueType  # 2
        """The profiler collects data for operations that take longer than the value of [slow_op_threshold]."""
        ALL: MongoCfgConfig3_6.OperationProfiling.Mode.ValueType  # 3
        """The profiler collects data for all operations."""

        MODE_FIELD_NUMBER: builtins.int
        SLOW_OP_THRESHOLD_FIELD_NUMBER: builtins.int
        mode: global___MongoCfgConfig3_6.OperationProfiling.Mode.ValueType
        """Operation profiling level. For details, see [MongoDB documentation](https://docs.mongodb.com/v3.6/tutorial/manage-the-database-profiler/)."""
        @property
        def slow_op_threshold(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The slow operation time threshold, in milliseconds. Operations that run
            for longer than this threshold are considered slow, and are processed by the profiler
            running in the SLOW_OP mode. For details see [MongoDB documentation](https://docs.mongodb.com/v3.6/reference/configuration-options/#operationProfiling.slowOpThresholdMs).
            """

        def __init__(
            self,
            *,
            mode: global___MongoCfgConfig3_6.OperationProfiling.Mode.ValueType = ...,
            slow_op_threshold: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["slow_op_threshold", b"slow_op_threshold"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["mode", b"mode", "slow_op_threshold", b"slow_op_threshold"]) -> None: ...

    @typing.final
    class Network(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MAX_INCOMING_CONNECTIONS_FIELD_NUMBER: builtins.int
        @property
        def max_incoming_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The maximum number of incoming connections."""

        def __init__(
            self,
            *,
            max_incoming_connections: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["max_incoming_connections", b"max_incoming_connections"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["max_incoming_connections", b"max_incoming_connections"]) -> None: ...

    STORAGE_FIELD_NUMBER: builtins.int
    OPERATION_PROFILING_FIELD_NUMBER: builtins.int
    NET_FIELD_NUMBER: builtins.int
    @property
    def storage(self) -> global___MongoCfgConfig3_6.Storage:
        """`storage` section of mongocfg configuration."""

    @property
    def operation_profiling(self) -> global___MongoCfgConfig3_6.OperationProfiling:
        """`operationProfiling` section of mongocfg configuration."""

    @property
    def net(self) -> global___MongoCfgConfig3_6.Network:
        """`net` section of mongocfg configuration."""

    def __init__(
        self,
        *,
        storage: global___MongoCfgConfig3_6.Storage | None = ...,
        operation_profiling: global___MongoCfgConfig3_6.OperationProfiling | None = ...,
        net: global___MongoCfgConfig3_6.Network | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["net", b"net", "operation_profiling", b"operation_profiling", "storage", b"storage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["net", b"net", "operation_profiling", b"operation_profiling", "storage", b"storage"]) -> None: ...

global___MongoCfgConfig3_6 = MongoCfgConfig3_6

@typing.final
class MongosConfig3_6(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Network(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MAX_INCOMING_CONNECTIONS_FIELD_NUMBER: builtins.int
        @property
        def max_incoming_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The maximum number of incoming connections."""

        def __init__(
            self,
            *,
            max_incoming_connections: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["max_incoming_connections", b"max_incoming_connections"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["max_incoming_connections", b"max_incoming_connections"]) -> None: ...

    NET_FIELD_NUMBER: builtins.int
    @property
    def net(self) -> global___MongosConfig3_6.Network:
        """Network settings for mongos."""

    def __init__(
        self,
        *,
        net: global___MongosConfig3_6.Network | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["net", b"net"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["net", b"net"]) -> None: ...

global___MongosConfig3_6 = MongosConfig3_6

@typing.final
class MongodConfigSet3_6(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MongodConfig3_6:
        """Effective mongod settings for a MongoDB 3.6 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """

    @property
    def user_config(self) -> global___MongodConfig3_6:
        """User-defined mongod settings for a MongoDB 3.6 cluster."""

    @property
    def default_config(self) -> global___MongodConfig3_6:
        """Default mongod configuration for a MongoDB 3.6 cluster."""

    def __init__(
        self,
        *,
        effective_config: global___MongodConfig3_6 | None = ...,
        user_config: global___MongodConfig3_6 | None = ...,
        default_config: global___MongodConfig3_6 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___MongodConfigSet3_6 = MongodConfigSet3_6

@typing.final
class MongoCfgConfigSet3_6(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MongoCfgConfig3_6:
        """Effective mongocfg settings for a MongoDB 3.6 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """

    @property
    def user_config(self) -> global___MongoCfgConfig3_6:
        """User-defined mongocfg settings for a MongoDB 3.6 cluster."""

    @property
    def default_config(self) -> global___MongoCfgConfig3_6:
        """Default mongocfg configuration for a MongoDB 3.6 cluster."""

    def __init__(
        self,
        *,
        effective_config: global___MongoCfgConfig3_6 | None = ...,
        user_config: global___MongoCfgConfig3_6 | None = ...,
        default_config: global___MongoCfgConfig3_6 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___MongoCfgConfigSet3_6 = MongoCfgConfigSet3_6

@typing.final
class MongosConfigSet3_6(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MongosConfig3_6:
        """Effective settings for a MongoDB 3.6 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """

    @property
    def user_config(self) -> global___MongosConfig3_6:
        """User-defined settings for a MongoDB 3.6 cluster."""

    @property
    def default_config(self) -> global___MongosConfig3_6:
        """Default configuration for a MongoDB 3.6 cluster."""

    def __init__(
        self,
        *,
        effective_config: global___MongosConfig3_6 | None = ...,
        user_config: global___MongosConfig3_6 | None = ...,
        default_config: global___MongosConfig3_6 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___MongosConfigSet3_6 = MongosConfigSet3_6