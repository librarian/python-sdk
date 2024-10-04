# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/iam/v1/auth_public_key.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius import annotations_pb2 as nebius_dot_annotations__pb2
from nebius.iam.v1 import access_pb2 as nebius_dot_iam_dot_v1_dot_access__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#nebius/iam/v1/auth_public_key.proto\x12\rnebius.iam.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a\x18nebius/annotations.proto\x1a\x1anebius/iam/v1/access.proto\"\xc5\x01\n\rAuthPublicKey\x12<\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadataB\x06\xbaH\x03\xc8\x01\x01\x12\x36\n\x04spec\x18\x02 \x01(\x0b\x32 .nebius.iam.v1.AuthPublicKeySpecB\x06\xbaH\x03\xc8\x01\x01\x12\x38\n\x06status\x18\x03 \x01(\x0b\x32\".nebius.iam.v1.AuthPublicKeyStatusB\x04\xbaJ\x01\x05:\x04\xbaJ\x01\x02\"\xa1\x01\n\x11\x41uthPublicKeySpec\x12-\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x16.nebius.iam.v1.AccountB\x04\xbaJ\x01\x02\x12\x34\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xbaJ\x01\x02\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\x04\x64\x61ta\x18\x04 \x01(\tB\x04\xbaJ\x01\x02\"\xea\x01\n\x13\x41uthPublicKeyStatus\x12\x37\n\x05state\x18\x01 \x01(\x0e\x32(.nebius.iam.v1.AuthPublicKeyStatus.State\x12\x13\n\x0b\x66ingerprint\x18\x02 \x01(\t\x12\x11\n\talgorithm\x18\x03 \x01(\t\x12\x10\n\x08key_size\x18\x04 \x01(\x05\"`\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x12\x0b\n\x07\x45XPIRED\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\x12\x0b\n\x07\x44\x45LETED\x10\x05\x42Y\n\x14\x61i.nebius.pub.iam.v1B\x12\x41uthPublicKeyProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/iam/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.iam.v1.auth_public_key_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.iam.v1B\022AuthPublicKeyProtoP\001Z+github.com/nebius/gosdk/proto/nebius/iam/v1'
  _AUTHPUBLICKEY.fields_by_name['metadata']._options = None
  _AUTHPUBLICKEY.fields_by_name['metadata']._serialized_options = b'\272H\003\310\001\001'
  _AUTHPUBLICKEY.fields_by_name['spec']._options = None
  _AUTHPUBLICKEY.fields_by_name['spec']._serialized_options = b'\272H\003\310\001\001'
  _AUTHPUBLICKEY.fields_by_name['status']._options = None
  _AUTHPUBLICKEY.fields_by_name['status']._serialized_options = b'\272J\001\005'
  _AUTHPUBLICKEY._options = None
  _AUTHPUBLICKEY._serialized_options = b'\272J\001\002'
  _AUTHPUBLICKEYSPEC.fields_by_name['account']._options = None
  _AUTHPUBLICKEYSPEC.fields_by_name['account']._serialized_options = b'\272J\001\002'
  _AUTHPUBLICKEYSPEC.fields_by_name['expires_at']._options = None
  _AUTHPUBLICKEYSPEC.fields_by_name['expires_at']._serialized_options = b'\272J\001\002'
  _AUTHPUBLICKEYSPEC.fields_by_name['data']._options = None
  _AUTHPUBLICKEYSPEC.fields_by_name['data']._serialized_options = b'\272J\001\002'
  _globals['_AUTHPUBLICKEY']._serialized_start=204
  _globals['_AUTHPUBLICKEY']._serialized_end=401
  _globals['_AUTHPUBLICKEYSPEC']._serialized_start=404
  _globals['_AUTHPUBLICKEYSPEC']._serialized_end=565
  _globals['_AUTHPUBLICKEYSTATUS']._serialized_start=568
  _globals['_AUTHPUBLICKEYSTATUS']._serialized_end=802
  _globals['_AUTHPUBLICKEYSTATUS_STATE']._serialized_start=706
  _globals['_AUTHPUBLICKEYSTATUS_STATE']._serialized_end=802
# @@protoc_insertion_point(module_scope)
