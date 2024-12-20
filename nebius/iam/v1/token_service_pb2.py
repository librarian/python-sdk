# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/iam/v1/token_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nebius import annotations_pb2 as nebius_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!nebius/iam/v1/token_service.proto\x12\rnebius.iam.v1\x1a\x18nebius/annotations.proto\"\xee\x01\n\x14\x45xchangeTokenRequest\x12\x12\n\ngrant_type\x18\x01 \x01(\t\x12\x1c\n\x14requested_token_type\x18\x02 \x01(\t\x12\x1d\n\rsubject_token\x18\x03 \x01(\tB\x06\xc0J\x01\xc8J\x01\x12\x1a\n\x12subject_token_type\x18\x04 \x01(\t\x12\x0e\n\x06scopes\x18\x05 \x03(\t\x12\x10\n\x08\x61udience\x18\x06 \x01(\t\x12\x1b\n\x0b\x61\x63tor_token\x18\x07 \x01(\tB\x06\xc0J\x01\xc8J\x01\x12\x18\n\x10\x61\x63tor_token_type\x18\x08 \x01(\t\x12\x10\n\x08resource\x18\t \x03(\t\"\x86\x01\n\x13\x43reateTokenResponse\x12\x1c\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\tB\x06\xc0J\x01\xc8J\x01\x12\x19\n\x11issued_token_type\x18\x02 \x01(\t\x12\x12\n\ntoken_type\x18\x03 \x01(\t\x12\x12\n\nexpires_in\x18\x04 \x01(\x03\x12\x0e\n\x06scopes\x18\x05 \x03(\tBX\n\x14\x61i.nebius.pub.iam.v1B\x11TokenServiceProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/iam/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.iam.v1.token_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.iam.v1B\021TokenServiceProtoP\001Z+github.com/nebius/gosdk/proto/nebius/iam/v1'
  _EXCHANGETOKENREQUEST.fields_by_name['subject_token']._options = None
  _EXCHANGETOKENREQUEST.fields_by_name['subject_token']._serialized_options = b'\300J\001\310J\001'
  _EXCHANGETOKENREQUEST.fields_by_name['actor_token']._options = None
  _EXCHANGETOKENREQUEST.fields_by_name['actor_token']._serialized_options = b'\300J\001\310J\001'
  _CREATETOKENRESPONSE.fields_by_name['access_token']._options = None
  _CREATETOKENRESPONSE.fields_by_name['access_token']._serialized_options = b'\300J\001\310J\001'
  _globals['_EXCHANGETOKENREQUEST']._serialized_start=79
  _globals['_EXCHANGETOKENREQUEST']._serialized_end=317
  _globals['_CREATETOKENRESPONSE']._serialized_start=320
  _globals['_CREATETOKENRESPONSE']._serialized_end=454
# @@protoc_insertion_point(module_scope)
