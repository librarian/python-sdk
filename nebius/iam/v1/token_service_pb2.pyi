"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ExchangeTokenRequest(google.protobuf.message.Message):
    """https://www.rfc-editor.org/rfc/rfc8693.html"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GRANT_TYPE_FIELD_NUMBER: builtins.int
    REQUESTED_TOKEN_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_TOKEN_FIELD_NUMBER: builtins.int
    SUBJECT_TOKEN_TYPE_FIELD_NUMBER: builtins.int
    SCOPES_FIELD_NUMBER: builtins.int
    AUDIENCE_FIELD_NUMBER: builtins.int
    ACTOR_TOKEN_FIELD_NUMBER: builtins.int
    ACTOR_TOKEN_TYPE_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    grant_type: builtins.str
    """required - urn:ietf:params:oauth:grant-type:token-exchange"""
    requested_token_type: builtins.str
    """optional type of requested token, default is urn:ietf:params:oauth:token-type:access_token"""
    subject_token: builtins.str
    """required - could be self signed JWT token"""
    subject_token_type: builtins.str
    """required, in case of jwt - urn:ietf:params:oauth:token-type:jwt"""
    audience: builtins.str
    """optional, name of the oauth client id on which this token will be used"""
    actor_token: builtins.str
    """optional, subject token for impersonation/delegation (who want to impersonate/delegate) in subject_token."""
    actor_token_type: builtins.str
    """optional, token type for the impersonation/delegation (who want to impersonate/delegate). Usually it's urn:ietf:params:oauth:token-type:access_token"""
    @property
    def scopes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """optional (scopes of the token)"""

    @property
    def resource(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """optional, list of resources approved to use by token, if applicable"""

    def __init__(
        self,
        *,
        grant_type: builtins.str = ...,
        requested_token_type: builtins.str = ...,
        subject_token: builtins.str = ...,
        subject_token_type: builtins.str = ...,
        scopes: collections.abc.Iterable[builtins.str] | None = ...,
        audience: builtins.str = ...,
        actor_token: builtins.str = ...,
        actor_token_type: builtins.str = ...,
        resource: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["actor_token", b"actor_token", "actor_token_type", b"actor_token_type", "audience", b"audience", "grant_type", b"grant_type", "requested_token_type", b"requested_token_type", "resource", b"resource", "scopes", b"scopes", "subject_token", b"subject_token", "subject_token_type", b"subject_token_type"]) -> None: ...

global___ExchangeTokenRequest = ExchangeTokenRequest

@typing.final
class CreateTokenResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCESS_TOKEN_FIELD_NUMBER: builtins.int
    ISSUED_TOKEN_TYPE_FIELD_NUMBER: builtins.int
    TOKEN_TYPE_FIELD_NUMBER: builtins.int
    EXPIRES_IN_FIELD_NUMBER: builtins.int
    SCOPES_FIELD_NUMBER: builtins.int
    access_token: builtins.str
    """required"""
    issued_token_type: builtins.str
    """required"""
    token_type: builtins.str
    """required - Bearer"""
    expires_in: builtins.int
    @property
    def scopes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        access_token: builtins.str = ...,
        issued_token_type: builtins.str = ...,
        token_type: builtins.str = ...,
        expires_in: builtins.int = ...,
        scopes: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["access_token", b"access_token", "expires_in", b"expires_in", "issued_token_type", b"issued_token_type", "scopes", b"scopes", "token_type", b"token_type"]) -> None: ...

global___CreateTokenResponse = CreateTokenResponse
