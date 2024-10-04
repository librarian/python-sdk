# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/iam/v1/tenant_user_account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius import annotations_pb2 as nebius_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'nebius/iam/v1/tenant_user_account.proto\x12\rnebius.iam.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a\x18nebius/annotations.proto\"\xd1\x01\n\x11TenantUserAccount\x12<\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadataB\x06\xbaH\x03\xc8\x01\x01\x12:\n\x04spec\x18\x02 \x01(\x0b\x32$.nebius.iam.v1.TenantUserAccountSpecB\x06\xbaH\x03\xc8\x01\x01\x12<\n\x06status\x18\x03 \x01(\x0b\x32&.nebius.iam.v1.TenantUserAccountStatusB\x04\xbaJ\x01\x05:\x04\xbaJ\x01\x02\"\xd2\x01\n\x1fTenantUserAccountWithAttributes\x12=\n\x13tenant_user_account\x18\x01 \x01(\x0b\x32 .nebius.iam.v1.TenantUserAccount\x12\x33\n\nattributes\x18\x02 \x01(\x0b\x32\x1d.nebius.iam.v1.UserAttributesH\x00\x12%\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x14.nebius.iam.v1.ErrorH\x00\x42\x14\n\x12\x61ttributesOptional\"\x81\x05\n\x0eUserAttributes\x12\x15\n\x03sub\x18\x14 \x01(\tB\x03\xc0J\x01H\x00\x88\x01\x01\x12\x16\n\x04name\x18\x01 \x01(\tB\x03\xc0J\x01H\x01\x88\x01\x01\x12\x1c\n\ngiven_name\x18\x02 \x01(\tB\x03\xc0J\x01H\x02\x88\x01\x01\x12\x1d\n\x0b\x66\x61mily_name\x18\x03 \x01(\tB\x03\xc0J\x01H\x03\x88\x01\x01\x12$\n\x12preferred_username\x18\x04 \x01(\tB\x03\xc0J\x01H\x04\x88\x01\x01\x12\x19\n\x07picture\x18\x05 \x01(\tB\x03\xc0J\x01H\x05\x88\x01\x01\x12n\n\x05\x65mail\x18\x06 \x01(\tBZ\xbaHT\xba\x01Q\n\x0cstring.email\x12#value must be a valid email address\x1a\x1cthis == \'\' || this.isEmail()\xc0J\x01H\x06\x88\x01\x01\x12\x1f\n\x0e\x65mail_verified\x18\x07 \x01(\x08\x42\x02\x18\x01H\x07\x88\x01\x01\x12\x1c\n\x08zoneinfo\x18\x08 \x01(\tB\x05\x18\x01\xc0J\x01H\x08\x88\x01\x01\x12\x18\n\x06locale\x18\t \x01(\tB\x03\xc0J\x01H\t\x88\x01\x01\x12\x1e\n\x0cphone_number\x18\n \x01(\tB\x03\xc0J\x01H\n\x88\x01\x01\x12&\n\x15phone_number_verified\x18\x0b \x01(\x08\x42\x02\x18\x01H\x0b\x88\x01\x01\x42\x06\n\x04_subB\x07\n\x05_nameB\r\n\x0b_given_nameB\x0e\n\x0c_family_nameB\x15\n\x13_preferred_usernameB\n\n\x08_pictureB\x08\n\x06_emailB\x11\n\x0f_email_verifiedB\x0b\n\t_zoneinfoB\t\n\x07_localeB\x0f\n\r_phone_numberB\x18\n\x16_phone_number_verified\"\x18\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x98\x01\n\x15TenantUserAccountSpec\x12R\n\x12visible_attributes\x18\x01 \x01(\x0b\x32\x36.nebius.iam.v1.TenantUserAccountSpec.VisibleAttributes\x1a+\n\x11VisibleAttributes\x12\x16\n\tattribute\x18\x01 \x03(\tB\x03\xc0J\x01\"\xcb\x01\n\x17TenantUserAccountStatus\x12;\n\x05state\x18\x01 \x01(\x0e\x32,.nebius.iam.v1.TenantUserAccountStatus.State\x12\x15\n\rinvitation_id\x18\x02 \x01(\t\x12\x15\n\rfederation_id\x18\x03 \x01(\t\"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x12\x0b\n\x07\x42LOCKED\x10\x03\x42]\n\x14\x61i.nebius.pub.iam.v1B\x16TenantUserAccountProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/iam/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.iam.v1.tenant_user_account_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.iam.v1B\026TenantUserAccountProtoP\001Z+github.com/nebius/gosdk/proto/nebius/iam/v1'
  _TENANTUSERACCOUNT.fields_by_name['metadata']._options = None
  _TENANTUSERACCOUNT.fields_by_name['metadata']._serialized_options = b'\272H\003\310\001\001'
  _TENANTUSERACCOUNT.fields_by_name['spec']._options = None
  _TENANTUSERACCOUNT.fields_by_name['spec']._serialized_options = b'\272H\003\310\001\001'
  _TENANTUSERACCOUNT.fields_by_name['status']._options = None
  _TENANTUSERACCOUNT.fields_by_name['status']._serialized_options = b'\272J\001\005'
  _TENANTUSERACCOUNT._options = None
  _TENANTUSERACCOUNT._serialized_options = b'\272J\001\002'
  _USERATTRIBUTES.fields_by_name['sub']._options = None
  _USERATTRIBUTES.fields_by_name['sub']._serialized_options = b'\300J\001'
  _USERATTRIBUTES.fields_by_name['name']._options = None
  _USERATTRIBUTES.fields_by_name['name']._serialized_options = b'\300J\001'
  _USERATTRIBUTES.fields_by_name['given_name']._options = None
  _USERATTRIBUTES.fields_by_name['given_name']._serialized_options = b'\300J\001'
  _USERATTRIBUTES.fields_by_name['family_name']._options = None
  _USERATTRIBUTES.fields_by_name['family_name']._serialized_options = b'\300J\001'
  _USERATTRIBUTES.fields_by_name['preferred_username']._options = None
  _USERATTRIBUTES.fields_by_name['preferred_username']._serialized_options = b'\300J\001'
  _USERATTRIBUTES.fields_by_name['picture']._options = None
  _USERATTRIBUTES.fields_by_name['picture']._serialized_options = b'\300J\001'
  _USERATTRIBUTES.fields_by_name['email']._options = None
  _USERATTRIBUTES.fields_by_name['email']._serialized_options = b'\272HT\272\001Q\n\014string.email\022#value must be a valid email address\032\034this == \'\' || this.isEmail()\300J\001'
  _USERATTRIBUTES.fields_by_name['email_verified']._options = None
  _USERATTRIBUTES.fields_by_name['email_verified']._serialized_options = b'\030\001'
  _USERATTRIBUTES.fields_by_name['zoneinfo']._options = None
  _USERATTRIBUTES.fields_by_name['zoneinfo']._serialized_options = b'\030\001\300J\001'
  _USERATTRIBUTES.fields_by_name['locale']._options = None
  _USERATTRIBUTES.fields_by_name['locale']._serialized_options = b'\300J\001'
  _USERATTRIBUTES.fields_by_name['phone_number']._options = None
  _USERATTRIBUTES.fields_by_name['phone_number']._serialized_options = b'\300J\001'
  _USERATTRIBUTES.fields_by_name['phone_number_verified']._options = None
  _USERATTRIBUTES.fields_by_name['phone_number_verified']._serialized_options = b'\030\001'
  _TENANTUSERACCOUNTSPEC_VISIBLEATTRIBUTES.fields_by_name['attribute']._options = None
  _TENANTUSERACCOUNTSPEC_VISIBLEATTRIBUTES.fields_by_name['attribute']._serialized_options = b'\300J\001'
  _globals['_TENANTUSERACCOUNT']._serialized_start=147
  _globals['_TENANTUSERACCOUNT']._serialized_end=356
  _globals['_TENANTUSERACCOUNTWITHATTRIBUTES']._serialized_start=359
  _globals['_TENANTUSERACCOUNTWITHATTRIBUTES']._serialized_end=569
  _globals['_USERATTRIBUTES']._serialized_start=572
  _globals['_USERATTRIBUTES']._serialized_end=1213
  _globals['_ERROR']._serialized_start=1215
  _globals['_ERROR']._serialized_end=1239
  _globals['_TENANTUSERACCOUNTSPEC']._serialized_start=1242
  _globals['_TENANTUSERACCOUNTSPEC']._serialized_end=1394
  _globals['_TENANTUSERACCOUNTSPEC_VISIBLEATTRIBUTES']._serialized_start=1351
  _globals['_TENANTUSERACCOUNTSPEC_VISIBLEATTRIBUTES']._serialized_end=1394
  _globals['_TENANTUSERACCOUNTSTATUS']._serialized_start=1397
  _globals['_TENANTUSERACCOUNTSTATUS']._serialized_end=1600
  _globals['_TENANTUSERACCOUNTSTATUS_STATE']._serialized_start=1531
  _globals['_TENANTUSERACCOUNTSTATUS_STATE']._serialized_end=1600
# @@protoc_insertion_point(module_scope)
