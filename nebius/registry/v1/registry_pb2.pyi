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
class Registry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata:
        """This is metadata about the resource, such as its id, name, labels, etc.
        This contains fields that may be updated both by the end user and the system.
        """

    @property
    def spec(self) -> global___RegistrySpec:
        """This is defined by the user and describes the desired state of system.
        Fill this in when creating or updating an object.
        """

    @property
    def status(self) -> global___RegistryStatus:
        """This is filled in by the server and reports the current state of the system."""

    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: global___RegistrySpec | None = ...,
        status: global___RegistryStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> None: ...

global___Registry = Registry

@typing.final
class RegistrySpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESCRIPTION_FIELD_NUMBER: builtins.int
    IMAGES_COUNT_FIELD_NUMBER: builtins.int
    description: builtins.str
    images_count: builtins.int
    """ Registry.Type type = 2;"""
    def __init__(
        self,
        *,
        description: builtins.str = ...,
        images_count: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "images_count", b"images_count"]) -> None: ...

global___RegistrySpec = RegistrySpec

@typing.final
class RegistryStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RegistryStatus._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CREATING: RegistryStatus._State.ValueType  # 0
        ACTIVE: RegistryStatus._State.ValueType  # 1
        DELETING: RegistryStatus._State.ValueType  # 2
        SUSPENDED: RegistryStatus._State.ValueType  # 3

    class State(_State, metaclass=_StateEnumTypeWrapper): ...
    CREATING: RegistryStatus.State.ValueType  # 0
    ACTIVE: RegistryStatus.State.ValueType  # 1
    DELETING: RegistryStatus.State.ValueType  # 2
    SUSPENDED: RegistryStatus.State.ValueType  # 3

    STATE_FIELD_NUMBER: builtins.int
    state: global___RegistryStatus.State.ValueType
    def __init__(
        self,
        *,
        state: global___RegistryStatus.State.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["state", b"state"]) -> None: ...

global___RegistryStatus = RegistryStatus
