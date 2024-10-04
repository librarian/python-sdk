# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/vpc/v1/network.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bnebius/vpc/v1/network.proto\x12\rnebius.vpc.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x18nebius/annotations.proto\x1a\x1fnebius/common/v1/metadata.proto\"\x97\x01\n\x07Network\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12(\n\x04spec\x18\x02 \x01(\x0b\x32\x1a.nebius.vpc.v1.NetworkSpec\x12,\n\x06status\x18\x03 \x01(\x0b\x32\x1c.nebius.vpc.v1.NetworkStatus\"\x9f\x01\n\x0bNetworkSpec\x12H\n\x12ipv4_private_pools\x18\x01 \x01(\x0b\x32&.nebius.vpc.v1.IPv4PrivateNetworkPoolsB\x04\xbaJ\x01\x07\x12\x46\n\x11ipv4_public_pools\x18\x02 \x01(\x0b\x32%.nebius.vpc.v1.IPv4PublicNetworkPoolsB\x04\xbaJ\x01\x07\"D\n\x17IPv4PrivateNetworkPools\x12)\n\x05pools\x18\x01 \x03(\x0b\x32\x1a.nebius.vpc.v1.NetworkPool\"C\n\x16IPv4PublicNetworkPools\x12)\n\x05pools\x18\x01 \x03(\x0b\x32\x1a.nebius.vpc.v1.NetworkPool\"!\n\x0bNetworkPool\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\"\x89\x01\n\rNetworkStatus\x12\x31\n\x05state\x18\x01 \x01(\x0e\x32\".nebius.vpc.v1.NetworkStatus.State\"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\x42S\n\x14\x61i.nebius.pub.vpc.v1B\x0cNetworkProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/vpc/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.vpc.v1.network_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.vpc.v1B\014NetworkProtoP\001Z+github.com/nebius/gosdk/proto/nebius/vpc/v1'
  _NETWORKSPEC.fields_by_name['ipv4_private_pools']._options = None
  _NETWORKSPEC.fields_by_name['ipv4_private_pools']._serialized_options = b'\272J\001\007'
  _NETWORKSPEC.fields_by_name['ipv4_public_pools']._options = None
  _NETWORKSPEC.fields_by_name['ipv4_public_pools']._serialized_options = b'\272J\001\007'
  _NETWORKPOOL.fields_by_name['id']._options = None
  _NETWORKPOOL.fields_by_name['id']._serialized_options = b'\272H\003\310\001\001'
  _globals['_NETWORK']._serialized_start=135
  _globals['_NETWORK']._serialized_end=286
  _globals['_NETWORKSPEC']._serialized_start=289
  _globals['_NETWORKSPEC']._serialized_end=448
  _globals['_IPV4PRIVATENETWORKPOOLS']._serialized_start=450
  _globals['_IPV4PRIVATENETWORKPOOLS']._serialized_end=518
  _globals['_IPV4PUBLICNETWORKPOOLS']._serialized_start=520
  _globals['_IPV4PUBLICNETWORKPOOLS']._serialized_end=587
  _globals['_NETWORKPOOL']._serialized_start=589
  _globals['_NETWORKPOOL']._serialized_end=622
  _globals['_NETWORKSTATUS']._serialized_start=625
  _globals['_NETWORKSTATUS']._serialized_end=762
  _globals['_NETWORKSTATUS_STATE']._serialized_start=693
  _globals['_NETWORKSTATUS_STATE']._serialized_end=762
# @@protoc_insertion_point(module_scope)
