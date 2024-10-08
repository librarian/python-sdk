"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import nebius.iam.v1.service_account_pb2
import nebius.iam.v1.tenant_user_account_pb2
import nebius.iam.v1.user_account_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetProfileRequest = GetProfileRequest

@typing.final
class GetProfileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_PROFILE_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_PROFILE_FIELD_NUMBER: builtins.int
    ANONYMOUS_PROFILE_FIELD_NUMBER: builtins.int
    @property
    def user_profile(self) -> global___UserProfile: ...
    @property
    def service_account_profile(self) -> global___ServiceAccountProfile: ...
    @property
    def anonymous_profile(self) -> global___AnonymousAccount: ...
    def __init__(
        self,
        *,
        user_profile: global___UserProfile | None = ...,
        service_account_profile: global___ServiceAccountProfile | None = ...,
        anonymous_profile: global___AnonymousAccount | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["anonymous_profile", b"anonymous_profile", "profile", b"profile", "service_account_profile", b"service_account_profile", "user_profile", b"user_profile"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["anonymous_profile", b"anonymous_profile", "profile", b"profile", "service_account_profile", b"service_account_profile", "user_profile", b"user_profile"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["profile", b"profile"]) -> typing.Literal["user_profile", "service_account_profile", "anonymous_profile"] | None: ...

global___GetProfileResponse = GetProfileResponse

@typing.final
class UserProfile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    FEDERATION_INFO_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    RETRIEVING_ERROR_FIELD_NUMBER: builtins.int
    TENANTS_FIELD_NUMBER: builtins.int
    id: builtins.str
    @property
    def federation_info(self) -> nebius.iam.v1.user_account_pb2.UserAccountExternalId: ...
    @property
    def attributes(self) -> nebius.iam.v1.tenant_user_account_pb2.UserAttributes: ...
    @property
    def retrieving_error(self) -> nebius.iam.v1.tenant_user_account_pb2.Error: ...
    @property
    def tenants(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserTenantInfo]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        federation_info: nebius.iam.v1.user_account_pb2.UserAccountExternalId | None = ...,
        attributes: nebius.iam.v1.tenant_user_account_pb2.UserAttributes | None = ...,
        retrieving_error: nebius.iam.v1.tenant_user_account_pb2.Error | None = ...,
        tenants: collections.abc.Iterable[global___UserTenantInfo] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["attributes", b"attributes", "attributes_optional", b"attributes_optional", "federation_info", b"federation_info", "retrieving_error", b"retrieving_error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["attributes", b"attributes", "attributes_optional", b"attributes_optional", "federation_info", b"federation_info", "id", b"id", "retrieving_error", b"retrieving_error", "tenants", b"tenants"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["attributes_optional", b"attributes_optional"]) -> typing.Literal["attributes", "retrieving_error"] | None: ...

global___UserProfile = UserProfile

@typing.final
class UserTenantInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TENANT_ID_FIELD_NUMBER: builtins.int
    TENANT_USER_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    tenant_id: builtins.str
    tenant_user_account_id: builtins.str
    def __init__(
        self,
        *,
        tenant_id: builtins.str = ...,
        tenant_user_account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["tenant_id", b"tenant_id", "tenant_user_account_id", b"tenant_user_account_id"]) -> None: ...

global___UserTenantInfo = UserTenantInfo

@typing.final
class ServiceAccountProfile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> nebius.iam.v1.service_account_pb2.ServiceAccount: ...
    def __init__(
        self,
        *,
        info: nebius.iam.v1.service_account_pb2.ServiceAccount | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["info", b"info"]) -> None: ...

global___ServiceAccountProfile = ServiceAccountProfile

@typing.final
class AnonymousAccount(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AnonymousAccount = AnonymousAccount
