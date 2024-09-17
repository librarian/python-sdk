# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/eventrouter/v1/rule_service.proto
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
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.serverless.eventrouter.v1 import rule_pb2 as yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9yandex/cloud/serverless/eventrouter/v1/rule_service.proto\x12&yandex.cloud.serverless.eventrouter.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a yandex/cloud/access/access.proto\x1a\x31yandex/cloud/serverless/eventrouter/v1/rule.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"\'\n\x0eGetRuleRequest\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x86\x01\n\x10ListRulesRequest\x12\x10\n\x06\x62us_id\x18\x01 \x01(\tH\x00\x12\x13\n\tfolder_id\x18\x02 \x01(\tH\x00\x12\x11\n\tpage_size\x18\x03 \x01(\x03\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\tB\x14\n\x0c\x63ontainer_id\x12\x04\xc0\xc1\x31\x01\"i\n\x11ListRulesResponse\x12;\n\x05rules\x18\x01 \x03(\x0b\x32,.yandex.cloud.serverless.eventrouter.v1.Rule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xe5\x03\n\x11\x43reateRuleRequest\x12\x14\n\x06\x62us_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x92\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x45.yandex.cloud.serverless.eventrouter.v1.CreateRuleRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12>\n\x06\x66ilter\x18\x05 \x01(\x0b\x32..yandex.cloud.serverless.eventrouter.v1.Filter\x12H\n\x07targets\x18\x06 \x03(\x0b\x32..yandex.cloud.serverless.eventrouter.v1.TargetB\x07\x82\xc8\x31\x03\x31-5\x12\x1b\n\x13\x64\x65letion_protection\x18\x07 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"5\n\x12\x43reateRuleMetadata\x12\x0f\n\x07rule_id\x18\x01 \x01(\t\x12\x0e\n\x06\x62us_id\x18\x02 \x01(\t\"\x97\x04\n\x11UpdateRuleRequest\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x92\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x45.yandex.cloud.serverless.eventrouter.v1.UpdateRuleRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12>\n\x06\x66ilter\x18\x06 \x01(\x0b\x32..yandex.cloud.serverless.eventrouter.v1.Filter\x12H\n\x07targets\x18\x07 \x03(\x0b\x32..yandex.cloud.serverless.eventrouter.v1.TargetB\x07\x82\xc8\x31\x03\x31-5\x12\x1b\n\x13\x64\x65letion_protection\x18\x08 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x12UpdateRuleMetadata\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"*\n\x11\x44\x65leteRuleRequest\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"+\n\x12\x44\x65leteRuleMetadata\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x8c\x01\n\x19ListRuleOperationsRequest\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"l\n\x1aListRuleOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"*\n\x11\x45nableRuleRequest\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"+\n\x12\x45nableRuleMetadata\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"+\n\x12\x44isableRuleRequest\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\",\n\x13\x44isableRuleMetadata\x12\x15\n\x07rule_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x32\xd3\x10\n\x0bRuleService\x12\x94\x01\n\x03Get\x12\x36.yandex.cloud.serverless.eventrouter.v1.GetRuleRequest\x1a,.yandex.cloud.serverless.eventrouter.v1.Rule\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/eventrouter/v1/rules/{rule_id}\x12\x9a\x01\n\x04List\x12\x38.yandex.cloud.serverless.eventrouter.v1.ListRulesRequest\x1a\x39.yandex.cloud.serverless.eventrouter.v1.ListRulesResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/eventrouter/v1/rules\x12\xa6\x01\n\x06\x43reate\x12\x39.yandex.cloud.serverless.eventrouter.v1.CreateRuleRequest\x1a!.yandex.cloud.operation.Operation\">\xb2\xd2*\x1a\n\x12\x43reateRuleMetadata\x12\x04Rule\x82\xd3\xe4\x93\x02\x1a\"\x15/eventrouter/v1/rules:\x01*\x12\xb0\x01\n\x06Update\x12\x39.yandex.cloud.serverless.eventrouter.v1.UpdateRuleRequest\x1a!.yandex.cloud.operation.Operation\"H\xb2\xd2*\x1a\n\x12UpdateRuleMetadata\x12\x04Rule\x82\xd3\xe4\x93\x02$2\x1f/eventrouter/v1/rules/{rule_id}:\x01*\x12\xbe\x01\n\x06\x44\x65lete\x12\x39.yandex.cloud.serverless.eventrouter.v1.DeleteRuleRequest\x1a!.yandex.cloud.operation.Operation\"V\xb2\xd2*+\n\x12\x44\x65leteRuleMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02!*\x1f/eventrouter/v1/rules/{rule_id}\x12\xc5\x01\n\x06\x45nable\x12\x39.yandex.cloud.serverless.eventrouter.v1.EnableRuleRequest\x1a!.yandex.cloud.operation.Operation\"]\xb2\xd2*+\n\x12\x45nableRuleMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02(\"&/eventrouter/v1/rules/{rule_id}:enable\x12\xc9\x01\n\x07\x44isable\x12:.yandex.cloud.serverless.eventrouter.v1.DisableRuleRequest\x1a!.yandex.cloud.operation.Operation\"_\xb2\xd2*,\n\x13\x44isableRuleMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02)\"\'/eventrouter/v1/rules/{rule_id}:disable\x12\xb5\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/eventrouter/v1/rules/{resource_id}:listAccessBindings\x12\xe4\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"}\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02:\"5/eventrouter/v1/rules/{resource_id}:setAccessBindings:\x01*\x12\xf1\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x83\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02=28/eventrouter/v1/rules/{resource_id}:updateAccessBindings:\x01*\x12\xcb\x01\n\x0eListOperations\x12\x41.yandex.cloud.serverless.eventrouter.v1.ListRuleOperationsRequest\x1a\x42.yandex.cloud.serverless.eventrouter.v1.ListRuleOperationsResponse\"2\x82\xd3\xe4\x93\x02,\x12*/eventrouter/v1/rules/{rule_id}/operationsB\x8b\x01\n*yandex.cloud.api.serverless.eventrouter.v1B\x05PERRSZVgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/eventrouter/v1;eventrouterb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.eventrouter.v1.rule_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n*yandex.cloud.api.serverless.eventrouter.v1B\005PERRSZVgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/eventrouter/v1;eventrouter'
  _GETRULEREQUEST.fields_by_name['rule_id']._options = None
  _GETRULEREQUEST.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _LISTRULESREQUEST.oneofs_by_name['container_id']._options = None
  _LISTRULESREQUEST.oneofs_by_name['container_id']._serialized_options = b'\300\3011\001'
  _CREATERULEREQUEST_LABELSENTRY._options = None
  _CREATERULEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATERULEREQUEST.fields_by_name['bus_id']._options = None
  _CREATERULEREQUEST.fields_by_name['bus_id']._serialized_options = b'\350\3071\001'
  _CREATERULEREQUEST.fields_by_name['name']._options = None
  _CREATERULEREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _CREATERULEREQUEST.fields_by_name['description']._options = None
  _CREATERULEREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATERULEREQUEST.fields_by_name['labels']._options = None
  _CREATERULEREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _CREATERULEREQUEST.fields_by_name['targets']._options = None
  _CREATERULEREQUEST.fields_by_name['targets']._serialized_options = b'\202\3101\0031-5'
  _UPDATERULEREQUEST_LABELSENTRY._options = None
  _UPDATERULEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATERULEREQUEST.fields_by_name['rule_id']._options = None
  _UPDATERULEREQUEST.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _UPDATERULEREQUEST.fields_by_name['name']._options = None
  _UPDATERULEREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _UPDATERULEREQUEST.fields_by_name['description']._options = None
  _UPDATERULEREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATERULEREQUEST.fields_by_name['labels']._options = None
  _UPDATERULEREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _UPDATERULEREQUEST.fields_by_name['targets']._options = None
  _UPDATERULEREQUEST.fields_by_name['targets']._serialized_options = b'\202\3101\0031-5'
  _UPDATERULEMETADATA.fields_by_name['rule_id']._options = None
  _UPDATERULEMETADATA.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _DELETERULEREQUEST.fields_by_name['rule_id']._options = None
  _DELETERULEREQUEST.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _DELETERULEMETADATA.fields_by_name['rule_id']._options = None
  _DELETERULEMETADATA.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _LISTRULEOPERATIONSREQUEST.fields_by_name['rule_id']._options = None
  _LISTRULEOPERATIONSREQUEST.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _LISTRULEOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTRULEOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTRULEOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTRULEOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTRULEOPERATIONSREQUEST.fields_by_name['filter']._options = None
  _LISTRULEOPERATIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _ENABLERULEREQUEST.fields_by_name['rule_id']._options = None
  _ENABLERULEREQUEST.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _ENABLERULEMETADATA.fields_by_name['rule_id']._options = None
  _ENABLERULEMETADATA.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _DISABLERULEREQUEST.fields_by_name['rule_id']._options = None
  _DISABLERULEREQUEST.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _DISABLERULEMETADATA.fields_by_name['rule_id']._options = None
  _DISABLERULEMETADATA.fields_by_name['rule_id']._serialized_options = b'\350\3071\001'
  _RULESERVICE.methods_by_name['Get']._options = None
  _RULESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002!\022\037/eventrouter/v1/rules/{rule_id}'
  _RULESERVICE.methods_by_name['List']._options = None
  _RULESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\027\022\025/eventrouter/v1/rules'
  _RULESERVICE.methods_by_name['Create']._options = None
  _RULESERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\032\n\022CreateRuleMetadata\022\004Rule\202\323\344\223\002\032\"\025/eventrouter/v1/rules:\001*'
  _RULESERVICE.methods_by_name['Update']._options = None
  _RULESERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\032\n\022UpdateRuleMetadata\022\004Rule\202\323\344\223\002$2\037/eventrouter/v1/rules/{rule_id}:\001*'
  _RULESERVICE.methods_by_name['Delete']._options = None
  _RULESERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*+\n\022DeleteRuleMetadata\022\025google.protobuf.Empty\202\323\344\223\002!*\037/eventrouter/v1/rules/{rule_id}'
  _RULESERVICE.methods_by_name['Enable']._options = None
  _RULESERVICE.methods_by_name['Enable']._serialized_options = b'\262\322*+\n\022EnableRuleMetadata\022\025google.protobuf.Empty\202\323\344\223\002(\"&/eventrouter/v1/rules/{rule_id}:enable'
  _RULESERVICE.methods_by_name['Disable']._options = None
  _RULESERVICE.methods_by_name['Disable']._serialized_options = b'\262\322*,\n\023DisableRuleMetadata\022\025google.protobuf.Empty\202\323\344\223\002)\"\'/eventrouter/v1/rules/{rule_id}:disable'
  _RULESERVICE.methods_by_name['ListAccessBindings']._options = None
  _RULESERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\0028\0226/eventrouter/v1/rules/{resource_id}:listAccessBindings'
  _RULESERVICE.methods_by_name['SetAccessBindings']._options = None
  _RULESERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002:\"5/eventrouter/v1/rules/{resource_id}:setAccessBindings:\001*'
  _RULESERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _RULESERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002=28/eventrouter/v1/rules/{resource_id}:updateAccessBindings:\001*'
  _RULESERVICE.methods_by_name['ListOperations']._options = None
  _RULESERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002,\022*/eventrouter/v1/rules/{rule_id}/operations'
  _globals['_GETRULEREQUEST']._serialized_start=355
  _globals['_GETRULEREQUEST']._serialized_end=394
  _globals['_LISTRULESREQUEST']._serialized_start=397
  _globals['_LISTRULESREQUEST']._serialized_end=531
  _globals['_LISTRULESRESPONSE']._serialized_start=533
  _globals['_LISTRULESRESPONSE']._serialized_end=638
  _globals['_CREATERULEREQUEST']._serialized_start=641
  _globals['_CREATERULEREQUEST']._serialized_end=1126
  _globals['_CREATERULEREQUEST_LABELSENTRY']._serialized_start=1081
  _globals['_CREATERULEREQUEST_LABELSENTRY']._serialized_end=1126
  _globals['_CREATERULEMETADATA']._serialized_start=1128
  _globals['_CREATERULEMETADATA']._serialized_end=1181
  _globals['_UPDATERULEREQUEST']._serialized_start=1184
  _globals['_UPDATERULEREQUEST']._serialized_end=1719
  _globals['_UPDATERULEREQUEST_LABELSENTRY']._serialized_start=1081
  _globals['_UPDATERULEREQUEST_LABELSENTRY']._serialized_end=1126
  _globals['_UPDATERULEMETADATA']._serialized_start=1721
  _globals['_UPDATERULEMETADATA']._serialized_end=1764
  _globals['_DELETERULEREQUEST']._serialized_start=1766
  _globals['_DELETERULEREQUEST']._serialized_end=1808
  _globals['_DELETERULEMETADATA']._serialized_start=1810
  _globals['_DELETERULEMETADATA']._serialized_end=1853
  _globals['_LISTRULEOPERATIONSREQUEST']._serialized_start=1856
  _globals['_LISTRULEOPERATIONSREQUEST']._serialized_end=1996
  _globals['_LISTRULEOPERATIONSRESPONSE']._serialized_start=1998
  _globals['_LISTRULEOPERATIONSRESPONSE']._serialized_end=2106
  _globals['_ENABLERULEREQUEST']._serialized_start=2108
  _globals['_ENABLERULEREQUEST']._serialized_end=2150
  _globals['_ENABLERULEMETADATA']._serialized_start=2152
  _globals['_ENABLERULEMETADATA']._serialized_end=2195
  _globals['_DISABLERULEREQUEST']._serialized_start=2197
  _globals['_DISABLERULEREQUEST']._serialized_end=2240
  _globals['_DISABLERULEMETADATA']._serialized_start=2242
  _globals['_DISABLERULEMETADATA']._serialized_end=2286
  _globals['_RULESERVICE']._serialized_start=2289
  _globals['_RULESERVICE']._serialized_end=4420
# @@protoc_insertion_point(module_scope)
