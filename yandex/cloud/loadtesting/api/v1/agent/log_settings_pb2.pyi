"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class LogSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLOUD_LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    cloud_log_group_id: builtins.str
    """Id of Yandex Cloud log group to upload agent logs to"""
    def __init__(
        self,
        *,
        cloud_log_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cloud_log_group_id", b"cloud_log_group_id"]) -> None: ...

global___LogSettings = LogSettings
