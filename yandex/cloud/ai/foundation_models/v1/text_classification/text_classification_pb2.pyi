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
class ClassificationLabel(google.protobuf.message.Message):
    """A pair of text label and corresponding confidence used in classification problems."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LABEL_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    label: builtins.str
    """A label with a class name."""
    confidence: builtins.float
    """Confidence of item's belonging to a class."""
    def __init__(
        self,
        *,
        label: builtins.str = ...,
        confidence: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["confidence", b"confidence", "label", b"label"]) -> None: ...

global___ClassificationLabel = ClassificationLabel

@typing.final
class ClassificationSample(google.protobuf.message.Message):
    """Description of a sample for the classification task."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    text: builtins.str
    """Text sample."""
    label: builtins.str
    """Expected label for a given text."""
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        label: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["label", b"label", "text", b"text"]) -> None: ...

global___ClassificationSample = ClassificationSample