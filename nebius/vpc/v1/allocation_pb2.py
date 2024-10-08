# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/vpc/v1/allocation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from nebius import annotations_pb2 as nebius_dot_annotations__pb2
from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius.vpc.v1 import pool_pb2 as nebius_dot_vpc_dot_v1_dot_pool__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1enebius/vpc/v1/allocation.proto\x12\rnebius.vpc.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x18nebius/annotations.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a\x18nebius/vpc/v1/pool.proto\"\xa0\x01\n\nAllocation\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12+\n\x04spec\x18\x02 \x01(\x0b\x32\x1d.nebius.vpc.v1.AllocationSpec\x12/\n\x06status\x18\x03 \x01(\x0b\x32\x1f.nebius.vpc.v1.AllocationStatus\"\xb0\x01\n\x0e\x41llocationSpec\x12\x46\n\x0cipv4_private\x18\x01 \x01(\x0b\x32(.nebius.vpc.v1.IPv4PrivateAllocationSpecB\x04\xbaJ\x01\x06H\x00\x12\x44\n\x0bipv4_public\x18\x02 \x01(\x0b\x32\'.nebius.vpc.v1.IPv4PublicAllocationSpecB\x04\xbaJ\x01\x06H\x00\x42\x10\n\x07ip_spec\x12\x05\xbaH\x02\x08\x01\"\xab\x02\n\x19IPv4PrivateAllocationSpec\x12\xc6\x01\n\x04\x63idr\x18\x01 \x01(\tB\xb7\x01\xbaH\xaf\x01\xba\x01\xab\x01\n\x11string.valid_cidr\x12.value must be a valid IP address, CIDR or mask\x1a\x66this == \'\' || this.matches(\'^/([0-9]|[1-2][0-9]|3[0-2])$\') || this.isIp(4) || this.isIpPrefix(4, true)\xbaJ\x01\x02\x12\x19\n\tsubnet_id\x18\x02 \x01(\tB\x04\xbaJ\x01\x02H\x00\x12\x17\n\x07pool_id\x18\x03 \x01(\tB\x04\xbaJ\x01\x02H\x00\x42\x11\n\x04pool\x12\t\xbaH\x02\x08\x01\xbaJ\x01\x02\"\xaa\x02\n\x18IPv4PublicAllocationSpec\x12\xc6\x01\n\x04\x63idr\x18\x01 \x01(\tB\xb7\x01\xbaH\xaf\x01\xba\x01\xab\x01\n\x11string.valid_cidr\x12.value must be a valid IP address, CIDR or mask\x1a\x66this == \'\' || this.matches(\'^/([0-9]|[1-2][0-9]|3[0-2])$\') || this.isIp(4) || this.isIpPrefix(4, true)\xbaJ\x01\x02\x12\x19\n\tsubnet_id\x18\x02 \x01(\tB\x04\xbaJ\x01\x02H\x00\x12\x17\n\x07pool_id\x18\x03 \x01(\tB\x04\xbaJ\x01\x02H\x00\x42\x11\n\x04pool\x12\t\xbaH\x02\x08\x01\xbaJ\x01\x02\"\x93\x02\n\x10\x41llocationStatus\x12\x34\n\x05state\x18\x01 \x01(\x0e\x32%.nebius.vpc.v1.AllocationStatus.State\x12\x31\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32 .nebius.vpc.v1.AllocationDetails\x12-\n\nassignment\x18\x03 \x01(\x0b\x32\x19.nebius.vpc.v1.Assignment\x12\x0e\n\x06static\x18\x04 \x01(\x08\"W\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\r\n\tALLOCATED\x10\x02\x12\x0c\n\x08\x41SSIGNED\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\"g\n\x11\x41llocationDetails\x12\x16\n\x0e\x61llocated_cidr\x18\x01 \x01(\t\x12\x0f\n\x07pool_id\x18\x02 \x01(\t\x12)\n\x07version\x18\x04 \x01(\x0e\x32\x18.nebius.vpc.v1.IpVersion\"\x9c\x01\n\nAssignment\x12\x46\n\x11network_interface\x18\x01 \x01(\x0b\x32).nebius.vpc.v1.NetworkInterfaceAssignmentH\x00\x12>\n\rload_balancer\x18\x02 \x01(\x0b\x32%.nebius.vpc.v1.LoadBalancerAssignmentH\x00\x42\x06\n\x04type\"?\n\x1aNetworkInterfaceAssignment\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"$\n\x16LoadBalancerAssignment\x12\n\n\x02id\x18\x01 \x01(\tBV\n\x14\x61i.nebius.pub.vpc.v1B\x0f\x41llocationProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/vpc/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.vpc.v1.allocation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.vpc.v1B\017AllocationProtoP\001Z+github.com/nebius/gosdk/proto/nebius/vpc/v1'
  _ALLOCATIONSPEC.oneofs_by_name['ip_spec']._options = None
  _ALLOCATIONSPEC.oneofs_by_name['ip_spec']._serialized_options = b'\272H\002\010\001'
  _ALLOCATIONSPEC.fields_by_name['ipv4_private']._options = None
  _ALLOCATIONSPEC.fields_by_name['ipv4_private']._serialized_options = b'\272J\001\006'
  _ALLOCATIONSPEC.fields_by_name['ipv4_public']._options = None
  _ALLOCATIONSPEC.fields_by_name['ipv4_public']._serialized_options = b'\272J\001\006'
  _IPV4PRIVATEALLOCATIONSPEC.oneofs_by_name['pool']._options = None
  _IPV4PRIVATEALLOCATIONSPEC.oneofs_by_name['pool']._serialized_options = b'\272H\002\010\001\272J\001\002'
  _IPV4PRIVATEALLOCATIONSPEC.fields_by_name['cidr']._options = None
  _IPV4PRIVATEALLOCATIONSPEC.fields_by_name['cidr']._serialized_options = b'\272H\257\001\272\001\253\001\n\021string.valid_cidr\022.value must be a valid IP address, CIDR or mask\032fthis == \'\' || this.matches(\'^/([0-9]|[1-2][0-9]|3[0-2])$\') || this.isIp(4) || this.isIpPrefix(4, true)\272J\001\002'
  _IPV4PRIVATEALLOCATIONSPEC.fields_by_name['subnet_id']._options = None
  _IPV4PRIVATEALLOCATIONSPEC.fields_by_name['subnet_id']._serialized_options = b'\272J\001\002'
  _IPV4PRIVATEALLOCATIONSPEC.fields_by_name['pool_id']._options = None
  _IPV4PRIVATEALLOCATIONSPEC.fields_by_name['pool_id']._serialized_options = b'\272J\001\002'
  _IPV4PUBLICALLOCATIONSPEC.oneofs_by_name['pool']._options = None
  _IPV4PUBLICALLOCATIONSPEC.oneofs_by_name['pool']._serialized_options = b'\272H\002\010\001\272J\001\002'
  _IPV4PUBLICALLOCATIONSPEC.fields_by_name['cidr']._options = None
  _IPV4PUBLICALLOCATIONSPEC.fields_by_name['cidr']._serialized_options = b'\272H\257\001\272\001\253\001\n\021string.valid_cidr\022.value must be a valid IP address, CIDR or mask\032fthis == \'\' || this.matches(\'^/([0-9]|[1-2][0-9]|3[0-2])$\') || this.isIp(4) || this.isIpPrefix(4, true)\272J\001\002'
  _IPV4PUBLICALLOCATIONSPEC.fields_by_name['subnet_id']._options = None
  _IPV4PUBLICALLOCATIONSPEC.fields_by_name['subnet_id']._serialized_options = b'\272J\001\002'
  _IPV4PUBLICALLOCATIONSPEC.fields_by_name['pool_id']._options = None
  _IPV4PUBLICALLOCATIONSPEC.fields_by_name['pool_id']._serialized_options = b'\272J\001\002'
  _globals['_ALLOCATION']._serialized_start=164
  _globals['_ALLOCATION']._serialized_end=324
  _globals['_ALLOCATIONSPEC']._serialized_start=327
  _globals['_ALLOCATIONSPEC']._serialized_end=503
  _globals['_IPV4PRIVATEALLOCATIONSPEC']._serialized_start=506
  _globals['_IPV4PRIVATEALLOCATIONSPEC']._serialized_end=805
  _globals['_IPV4PUBLICALLOCATIONSPEC']._serialized_start=808
  _globals['_IPV4PUBLICALLOCATIONSPEC']._serialized_end=1106
  _globals['_ALLOCATIONSTATUS']._serialized_start=1109
  _globals['_ALLOCATIONSTATUS']._serialized_end=1384
  _globals['_ALLOCATIONSTATUS_STATE']._serialized_start=1297
  _globals['_ALLOCATIONSTATUS_STATE']._serialized_end=1384
  _globals['_ALLOCATIONDETAILS']._serialized_start=1386
  _globals['_ALLOCATIONDETAILS']._serialized_end=1489
  _globals['_ASSIGNMENT']._serialized_start=1492
  _globals['_ASSIGNMENT']._serialized_end=1648
  _globals['_NETWORKINTERFACEASSIGNMENT']._serialized_start=1650
  _globals['_NETWORKINTERFACEASSIGNMENT']._serialized_end=1713
  _globals['_LOADBALANCERASSIGNMENT']._serialized_start=1715
  _globals['_LOADBALANCERASSIGNMENT']._serialized_end=1751
# @@protoc_insertion_point(module_scope)
