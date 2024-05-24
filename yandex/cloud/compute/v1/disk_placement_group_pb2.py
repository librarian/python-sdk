# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/disk_placement_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/compute/v1/disk_placement_group.proto\x12\x17yandex.cloud.compute.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf4\x04\n\x12\x44iskPlacementGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12G\n\x06labels\x18\x06 \x03(\x0b\x32\x37.yandex.cloud.compute.v1.DiskPlacementGroup.LabelsEntry\x12\x0f\n\x07zone_id\x18\x07 \x01(\t\x12\x42\n\x06status\x18\x0b \x01(\x0e\x32\x32.yandex.cloud.compute.v1.DiskPlacementGroup.Status\x12Y\n\x19spread_placement_strategy\x18\x08 \x01(\x0b\x32\x34.yandex.cloud.compute.v1.DiskSpreadPlacementStrategyH\x00\x12_\n\x1cpartition_placement_strategy\x18\t \x01(\x0b\x32\x37.yandex.cloud.compute.v1.DiskPartitionPlacementStrategyH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"G\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x04\x42\x14\n\x12placement_strategyJ\x04\x08\n\x10\x0b\"\x1d\n\x1b\x44iskSpreadPlacementStrategy\"4\n\x1e\x44iskPartitionPlacementStrategy\x12\x12\n\npartitions\x18\x01 \x01(\x03\x42\x62\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.disk_placement_group_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _DISKPLACEMENTGROUP_LABELSENTRY._options = None
  _DISKPLACEMENTGROUP_LABELSENTRY._serialized_options = b'8\001'
  _globals['_DISKPLACEMENTGROUP']._serialized_start=113
  _globals['_DISKPLACEMENTGROUP']._serialized_end=741
  _globals['_DISKPLACEMENTGROUP_LABELSENTRY']._serialized_start=595
  _globals['_DISKPLACEMENTGROUP_LABELSENTRY']._serialized_end=640
  _globals['_DISKPLACEMENTGROUP_STATUS']._serialized_start=642
  _globals['_DISKPLACEMENTGROUP_STATUS']._serialized_end=713
  _globals['_DISKSPREADPLACEMENTSTRATEGY']._serialized_start=743
  _globals['_DISKSPREADPLACEMENTSTRATEGY']._serialized_end=772
  _globals['_DISKPARTITIONPLACEMENTSTRATEGY']._serialized_start=774
  _globals['_DISKPARTITIONPLACEMENTSTRATEGY']._serialized_end=826
# @@protoc_insertion_point(module_scope)
