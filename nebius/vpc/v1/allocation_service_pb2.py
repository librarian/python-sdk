# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/vpc/v1/allocation_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius.common.v1 import operation_pb2 as nebius_dot_common_dot_v1_dot_operation__pb2
from nebius.vpc.v1 import allocation_pb2 as nebius_dot_vpc_dot_v1_dot_allocation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&nebius/vpc/v1/allocation_service.proto\x12\rnebius.vpc.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a nebius/common/v1/operation.proto\x1a\x1enebius/vpc/v1/allocation.proto\"*\n\x14GetAllocationRequest\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\"M\n\x1aGetAllocationByNameRequest\x12\x19\n\tparent_id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\x12\x14\n\x04name\x18\x02 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\"Z\n\x16ListAllocationsRequest\x12\x19\n\tparent_id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"\\\n\x17ListAllocationsResponse\x12(\n\x05items\x18\x01 \x03(\x0b\x32\x19.nebius.vpc.v1.Allocation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8c\x01\n\x17\x43reateAllocationRequest\x12<\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadataB\x06\xbaH\x03\xc8\x01\x01\x12\x33\n\x04spec\x18\x02 \x01(\x0b\x32\x1d.nebius.vpc.v1.AllocationSpecB\x06\xbaH\x03\xc8\x01\x01\"|\n\x17UpdateAllocationRequest\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12+\n\x04spec\x18\x02 \x01(\x0b\x32\x1d.nebius.vpc.v1.AllocationSpec\"-\n\x17\x44\x65leteAllocationRequest\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\x32\xf1\x03\n\x11\x41llocationService\x12\x45\n\x03Get\x12#.nebius.vpc.v1.GetAllocationRequest\x1a\x19.nebius.vpc.v1.Allocation\x12Q\n\tGetByName\x12).nebius.vpc.v1.GetAllocationByNameRequest\x1a\x19.nebius.vpc.v1.Allocation\x12U\n\x04List\x12%.nebius.vpc.v1.ListAllocationsRequest\x1a&.nebius.vpc.v1.ListAllocationsResponse\x12M\n\x06\x43reate\x12&.nebius.vpc.v1.CreateAllocationRequest\x1a\x1b.nebius.common.v1.Operation\x12M\n\x06Update\x12&.nebius.vpc.v1.UpdateAllocationRequest\x1a\x1b.nebius.common.v1.Operation\x12M\n\x06\x44\x65lete\x12&.nebius.vpc.v1.DeleteAllocationRequest\x1a\x1b.nebius.common.v1.OperationB]\n\x14\x61i.nebius.pub.vpc.v1B\x16\x41llocationServiceProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/vpc/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.vpc.v1.allocation_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.vpc.v1B\026AllocationServiceProtoP\001Z+github.com/nebius/gosdk/proto/nebius/vpc/v1'
  _GETALLOCATIONREQUEST.fields_by_name['id']._options = None
  _GETALLOCATIONREQUEST.fields_by_name['id']._serialized_options = b'\272H\003\310\001\001'
  _GETALLOCATIONBYNAMEREQUEST.fields_by_name['parent_id']._options = None
  _GETALLOCATIONBYNAMEREQUEST.fields_by_name['parent_id']._serialized_options = b'\272H\003\310\001\001'
  _GETALLOCATIONBYNAMEREQUEST.fields_by_name['name']._options = None
  _GETALLOCATIONBYNAMEREQUEST.fields_by_name['name']._serialized_options = b'\272H\003\310\001\001'
  _LISTALLOCATIONSREQUEST.fields_by_name['parent_id']._options = None
  _LISTALLOCATIONSREQUEST.fields_by_name['parent_id']._serialized_options = b'\272H\003\310\001\001'
  _CREATEALLOCATIONREQUEST.fields_by_name['metadata']._options = None
  _CREATEALLOCATIONREQUEST.fields_by_name['metadata']._serialized_options = b'\272H\003\310\001\001'
  _CREATEALLOCATIONREQUEST.fields_by_name['spec']._options = None
  _CREATEALLOCATIONREQUEST.fields_by_name['spec']._serialized_options = b'\272H\003\310\001\001'
  _DELETEALLOCATIONREQUEST.fields_by_name['id']._options = None
  _DELETEALLOCATIONREQUEST.fields_by_name['id']._serialized_options = b'\272H\003\310\001\001'
  _globals['_GETALLOCATIONREQUEST']._serialized_start=185
  _globals['_GETALLOCATIONREQUEST']._serialized_end=227
  _globals['_GETALLOCATIONBYNAMEREQUEST']._serialized_start=229
  _globals['_GETALLOCATIONBYNAMEREQUEST']._serialized_end=306
  _globals['_LISTALLOCATIONSREQUEST']._serialized_start=308
  _globals['_LISTALLOCATIONSREQUEST']._serialized_end=398
  _globals['_LISTALLOCATIONSRESPONSE']._serialized_start=400
  _globals['_LISTALLOCATIONSRESPONSE']._serialized_end=492
  _globals['_CREATEALLOCATIONREQUEST']._serialized_start=495
  _globals['_CREATEALLOCATIONREQUEST']._serialized_end=635
  _globals['_UPDATEALLOCATIONREQUEST']._serialized_start=637
  _globals['_UPDATEALLOCATIONREQUEST']._serialized_end=761
  _globals['_DELETEALLOCATIONREQUEST']._serialized_start=763
  _globals['_DELETEALLOCATIONREQUEST']._serialized_end=808
  _globals['_ALLOCATIONSERVICE']._serialized_start=811
  _globals['_ALLOCATIONSERVICE']._serialized_end=1308
# @@protoc_insertion_point(module_scope)