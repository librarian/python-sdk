"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import nebius.common.v1.metadata_pb2
import nebius.vpc.v1.pool_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Allocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> nebius.common.v1.metadata_pb2.ResourceMetadata:
        """Metadata for the Allocation.
        `metadata.parent_id` represents IAM Container.
        """

    @property
    def spec(self) -> global___AllocationSpec:
        """Specifications for the allocation, detailing its name and IP configuration."""

    @property
    def status(self) -> global___AllocationStatus:
        """Contains the current status of the allocation, indicating its state and any additional details."""

    def __init__(
        self,
        *,
        metadata: nebius.common.v1.metadata_pb2.ResourceMetadata | None = ...,
        spec: global___AllocationSpec | None = ...,
        status: global___AllocationStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "spec", b"spec", "status", b"status"]) -> None: ...

global___Allocation = Allocation

@typing.final
class AllocationSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IPV4_PRIVATE_FIELD_NUMBER: builtins.int
    IPV4_PUBLIC_FIELD_NUMBER: builtins.int
    @property
    def ipv4_private(self) -> global___IPv4PrivateAllocationSpec: ...
    @property
    def ipv4_public(self) -> global___IPv4PublicAllocationSpec: ...
    def __init__(
        self,
        *,
        ipv4_private: global___IPv4PrivateAllocationSpec | None = ...,
        ipv4_public: global___IPv4PublicAllocationSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ip_spec", b"ip_spec", "ipv4_private", b"ipv4_private", "ipv4_public", b"ipv4_public"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ip_spec", b"ip_spec", "ipv4_private", b"ipv4_private", "ipv4_public", b"ipv4_public"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["ip_spec", b"ip_spec"]) -> typing.Literal["ipv4_private", "ipv4_public"] | None: ...

global___AllocationSpec = AllocationSpec

@typing.final
class IPv4PrivateAllocationSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CIDR_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    POOL_ID_FIELD_NUMBER: builtins.int
    cidr: builtins.str
    """CIDR block for IPv4 Allocation.
    May be a single IP address (such as 10.2.3.4),
    a prefix length (such as /24) or a CIDR-formatted string (such as 10.1.2.0/24).
    Random address (/32) from pool would be allocated if field is omitted.
    """
    subnet_id: builtins.str
    """Subnet ID.
    Required same subnet to use allocation in subnet-resources (e.g. Network Interface)
    """
    pool_id: builtins.str
    """Pool for the IPv4 private allocation."""
    def __init__(
        self,
        *,
        cidr: builtins.str = ...,
        subnet_id: builtins.str = ...,
        pool_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pool", b"pool", "pool_id", b"pool_id", "subnet_id", b"subnet_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cidr", b"cidr", "pool", b"pool", "pool_id", b"pool_id", "subnet_id", b"subnet_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["pool", b"pool"]) -> typing.Literal["subnet_id", "pool_id"] | None: ...

global___IPv4PrivateAllocationSpec = IPv4PrivateAllocationSpec

@typing.final
class IPv4PublicAllocationSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CIDR_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    POOL_ID_FIELD_NUMBER: builtins.int
    cidr: builtins.str
    """CIDR block for IPv4 Allocation.
    May be a single IP address (such as 10.2.3.4),
    a prefix length (such as /32) or a CIDR-formatted string (such as 10.1.2.0/32).
    Random address (/32) from pool would be allocated if field is omitted.
    """
    subnet_id: builtins.str
    """Subnet ID.
    Required same subnet to use allocation in subnet-resources (e.g. Network Interface)
    """
    pool_id: builtins.str
    """Pool for the IPv4 private allocation."""
    def __init__(
        self,
        *,
        cidr: builtins.str = ...,
        subnet_id: builtins.str = ...,
        pool_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pool", b"pool", "pool_id", b"pool_id", "subnet_id", b"subnet_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cidr", b"cidr", "pool", b"pool", "pool_id", b"pool_id", "subnet_id", b"subnet_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["pool", b"pool"]) -> typing.Literal["subnet_id", "pool_id"] | None: ...

global___IPv4PublicAllocationSpec = IPv4PublicAllocationSpec

