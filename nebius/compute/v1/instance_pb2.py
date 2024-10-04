# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/compute/v1/instance.proto
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
from nebius.compute.v1 import network_interface_pb2 as nebius_dot_compute_dot_v1_dot_network__interface__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n nebius/compute/v1/instance.proto\x12\x11nebius.compute.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fnebius/common/v1/metadata.proto\x1a\x18nebius/annotations.proto\x1a)nebius/compute/v1/network_interface.proto\"\xa2\x01\n\x08Instance\x12\x34\n\x08metadata\x18\x01 \x01(\x0b\x32\".nebius.common.v1.ResourceMetadata\x12-\n\x04spec\x18\x02 \x01(\x0b\x32\x1f.nebius.compute.v1.InstanceSpec\x12\x31\n\x06status\x18\x03 \x01(\x0b\x32!.nebius.compute.v1.InstanceStatus\"\x8b\x04\n\x0cInstanceSpec\x12 \n\x12service_account_id\x18\x01 \x01(\tB\x04\xbaJ\x01\x02\x12?\n\tresources\x18\x02 \x01(\x0b\x32 .nebius.compute.v1.ResourcesSpecB\n\xbaH\x03\xc8\x01\x01\xbaJ\x01\x02\x12\x44\n\x0bgpu_cluster\x18\x03 \x01(\x0b\x32).nebius.compute.v1.InstanceGpuClusterSpecB\x04\xbaJ\x01\x02\x12O\n\x12network_interfaces\x18\x04 \x03(\x0b\x32\'.nebius.compute.v1.NetworkInterfaceSpecB\n\xbaH\x03\xc8\x01\x01\xbaJ\x01\x02\x12<\n\tboot_disk\x18\x05 \x01(\x0b\x32#.nebius.compute.v1.AttachedDiskSpecB\x04\xbaJ\x01\x02\x12<\n\x0fsecondary_disks\x18\x06 \x03(\x0b\x32#.nebius.compute.v1.AttachedDiskSpec\x12\x44\n\x0b\x66ilesystems\x18\x07 \x03(\x0b\x32).nebius.compute.v1.AttachedFilesystemSpecB\x04\xbaJ\x01\x02\x12.\n\x14\x63loud_init_user_data\x18\x08 \x01(\tB\x10\xbaH\x06r\x04\x18\x80\x80\x02\xbaJ\x01\x02\xc0J\x01\x12\x0f\n\x07stopped\x18\r \x01(\x08\";\n\rResourcesSpec\x12\x10\n\x08platform\x18\x01 \x01(\t\x12\x10\n\x06preset\x18\x02 \x01(\tH\x00\x42\x06\n\x04size\"$\n\x16InstanceGpuClusterSpec\x12\n\n\x02id\x18\x01 \x01(\t\"\x82\x02\n\x10\x41ttachedDiskSpec\x12K\n\x0b\x61ttach_mode\x18\x01 \x01(\x0e\x32..nebius.compute.v1.AttachedDiskSpec.AttachModeB\x06\xbaH\x03\xc8\x01\x01\x12\x38\n\rexisting_disk\x18\x02 \x01(\x0b\x32\x1f.nebius.compute.v1.ExistingDiskH\x00\x12\x1a\n\tdevice_id\x18\x03 \x01(\tB\x07\xbaH\x04r\x02\x18\x14\"<\n\nAttachMode\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tREAD_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\x42\r\n\x04type\x12\x05\xbaH\x02\x08\x01\"\"\n\x0c\x45xistingDisk\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\"(\n\x12\x45xistingFilesystem\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\"\x99\x02\n\x16\x41ttachedFilesystemSpec\x12Q\n\x0b\x61ttach_mode\x18\x01 \x01(\x0e\x32\x34.nebius.compute.v1.AttachedFilesystemSpec.AttachModeB\x06\xbaH\x03\xc8\x01\x01\x12\x19\n\tmount_tag\x18\x02 \x01(\tB\x06\xbaH\x03\xc8\x01\x01\x12\x44\n\x13\x65xisting_filesystem\x18\x03 \x01(\x0b\x32%.nebius.compute.v1.ExistingFilesystemH\x00\"<\n\nAttachMode\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tREAD_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\x42\r\n\x04type\x12\x05\xbaH\x02\x08\x01\"\xba\x02\n\x0eInstanceStatus\x12>\n\x05state\x18\x01 \x01(\x0e\x32/.nebius.compute.v1.InstanceStatus.InstanceState\x12\x45\n\x12network_interfaces\x18\x02 \x03(\x0b\x32).nebius.compute.v1.NetworkInterfaceStatus\x12\x13\n\x0breconciling\x18\x05 \x01(\x08\"\x8b\x01\n\rInstanceState\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0c\n\x08UPDATING\x10\x02\x12\x0c\n\x08STARTING\x10\x03\x12\x0b\n\x07RUNNING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08\x44\x45LETING\x10\x07\x12\t\n\x05\x45RROR\x10\x08\x42\\\n\x18\x61i.nebius.pub.compute.v1B\rInstanceProtoP\x01Z/github.com/nebius/gosdk/proto/nebius/compute/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.compute.v1.instance_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030ai.nebius.pub.compute.v1B\rInstanceProtoP\001Z/github.com/nebius/gosdk/proto/nebius/compute/v1'
  _INSTANCESPEC.fields_by_name['service_account_id']._options = None
  _INSTANCESPEC.fields_by_name['service_account_id']._serialized_options = b'\272J\001\002'
  _INSTANCESPEC.fields_by_name['resources']._options = None
  _INSTANCESPEC.fields_by_name['resources']._serialized_options = b'\272H\003\310\001\001\272J\001\002'
  _INSTANCESPEC.fields_by_name['gpu_cluster']._options = None
  _INSTANCESPEC.fields_by_name['gpu_cluster']._serialized_options = b'\272J\001\002'
  _INSTANCESPEC.fields_by_name['network_interfaces']._options = None
  _INSTANCESPEC.fields_by_name['network_interfaces']._serialized_options = b'\272H\003\310\001\001\272J\001\002'
  _INSTANCESPEC.fields_by_name['boot_disk']._options = None
  _INSTANCESPEC.fields_by_name['boot_disk']._serialized_options = b'\272J\001\002'
  _INSTANCESPEC.fields_by_name['filesystems']._options = None
  _INSTANCESPEC.fields_by_name['filesystems']._serialized_options = b'\272J\001\002'
  _INSTANCESPEC.fields_by_name['cloud_init_user_data']._options = None
  _INSTANCESPEC.fields_by_name['cloud_init_user_data']._serialized_options = b'\272H\006r\004\030\200\200\002\272J\001\002\300J\001'
  _ATTACHEDDISKSPEC.oneofs_by_name['type']._options = None
  _ATTACHEDDISKSPEC.oneofs_by_name['type']._serialized_options = b'\272H\002\010\001'
  _ATTACHEDDISKSPEC.fields_by_name['attach_mode']._options = None
  _ATTACHEDDISKSPEC.fields_by_name['attach_mode']._serialized_options = b'\272H\003\310\001\001'
  _ATTACHEDDISKSPEC.fields_by_name['device_id']._options = None
  _ATTACHEDDISKSPEC.fields_by_name['device_id']._serialized_options = b'\272H\004r\002\030\024'
  _EXISTINGDISK.fields_by_name['id']._options = None
  _EXISTINGDISK.fields_by_name['id']._serialized_options = b'\272H\003\310\001\001'
  _EXISTINGFILESYSTEM.fields_by_name['id']._options = None
  _EXISTINGFILESYSTEM.fields_by_name['id']._serialized_options = b'\272H\003\310\001\001'
  _ATTACHEDFILESYSTEMSPEC.oneofs_by_name['type']._options = None
  _ATTACHEDFILESYSTEMSPEC.oneofs_by_name['type']._serialized_options = b'\272H\002\010\001'
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['attach_mode']._options = None
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['attach_mode']._serialized_options = b'\272H\003\310\001\001'
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['mount_tag']._options = None
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['mount_tag']._serialized_options = b'\272H\003\310\001\001'
  _globals['_INSTANCE']._serialized_start=187
  _globals['_INSTANCE']._serialized_end=349
  _globals['_INSTANCESPEC']._serialized_start=352
  _globals['_INSTANCESPEC']._serialized_end=875
  _globals['_RESOURCESSPEC']._serialized_start=877
  _globals['_RESOURCESSPEC']._serialized_end=936
  _globals['_INSTANCEGPUCLUSTERSPEC']._serialized_start=938
  _globals['_INSTANCEGPUCLUSTERSPEC']._serialized_end=974
  _globals['_ATTACHEDDISKSPEC']._serialized_start=977
  _globals['_ATTACHEDDISKSPEC']._serialized_end=1235
  _globals['_ATTACHEDDISKSPEC_ATTACHMODE']._serialized_start=1160
  _globals['_ATTACHEDDISKSPEC_ATTACHMODE']._serialized_end=1220
  _globals['_EXISTINGDISK']._serialized_start=1237
  _globals['_EXISTINGDISK']._serialized_end=1271
  _globals['_EXISTINGFILESYSTEM']._serialized_start=1273
  _globals['_EXISTINGFILESYSTEM']._serialized_end=1313
  _globals['_ATTACHEDFILESYSTEMSPEC']._serialized_start=1316
  _globals['_ATTACHEDFILESYSTEMSPEC']._serialized_end=1597
  _globals['_ATTACHEDFILESYSTEMSPEC_ATTACHMODE']._serialized_start=1160
  _globals['_ATTACHEDFILESYSTEMSPEC_ATTACHMODE']._serialized_end=1220
  _globals['_INSTANCESTATUS']._serialized_start=1600
  _globals['_INSTANCESTATUS']._serialized_end=1914
  _globals['_INSTANCESTATUS_INSTANCESTATE']._serialized_start=1775
  _globals['_INSTANCESTATUS_INSTANCESTATE']._serialized_end=1914
# @@protoc_insertion_point(module_scope)