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
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _GpuInterconnectType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _GpuInterconnectTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_GpuInterconnectType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    GPU_INTERCONNECT_TYPE_UNSPECIFIED: _GpuInterconnectType.ValueType  # 0
    INFINIBAND: _GpuInterconnectType.ValueType  # 1
    """InfiniBand interconnect."""

class GpuInterconnectType(_GpuInterconnectType, metaclass=_GpuInterconnectTypeEnumTypeWrapper): ...

GPU_INTERCONNECT_TYPE_UNSPECIFIED: GpuInterconnectType.ValueType  # 0
INFINIBAND: GpuInterconnectType.ValueType  # 1
"""InfiniBand interconnect."""
global___GpuInterconnectType = GpuInterconnectType

@typing.final
class GpuCluster(google.protobuf.message.Message):
    """A GPU cluster. For details about the concept, see [documentation](/docs/compute/concepts/gpu-cluster)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[GpuCluster._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: GpuCluster._Status.ValueType  # 0
        CREATING: GpuCluster._Status.ValueType  # 1
        """GPU cluster is being created."""
        READY: GpuCluster._Status.ValueType  # 2
        """GPU cluster is ready to use."""
        ERROR: GpuCluster._Status.ValueType  # 3
        """GPU cluster encountered a problem and cannot operate."""
        DELETING: GpuCluster._Status.ValueType  # 4
        """GPU cluster is being deleted."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: GpuCluster.Status.ValueType  # 0
    CREATING: GpuCluster.Status.ValueType  # 1
    """GPU cluster is being created."""
    READY: GpuCluster.Status.ValueType  # 2
    """GPU cluster is ready to use."""
    ERROR: GpuCluster.Status.ValueType  # 3
    """GPU cluster encountered a problem and cannot operate."""
    DELETING: GpuCluster.Status.ValueType  # 4
    """GPU cluster is being deleted."""

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
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    INTERCONNECT_TYPE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of GPU cluster."""
    folder_id: builtins.str
    """ID of the folder that the GPU cluster belongs to."""
    name: builtins.str
    """Name of the GPU cluster.

    The name is unique within the folder.
    """
    description: builtins.str
    """Description of the GPU cluster."""
    status: global___GpuCluster.Status.ValueType
    """Status of the GPU cluster."""
    zone_id: builtins.str
    """ID of the availability zone where the GPU cluster resides."""
    interconnect_type: global___GpuInterconnectType.ValueType
    """Type of interconnect used for this GPU cluster."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """GPU cluster labels as `key:value` pairs."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        status: global___GpuCluster.Status.ValueType = ...,
        zone_id: builtins.str = ...,
        interconnect_type: global___GpuInterconnectType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "interconnect_type", b"interconnect_type", "labels", b"labels", "name", b"name", "status", b"status", "zone_id", b"zone_id"]) -> None: ...

global___GpuCluster = GpuCluster