# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/kafka/v1/topic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud.mdb.kafka.v1 import common_pb2 as yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%yandex/cloud/mdb/kafka/v1/topic.proto\x12\x19yandex.cloud.mdb.kafka.v1\x1a google/protobuf/descriptor.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a&yandex/cloud/mdb/kafka/v1/common.proto\"\xd3\x02\n\x05Topic\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12/\n\npartitions\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x12replication_factor\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12V\n\x10topic_config_2_8\x18\x07 \x01(\x0b\x32).yandex.cloud.mdb.kafka.v1.TopicConfig2_8H\x00R\x0ftopicConfig_2_8\x12P\n\x0etopic_config_3\x18\x08 \x01(\x0b\x32\'.yandex.cloud.mdb.kafka.v1.TopicConfig3H\x00R\rtopicConfig_3B\x0e\n\x0ctopic_configJ\x04\x08\x05\x10\x07\"\xc3\x02\n\tTopicSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\npartitions\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x12replication_factor\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12V\n\x10topic_config_2_8\x18\x06 \x01(\x0b\x32).yandex.cloud.mdb.kafka.v1.TopicConfig2_8H\x00R\x0ftopicConfig_2_8\x12P\n\x0etopic_config_3\x18\x07 \x01(\x0b\x32\'.yandex.cloud.mdb.kafka.v1.TopicConfig3H\x00R\rtopicConfig_3B\x0e\n\x0ctopic_configJ\x04\x08\x04\x10\x06\"\x8c\x07\n\x0eTopicConfig2_8\x12O\n\x0e\x63leanup_policy\x18\x01 \x01(\x0e\x32\x37.yandex.cloud.mdb.kafka.v1.TopicConfig2_8.CleanupPolicy\x12\x44\n\x10\x63ompression_type\x18\x02 \x01(\x0e\x32*.yandex.cloud.mdb.kafka.v1.CompressionType\x12\x38\n\x13\x64\x65lete_retention_ms\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14\x66ile_delete_delay_ms\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0e\x66lush_messages\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12-\n\x08\x66lush_ms\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x15min_compaction_lag_ms\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x34\n\x0fretention_bytes\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0cretention_ms\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11max_message_bytes\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13min_insync_replicas\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\rsegment_bytes\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12/\n\x0bpreallocate\x18\r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x8d\x01\n\rCleanupPolicy\x12\x1e\n\x1a\x43LEANUP_POLICY_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43LEANUP_POLICY_DELETE\x10\x01\x12\x1a\n\x16\x43LEANUP_POLICY_COMPACT\x10\x02\x12%\n!CLEANUP_POLICY_COMPACT_AND_DELETE\x10\x03\"\x88\x07\n\x0cTopicConfig3\x12M\n\x0e\x63leanup_policy\x18\x01 \x01(\x0e\x32\x35.yandex.cloud.mdb.kafka.v1.TopicConfig3.CleanupPolicy\x12\x44\n\x10\x63ompression_type\x18\x02 \x01(\x0e\x32*.yandex.cloud.mdb.kafka.v1.CompressionType\x12\x38\n\x13\x64\x65lete_retention_ms\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14\x66ile_delete_delay_ms\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0e\x66lush_messages\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12-\n\x08\x66lush_ms\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x15min_compaction_lag_ms\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x34\n\x0fretention_bytes\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0cretention_ms\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11max_message_bytes\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13min_insync_replicas\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\rsegment_bytes\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12/\n\x0bpreallocate\x18\r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x8d\x01\n\rCleanupPolicy\x12\x1e\n\x1a\x43LEANUP_POLICY_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43LEANUP_POLICY_DELETE\x10\x01\x12\x1a\n\x16\x43LEANUP_POLICY_COMPACT\x10\x02\x12%\n!CLEANUP_POLICY_COMPACT_AND_DELETE\x10\x03\x42\x64\n\x1dyandex.cloud.api.mdb.kafka.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/kafka/v1;kafkab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.kafka.v1.topic_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035yandex.cloud.api.mdb.kafka.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/kafka/v1;kafka'
  _globals['_TOPIC']._serialized_start=175
  _globals['_TOPIC']._serialized_end=514
  _globals['_TOPICSPEC']._serialized_start=517
  _globals['_TOPICSPEC']._serialized_end=840
  _globals['_TOPICCONFIG2_8']._serialized_start=843
  _globals['_TOPICCONFIG2_8']._serialized_end=1751
  _globals['_TOPICCONFIG2_8_CLEANUPPOLICY']._serialized_start=1610
  _globals['_TOPICCONFIG2_8_CLEANUPPOLICY']._serialized_end=1751
  _globals['_TOPICCONFIG3']._serialized_start=1754
  _globals['_TOPICCONFIG3']._serialized_end=2658
  _globals['_TOPICCONFIG3_CLEANUPPOLICY']._serialized_start=1610
  _globals['_TOPICCONFIG3_CLEANUPPOLICY']._serialized_end=1751
# @@protoc_insertion_point(module_scope)
