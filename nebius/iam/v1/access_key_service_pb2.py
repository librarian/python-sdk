# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/iam/v1/access_key_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nebius import annotations_pb2 as nebius_dot_annotations__pb2
from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius.common.v1 import operation_pb2 as nebius_dot_common_dot_v1_dot_operation__pb2
from nebius.iam.v1 import access_key_pb2 as nebius_dot_iam_dot_v1_dot_access__key__pb2
from nebius.iam.v1 import access_pb2 as nebius_dot_iam_dot_v1_dot_access__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&nebius/iam/v1/access_key_service.proto\x12\rnebius.iam.v1\x1a\x18nebius/annotations.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a nebius/common/v1/operation.proto\x1a\x1enebius/iam/v1/access_key.proto\x1a\x1anebius/iam/v1/access.proto\"z\n\x16\x43reateAccessKeyRequest\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12*\n\x04spec\x18\x02 \x01(\x0b\x32\x1c.nebius.iam.v1.AccessKeySpec\"D\n\x0bKeyIdentity\x12\x0c\n\x02id\x18\x01 \x01(\tH\x00\x12\x1b\n\x11\x61ws_access_key_id\x18\x02 \x01(\tH\x00\x42\n\n\x08identity\"+\n\x1dGetAccessKeySecretOnceRequest\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\x17GetAccessKeyByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"7\n\x1aGetAccessKeyByAwsIdRequest\x12\x19\n\x11\x61ws_access_key_id\x18\x01 \x01(\t\"t\n\x15ListAccessKeysRequest\x12\x11\n\tparent_id\x18\x01 \x01(\t\x12\x16\n\tpage_size\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\tB\x0c\n\n_page_size\"\x80\x01\n\x1eListAccessKeysByAccountRequest\x12\'\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x16.nebius.iam.v1.Account\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"z\n\x16UpdateAccessKeyRequest\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12*\n\x04spec\x18\x02 \x01(\x0b\x32\x1c.nebius.iam.v1.AccessKeySpec\"B\n\x18\x41\x63tivateAccessKeyRequest\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.nebius.iam.v1.KeyIdentity\"D\n\x1a\x44\x65\x61\x63tivateAccessKeyRequest\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.nebius.iam.v1.KeyIdentity\"@\n\x16\x44\x65leteAccessKeyRequest\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.nebius.iam.v1.KeyIdentity\"5\n\x1eGetAccessKeySecretOnceResponse\x12\x13\n\x06secret\x18\x01 \x01(\tB\x03\xc0J\x01\"Z\n\x16ListAccessKeysResponse\x12\'\n\x05items\x18\x01 \x03(\x0b\x32\x18.nebius.iam.v1.AccessKey\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xfa\x06\n\x10\x41\x63\x63\x65ssKeyService\x12L\n\x06\x43reate\x12%.nebius.iam.v1.CreateAccessKeyRequest\x1a\x1b.nebius.common.v1.Operation\x12S\n\x04List\x12$.nebius.iam.v1.ListAccessKeysRequest\x1a%.nebius.iam.v1.ListAccessKeysResponse\x12\x65\n\rListByAccount\x12-.nebius.iam.v1.ListAccessKeysByAccountRequest\x1a%.nebius.iam.v1.ListAccessKeysResponse\x12L\n\x06Update\x12%.nebius.iam.v1.UpdateAccessKeyRequest\x1a\x1b.nebius.common.v1.Operation\x12K\n\x07GetById\x12&.nebius.iam.v1.GetAccessKeyByIdRequest\x1a\x18.nebius.iam.v1.AccessKey\x12Q\n\nGetByAwsId\x12).nebius.iam.v1.GetAccessKeyByAwsIdRequest\x1a\x18.nebius.iam.v1.AccessKey\x12l\n\rGetSecretOnce\x12,.nebius.iam.v1.GetAccessKeySecretOnceRequest\x1a-.nebius.iam.v1.GetAccessKeySecretOnceResponse\x12P\n\x08\x41\x63tivate\x12\'.nebius.iam.v1.ActivateAccessKeyRequest\x1a\x1b.nebius.common.v1.Operation\x12T\n\nDeactivate\x12).nebius.iam.v1.DeactivateAccessKeyRequest\x1a\x1b.nebius.common.v1.Operation\x12L\n\x06\x44\x65lete\x12%.nebius.iam.v1.DeleteAccessKeyRequest\x1a\x1b.nebius.common.v1.Operation\x1a\n\xbaJ\x07\x63pl.iamB\\\n\x14\x61i.nebius.pub.iam.v1B\x15\x41\x63\x63\x65ssKeyServiceProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/iam/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.iam.v1.access_key_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.iam.v1B\025AccessKeyServiceProtoP\001Z+github.com/nebius/gosdk/proto/nebius/iam/v1'
  _GETACCESSKEYSECRETONCERESPONSE.fields_by_name['secret']._options = None
  _GETACCESSKEYSECRETONCERESPONSE.fields_by_name['secret']._serialized_options = b'\300J\001'
  _ACCESSKEYSERVICE._options = None
  _ACCESSKEYSERVICE._serialized_options = b'\272J\007cpl.iam'
  _globals['_CREATEACCESSKEYREQUEST']._serialized_start=210
  _globals['_CREATEACCESSKEYREQUEST']._serialized_end=332
  _globals['_KEYIDENTITY']._serialized_start=334
  _globals['_KEYIDENTITY']._serialized_end=402
  _globals['_GETACCESSKEYSECRETONCEREQUEST']._serialized_start=404
  _globals['_GETACCESSKEYSECRETONCEREQUEST']._serialized_end=447
  _globals['_GETACCESSKEYBYIDREQUEST']._serialized_start=449
  _globals['_GETACCESSKEYBYIDREQUEST']._serialized_end=486
  _globals['_GETACCESSKEYBYAWSIDREQUEST']._serialized_start=488
  _globals['_GETACCESSKEYBYAWSIDREQUEST']._serialized_end=543
  _globals['_LISTACCESSKEYSREQUEST']._serialized_start=545
  _globals['_LISTACCESSKEYSREQUEST']._serialized_end=661
  _globals['_LISTACCESSKEYSBYACCOUNTREQUEST']._serialized_start=664
  _globals['_LISTACCESSKEYSBYACCOUNTREQUEST']._serialized_end=792
  _globals['_UPDATEACCESSKEYREQUEST']._serialized_start=794
  _globals['_UPDATEACCESSKEYREQUEST']._serialized_end=916
  _globals['_ACTIVATEACCESSKEYREQUEST']._serialized_start=918
  _globals['_ACTIVATEACCESSKEYREQUEST']._serialized_end=984
  _globals['_DEACTIVATEACCESSKEYREQUEST']._serialized_start=986
  _globals['_DEACTIVATEACCESSKEYREQUEST']._serialized_end=1054
  _globals['_DELETEACCESSKEYREQUEST']._serialized_start=1056
  _globals['_DELETEACCESSKEYREQUEST']._serialized_end=1120
  _globals['_GETACCESSKEYSECRETONCERESPONSE']._serialized_start=1122
  _globals['_GETACCESSKEYSECRETONCERESPONSE']._serialized_end=1175
  _globals['_LISTACCESSKEYSRESPONSE']._serialized_start=1177
  _globals['_LISTACCESSKEYSRESPONSE']._serialized_end=1267
  _globals['_ACCESSKEYSERVICE']._serialized_start=1270
  _globals['_ACCESSKEYSERVICE']._serialized_end=2160
# @@protoc_insertion_point(module_scope)
