# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/elasticsearch/v1/config/elasticsearch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<yandex/cloud/mdb/elasticsearch/v1/config/elasticsearch.proto\x12(yandex.cloud.mdb.elasticsearch.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xb0\x01\n\x14\x45lasticsearchConfig7\x12\x35\n\x10max_clause_count\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x1c\n\x14\x66ielddata_cache_size\x18\x04 \x01(\t\x12 \n\x18reindex_remote_whitelist\x18\x06 \x01(\t\x12\x1b\n\x13reindex_ssl_ca_path\x18\x07 \x01(\tJ\x04\x08\x05\x10\x06\"\xa6\x02\n\x17\x45lasticsearchConfigSet7\x12^\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32>.yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7B\x04\xe8\xc7\x31\x01\x12S\n\x0buser_config\x18\x02 \x01(\x0b\x32>.yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7\x12V\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32>.yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7B\x8a\x01\n,yandex.cloud.api.mdb.elasticsearch.v1.configZZgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1/config;elasticsearchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.elasticsearch.v1.config.elasticsearch_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n,yandex.cloud.api.mdb.elasticsearch.v1.configZZgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1/config;elasticsearch'
  _ELASTICSEARCHCONFIGSET7.fields_by_name['effective_config']._options = None
  _ELASTICSEARCHCONFIGSET7.fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _globals['_ELASTICSEARCHCONFIG7']._serialized_start=170
  _globals['_ELASTICSEARCHCONFIG7']._serialized_end=346
  _globals['_ELASTICSEARCHCONFIGSET7']._serialized_start=349
  _globals['_ELASTICSEARCHCONFIGSET7']._serialized_end=643
# @@protoc_insertion_point(module_scope)
