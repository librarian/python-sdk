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
class Network(google.protobuf.message.Message):
    """Defines a Network, which serves as a virtual representation of a traditional LAN
    within a cloud environment.
    Networks facilitate communication between subnets.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata:
        """Metadata for the network resource.
        `metadata.parent_id` represents IAM container
        """

    @property
    def spec(self) -> global___NetworkSpec:
        """Specification of the network."""

    @property
    def status(self) -> global___NetworkStatus:
        """Status of the network."""

    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: global___NetworkSpec | None = ...,
        status: global___NetworkStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> None: ...

global___Network = Network

@typing.final
class NetworkSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IPV4_PRIVATE_POOLS_FIELD_NUMBER: builtins.int
    IPV4_PUBLIC_POOLS_FIELD_NUMBER: builtins.int
    @property
    def ipv4_private_pools(self) -> global___IPv4PrivateNetworkPools:
        """Pools for private ipv4 addresses.
        Default private pools will be created if not specified.
        """

    @property
    def ipv4_public_pools(self) -> global___IPv4PublicNetworkPools:
        """Pools for public ipv4 addresses.
        Default public pool will be used if not specified.
        """

    def __init__(
        self,
        *,
        ipv4_private_pools: global___IPv4PrivateNetworkPools | None = ...,
        ipv4_public_pools: global___IPv4PublicNetworkPools | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ipv4_private_pools", b"ipv4_private_pools", "ipv4_public_pools", b"ipv4_public_pools"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ipv4_private_pools", b"ipv4_private_pools", "ipv4_public_pools", b"ipv4_public_pools"]) -> None: ...

global___NetworkSpec = NetworkSpec

@typing.final
class IPv4PrivateNetworkPools(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOLS_FIELD_NUMBER: builtins.int
    @property
    def pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetworkPool]: ...
    def __init__(
        self,
        *,
        pools: collections.abc.Iterable[global___NetworkPool] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["pools", b"pools"]) -> None: ...

global___IPv4PrivateNetworkPools = IPv4PrivateNetworkPools

@typing.final
class IPv4PublicNetworkPools(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOLS_FIELD_NUMBER: builtins.int
    @property
    def pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetworkPool]: ...
    def __init__(
        self,
        *,
        pools: collections.abc.Iterable[global___NetworkPool] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["pools", b"pools"]) -> None: ...

global___IPv4PublicNetworkPools = IPv4PublicNetworkPools

@typing.final
class NetworkPool(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___NetworkPool = NetworkPool

@typing.final
class NetworkStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[NetworkStatus._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATE_UNSPECIFIED: NetworkStatus._State.ValueType  # 0
        """Default state, unspecified."""
        CREATING: NetworkStatus._State.ValueType  # 1
        """Network is being created."""
        READY: NetworkStatus._State.ValueType  # 2
        """Network is ready for use."""
        DELETING: NetworkStatus._State.ValueType  # 3
        """Network is being deleted."""

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """Enumeration of possible states of the network."""

    STATE_UNSPECIFIED: NetworkStatus.State.ValueType  # 0
    """Default state, unspecified."""
    CREATING: NetworkStatus.State.ValueType  # 1
    """Network is being created."""
    READY: NetworkStatus.State.ValueType  # 2
    """Network is ready for use."""
    DELETING: NetworkStatus.State.ValueType  # 3
    """Network is being deleted."""

    STATE_FIELD_NUMBER: builtins.int
    state: global___NetworkStatus.State.ValueType
    """Current state of the network."""
    def __init__(
        self,
        *,
        state: global___NetworkStatus.State.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["state", b"state"]) -> None: ...

global___NetworkStatus = NetworkStatus
