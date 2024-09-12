# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/smartwebsecurity/v1/advanced_rate_limiter/advanced_rate_limiter_profile_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter import advanced_rate_limiter_profile_pb2 as yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nbyandex/cloud/smartwebsecurity/v1/advanced_rate_limiter/advanced_rate_limiter_profile_service.proto\x12\x36yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1aZyandex/cloud/smartwebsecurity/v1/advanced_rate_limiter/advanced_rate_limiter_profile.proto\x1a\x1dyandex/cloud/validation.proto\"V\n$GetAdvancedRateLimiterProfileRequest\x12.\n advanced_rate_limiter_profile_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"A\n&ListAdvancedRateLimiterProfilesRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\xa5\x01\n\'ListAdvancedRateLimiterProfilesResponse\x12z\n\x1e\x61\x64vanced_rate_limiter_profiles\x18\x01 \x03(\x0b\x32R.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfile\"\x87\x03\n\'CreateAdvancedRateLimiterProfileRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12{\n\x06labels\x18\x02 \x03(\x0b\x32k.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.CreateAdvancedRateLimiterProfileRequest.LabelsEntry\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12t\n\x1b\x61\x64vanced_rate_limiter_rules\x18\x05 \x03(\x0b\x32O.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"T\n(CreateAdvancedRateLimiterProfileMetadata\x12(\n advanced_rate_limiter_profile_id\x18\x01 \x01(\t\"\xcf\x03\n\'UpdateAdvancedRateLimiterProfileRequest\x12.\n advanced_rate_limiter_profile_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12{\n\x06labels\x18\x03 \x03(\x0b\x32k.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.UpdateAdvancedRateLimiterProfileRequest.LabelsEntry\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12t\n\x1b\x61\x64vanced_rate_limiter_rules\x18\x06 \x03(\x0b\x32O.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"T\n(UpdateAdvancedRateLimiterProfileMetadata\x12(\n advanced_rate_limiter_profile_id\x18\x01 \x01(\t\"Y\n\'DeleteAdvancedRateLimiterProfileRequest\x12.\n advanced_rate_limiter_profile_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"T\n(DeleteAdvancedRateLimiterProfileMetadata\x12(\n advanced_rate_limiter_profile_id\x18\x01 \x01(\t2\xc1\x0b\n!AdvancedRateLimiterProfileService\x12\x94\x02\n\x03Get\x12\\.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.GetAdvancedRateLimiterProfileRequest\x1aR.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfile\"[\x82\xd3\xe4\x93\x02U\x12S/smartwebsecurity/v1/advancedRateLimiterProfiles/{advanced_rate_limiter_profile_id}\x12\x81\x02\n\x04List\x12^.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.ListAdvancedRateLimiterProfilesRequest\x1a_.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.ListAdvancedRateLimiterProfilesResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/smartwebsecurity/v1/advancedRateLimiterProfiles\x12\x94\x02\n\x06\x43reate\x12_.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.CreateAdvancedRateLimiterProfileRequest\x1a!.yandex.cloud.operation.Operation\"\x85\x01\xb2\xd2*F\n(CreateAdvancedRateLimiterProfileMetadata\x12\x1a\x41\x64vancedRateLimiterProfile\x82\xd3\xe4\x93\x02\x35\"0/smartwebsecurity/v1/advancedRateLimiterProfiles:\x01*\x12\xb7\x02\n\x06Update\x12_.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.UpdateAdvancedRateLimiterProfileRequest\x1a!.yandex.cloud.operation.Operation\"\xa8\x01\xb2\xd2*F\n(UpdateAdvancedRateLimiterProfileMetadata\x12\x1a\x41\x64vancedRateLimiterProfile\x82\xd3\xe4\x93\x02X2S/smartwebsecurity/v1/advancedRateLimiterProfiles/{advanced_rate_limiter_profile_id}:\x01*\x12\xaf\x02\n\x06\x44\x65lete\x12_.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.DeleteAdvancedRateLimiterProfileRequest\x1a!.yandex.cloud.operation.Operation\"\xa0\x01\xb2\xd2*A\n(DeleteAdvancedRateLimiterProfileMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02U*S/smartwebsecurity/v1/advancedRateLimiterProfiles/{advanced_rate_limiter_profile_id}B\xa9\x01\n:yandex.cloud.api.smartwebsecurity.v1.advanced_rate_limiterZkgithub.com/yandex-cloud/go-genproto/yandex/cloud/smartwebsecurity/v1/advanced_rate_limiter;smartwebsecurityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.advanced_rate_limiter_profile_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n:yandex.cloud.api.smartwebsecurity.v1.advanced_rate_limiterZkgithub.com/yandex-cloud/go-genproto/yandex/cloud/smartwebsecurity/v1/advanced_rate_limiter;smartwebsecurity'
  _GETADVANCEDRATELIMITERPROFILEREQUEST.fields_by_name['advanced_rate_limiter_profile_id']._options = None
  _GETADVANCEDRATELIMITERPROFILEREQUEST.fields_by_name['advanced_rate_limiter_profile_id']._serialized_options = b'\350\3071\001'
  _LISTADVANCEDRATELIMITERPROFILESREQUEST.fields_by_name['folder_id']._options = None
  _LISTADVANCEDRATELIMITERPROFILESREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATEADVANCEDRATELIMITERPROFILEREQUEST_LABELSENTRY._options = None
  _CREATEADVANCEDRATELIMITERPROFILEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEADVANCEDRATELIMITERPROFILEREQUEST.fields_by_name['folder_id']._options = None
  _CREATEADVANCEDRATELIMITERPROFILEREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _UPDATEADVANCEDRATELIMITERPROFILEREQUEST_LABELSENTRY._options = None
  _UPDATEADVANCEDRATELIMITERPROFILEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEADVANCEDRATELIMITERPROFILEREQUEST.fields_by_name['advanced_rate_limiter_profile_id']._options = None
  _UPDATEADVANCEDRATELIMITERPROFILEREQUEST.fields_by_name['advanced_rate_limiter_profile_id']._serialized_options = b'\350\3071\001'
  _DELETEADVANCEDRATELIMITERPROFILEREQUEST.fields_by_name['advanced_rate_limiter_profile_id']._options = None
  _DELETEADVANCEDRATELIMITERPROFILEREQUEST.fields_by_name['advanced_rate_limiter_profile_id']._serialized_options = b'\350\3071\001'
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['Get']._options = None
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002U\022S/smartwebsecurity/v1/advancedRateLimiterProfiles/{advanced_rate_limiter_profile_id}'
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['List']._options = None
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\0022\0220/smartwebsecurity/v1/advancedRateLimiterProfiles'
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['Create']._options = None
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['Create']._serialized_options = b'\262\322*F\n(CreateAdvancedRateLimiterProfileMetadata\022\032AdvancedRateLimiterProfile\202\323\344\223\0025\"0/smartwebsecurity/v1/advancedRateLimiterProfiles:\001*'
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['Update']._options = None
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['Update']._serialized_options = b'\262\322*F\n(UpdateAdvancedRateLimiterProfileMetadata\022\032AdvancedRateLimiterProfile\202\323\344\223\002X2S/smartwebsecurity/v1/advancedRateLimiterProfiles/{advanced_rate_limiter_profile_id}:\001*'
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['Delete']._options = None
  _ADVANCEDRATELIMITERPROFILESERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*A\n(DeleteAdvancedRateLimiterProfileMetadata\022\025google.protobuf.Empty\202\323\344\223\002U*S/smartwebsecurity/v1/advancedRateLimiterProfiles/{advanced_rate_limiter_profile_id}'
  _globals['_GETADVANCEDRATELIMITERPROFILEREQUEST']._serialized_start=419
  _globals['_GETADVANCEDRATELIMITERPROFILEREQUEST']._serialized_end=505
  _globals['_LISTADVANCEDRATELIMITERPROFILESREQUEST']._serialized_start=507
  _globals['_LISTADVANCEDRATELIMITERPROFILESREQUEST']._serialized_end=572
  _globals['_LISTADVANCEDRATELIMITERPROFILESRESPONSE']._serialized_start=575
  _globals['_LISTADVANCEDRATELIMITERPROFILESRESPONSE']._serialized_end=740
  _globals['_CREATEADVANCEDRATELIMITERPROFILEREQUEST']._serialized_start=743
  _globals['_CREATEADVANCEDRATELIMITERPROFILEREQUEST']._serialized_end=1134
  _globals['_CREATEADVANCEDRATELIMITERPROFILEREQUEST_LABELSENTRY']._serialized_start=1089
  _globals['_CREATEADVANCEDRATELIMITERPROFILEREQUEST_LABELSENTRY']._serialized_end=1134
  _globals['_CREATEADVANCEDRATELIMITERPROFILEMETADATA']._serialized_start=1136
  _globals['_CREATEADVANCEDRATELIMITERPROFILEMETADATA']._serialized_end=1220
  _globals['_UPDATEADVANCEDRATELIMITERPROFILEREQUEST']._serialized_start=1223
  _globals['_UPDATEADVANCEDRATELIMITERPROFILEREQUEST']._serialized_end=1686
  _globals['_UPDATEADVANCEDRATELIMITERPROFILEREQUEST_LABELSENTRY']._serialized_start=1089
  _globals['_UPDATEADVANCEDRATELIMITERPROFILEREQUEST_LABELSENTRY']._serialized_end=1134
  _globals['_UPDATEADVANCEDRATELIMITERPROFILEMETADATA']._serialized_start=1688
  _globals['_UPDATEADVANCEDRATELIMITERPROFILEMETADATA']._serialized_end=1772
  _globals['_DELETEADVANCEDRATELIMITERPROFILEREQUEST']._serialized_start=1774
  _globals['_DELETEADVANCEDRATELIMITERPROFILEREQUEST']._serialized_end=1863
  _globals['_DELETEADVANCEDRATELIMITERPROFILEMETADATA']._serialized_start=1865
  _globals['_DELETEADVANCEDRATELIMITERPROFILEMETADATA']._serialized_end=1949
  _globals['_ADVANCEDRATELIMITERPROFILESERVICE']._serialized_start=1952
  _globals['_ADVANCEDRATELIMITERPROFILESERVICE']._serialized_end=3425
# @@protoc_insertion_point(module_scope)
