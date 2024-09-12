# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/smartwebsecurity/v1/advanced_rate_limiter/advanced_rate_limiter_profile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.smartwebsecurity.v1 import security_profile_pb2 as yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_security__profile__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nZyandex/cloud/smartwebsecurity/v1/advanced_rate_limiter/advanced_rate_limiter_profile.proto\x12\x36yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x37yandex/cloud/smartwebsecurity/v1/security_profile.proto\x1a\x1dyandex/cloud/validation.proto\"\xb0\x04\n\x1a\x41\x64vancedRateLimiterProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\xab\x01\n\x06labels\x18\x03 \x03(\x0b\x32^.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfile.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x38\n\x04name\x18\x04 \x01(\tB*\xe8\xc7\x31\x01\xf2\xc7\x31\x1a[a-zA-Z0-9][a-zA-Z0-9-_.]*\x8a\xc8\x31\x04\x31-50\x12\x1e\n\x0b\x64\x65scription\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=512\x12t\n\x1b\x61\x64vanced_rate_limiter_rules\x18\x06 \x03(\x0b\x32O.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x63loud_id\x18\t \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x08\x10\t\"\xe3\x10\n\x17\x41\x64vancedRateLimiterRule\x12\x38\n\x04name\x18\x01 \x01(\tB*\xe8\xc7\x31\x01\xf2\xc7\x31\x1a[a-zA-Z0-9][a-zA-Z0-9-_.]*\x8a\xc8\x31\x04\x31-50\x12\x1e\n\x08priority\x18\x02 \x01(\x03\x42\x0c\xfa\xc7\x31\x08\x31-999999\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=512\x12\x0f\n\x07\x64ry_run\x18\x04 \x01(\x08\x12s\n\x0cstatic_quota\x18\x05 \x01(\x0b\x32[.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule.StaticQuotaH\x00\x12u\n\rdynamic_quota\x18\x06 \x01(\x0b\x32\\.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule.DynamicQuotaH\x00\x1a\xa7\x02\n\x0bStaticQuota\x12\x66\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32V.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule.Action\x12>\n\tcondition\x18\x02 \x01(\x0b\x32+.yandex.cloud.smartwebsecurity.v1.Condition\x12\"\n\x05limit\x18\x03 \x01(\x03\x42\x13\xfa\xc7\x31\x0f\x31-9999999999999\x12L\n\x06period\x18\x04 \x01(\x03\x42<\xfa\xc7\x31\x38\x31,5,10,30,60,120,180,240,300,600,900,1200,1800,2700,3600\x1a\xe2\n\n\x0c\x44ynamicQuota\x12\x66\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32V.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule.Action\x12>\n\tcondition\x18\x02 \x01(\x0b\x32+.yandex.cloud.smartwebsecurity.v1.Condition\x12\"\n\x05limit\x18\x03 \x01(\x03\x42\x13\xfa\xc7\x31\x0f\x31-9999999999999\x12L\n\x06period\x18\x04 \x01(\x03\x42<\xfa\xc7\x31\x38\x31,5,10,30,60,120,180,240,300,600,900,1200,1800,2700,3600\x12\x8d\x01\n\x0f\x63haracteristics\x18\x05 \x03(\x0b\x32k.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule.DynamicQuota.CharacteristicB\x07\x82\xc8\x31\x03<=3\x1a\xa7\x07\n\x0e\x43haracteristic\x12\xa2\x01\n\x15simple_characteristic\x18\x01 \x01(\x0b\x32\x80\x01.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule.DynamicQuota.Characteristic.SimpleCharacteristicH\x00\x12\x9b\x01\n\x12key_characteristic\x18\x02 \x01(\x0b\x32}.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule.DynamicQuota.Characteristic.KeyCharacteristicH\x00\x12\x18\n\x10\x63\x61se_insensitive\x18\n \x01(\x08\x1a\x89\x02\n\x14SimpleCharacteristic\x12\x94\x01\n\x04type\x18\x01 \x01(\x0e\x32\x85\x01.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule.DynamicQuota.Characteristic.SimpleCharacteristic.Type\"Z\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cREQUEST_PATH\x10\x01\x12\x0f\n\x0bHTTP_METHOD\x10\x02\x12\x06\n\x02IP\x10\x03\x12\x07\n\x03GEO\x10\x04\x12\x08\n\x04HOST\x10\x05\x1a\x83\x02\n\x11KeyCharacteristic\x12\x91\x01\n\x04type\x18\x01 \x01(\x0e\x32\x82\x01.yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterRule.DynamicQuota.Characteristic.KeyCharacteristic.Type\x12\r\n\x05value\x18\x02 \x01(\t\"K\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nCOOKIE_KEY\x10\x01\x12\x0e\n\nHEADER_KEY\x10\x02\x12\r\n\tQUERY_KEY\x10\x03\x42 \n\x18\x63haracteristic_specifier\x12\x04\xc0\xc1\x31\x01J\x04\x08\x03\x10\n\"*\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x08\n\x04\x44\x45NY\x10\x01\x42\x16\n\x0erule_specifier\x12\x04\xc0\xc1\x31\x01\x42\xa9\x01\n:yandex.cloud.api.smartwebsecurity.v1.advanced_rate_limiterZkgithub.com/yandex-cloud/go-genproto/yandex/cloud/smartwebsecurity/v1/advanced_rate_limiter;smartwebsecurityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.advanced_rate_limiter_profile_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n:yandex.cloud.api.smartwebsecurity.v1.advanced_rate_limiterZkgithub.com/yandex-cloud/go-genproto/yandex/cloud/smartwebsecurity/v1/advanced_rate_limiter;smartwebsecurity'
  _ADVANCEDRATELIMITERPROFILE_LABELSENTRY._options = None
  _ADVANCEDRATELIMITERPROFILE_LABELSENTRY._serialized_options = b'8\001'
  _ADVANCEDRATELIMITERPROFILE.fields_by_name['labels']._options = None
  _ADVANCEDRATELIMITERPROFILE.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _ADVANCEDRATELIMITERPROFILE.fields_by_name['name']._options = None
  _ADVANCEDRATELIMITERPROFILE.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\032[a-zA-Z0-9][a-zA-Z0-9-_.]*\212\3101\0041-50'
  _ADVANCEDRATELIMITERPROFILE.fields_by_name['description']._options = None
  _ADVANCEDRATELIMITERPROFILE.fields_by_name['description']._serialized_options = b'\212\3101\005<=512'
  _ADVANCEDRATELIMITERRULE_STATICQUOTA.fields_by_name['limit']._options = None
  _ADVANCEDRATELIMITERRULE_STATICQUOTA.fields_by_name['limit']._serialized_options = b'\372\3071\0171-9999999999999'
  _ADVANCEDRATELIMITERRULE_STATICQUOTA.fields_by_name['period']._options = None
  _ADVANCEDRATELIMITERRULE_STATICQUOTA.fields_by_name['period']._serialized_options = b'\372\307181,5,10,30,60,120,180,240,300,600,900,1200,1800,2700,3600'
  _ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC.oneofs_by_name['characteristic_specifier']._options = None
  _ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC.oneofs_by_name['characteristic_specifier']._serialized_options = b'\300\3011\001'
  _ADVANCEDRATELIMITERRULE_DYNAMICQUOTA.fields_by_name['limit']._options = None
  _ADVANCEDRATELIMITERRULE_DYNAMICQUOTA.fields_by_name['limit']._serialized_options = b'\372\3071\0171-9999999999999'
  _ADVANCEDRATELIMITERRULE_DYNAMICQUOTA.fields_by_name['period']._options = None
  _ADVANCEDRATELIMITERRULE_DYNAMICQUOTA.fields_by_name['period']._serialized_options = b'\372\307181,5,10,30,60,120,180,240,300,600,900,1200,1800,2700,3600'
  _ADVANCEDRATELIMITERRULE_DYNAMICQUOTA.fields_by_name['characteristics']._options = None
  _ADVANCEDRATELIMITERRULE_DYNAMICQUOTA.fields_by_name['characteristics']._serialized_options = b'\202\3101\003<=3'
  _ADVANCEDRATELIMITERRULE.oneofs_by_name['rule_specifier']._options = None
  _ADVANCEDRATELIMITERRULE.oneofs_by_name['rule_specifier']._serialized_options = b'\300\3011\001'
  _ADVANCEDRATELIMITERRULE.fields_by_name['name']._options = None
  _ADVANCEDRATELIMITERRULE.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\032[a-zA-Z0-9][a-zA-Z0-9-_.]*\212\3101\0041-50'
  _ADVANCEDRATELIMITERRULE.fields_by_name['priority']._options = None
  _ADVANCEDRATELIMITERRULE.fields_by_name['priority']._serialized_options = b'\372\3071\0101-999999'
  _ADVANCEDRATELIMITERRULE.fields_by_name['description']._options = None
  _ADVANCEDRATELIMITERRULE.fields_by_name['description']._serialized_options = b'\212\3101\005<=512'
  _globals['_ADVANCEDRATELIMITERPROFILE']._serialized_start=272
  _globals['_ADVANCEDRATELIMITERPROFILE']._serialized_end=832
  _globals['_ADVANCEDRATELIMITERPROFILE_LABELSENTRY']._serialized_start=781
  _globals['_ADVANCEDRATELIMITERPROFILE_LABELSENTRY']._serialized_end=826
  _globals['_ADVANCEDRATELIMITERRULE']._serialized_start=835
  _globals['_ADVANCEDRATELIMITERRULE']._serialized_end=2982
  _globals['_ADVANCEDRATELIMITERRULE_STATICQUOTA']._serialized_start=1238
  _globals['_ADVANCEDRATELIMITERRULE_STATICQUOTA']._serialized_end=1533
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA']._serialized_start=1536
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA']._serialized_end=2914
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC']._serialized_start=1979
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC']._serialized_end=2914
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC_SIMPLECHARACTERISTIC']._serialized_start=2347
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC_SIMPLECHARACTERISTIC']._serialized_end=2612
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC_SIMPLECHARACTERISTIC_TYPE']._serialized_start=2522
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC_SIMPLECHARACTERISTIC_TYPE']._serialized_end=2612
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC_KEYCHARACTERISTIC']._serialized_start=2615
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC_KEYCHARACTERISTIC']._serialized_end=2874
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC_KEYCHARACTERISTIC_TYPE']._serialized_start=2799
  _globals['_ADVANCEDRATELIMITERRULE_DYNAMICQUOTA_CHARACTERISTIC_KEYCHARACTERISTIC_TYPE']._serialized_end=2874
  _globals['_ADVANCEDRATELIMITERRULE_ACTION']._serialized_start=2916
  _globals['_ADVANCEDRATELIMITERRULE_ACTION']._serialized_end=2958
# @@protoc_insertion_point(module_scope)
