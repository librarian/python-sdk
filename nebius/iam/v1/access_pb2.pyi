"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Account(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class UserAccount(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ID_FIELD_NUMBER: builtins.int
        id: builtins.str
        def __init__(
            self,
            *,
            id: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

    @typing.final
    class ServiceAccount(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ID_FIELD_NUMBER: builtins.int
        id: builtins.str
        def __init__(
            self,
            *,
            id: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

    @typing.final
    class AnonymousAccount(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    USER_ACCOUNT_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_FIELD_NUMBER: builtins.int
    ANONYMOUS_ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def user_account(self) -> global___Account.UserAccount: ...
    @property
    def service_account(self) -> global___Account.ServiceAccount: ...
    @property
    def anonymous_account(self) -> global___Account.AnonymousAccount: ...
    def __init__(
        self,
        *,
        user_account: global___Account.UserAccount | None = ...,
        service_account: global___Account.ServiceAccount | None = ...,
        anonymous_account: global___Account.AnonymousAccount | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["anonymous_account", b"anonymous_account", "service_account", b"service_account", "type", b"type", "user_account", b"user_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["anonymous_account", b"anonymous_account", "service_account", b"service_account", "type", b"type", "user_account", b"user_account"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["user_account", "service_account", "anonymous_account"] | None: ...

global___Account = Account
