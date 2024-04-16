# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v2/jobs/jobs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/datasphere/v2/jobs/jobs.proto\x12\x1fyandex.cloud.datasphere.v2.jobs\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc8\x03\n\rJobParameters\x12:\n\x0binput_files\x18\x01 \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12?\n\x0coutput_files\x18\x02 \x03(\x0b\x32).yandex.cloud.datasphere.v2.jobs.FileDesc\x12\x14\n\x0cs3_mount_ids\x18\x03 \x03(\t\x12\x13\n\x0b\x64\x61taset_ids\x18\x04 \x03(\t\x12\x0b\n\x03\x63md\x18\x05 \x01(\t\x12\x39\n\x03\x65nv\x18\x06 \x01(\x0b\x32,.yandex.cloud.datasphere.v2.jobs.Environment\x12\x1b\n\x13\x61ttach_project_disk\x18\x07 \x01(\x08\x12O\n\x13\x63loud_instance_type\x18\x08 \x01(\x0b\x32\x32.yandex.cloud.datasphere.v2.jobs.CloudInstanceType\x12Y\n\x18\x65xtended_working_storage\x18\t \x01(\x0b\x32\x37.yandex.cloud.datasphere.v2.jobs.ExtendedWorkingStorage\"!\n\x11\x43loudInstanceType\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xb2\x01\n\x16\x45xtendedWorkingStorage\x12Q\n\x04type\x18\x01 \x01(\x0e\x32\x43.yandex.cloud.datasphere.v2.jobs.ExtendedWorkingStorage.StorageType\x12\x0f\n\x07size_gb\x18\x02 \x01(\x03\"4\n\x0bStorageType\x12\x1c\n\x18STORAGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03SSD\x10\x01\"\xb3\x01\n\x04\x46ile\x12\x37\n\x04\x64\x65sc\x18\x01 \x01(\x0b\x32).yandex.cloud.datasphere.v2.jobs.FileDesc\x12\x0e\n\x06sha256\x18\x02 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\x03\x12N\n\x10\x63ompression_type\x18\x04 \x01(\x0e\x32\x34.yandex.cloud.datasphere.v2.jobs.FileCompressionType\"O\n\x0bStorageFile\x12\x33\n\x04\x66ile\x18\x01 \x01(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12\x0b\n\x03url\x18\x02 \x01(\t\"%\n\x08\x46ileDesc\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0b\n\x03var\x18\x02 \x01(\t\"\xc3\x02\n\x0b\x45nvironment\x12\x44\n\x04vars\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.datasphere.v2.jobs.Environment.VarsEntry\x12\"\n\x18\x64ocker_image_resource_id\x18\x02 \x01(\tH\x00\x12M\n\x11\x64ocker_image_spec\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.datasphere.v2.jobs.DockerImageSpecH\x00\x12>\n\npython_env\x18\x04 \x01(\x0b\x32*.yandex.cloud.datasphere.v2.jobs.PythonEnv\x1a+\n\tVarsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0e\n\x0c\x64ocker_image\"\x84\x01\n\x0f\x44ockerImageSpec\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x1d\n\x13password_plain_text\x18\x03 \x01(\tH\x00\x12!\n\x17password_ds_secret_name\x18\x04 \x01(\tH\x00\x42\n\n\x08password\"]\n\tPythonEnv\x12\x12\n\nconda_yaml\x18\x01 \x01(\t\x12<\n\rlocal_modules\x18\x02 \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\"\x99\x05\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x06status\x18\x06 \x01(\x0e\x32*.yandex.cloud.datasphere.v2.jobs.JobStatus\x12\x0e\n\x06\x63onfig\x18\x07 \x01(\t\x12\x15\n\rcreated_by_id\x18\x08 \x01(\t\x12\x12\n\nproject_id\x18\t \x01(\t\x12\x46\n\x0ejob_parameters\x18\n \x01(\x0b\x32..yandex.cloud.datasphere.v2.jobs.JobParameters\x12\x33\n\x0f\x64\x61ta_expires_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x64\x61ta_cleared\x18\x0c \x01(\x08\x12;\n\x0coutput_files\x18\r \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12\x38\n\tlog_files\x18\x0e \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12?\n\x10\x64iagnostic_files\x18\x0f \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12\x17\n\x0f\x64\x61ta_size_bytes\x18\x10 \x01(\x03\" \n\tJobResult\x12\x13\n\x0breturn_code\x18\x01 \x01(\x03*O\n\x13\x46ileCompressionType\x12%\n!FILE_COMPRESSION_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x07\n\x03ZIP\x10\x02*\x81\x01\n\tJobStatus\x12\x1a\n\x16JOB_STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\r\n\tEXECUTING\x10\x02\x12\x14\n\x10UPLOADING_OUTPUT\x10\x03\x12\x0b\n\x07SUCCESS\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x12\r\n\tCANCELLED\x10\x06\x42{\n#yandex.cloud.api.datasphere.v2.jobsB\x04JobsZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2/jobs;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.jobs.jobs_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.datasphere.v2.jobsB\004JobsZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2/jobs;datasphere'
  _ENVIRONMENT_VARSENTRY._options = None
  _ENVIRONMENT_VARSENTRY._serialized_options = b'8\001'
  _globals['_FILECOMPRESSIONTYPE']._serialized_start=2347
  _globals['_FILECOMPRESSIONTYPE']._serialized_end=2426
  _globals['_JOBSTATUS']._serialized_start=2429
  _globals['_JOBSTATUS']._serialized_end=2558
  _globals['_JOBPARAMETERS']._serialized_start=113
  _globals['_JOBPARAMETERS']._serialized_end=569
  _globals['_CLOUDINSTANCETYPE']._serialized_start=571
  _globals['_CLOUDINSTANCETYPE']._serialized_end=604
  _globals['_EXTENDEDWORKINGSTORAGE']._serialized_start=607
  _globals['_EXTENDEDWORKINGSTORAGE']._serialized_end=785
  _globals['_EXTENDEDWORKINGSTORAGE_STORAGETYPE']._serialized_start=733
  _globals['_EXTENDEDWORKINGSTORAGE_STORAGETYPE']._serialized_end=785
  _globals['_FILE']._serialized_start=788
  _globals['_FILE']._serialized_end=967
  _globals['_STORAGEFILE']._serialized_start=969
  _globals['_STORAGEFILE']._serialized_end=1048
  _globals['_FILEDESC']._serialized_start=1050
  _globals['_FILEDESC']._serialized_end=1087
  _globals['_ENVIRONMENT']._serialized_start=1090
  _globals['_ENVIRONMENT']._serialized_end=1413
  _globals['_ENVIRONMENT_VARSENTRY']._serialized_start=1354
  _globals['_ENVIRONMENT_VARSENTRY']._serialized_end=1397
  _globals['_DOCKERIMAGESPEC']._serialized_start=1416
  _globals['_DOCKERIMAGESPEC']._serialized_end=1548
  _globals['_PYTHONENV']._serialized_start=1550
  _globals['_PYTHONENV']._serialized_end=1643
  _globals['_JOB']._serialized_start=1646
  _globals['_JOB']._serialized_end=2311
  _globals['_JOBRESULT']._serialized_start=2313
  _globals['_JOBRESULT']._serialized_end=2345
# @@protoc_insertion_point(module_scope)
