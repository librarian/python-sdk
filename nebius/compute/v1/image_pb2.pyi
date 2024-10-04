"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
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
class Image(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> global___ImageSpec: ...
    @property
    def status(self) -> global___ImageStatus: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: global___ImageSpec | None = ...,
        status: global___ImageStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> None: ...

global___Image = Image

@typing.final
class ImageSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESCRIPTION_FIELD_NUMBER: builtins.int
    IMAGE_FAMILY_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    description: builtins.str
    image_family: builtins.str
    version: builtins.str
    def __init__(
        self,
        *,
        description: builtins.str | None = ...,
        image_family: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_description", b"_description", "description", b"description"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_description", b"_description", "description", b"description", "image_family", b"image_family", "version", b"version"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_description", b"_description"]) -> typing.Literal["description"] | None: ...

global___ImageSpec = ImageSpec

@typing.final
class ImageStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ImageStatus._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSPECIFIED: ImageStatus._State.ValueType  # 0
        CREATING: ImageStatus._State.ValueType  # 1
        READY: ImageStatus._State.ValueType  # 2
        UPDATING: ImageStatus._State.ValueType  # 3
        DELETING: ImageStatus._State.ValueType  # 4
        ERROR: ImageStatus._State.ValueType  # 5

    class State(_State, metaclass=_StateEnumTypeWrapper): ...
    UNSPECIFIED: ImageStatus.State.ValueType  # 0
    CREATING: ImageStatus.State.ValueType  # 1
    READY: ImageStatus.State.ValueType  # 2
    UPDATING: ImageStatus.State.ValueType  # 3
    DELETING: ImageStatus.State.ValueType  # 4
    ERROR: ImageStatus.State.ValueType  # 5

    STATE_FIELD_NUMBER: builtins.int
    STATE_DESCRIPTION_FIELD_NUMBER: builtins.int
    STORAGE_SIZE_BYTES_FIELD_NUMBER: builtins.int
    MIN_DISK_SIZE_BYTES_FIELD_NUMBER: builtins.int
    RECONCILING_FIELD_NUMBER: builtins.int
    state: global___ImageStatus.State.ValueType
    state_description: builtins.str
    storage_size_bytes: builtins.int
    min_disk_size_bytes: builtins.int
    reconciling: builtins.bool
    """Indicates whether there is an ongoing operation"""
    def __init__(
        self,
        *,
        state: global___ImageStatus.State.ValueType = ...,
        state_description: builtins.str = ...,
        storage_size_bytes: builtins.int = ...,
        min_disk_size_bytes: builtins.int = ...,
        reconciling: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["min_disk_size_bytes", b"min_disk_size_bytes", "reconciling", b"reconciling", "state", b"state", "state_description", b"state_description", "storage_size_bytes", b"storage_size_bytes"]) -> None: ...

global___ImageStatus = ImageStatus
