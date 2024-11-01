# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/logging/v1/agentmanager/version_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from nebius import annotations_pb2 as nebius_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4nebius/logging/v1/agentmanager/version_service.proto\x12\x1enebius.logging.agentmanager.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x18nebius/annotations.proto\"\xd2\x03\n\x11GetVersionRequest\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).nebius.logging.agentmanager.v1.AgentType\x12\x15\n\ragent_version\x18\x02 \x01(\t\x12\x17\n\x0fupdater_version\x18\x03 \x01(\t\x12\x11\n\tparent_id\x18\x04 \x01(\t\x12\x13\n\x0binstance_id\x18\x05 \x01(\t\x12\x37\n\x07os_info\x18\x06 \x01(\x0b\x32&.nebius.logging.agentmanager.v1.OSInfo\x12?\n\x0b\x61gent_state\x18\x07 \x01(\x0e\x32*.nebius.logging.agentmanager.v1.AgentState\x12/\n\x0c\x61gent_uptime\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x30\n\rsystem_uptime\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x31\n\x0eupdater_uptime\x18\n \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1c\n\x14\x61gent_state_messages\x18\x0b \x03(\t\";\n\x06OSInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05uname\x18\x02 \x01(\t\x12\x14\n\x0c\x61rchitecture\x18\x03 \x01(\t\"\xa6\x02\n\x12GetVersionResponse\x12\x36\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32&.nebius.logging.agentmanager.v1.Action\x12>\n\x03nop\x18\x02 \x01(\x0b\x32/.nebius.logging.agentmanager.v1.NopActionParamsH\x00\x12\x44\n\x06update\x18\x03 \x01(\x0b\x32\x32.nebius.logging.agentmanager.v1.UpdateActionParamsH\x00\x12\x46\n\x07restart\x18\x04 \x01(\x0b\x32\x33.nebius.logging.agentmanager.v1.RestartActionParamsH\x00\x42\n\n\x08response\"\x11\n\x0fNopActionParams\"7\n\x12UpdateActionParams\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x10\n\x08repo_url\x18\x02 \x01(\t\"\x15\n\x13RestartActionParams*0\n\tAgentType\x12\x13\n\x0f\x41GENT_UNDEFINED\x10\x00\x12\x0e\n\nO11Y_AGENT\x10\x01*E\n\nAgentState\x12\x13\n\x0fSTATE_UNDEFINED\x10\x00\x12\x11\n\rSTATE_HEALTHY\x10\x01\x12\x0f\n\x0bSTATE_ERROR\x10\x02*@\n\x06\x41\x63tion\x12\x14\n\x10\x41\x43TION_UNDEFINED\x10\x00\x12\x07\n\x03NOP\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\x0b\n\x07RESTART\x10\x03\x32\xa5\x01\n\x0eVersionService\x12s\n\nGetVersion\x12\x31.nebius.logging.agentmanager.v1.GetVersionRequest\x1a\x32.nebius.logging.agentmanager.v1.GetVersionResponse\x1a\x1e\xbaJ\x1bobservability-agent-managerB|\n%ai.nebius.pub.logging.v1.agentmanagerB\x13VersionServiceProtoP\x01Z<github.com/nebius/gosdk/proto/nebius/logging/v1/agentmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.logging.v1.agentmanager.version_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%ai.nebius.pub.logging.v1.agentmanagerB\023VersionServiceProtoP\001Z<github.com/nebius/gosdk/proto/nebius/logging/v1/agentmanager'
  _VERSIONSERVICE._options = None
  _VERSIONSERVICE._serialized_options = b'\272J\033observability-agent-manager'
  _globals['_AGENTTYPE']._serialized_start=1072
  _globals['_AGENTTYPE']._serialized_end=1120
  _globals['_AGENTSTATE']._serialized_start=1122
  _globals['_AGENTSTATE']._serialized_end=1191
  _globals['_ACTION']._serialized_start=1193
  _globals['_ACTION']._serialized_end=1257
  _globals['_GETVERSIONREQUEST']._serialized_start=147
  _globals['_GETVERSIONREQUEST']._serialized_end=613
  _globals['_OSINFO']._serialized_start=615
  _globals['_OSINFO']._serialized_end=674
  _globals['_GETVERSIONRESPONSE']._serialized_start=677
  _globals['_GETVERSIONRESPONSE']._serialized_end=971
  _globals['_NOPACTIONPARAMS']._serialized_start=973
  _globals['_NOPACTIONPARAMS']._serialized_end=990
  _globals['_UPDATEACTIONPARAMS']._serialized_start=992
  _globals['_UPDATEACTIONPARAMS']._serialized_end=1047
  _globals['_RESTARTACTIONPARAMS']._serialized_start=1049
  _globals['_RESTARTACTIONPARAMS']._serialized_end=1070
  _globals['_VERSIONSERVICE']._serialized_start=1260
  _globals['_VERSIONSERVICE']._serialized_end=1425
# @@protoc_insertion_point(module_scope)
