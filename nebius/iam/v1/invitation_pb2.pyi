"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import nebius.common.v1.metadata_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Invitation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata: ...
    @property
    def spec(self) -> global___InvitationSpec: ...
    @property
    def status(self) -> global___InvitationStatus: ...
    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: global___InvitationSpec | None = ...,
        status: global___InvitationStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> None: ...

global___Invitation = Invitation

@typing.final
class InvitationSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESCRIPTION_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    description: builtins.str
    email: builtins.str
    def __init__(
        self,
        *,
        description: builtins.str = ...,
        email: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["contact", b"contact", "email", b"email"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["contact", b"contact", "description", b"description", "email", b"email"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["contact", b"contact"]) -> typing.Literal["email"] | None: ...

global___InvitationSpec = InvitationSpec

@typing.final
class InvitationStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[InvitationStatus._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSPECIFIED: InvitationStatus._State.ValueType  # 0
        CREATING: InvitationStatus._State.ValueType  # 4
        """contacts data is not stored in pds yet. probably will GC it later"""
        CREATED: InvitationStatus._State.ValueType  # 5
        """notification is not sent yet"""
        PENDING: InvitationStatus._State.ValueType  # 1
        """notification is sent, we are waiting for the user to approve the notification"""
        EXPIRED: InvitationStatus._State.ValueType  # 2
        """notification is expired, accept is no longer possible"""
        ACCEPTED: InvitationStatus._State.ValueType  # 3
        """notification is accepted"""

    class State(_State, metaclass=_StateEnumTypeWrapper): ...
    UNSPECIFIED: InvitationStatus.State.ValueType  # 0
    CREATING: InvitationStatus.State.ValueType  # 4
    """contacts data is not stored in pds yet. probably will GC it later"""
    CREATED: InvitationStatus.State.ValueType  # 5
    """notification is not sent yet"""
    PENDING: InvitationStatus.State.ValueType  # 1
    """notification is sent, we are waiting for the user to approve the notification"""
    EXPIRED: InvitationStatus.State.ValueType  # 2
    """notification is expired, accept is no longer possible"""
    ACCEPTED: InvitationStatus.State.ValueType  # 3
    """notification is accepted"""

    TENANT_USER_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    tenant_user_account_id: builtins.str
    state: global___InvitationStatus.State.ValueType
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        tenant_user_account_id: builtins.str = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        state: global___InvitationStatus.State.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expires_at", b"expires_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["expires_at", b"expires_at", "state", b"state", "tenant_user_account_id", b"tenant_user_account_id"]) -> None: ...

global___InvitationStatus = InvitationStatus
