"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import nebius.common.v1.metadata_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GpuCluster(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> global___GpuClusterSpec: ...
    @property
    def status(self) -> global___GpuClusterStatus: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: global___GpuClusterSpec | None = ...,
        status: global___GpuClusterStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> None: ...

global___GpuCluster = GpuCluster

@typing.final
class GpuClusterSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFINIBAND_FABRIC_FIELD_NUMBER: builtins.int
    infiniband_fabric: builtins.str
    def __init__(
        self,
        *,
        infiniband_fabric: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["infiniband_fabric", b"infiniband_fabric"]) -> None: ...

global___GpuClusterSpec = GpuClusterSpec

@typing.final
class GpuClusterStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INSTANCES_FIELD_NUMBER: builtins.int
    RECONCILING_FIELD_NUMBER: builtins.int
    reconciling: builtins.bool
    """Indicates whether there is an ongoing operation"""
    @property
    def instances(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        instances: collections.abc.Iterable[builtins.str] | None = ...,
        reconciling: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["instances", b"instances", "reconciling", b"reconciling"]) -> None: ...

global___GpuClusterStatus = GpuClusterStatus
