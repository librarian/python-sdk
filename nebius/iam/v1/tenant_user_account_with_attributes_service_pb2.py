# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/iam/v1/tenant_user_account_with_attributes_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nebius import annotations_pb2 as nebius_dot_annotations__pb2
from nebius.iam.v1 import tenant_user_account_pb2 as nebius_dot_iam_dot_v1_dot_tenant__user__account__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?nebius/iam/v1/tenant_user_account_with_attributes_service.proto\x12\rnebius.iam.v1\x1a\x18nebius/annotations.proto\x1a\'nebius/iam/v1/tenant_user_account.proto\"7\n)GetTenantUserAccountWithAttributesRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x8f\x01\n+ListTenantUserAccountsWithAttributesRequest\x12\x11\n\tparent_id\x18\x01 \x01(\t\x12\x16\n\tpage_size\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06\x66ilter\x18\x04 \x01(\tB\x03\xc0J\x01\x42\x0c\n\n_page_size\"\x86\x01\n,ListTenantUserAccountsWithAttributesResponse\x12=\n\x05items\x18\x01 \x03(\x0b\x32..nebius.iam.v1.TenantUserAccountWithAttributes\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa6\x02\n&TenantUserAccountWithAttributesService\x12o\n\x03Get\x12\x38.nebius.iam.v1.GetTenantUserAccountWithAttributesRequest\x1a..nebius.iam.v1.TenantUserAccountWithAttributes\x12\x7f\n\x04List\x12:.nebius.iam.v1.ListTenantUserAccountsWithAttributesRequest\x1a;.nebius.iam.v1.ListTenantUserAccountsWithAttributesResponse\x1a\n\xbaJ\x07\x63pl.iamBr\n\x14\x61i.nebius.pub.iam.v1B+TenantUserAccountWithAttributesServiceProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/iam/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.iam.v1.tenant_user_account_with_attributes_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.iam.v1B+TenantUserAccountWithAttributesServiceProtoP\001Z+github.com/nebius/gosdk/proto/nebius/iam/v1'
  _LISTTENANTUSERACCOUNTSWITHATTRIBUTESREQUEST.fields_by_name['filter']._options = None
  _LISTTENANTUSERACCOUNTSWITHATTRIBUTESREQUEST.fields_by_name['filter']._serialized_options = b'\300J\001'
  _TENANTUSERACCOUNTWITHATTRIBUTESSERVICE._options = None
  _TENANTUSERACCOUNTWITHATTRIBUTESSERVICE._serialized_options = b'\272J\007cpl.iam'
  _globals['_GETTENANTUSERACCOUNTWITHATTRIBUTESREQUEST']._serialized_start=149
  _globals['_GETTENANTUSERACCOUNTWITHATTRIBUTESREQUEST']._serialized_end=204
  _globals['_LISTTENANTUSERACCOUNTSWITHATTRIBUTESREQUEST']._serialized_start=207
  _globals['_LISTTENANTUSERACCOUNTSWITHATTRIBUTESREQUEST']._serialized_end=350
  _globals['_LISTTENANTUSERACCOUNTSWITHATTRIBUTESRESPONSE']._serialized_start=353
  _globals['_LISTTENANTUSERACCOUNTSWITHATTRIBUTESRESPONSE']._serialized_end=487
  _globals['_TENANTUSERACCOUNTWITHATTRIBUTESSERVICE']._serialized_start=490
  _globals['_TENANTUSERACCOUNTWITHATTRIBUTESSERVICE']._serialized_end=784
# @@protoc_insertion_point(module_scope)
