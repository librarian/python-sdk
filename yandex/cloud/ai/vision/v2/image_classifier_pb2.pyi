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
import sys
import typing
import yandex.cloud.ai.vision.v2.image_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Label(google.protobuf.message.Message):
    """Description of single label"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """   Label name"""
    description: builtins.str
    """   human readable description of label"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "name", b"name"]) -> None: ...

global___Label = Label

@typing.final
class ClassAnnotation(google.protobuf.message.Message):
    """Image annotation for specific label"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LABEL_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    confidence: builtins.float
    """   confidence for each label"""
    @property
    def label(self) -> global___Label:
        """   list of annotated labels"""

    def __init__(
        self,
        *,
        label: global___Label | None = ...,
        confidence: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["label", b"label"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["confidence", b"confidence", "label", b"label"]) -> None: ...

global___ClassAnnotation = ClassAnnotation

@typing.final
class ClassifierSpecification(google.protobuf.message.Message):
    """Specification of model used for annotation"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ClassificationType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ClassificationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ClassifierSpecification._ClassificationType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CLASSIFICATION_TYPE_UNSPECIFIED: ClassifierSpecification._ClassificationType.ValueType  # 0
        MULTI_LABEL: ClassifierSpecification._ClassificationType.ValueType  # 1
        MULTI_CLASS: ClassifierSpecification._ClassificationType.ValueType  # 2

    class ClassificationType(_ClassificationType, metaclass=_ClassificationTypeEnumTypeWrapper): ...
    CLASSIFICATION_TYPE_UNSPECIFIED: ClassifierSpecification.ClassificationType.ValueType  # 0
    MULTI_LABEL: ClassifierSpecification.ClassificationType.ValueType  # 1
    MULTI_CLASS: ClassifierSpecification.ClassificationType.ValueType  # 2

    LABELS_FIELD_NUMBER: builtins.int
    CLASSIFICATION_TYPE_FIELD_NUMBER: builtins.int
    classification_type: global___ClassifierSpecification.ClassificationType.ValueType
    """   type of annotation: exclusive (multi-class) or non-exclusive (multi-label)"""
    @property
    def labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Label]:
        """ List of labels, annotated by service"""

    def __init__(
        self,
        *,
        labels: collections.abc.Iterable[global___Label] | None = ...,
        classification_type: global___ClassifierSpecification.ClassificationType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["classification_type", b"classification_type", "labels", b"labels"]) -> None: ...

global___ClassifierSpecification = ClassifierSpecification

@typing.final
class AnnotationResponse(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    CLASSIFIER_SPECIFICATION_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """ internal service requestId"""
    @property
    def classifier_specification(self) -> global___ClassifierSpecification:
        """ class specification"""

    @property
    def annotations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClassAnnotation]:
        """   annotations for each class"""

    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        classifier_specification: global___ClassifierSpecification | None = ...,
        annotations: collections.abc.Iterable[global___ClassAnnotation] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["classifier_specification", b"classifier_specification"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["annotations", b"annotations", "classifier_specification", b"classifier_specification", "request_id", b"request_id"]) -> None: ...

global___AnnotationResponse = AnnotationResponse

@typing.final
class AnnotationRequest(google.protobuf.message.Message):
    """request for annotation"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_FIELD_NUMBER: builtins.int
    @property
    def image(self) -> yandex.cloud.ai.vision.v2.image_pb2.Image:
        """   image to annotate"""

    def __init__(
        self,
        *,
        image: yandex.cloud.ai.vision.v2.image_pb2.Image | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["image", b"image"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["image", b"image"]) -> None: ...

global___AnnotationRequest = AnnotationRequest