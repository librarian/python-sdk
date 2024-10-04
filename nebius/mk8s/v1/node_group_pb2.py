# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/mk8s/v1/node_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from nebius import annotations_pb2 as nebius_dot_annotations__pb2
from nebius.common.v1 import metadata_pb2 as nebius_dot_common_dot_v1_dot_metadata__pb2
from nebius.mk8s.v1 import instance_template_pb2 as nebius_dot_mk8s_dot_v1_dot_instance__template__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fnebius/mk8s/v1/node_group.proto\x12\x0enebius.mk8s.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x18nebius/annotations.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a&nebius/mk8s/v1/instance_template.proto\"\x9f\x01\n\tNodeGroup\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12+\n\x04spec\x18\x02 \x01(\x0b\x32\x1d.nebius.mk8s.v1.NodeGroupSpec\x12/\n\x06status\x18\x03 \x01(\x0b\x32\x1f.nebius.mk8s.v1.NodeGroupStatus\"\xba\x01\n\rNodeGroupSpec\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1a\n\x10\x66ixed_node_count\x18\x02 \x01(\x03H\x00\x12.\n\x08template\x18\x03 \x01(\x0b\x32\x1c.nebius.mk8s.v1.NodeTemplate\x12=\n\x08strategy\x18\x04 \x01(\x0b\x32+.nebius.mk8s.v1.NodeGroupDeploymentStrategyB\r\n\x04size\x12\x05\xbaH\x02\x08\x01\"\xdb\x03\n\x0cNodeTemplate\x12\x36\n\x08metadata\x18\x01 \x01(\x0b\x32$.nebius.mk8s.v1.NodeMetadataTemplate\x12)\n\x06taints\x18\x02 \x03(\x0b\x32\x19.nebius.mk8s.v1.NodeTaint\x12\x38\n\tresources\x18\x03 \x01(\x0b\x32\x1d.nebius.mk8s.v1.ResourcesSpecB\x06\xbaH\x03\xc8\x01\x01\x12\x31\n\tboot_disk\x18\t \x01(\x0b\x32\x18.nebius.mk8s.v1.DiskSpecB\x04\xbaJ\x01\x07\x12\x33\n\x0bgpu_cluster\x18\x04 \x01(\x0b\x32\x1e.nebius.mk8s.v1.GpuClusterSpec\x12J\n\x12network_interfaces\x18\x05 \x03(\x0b\x32(.nebius.mk8s.v1.NetworkInterfaceTemplateB\x04\xbaJ\x01\x07\x12;\n\x0b\x66ilesystems\x18\x07 \x03(\x0b\x32&.nebius.mk8s.v1.AttachedFilesystemSpec\x12!\n\x14\x63loud_init_user_data\x18\x06 \x01(\tB\x03\xc0J\x01\x12\x1a\n\x12service_account_id\x18\n \x01(\t\"\x87\x01\n\x14NodeMetadataTemplate\x12@\n\x06labels\x18\x01 \x03(\x0b\x32\x30.nebius.mk8s.v1.NodeMetadataTemplate.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1c\n\x0eGpuClusterSpec\x12\n\n\x02id\x18\x01 \x01(\t\"u\n\x18NetworkInterfaceTemplate\x12@\n\x11public_ip_address\x18\x01 \x01(\x0b\x32\x1f.nebius.mk8s.v1.PublicIPAddressB\x04\xbaJ\x01\x06\x12\x17\n\tsubnet_id\x18\x03 \x01(\tB\x04\xbaJ\x01\x07\"\x11\n\x0fPublicIPAddress\"\x93\x02\n\x16\x41ttachedFilesystemSpec\x12N\n\x0b\x61ttach_mode\x18\x01 \x01(\x0e\x32\x31.nebius.mk8s.v1.AttachedFilesystemSpec.AttachModeB\x06\xbaH\x03\xc8\x01\x01\x12\x19\n\tmount_tag\x18\x02 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\x12\x41\n\x13\x65xisting_filesystem\x18\x03 \x01(\x0b\x32\".nebius.mk8s.v1.ExistingFilesystemH\x00\"<\n\nAttachMode\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tREAD_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\x42\r\n\x04type\x12\x05\xbaH\x02\x08\x01\"(\n\x12\x45xistingFilesystem\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\"\xcc\x01\n\tNodeTaint\x12\x13\n\x03key\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\x12\x15\n\x05value\x18\x02 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\x12\x38\n\x06\x65\x66\x66\x65\x63t\x18\x03 \x01(\x0e\x32 .nebius.mk8s.v1.NodeTaint.EffectB\x06\xbaH\x03\xc8\x01\x01\"Y\n\x06\x45\x66\x66\x65\x63t\x12\x16\n\x12\x45\x46\x46\x45\x43T_UNSPECIFIED\x10\x00\x12\x0e\n\nNO_EXECUTE\x10\x01\x12\x0f\n\x0bNO_SCHEDULE\x10\x02\x12\x16\n\x12PREFER_NO_SCHEDULE\x10\x03\"\xbb\x01\n\x1bNodeGroupDeploymentStrategy\x12\x37\n\x0fmax_unavailable\x18\x01 \x01(\x0b\x32\x1e.nebius.mk8s.v1.PercentOrCount\x12\x31\n\tmax_surge\x18\x02 \x01(\x0b\x32\x1e.nebius.mk8s.v1.PercentOrCount\x12\x30\n\rdrain_timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\"D\n\x0ePercentOrCount\x12\x11\n\x07percent\x18\x01 \x01(\x03H\x00\x12\x0f\n\x05\x63ount\x18\x02 \x01(\x03H\x00\x42\x0e\n\x05value\x12\x05\xbaH\x02\x08\x01\"\xa0\x02\n\x0fNodeGroupStatus\x12\x34\n\x05state\x18\x01 \x01(\x0e\x32%.nebius.mk8s.v1.NodeGroupStatus.State\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x19\n\x11target_node_count\x18\x03 \x01(\x03\x12\x12\n\nnode_count\x18\x04 \x01(\x03\x12\x1b\n\x13outdated_node_count\x18\x05 \x01(\x03\x12\x18\n\x10ready_node_count\x18\x06 \x01(\x03\x12\x13\n\x0breconciling\x18\x64 \x01(\x08\"K\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\x42W\n\x15\x61i.nebius.pub.mk8s.v1B\x0eNodeGroupProtoP\x01Z,github.com/nebius/gosdk/proto/nebius/mk8s/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.mk8s.v1.node_group_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025ai.nebius.pub.mk8s.v1B\016NodeGroupProtoP\001Z,github.com/nebius/gosdk/proto/nebius/mk8s/v1'
  _NODEGROUPSPEC.oneofs_by_name['size']._options = None
  _NODEGROUPSPEC.oneofs_by_name['size']._serialized_options = b'\272H\002\010\001'
  _NODETEMPLATE.fields_by_name['resources']._options = None
  _NODETEMPLATE.fields_by_name['resources']._serialized_options = b'\272H\003\310\001\001'
  _NODETEMPLATE.fields_by_name['boot_disk']._options = None
  _NODETEMPLATE.fields_by_name['boot_disk']._serialized_options = b'\272J\001\007'
  _NODETEMPLATE.fields_by_name['network_interfaces']._options = None
  _NODETEMPLATE.fields_by_name['network_interfaces']._serialized_options = b'\272J\001\007'
  _NODETEMPLATE.fields_by_name['cloud_init_user_data']._options = None
  _NODETEMPLATE.fields_by_name['cloud_init_user_data']._serialized_options = b'\300J\001'
  _NODEMETADATATEMPLATE_LABELSENTRY._options = None
  _NODEMETADATATEMPLATE_LABELSENTRY._serialized_options = b'8\001'
  _NETWORKINTERFACETEMPLATE.fields_by_name['public_ip_address']._options = None
  _NETWORKINTERFACETEMPLATE.fields_by_name['public_ip_address']._serialized_options = b'\272J\001\006'
  _NETWORKINTERFACETEMPLATE.fields_by_name['subnet_id']._options = None
  _NETWORKINTERFACETEMPLATE.fields_by_name['subnet_id']._serialized_options = b'\272J\001\007'
  _ATTACHEDFILESYSTEMSPEC.oneofs_by_name['type']._options = None
  _ATTACHEDFILESYSTEMSPEC.oneofs_by_name['type']._serialized_options = b'\272H\002\010\001'
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['attach_mode']._options = None
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['attach_mode']._serialized_options = b'\272H\003\310\001\001'
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['mount_tag']._options = None
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['mount_tag']._serialized_options = b'\272H\003\310\001\001'
  _EXISTINGFILESYSTEM.fields_by_name['id']._options = None
  _EXISTINGFILESYSTEM.fields_by_name['id']._serialized_options = b'\272H\003\310\001\001'
  _NODETAINT.fields_by_name['key']._options = None
  _NODETAINT.fields_by_name['key']._serialized_options = b'\272H\003\310\001\001'
  _NODETAINT.fields_by_name['value']._options = None
  _NODETAINT.fields_by_name['value']._serialized_options = b'\272H\003\310\001\001'
  _NODETAINT.fields_by_name['effect']._options = None
  _NODETAINT.fields_by_name['effect']._serialized_options = b'\272H\003\310\001\001'
  _PERCENTORCOUNT.oneofs_by_name['value']._options = None
  _PERCENTORCOUNT.oneofs_by_name['value']._serialized_options = b'\272H\002\010\001'
  _globals['_NODEGROUP']._serialized_start=212
  _globals['_NODEGROUP']._serialized_end=371
  _globals['_NODEGROUPSPEC']._serialized_start=374
  _globals['_NODEGROUPSPEC']._serialized_end=560
  _globals['_NODETEMPLATE']._serialized_start=563
  _globals['_NODETEMPLATE']._serialized_end=1038
  _globals['_NODEMETADATATEMPLATE']._serialized_start=1041
  _globals['_NODEMETADATATEMPLATE']._serialized_end=1176
  _globals['_NODEMETADATATEMPLATE_LABELSENTRY']._serialized_start=1131
  _globals['_NODEMETADATATEMPLATE_LABELSENTRY']._serialized_end=1176
  _globals['_GPUCLUSTERSPEC']._serialized_start=1178
  _globals['_GPUCLUSTERSPEC']._serialized_end=1206
  _globals['_NETWORKINTERFACETEMPLATE']._serialized_start=1208
  _globals['_NETWORKINTERFACETEMPLATE']._serialized_end=1325
  _globals['_PUBLICIPADDRESS']._serialized_start=1327
  _globals['_PUBLICIPADDRESS']._serialized_end=1344
  _globals['_ATTACHEDFILESYSTEMSPEC']._serialized_start=1347
  _globals['_ATTACHEDFILESYSTEMSPEC']._serialized_end=1622
  _globals['_ATTACHEDFILESYSTEMSPEC_ATTACHMODE']._serialized_start=1547
  _globals['_ATTACHEDFILESYSTEMSPEC_ATTACHMODE']._serialized_end=1607
  _globals['_EXISTINGFILESYSTEM']._serialized_start=1624
  _globals['_EXISTINGFILESYSTEM']._serialized_end=1664
  _globals['_NODETAINT']._serialized_start=1667
  _globals['_NODETAINT']._serialized_end=1871
  _globals['_NODETAINT_EFFECT']._serialized_start=1782
  _globals['_NODETAINT_EFFECT']._serialized_end=1871
  _globals['_NODEGROUPDEPLOYMENTSTRATEGY']._serialized_start=1874
  _globals['_NODEGROUPDEPLOYMENTSTRATEGY']._serialized_end=2061
  _globals['_PERCENTORCOUNT']._serialized_start=2063
  _globals['_PERCENTORCOUNT']._serialized_end=2131
  _globals['_NODEGROUPSTATUS']._serialized_start=2134
  _globals['_NODEGROUPSTATUS']._serialized_end=2422
  _globals['_NODEGROUPSTATUS_STATE']._serialized_start=2347
  _globals['_NODEGROUPSTATUS_STATE']._serialized_end=2422
# @@protoc_insertion_point(module_scope)