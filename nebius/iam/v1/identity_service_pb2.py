# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/iam/v1/identity_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nebius import annotations_pb2 as nebius_dot_annotations__pb2
from nebius.iam.v1 import token_service_pb2 as nebius_dot_iam_dot_v1_dot_token__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$nebius/iam/v1/identity_service.proto\x12\rnebius.iam.v1\x1a\x18nebius/annotations.proto\x1a!nebius/iam/v1/token_service.proto2|\n\x0fIdentityService\x12X\n\rExchangeToken\x12#.nebius.iam.v1.ExchangeTokenRequest\x1a\".nebius.iam.v1.CreateTokenResponse\x1a\x0f\xbaJ\x0cidentity.iamB[\n\x14\x61i.nebius.pub.iam.v1B\x14IdentityServiceProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/iam/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.iam.v1.identity_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.iam.v1B\024IdentityServiceProtoP\001Z+github.com/nebius/gosdk/proto/nebius/iam/v1'
  _IDENTITYSERVICE._options = None
  _IDENTITYSERVICE._serialized_options = b'\272J\014identity.iam'
  _globals['_IDENTITYSERVICE']._serialized_start=116
  _globals['_IDENTITYSERVICE']._serialized_end=240
# @@protoc_insertion_point(module_scope)
