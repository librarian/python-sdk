"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class LifecycleConfiguration(google.protobuf.message.Message):
    """The lifecycle configuration consists of one or more rules.
    An Lifecycle configuration can have up to 1,000 rules.
    Each rule consists of the following:
    - A filter identifying a subset of objects to which the rule applies.
      The filter can be based on a key name prefix, object size, or any combination of these.
    - A status indicating whether the rule is currently active.
    - One or more lifecycle expiration actions that you want to be performed on the objects
      identified by the filter. If the state of your bucket is versioning-enabled or versioning-suspended
      (bucket.spec.versioning_policy equals to ENABLED or SUSPENDED) you can have many versions of the same
      object (one current version and zero or more noncurrent versions). The system provides predefined actions
      that you can specify for current and noncurrent object versions.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RULES_FIELD_NUMBER: builtins.int
    @property
    def rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LifecycleRule]: ...
    def __init__(
        self,
        *,
        rules: collections.abc.Iterable[global___LifecycleRule] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["rules", b"rules"]) -> None: ...

global___LifecycleConfiguration = LifecycleConfiguration

@typing.final
class LifecycleRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LifecycleRule._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: LifecycleRule._Status.ValueType  # 0
        ENABLED: LifecycleRule._Status.ValueType  # 1
        DISABLED: LifecycleRule._Status.ValueType  # 2

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: LifecycleRule.Status.ValueType  # 0
    ENABLED: LifecycleRule.Status.ValueType  # 1
    DISABLED: LifecycleRule.Status.ValueType  # 2

    ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    EXPIRATION_FIELD_NUMBER: builtins.int
    NONCURRENT_VERSION_EXPIRATION_FIELD_NUMBER: builtins.int
    ABORT_INCOMPLETE_MULTIPART_UPLOAD_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Unique identifier for the rule per configuration.
    The value cannot be longer than 255 characters.
    """
    status: global___LifecycleRule.Status.ValueType
    @property
    def filter(self) -> global___LifecycleFilter:
        """The Filter is used to identify objects that a Lifecycle Rule applies to.
        The Lifecycle Rule will apply to any object matching all of the predicates
        configured inside (using logical AND).
        """

    @property
    def expiration(self) -> global___LifecycleExpiration:
        """Specifies the expiration for the lifecycle of the object in the form of date, days and,
        whether the object has a delete marker.
        """

    @property
    def noncurrent_version_expiration(self) -> global___LifecycleNoncurrentVersionExpiration:
        """Specifies when noncurrent object versions expire.
        It works only on a bucket that has versioning enabled (or suspended).
        """

    @property
    def abort_incomplete_multipart_upload(self) -> global___LifecycleAbortIncompleteMultipartUpload:
        """Specifies the days since the initiation of an incomplete multipart upload that
        the system will wait before permanently removing all parts of the upload.
        """

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        status: global___LifecycleRule.Status.ValueType = ...,
        filter: global___LifecycleFilter | None = ...,
        expiration: global___LifecycleExpiration | None = ...,
        noncurrent_version_expiration: global___LifecycleNoncurrentVersionExpiration | None = ...,
        abort_incomplete_multipart_upload: global___LifecycleAbortIncompleteMultipartUpload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["abort_incomplete_multipart_upload", b"abort_incomplete_multipart_upload", "expiration", b"expiration", "filter", b"filter", "noncurrent_version_expiration", b"noncurrent_version_expiration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["abort_incomplete_multipart_upload", b"abort_incomplete_multipart_upload", "expiration", b"expiration", "filter", b"filter", "id", b"id", "noncurrent_version_expiration", b"noncurrent_version_expiration", "status", b"status"]) -> None: ...

global___LifecycleRule = LifecycleRule

@typing.final
class LifecycleFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREFIX_FIELD_NUMBER: builtins.int
    OBJECT_SIZE_GREATER_THAN_BYTES_FIELD_NUMBER: builtins.int
    OBJECT_SIZE_LESS_THAN_BYTES_FIELD_NUMBER: builtins.int
    prefix: builtins.str
    """Prefix identifying one or more objects to which the rule applies.
    If prefix is empty, the rule applies to all objects in the bucket.
    """
    object_size_greater_than_bytes: builtins.int
    """Minimum object size to which the rule applies."""
    object_size_less_than_bytes: builtins.int
    """Maximum object size to which the rule applies."""
    def __init__(
        self,
        *,
        prefix: builtins.str = ...,
        object_size_greater_than_bytes: builtins.int = ...,
        object_size_less_than_bytes: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["object_size_greater_than_bytes", b"object_size_greater_than_bytes", "object_size_less_than_bytes", b"object_size_less_than_bytes", "prefix", b"prefix"]) -> None: ...

global___LifecycleFilter = LifecycleFilter

@typing.final
class LifecycleExpiration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATE_FIELD_NUMBER: builtins.int
    DAYS_FIELD_NUMBER: builtins.int
    EXPIRED_OBJECT_DELETE_MARKER_FIELD_NUMBER: builtins.int
    days: builtins.int
    """Indicates the lifetime, in days, of the objects that are subject to the rule.
    The value must be a non-zero positive integer.
    """
    expired_object_delete_marker: builtins.bool
    """Indicates whether the system will remove a "delete marker" with no noncurrent versions.
    If set to true, the "delete marker" will be permanently removed.
    If set to false the policy takes no action.
    This cannot be specified with Days or Date in a LifecycleExpiration Policy.
    """
    @property
    def date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Indicates at what date the object will be deleted. The time is always midnight UTC."""

    def __init__(
        self,
        *,
        date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        days: builtins.int = ...,
        expired_object_delete_marker: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["date", b"date", "days", b"days", "expired_with", b"expired_with"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["date", b"date", "days", b"days", "expired_object_delete_marker", b"expired_object_delete_marker", "expired_with", b"expired_with"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["expired_with", b"expired_with"]) -> typing.Literal["date", "days"] | None: ...

global___LifecycleExpiration = LifecycleExpiration

@typing.final
class LifecycleNoncurrentVersionExpiration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEWER_NONCURRENT_VERSIONS_FIELD_NUMBER: builtins.int
    NONCURRENT_DAYS_FIELD_NUMBER: builtins.int
    newer_noncurrent_versions: builtins.int
    """Specifies how many noncurrent versions the system will retain."""
    noncurrent_days: builtins.int
    """Specifies the number of days an object is noncurrent before the system will expire it."""
    def __init__(
        self,
        *,
        newer_noncurrent_versions: builtins.int | None = ...,
        noncurrent_days: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_newer_noncurrent_versions", b"_newer_noncurrent_versions", "newer_noncurrent_versions", b"newer_noncurrent_versions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_newer_noncurrent_versions", b"_newer_noncurrent_versions", "newer_noncurrent_versions", b"newer_noncurrent_versions", "noncurrent_days", b"noncurrent_days"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_newer_noncurrent_versions", b"_newer_noncurrent_versions"]) -> typing.Literal["newer_noncurrent_versions"] | None: ...

global___LifecycleNoncurrentVersionExpiration = LifecycleNoncurrentVersionExpiration

@typing.final
class LifecycleAbortIncompleteMultipartUpload(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DAYS_AFTER_INITIATION_FIELD_NUMBER: builtins.int
    days_after_initiation: builtins.int
    """Specifies the days since the initiation of an incomplete multipart upload that
    the system will wait before permanently removing all parts of the upload.
    """
    def __init__(
        self,
        *,
        days_after_initiation: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["days_after_initiation", b"days_after_initiation"]) -> None: ...

global___LifecycleAbortIncompleteMultipartUpload = LifecycleAbortIncompleteMultipartUpload
