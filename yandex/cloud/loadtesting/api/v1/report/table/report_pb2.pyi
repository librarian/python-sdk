"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.loadtesting.api.v1.common.quantiles_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Report(google.protobuf.message.Message):
    """Aggregated test results."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class HttpCodesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class NetCodesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    HTTP_CODES_FIELD_NUMBER: builtins.int
    NET_CODES_FIELD_NUMBER: builtins.int
    QUANTILES_FIELD_NUMBER: builtins.int
    @property
    def http_codes(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.int]:
        """Total count of HTTP responses, grouped by HTTP response code."""

    @property
    def net_codes(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.int]:
        """Total count of network responses, grouped by response code."""

    @property
    def quantiles(self) -> yandex.cloud.loadtesting.api.v1.common.quantiles_pb2.Quantiles:
        """Response time statistics, aggregated by quantiles."""

    def __init__(
        self,
        *,
        http_codes: collections.abc.Mapping[builtins.int, builtins.int] | None = ...,
        net_codes: collections.abc.Mapping[builtins.int, builtins.int] | None = ...,
        quantiles: yandex.cloud.loadtesting.api.v1.common.quantiles_pb2.Quantiles | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["quantiles", b"quantiles"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["http_codes", b"http_codes", "net_codes", b"net_codes", "quantiles", b"quantiles"]) -> None: ...

global___Report = Report