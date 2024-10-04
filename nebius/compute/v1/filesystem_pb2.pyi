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
import nebius.common.v1.metadata_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Filesystem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> global___FilesystemSpec: ...
    @property
    def status(self) -> global___FilesystemStatus: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: global___FilesystemSpec | None = ...,
        status: global___FilesystemStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> None: ...

global___Filesystem = Filesystem

@typing.final
class FilesystemSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _FilesystemType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _FilesystemTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FilesystemSpec._FilesystemType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSPECIFIED: FilesystemSpec._FilesystemType.ValueType  # 0
        NETWORK_SSD: FilesystemSpec._FilesystemType.ValueType  # 1
        """the list of available types will be clarified later, it is not final version"""
        NETWORK_HDD: FilesystemSpec._FilesystemType.ValueType  # 2

    class FilesystemType(_FilesystemType, metaclass=_FilesystemTypeEnumTypeWrapper): ...
    UNSPECIFIED: FilesystemSpec.FilesystemType.ValueType  # 0
    NETWORK_SSD: FilesystemSpec.FilesystemType.ValueType  # 1
    """the list of available types will be clarified later, it is not final version"""
    NETWORK_HDD: FilesystemSpec.FilesystemType.ValueType  # 2

    SIZE_BYTES_FIELD_NUMBER: builtins.int
    SIZE_KIBIBYTES_FIELD_NUMBER: builtins.int
    SIZE_MEBIBYTES_FIELD_NUMBER: builtins.int
    SIZE_GIBIBYTES_FIELD_NUMBER: builtins.int
    BLOCK_SIZE_BYTES_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    size_bytes: builtins.int
    size_kibibytes: builtins.int
    size_mebibytes: builtins.int
    size_gibibytes: builtins.int
    block_size_bytes: builtins.int
    type: global___FilesystemSpec.FilesystemType.ValueType
    def __init__(
        self,
        *,
        size_bytes: builtins.int = ...,
        size_kibibytes: builtins.int = ...,
        size_mebibytes: builtins.int = ...,
        size_gibibytes: builtins.int = ...,
        block_size_bytes: builtins.int = ...,
        type: global___FilesystemSpec.FilesystemType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["size", b"size", "size_bytes", b"size_bytes", "size_gibibytes", b"size_gibibytes", "size_kibibytes", b"size_kibibytes", "size_mebibytes", b"size_mebibytes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["block_size_bytes", b"block_size_bytes", "size", b"size", "size_bytes", b"size_bytes", "size_gibibytes", b"size_gibibytes", "size_kibibytes", b"size_kibibytes", "size_mebibytes", b"size_mebibytes", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["size", b"size"]) -> typing.Literal["size_bytes", "size_kibibytes", "size_mebibytes", "size_gibibytes"] | None: ...

global___FilesystemSpec = FilesystemSpec

@typing.final
class FilesystemStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FilesystemStatus._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSPECIFIED: FilesystemStatus._State.ValueType  # 0
        CREATING: FilesystemStatus._State.ValueType  # 1
        READY: FilesystemStatus._State.ValueType  # 2
        UPDATING: FilesystemStatus._State.ValueType  # 3
        DELETING: FilesystemStatus._State.ValueType  # 4
        ERROR: FilesystemStatus._State.ValueType  # 5

    class State(_State, metaclass=_StateEnumTypeWrapper): ...
    UNSPECIFIED: FilesystemStatus.State.ValueType  # 0
    CREATING: FilesystemStatus.State.ValueType  # 1
    READY: FilesystemStatus.State.ValueType  # 2
    UPDATING: FilesystemStatus.State.ValueType  # 3
    DELETING: FilesystemStatus.State.ValueType  # 4
    ERROR: FilesystemStatus.State.ValueType  # 5

    STATE_FIELD_NUMBER: builtins.int
    STATE_DESCRIPTION_FIELD_NUMBER: builtins.int
    READ_WRITE_ATTACHMENTS_FIELD_NUMBER: builtins.int
    READ_ONLY_ATTACHMENTS_FIELD_NUMBER: builtins.int
    SIZE_BYTES_FIELD_NUMBER: builtins.int
    RECONCILING_FIELD_NUMBER: builtins.int
    state: global___FilesystemStatus.State.ValueType
    state_description: builtins.str
    size_bytes: builtins.int
    reconciling: builtins.bool
    """Indicates whether there is an ongoing operation"""
    @property
    def read_write_attachments(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def read_only_attachments(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        state: global___FilesystemStatus.State.ValueType = ...,
        state_description: builtins.str = ...,
        read_write_attachments: collections.abc.Iterable[builtins.str] | None = ...,
        read_only_attachments: collections.abc.Iterable[builtins.str] | None = ...,
        size_bytes: builtins.int = ...,
        reconciling: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["read_only_attachments", b"read_only_attachments", "read_write_attachments", b"read_write_attachments", "reconciling", b"reconciling", "size_bytes", b"size_bytes", "state", b"state", "state_description", b"state_description"]) -> None: ...

global___FilesystemStatus = FilesystemStatus
