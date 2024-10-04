# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/iam/v1/project_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from nebius import annotations_pb2 as nebius_dot_annotations__pb2
from nebius.iam.v1 import container_pb2 as nebius_dot_iam_dot_v1_dot_container__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#nebius/iam/v1/project_service.proto\x12\rnebius.iam.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x18nebius/annotations.proto\x1a\x1dnebius/iam/v1/container.proto\"\x1f\n\x11GetProjectRequest\x12\n\n\x02id\x18\x01 \x01(\t\"J\n\x17GetProjectByNameRequest\x12\x19\n\tparent_id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\x12\x14\n\x04name\x18\x02 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\"r\n\x13ListProjectsRequest\x12\x11\n\tparent_id\x18\x01 \x01(\t\x12\x16\n\tpage_size\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\tB\x0c\n\n_page_size\"X\n\x14ListProjectsResponse\x12\'\n\x05items\x18\x01 \x03(\x0b\x32\x18.nebius.iam.v1.Container\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xff\x01\n\x0eProjectService\x12\x41\n\x03Get\x12 .nebius.iam.v1.GetProjectRequest\x1a\x18.nebius.iam.v1.Container\x12M\n\tGetByName\x12&.nebius.iam.v1.GetProjectByNameRequest\x1a\x18.nebius.iam.v1.Container\x12O\n\x04List\x12\".nebius.iam.v1.ListProjectsRequest\x1a#.nebius.iam.v1.ListProjectsResponse\x1a\n\xbaJ\x07\x63pl.iamBZ\n\x14\x61i.nebius.pub.iam.v1B\x13ProjectServiceProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/iam/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.iam.v1.project_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.iam.v1B\023ProjectServiceProtoP\001Z+github.com/nebius/gosdk/proto/nebius/iam/v1'
  _GETPROJECTBYNAMEREQUEST.fields_by_name['parent_id']._options = None
  _GETPROJECTBYNAMEREQUEST.fields_by_name['parent_id']._serialized_options = b'\272H\003\310\001\001'
  _GETPROJECTBYNAMEREQUEST.fields_by_name['name']._options = None
  _GETPROJECTBYNAMEREQUEST.fields_by_name['name']._serialized_options = b'\272H\003\310\001\001'
  _PROJECTSERVICE._options = None
  _PROJECTSERVICE._serialized_options = b'\272J\007cpl.iam'
  _globals['_GETPROJECTREQUEST']._serialized_start=140
  _globals['_GETPROJECTREQUEST']._serialized_end=171
  _globals['_GETPROJECTBYNAMEREQUEST']._serialized_start=173
  _globals['_GETPROJECTBYNAMEREQUEST']._serialized_end=247
  _globals['_LISTPROJECTSREQUEST']._serialized_start=249
  _globals['_LISTPROJECTSREQUEST']._serialized_end=363
  _globals['_LISTPROJECTSRESPONSE']._serialized_start=365
  _globals['_LISTPROJECTSRESPONSE']._serialized_end=453
  _globals['_PROJECTSERVICE']._serialized_start=456
  _globals['_PROJECTSERVICE']._serialized_end=711
# @@protoc_insertion_point(module_scope)
