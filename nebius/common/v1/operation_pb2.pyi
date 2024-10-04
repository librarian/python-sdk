"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Operation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class RequestHeader(google.protobuf.message.Message):
        """Request header is a container for all the values of a particular header of a request
        as there is no such thing as map<string, repeated string>
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VALUES_FIELD_NUMBER: builtins.int
        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """The values of a particular header from a request"""

        def __init__(
            self,
            *,
            values: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["values", b"values"]) -> None: ...

    @typing.final
    class RequestHeadersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Operation.RequestHeader: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___Operation.RequestHeader | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    REQUEST_HEADERS_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    PROGRESS_DATA_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the operation."""
    description: builtins.str
    """Human-readable description of the operation. 0-256 characters long."""
    created_by: builtins.str
    """ID of the user or service account who initiated the operation."""
    resource_id: builtins.str
    """ID of the resource that this operation creates, updates, deletes or otherwise changes.

    If the operation affects multiple resources or does not affect any API resources at all
    (e.g. a routine maintenance operation visible to the user), the [resource_id] must be empty.
    """
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def finished_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the operation has finished."""

    @property
    def request(self) -> google.protobuf.any_pb2.Any:
        """The request that generated this operation."""

    @property
    def request_headers(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Operation.RequestHeader]:
        """The request headers that are essential for the request that generated the operation.
        For instance, `x-resetmask`. Without these headers the request might have been processed
        differently if repeated.
        All the header names *must* be converted to lower case.
        Validator is based on:
        https://httpwg.org/specs/rfc9110.html#considerations.for.new.field.names
        """

    @property
    def progress_data(self) -> google.protobuf.any_pb2.Any:
        """Additional information about the progress of an operation, e.g., a progress percentage.
        MAY be absent while the operation is running, MUST be absent after the operation has completed.

        Format of message inside [progress_data] is service-dependent and MUST be documented by the
        service, IF it is used.
        """

    @property
    def status(self) -> google.rpc.status_pb2.Status:
        """The status of this operation. Set when this operation is completed.
        See https://github.com/grpc/grpc/blob/master/src/proto/grpc/status/status.proto.

        [status.code] is https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto:
        - If [status.code] == OK, the operation has completed successfully.
        - If [status.code] != OK, the operation has failed or has been cancelled.
          - [status.message] will contain a user-readable and actionable error message.
          - [status.details] will contain additional diagnostic information in the form of
            [ServiceError] from nebius/common/v1/error.proto
        - [status.code] must belong to an Operation-compatible subset of GRPC codes:
          OK, CANCELLED, PERMISSION_DENIED, RESOURCE_EXHAUSTED, FAILED_PRECONDITION, ABORTED, INTERNAL
        """

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        description: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_by: builtins.str = ...,
        finished_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        request: google.protobuf.any_pb2.Any | None = ...,
        request_headers: collections.abc.Mapping[builtins.str, global___Operation.RequestHeader] | None = ...,
        resource_id: builtins.str = ...,
        progress_data: google.protobuf.any_pb2.Any | None = ...,
        status: google.rpc.status_pb2.Status | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "finished_at", b"finished_at", "progress_data", b"progress_data", "request", b"request", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "created_by", b"created_by", "description", b"description", "finished_at", b"finished_at", "id", b"id", "progress_data", b"progress_data", "request", b"request", "request_headers", b"request_headers", "resource_id", b"resource_id", "status", b"status"]) -> None: ...

global___Operation = Operation
