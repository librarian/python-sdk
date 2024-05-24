# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/greenplum/v1/cluster.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
from yandex.cloud.mdb.greenplum.v1 import config_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_config__pb2
from yandex.cloud.mdb.greenplum.v1 import maintenance_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_maintenance__pb2
from yandex.cloud.mdb.greenplum.v1 import pxf_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/mdb/greenplum/v1/cluster.proto\x12\x1dyandex.cloud.mdb.greenplum.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/type/timeofday.proto\x1a*yandex/cloud/mdb/greenplum/v1/config.proto\x1a/yandex/cloud/mdb/greenplum/v1/maintenance.proto\x1a\'yandex/cloud/mdb/greenplum/v1/pxf.proto\x1a\x1dyandex/cloud/validation.proto\"\xfb\x0b\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x04name\x18\x04 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\x12>\n\x06\x63onfig\x18\x05 \x01(\x0b\x32..yandex.cloud.mdb.greenplum.v1.GreenplumConfig\x12\x1e\n\x0b\x64\x65scription\x18\x06 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x42\n\x06labels\x18\x07 \x03(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.Cluster.LabelsEntry\x12G\n\x0b\x65nvironment\x18\x08 \x01(\x0e\x32\x32.yandex.cloud.mdb.greenplum.v1.Cluster.Environment\x12=\n\nmonitoring\x18\t \x03(\x0b\x32).yandex.cloud.mdb.greenplum.v1.Monitoring\x12L\n\rmaster_config\x18\n \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.MasterSubclusterConfig\x12N\n\x0esegment_config\x18\x0b \x01(\x0b\x32\x36.yandex.cloud.mdb.greenplum.v1.SegmentSubclusterConfig\x12\x19\n\x11master_host_count\x18\x0c \x01(\x03\x12\x1a\n\x12segment_host_count\x18\r \x01(\x03\x12\x17\n\x0fsegment_in_host\x18\x0e \x01(\x03\x12\x12\n\nnetwork_id\x18\x0f \x01(\t\x12=\n\x06health\x18\x10 \x01(\x0e\x32-.yandex.cloud.mdb.greenplum.v1.Cluster.Health\x12=\n\x06status\x18\x11 \x01(\x0e\x32-.yandex.cloud.mdb.greenplum.v1.Cluster.Status\x12L\n\x12maintenance_window\x18\x12 \x01(\x0b\x32\x30.yandex.cloud.mdb.greenplum.v1.MaintenanceWindow\x12N\n\x11planned_operation\x18\x13 \x01(\x0b\x32\x33.yandex.cloud.mdb.greenplum.v1.MaintenanceOperation\x12\x1a\n\x12security_group_ids\x18\x14 \x03(\t\x12\x11\n\tuser_name\x18\x15 \x01(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x16 \x01(\x08\x12\x16\n\x0ehost_group_ids\x18\x17 \x03(\t\x12G\n\x0e\x63luster_config\x18\x18 \x01(\x0b\x32/.yandex.cloud.mdb.greenplum.v1.ClusterConfigSet\x12\x42\n\rcloud_storage\x18\x1a \x01(\x0b\x32+.yandex.cloud.mdb.greenplum.v1.CloudStorage\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0b\x45nvironment\x12\x1b\n\x17\x45NVIRONMENT_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\r\n\tPRESTABLE\x10\x02\"O\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\x12\x0e\n\nUNBALANCED\x10\x04\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08STARTING\x10\x07J\x04\x08\x19\x10\x1a\"\xcf\x06\n\x10\x43lusterConfigSet\x12s\n\x19greenplum_config_set_6_17\x18\x01 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.GreenplumConfigSet6_17H\x00R\x17greenplumConfigSet_6_17\x12s\n\x19greenplum_config_set_6_19\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.GreenplumConfigSet6_19H\x00R\x17greenplumConfigSet_6_19\x12s\n\x19greenplum_config_set_6_21\x18\x04 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.GreenplumConfigSet6_21H\x00R\x17greenplumConfigSet_6_21\x12s\n\x19greenplum_config_set_6_22\x18\x05 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.GreenplumConfigSet6_22H\x00R\x17greenplumConfigSet_6_22\x12j\n\x16greenplum_config_set_6\x18\t \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfigSet6H\x00R\x14greenplumConfigSet_6\x12\x46\n\x04pool\x18\x03 \x01(\x0b\x32\x38.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfigSet\x12X\n\x15\x62\x61\x63kground_activities\x18\x06 \x01(\x0b\x32\x39.yandex.cloud.mdb.greenplum.v1.BackgroundActivitiesConfig\x12?\n\npxf_config\x18\x08 \x01(\x0b\x32+.yandex.cloud.mdb.greenplum.v1.PXFConfigSetB\x12\n\x10greenplum_configJ\x04\x08\x07\x10\x08\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\xb0\x02\n\x0fGreenplumConfig\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x33\n\x13\x62\x61\x63kup_window_start\x18\x02 \x01(\x0b\x32\x16.google.type.TimeOfDay\x12H\n\x19\x62\x61\x63kup_retain_period_days\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x31-60\x12\x35\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0b\x32%.yandex.cloud.mdb.greenplum.v1.Access\x12\x19\n\x07zone_id\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1b\n\tsubnet_id\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x18\n\x10\x61ssign_public_ip\x18\x06 \x01(\x08J\x04\x08\x07\x10\t\"C\n\x06\x41\x63\x63\x65ss\x12\x11\n\tdata_lens\x18\x01 \x01(\x08\x12\x0f\n\x07web_sql\x18\x02 \x01(\x08\x12\x15\n\rdata_transfer\x18\x03 \x01(\x08\"\xd6\x01\n\x16GreenplumRestoreConfig\x12\x33\n\x13\x62\x61\x63kup_window_start\x18\x01 \x01(\x0b\x32\x16.google.type.TimeOfDay\x12\x35\n\x06\x61\x63\x63\x65ss\x18\x02 \x01(\x0b\x32%.yandex.cloud.mdb.greenplum.v1.Access\x12\x19\n\x07zone_id\x18\x03 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1b\n\tsubnet_id\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x18\n\x10\x61ssign_public_ip\x18\x05 \x01(\x08\"A\n\x10RestoreResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\"\x1e\n\x0c\x43loudStorage\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x42p\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplumb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.greenplum.v1.cluster_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplum'
  _CLUSTER_LABELSENTRY._options = None
  _CLUSTER_LABELSENTRY._serialized_options = b'8\001'
  _CLUSTER.fields_by_name['name']._options = None
  _CLUSTER.fields_by_name['name']._serialized_options = b'\350\3071\001\212\3101\004<=63'
  _CLUSTER.fields_by_name['description']._options = None
  _CLUSTER.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _GREENPLUMCONFIG.fields_by_name['backup_retain_period_days']._options = None
  _GREENPLUMCONFIG.fields_by_name['backup_retain_period_days']._serialized_options = b'\372\3071\0041-60'
  _GREENPLUMCONFIG.fields_by_name['zone_id']._options = None
  _GREENPLUMCONFIG.fields_by_name['zone_id']._serialized_options = b'\212\3101\004<=50'
  _GREENPLUMCONFIG.fields_by_name['subnet_id']._options = None
  _GREENPLUMCONFIG.fields_by_name['subnet_id']._serialized_options = b'\212\3101\004<=50'
  _GREENPLUMRESTORECONFIG.fields_by_name['zone_id']._options = None
  _GREENPLUMRESTORECONFIG.fields_by_name['zone_id']._serialized_options = b'\212\3101\004<=50'
  _GREENPLUMRESTORECONFIG.fields_by_name['subnet_id']._options = None
  _GREENPLUMRESTORECONFIG.fields_by_name['subnet_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CLUSTER']._serialized_start=338
  _globals['_CLUSTER']._serialized_end=1869
  _globals['_CLUSTER_LABELSENTRY']._serialized_start=1539
  _globals['_CLUSTER_LABELSENTRY']._serialized_end=1584
  _globals['_CLUSTER_ENVIRONMENT']._serialized_start=1586
  _globals['_CLUSTER_ENVIRONMENT']._serialized_end=1659
  _globals['_CLUSTER_HEALTH']._serialized_start=1661
  _globals['_CLUSTER_HEALTH']._serialized_end=1740
  _globals['_CLUSTER_STATUS']._serialized_start=1742
  _globals['_CLUSTER_STATUS']._serialized_end=1863
  _globals['_CLUSTERCONFIGSET']._serialized_start=1872
  _globals['_CLUSTERCONFIGSET']._serialized_end=2719
  _globals['_MONITORING']._serialized_start=2721
  _globals['_MONITORING']._serialized_end=2782
  _globals['_GREENPLUMCONFIG']._serialized_start=2785
  _globals['_GREENPLUMCONFIG']._serialized_end=3089
  _globals['_ACCESS']._serialized_start=3091
  _globals['_ACCESS']._serialized_end=3158
  _globals['_GREENPLUMRESTORECONFIG']._serialized_start=3161
  _globals['_GREENPLUMRESTORECONFIG']._serialized_end=3375
  _globals['_RESTORERESOURCES']._serialized_start=3377
  _globals['_RESTORERESOURCES']._serialized_end=3442
  _globals['_CLOUDSTORAGE']._serialized_start=3444
  _globals['_CLOUDSTORAGE']._serialized_end=3474
# @@protoc_insertion_point(module_scope)
