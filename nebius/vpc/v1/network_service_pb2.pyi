"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import nebius.vpc.v1.network_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetNetworkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___GetNetworkRequest = GetNetworkRequest

@typing.final
class GetNetworkByNameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    parent_id: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        parent_id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "parent_id", b"parent_id"]) -> None: ...

global___GetNetworkByNameRequest = GetNetworkByNameRequest

@typing.final
class ListNetworksRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARENT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent_id: builtins.str
    page_size: builtins.int
    page_token: builtins.str
    def __init__(
        self,
        *,
        parent_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "parent_id", b"parent_id"]) -> None: ...

global___ListNetworksRequest = ListNetworksRequest

@typing.final
class ListNetworksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[nebius.vpc.v1.network_pb2.Network]: ...
    def __init__(
        self,
        *,
        items: collections.abc.Iterable[nebius.vpc.v1.network_pb2.Network] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["items", b"items", "next_page_token", b"next_page_token"]) -> None: ...

global___ListNetworksResponse = ListNetworksResponse