@typing.final
class AllocationStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AllocationStatus._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATE_UNSPECIFIED: AllocationStatus._State.ValueType  # 0
        """Default state, unspecified."""
        CREATING: AllocationStatus._State.ValueType  # 1
        """Allocation is being created."""
        ALLOCATED: AllocationStatus._State.ValueType  # 2
        """Allocation is ready for use."""
        ASSIGNED: AllocationStatus._State.ValueType  # 3
        """Allocation is used."""
        DELETING: AllocationStatus._State.ValueType  # 4
        """Allocation is being deleted."""

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """Enumeration of possible states of the Allocation."""

    STATE_UNSPECIFIED: AllocationStatus.State.ValueType  # 0
    """Default state, unspecified."""
    CREATING: AllocationStatus.State.ValueType  # 1
    """Allocation is being created."""
    ALLOCATED: AllocationStatus.State.ValueType  # 2
    """Allocation is ready for use."""
    ASSIGNED: AllocationStatus.State.ValueType  # 3
    """Allocation is used."""
    DELETING: AllocationStatus.State.ValueType  # 4
    """Allocation is being deleted."""

    STATE_FIELD_NUMBER: builtins.int
    DETAILS_FIELD_NUMBER: builtins.int
    ASSIGNMENT_FIELD_NUMBER: builtins.int
    STATIC_FIELD_NUMBER: builtins.int
    state: global___AllocationStatus.State.ValueType
    """This field represents the current state of the allocation."""
    static: builtins.bool
    """If false - Lifecycle of allocation depends on resource that using it."""
    @property
    def details(self) -> global___AllocationDetails:
        """Detailed information about the allocation status,
        including the allocated CIDR, pool ID and IP version.
        """

    @property
    def assignment(self) -> global___Assignment:
        """Information about the assignment associated with the allocation,
        such as network interface or load balancer assignment.
        """

    def __init__(
        self,
        *,
        state: global___AllocationStatus.State.ValueType = ...,
        details: global___AllocationDetails | None = ...,
        assignment: global___Assignment | None = ...,
        static: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["assignment", b"assignment", "details", b"details"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assignment", b"assignment", "details", b"details", "state", b"state", "static", b"static"]) -> None: ...

global___AllocationStatus = AllocationStatus

@typing.final
class AllocationDetails(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOCATED_CIDR_FIELD_NUMBER: builtins.int
    POOL_ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    allocated_cidr: builtins.str
    pool_id: builtins.str
    version: nebius.vpc.v1.pool_pb2.IpVersion.ValueType
    def __init__(
        self,
        *,
        allocated_cidr: builtins.str = ...,
        pool_id: builtins.str = ...,
        version: nebius.vpc.v1.pool_pb2.IpVersion.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["allocated_cidr", b"allocated_cidr", "pool_id", b"pool_id", "version", b"version"]) -> None: ...

global___AllocationDetails = AllocationDetails

@typing.final
class Assignment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_INTERFACE_FIELD_NUMBER: builtins.int
    LOAD_BALANCER_FIELD_NUMBER: builtins.int
    @property
    def network_interface(self) -> global___NetworkInterfaceAssignment: ...
    @property
    def load_balancer(self) -> global___LoadBalancerAssignment: ...
    def __init__(
        self,
        *,
        network_interface: global___NetworkInterfaceAssignment | None = ...,
        load_balancer: global___LoadBalancerAssignment | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["load_balancer", b"load_balancer", "network_interface", b"network_interface", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["load_balancer", b"load_balancer", "network_interface", b"network_interface", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["network_interface", "load_balancer"] | None: ...

global___Assignment = Assignment

@typing.final
class NetworkInterfaceAssignment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INSTANCE_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    instance_id: builtins.str
    """ID of the Compute instance network interface belongs to."""
    name: builtins.str
    """Network interface name"""
    def __init__(
        self,
        *,
        instance_id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["instance_id", b"instance_id", "name", b"name"]) -> None: ...

global___NetworkInterfaceAssignment = NetworkInterfaceAssignment

@typing.final
class LoadBalancerAssignment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the Load Balancer."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___LoadBalancerAssignment = LoadBalancerAssignment