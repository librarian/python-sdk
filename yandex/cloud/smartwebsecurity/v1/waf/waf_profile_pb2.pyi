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
import yandex.cloud.smartwebsecurity.v1.security_profile_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class WafProfile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class CoreRuleSet(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        INBOUND_ANOMALY_SCORE_FIELD_NUMBER: builtins.int
        PARANOIA_LEVEL_FIELD_NUMBER: builtins.int
        RULE_SET_FIELD_NUMBER: builtins.int
        inbound_anomaly_score: builtins.int
        """Anomaly score.
        Enter an integer within the range of 2 and 10000.
        The higher this value, the more likely it is that the request that satisfies the rule is an attack.
        See [Rules](/docs/smartwebsecurity/concepts/waf#anomaly) for more details.
        """
        paranoia_level: builtins.int
        """Paranoia level.
        Enter an integer within the range of 1 and 4.
        Paranoia level classifies rules according to their aggression. The higher the paranoia level, the better your protection,
        but also the higher the probability of WAF false positives.
        See [Rules](/docs/smartwebsecurity/concepts/waf#paranoia) for more details.
        NOTE: this option has no effect on enabling or disabling rules.
        it is used only as recommendation for user to enable all rules with paranoia_level <= this value.
        """
        @property
        def rule_set(self) -> global___RuleSet:
            """Rule set."""

        def __init__(
            self,
            *,
            inbound_anomaly_score: builtins.int = ...,
            paranoia_level: builtins.int = ...,
            rule_set: global___RuleSet | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["rule_set", b"rule_set"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["inbound_anomaly_score", b"inbound_anomaly_score", "paranoia_level", b"paranoia_level", "rule_set", b"rule_set"]) -> None: ...

    @typing.final
    class AnalyzeRequestBody(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _Action:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _ActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WafProfile.AnalyzeRequestBody._Action.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            ACTION_UNSPECIFIED: WafProfile.AnalyzeRequestBody._Action.ValueType  # 0
            IGNORE: WafProfile.AnalyzeRequestBody._Action.ValueType  # 1
            """Ignore request."""
            DENY: WafProfile.AnalyzeRequestBody._Action.ValueType  # 2
            """Deny request."""

        class Action(_Action, metaclass=_ActionEnumTypeWrapper):
            """Action to perform if maximum size of body exceeded."""

        ACTION_UNSPECIFIED: WafProfile.AnalyzeRequestBody.Action.ValueType  # 0
        IGNORE: WafProfile.AnalyzeRequestBody.Action.ValueType  # 1
        """Ignore request."""
        DENY: WafProfile.AnalyzeRequestBody.Action.ValueType  # 2
        """Deny request."""

        IS_ENABLED_FIELD_NUMBER: builtins.int
        SIZE_LIMIT_FIELD_NUMBER: builtins.int
        SIZE_LIMIT_ACTION_FIELD_NUMBER: builtins.int
        is_enabled: builtins.bool
        """Possible to turn analyzer on and turn if off."""
        size_limit: builtins.int
        """Maximum size of body to pass to analyzer. In kilobytes."""
        size_limit_action: global___WafProfile.AnalyzeRequestBody.Action.ValueType
        """Action to perform if maximum size of body exceeded."""
        def __init__(
            self,
            *,
            is_enabled: builtins.bool = ...,
            size_limit: builtins.int = ...,
            size_limit_action: global___WafProfile.AnalyzeRequestBody.Action.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["is_enabled", b"is_enabled", "size_limit", b"size_limit", "size_limit_action", b"size_limit_action"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CLOUD_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    RULES_FIELD_NUMBER: builtins.int
    EXCLUSION_RULES_FIELD_NUMBER: builtins.int
    CORE_RULE_SET_FIELD_NUMBER: builtins.int
    ANALYZE_REQUEST_BODY_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the WAF profile."""
    folder_id: builtins.str
    """ID of the folder that the WAF profile belongs to."""
    cloud_id: builtins.str
    """ID of the cloud that the WAF profile belongs to."""
    name: builtins.str
    """Name of the WAF profile. The name is unique within the folder. 1-50 characters long."""
    description: builtins.str
    """Optional description of the WAF profile."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels as `` key:value `` pairs. Maximum of 64 per resource."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""

    @property
    def rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WafProfileRule]:
        """Settings for each rule in rule set."""

    @property
    def exclusion_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WafProfileExclusionRule]:
        """List of exclusion rules. See [Rules](/docs/smartwebsecurity/concepts/waf#exclusion-rules)."""

    @property
    def core_rule_set(self) -> global___WafProfile.CoreRuleSet:
        """Core rule set settings. See [Basic rule set](/docs/smartwebsecurity/concepts/waf#rules-set) for details."""

    @property
    def analyze_request_body(self) -> global___WafProfile.AnalyzeRequestBody:
        """Parameters for request body analyzer."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        cloud_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        rules: collections.abc.Iterable[global___WafProfileRule] | None = ...,
        exclusion_rules: collections.abc.Iterable[global___WafProfileExclusionRule] | None = ...,
        core_rule_set: global___WafProfile.CoreRuleSet | None = ...,
        analyze_request_body: global___WafProfile.AnalyzeRequestBody | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["analyze_request_body", b"analyze_request_body", "core_rule_set", b"core_rule_set", "created_at", b"created_at", "rule_set", b"rule_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["analyze_request_body", b"analyze_request_body", "cloud_id", b"cloud_id", "core_rule_set", b"core_rule_set", "created_at", b"created_at", "description", b"description", "exclusion_rules", b"exclusion_rules", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "rule_set", b"rule_set", "rules", b"rules"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["rule_set", b"rule_set"]) -> typing.Literal["core_rule_set"] | None: ...

global___WafProfile = WafProfile

@typing.final
class WafProfileRule(google.protobuf.message.Message):
    """WafProfileRule object. Determines settings for each rule_id in rule set."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RULE_ID_FIELD_NUMBER: builtins.int
    IS_ENABLED_FIELD_NUMBER: builtins.int
    IS_BLOCKING_FIELD_NUMBER: builtins.int
    rule_id: builtins.str
    """Rule ID."""
    is_enabled: builtins.bool
    """Determines is it rule enabled or not."""
    is_blocking: builtins.bool
    """Determines is it rule blocking or not."""
    def __init__(
        self,
        *,
        rule_id: builtins.str = ...,
        is_enabled: builtins.bool = ...,
        is_blocking: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["is_blocking", b"is_blocking", "is_enabled", b"is_enabled", "rule_id", b"rule_id"]) -> None: ...

global___WafProfileRule = WafProfileRule

@typing.final
class WafProfileExclusionRule(google.protobuf.message.Message):
    """A WafProfileExclusionRule object. See [Exclusion rules](/docs/smartwebsecurity/concepts/waf#exclusion-rules)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class ExcludeRules(google.protobuf.message.Message):
        """Determines list of excluded rules."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        EXCLUDE_ALL_FIELD_NUMBER: builtins.int
        RULE_IDS_FIELD_NUMBER: builtins.int
        exclude_all: builtins.bool
        """Set this option true to exclude all rules."""
        @property
        def rule_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """List of rules to exclude."""

        def __init__(
            self,
            *,
            exclude_all: builtins.bool = ...,
            rule_ids: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["exclude_all", b"exclude_all", "rule_ids", b"rule_ids"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    EXCLUDE_RULES_FIELD_NUMBER: builtins.int
    LOG_EXCLUDED_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of exclusion rule."""
    description: builtins.str
    """Optional description of the rule. 0-512 characters long."""
    log_excluded: builtins.bool
    """Records the fact that an exception rule is triggered."""
    @property
    def condition(self) -> yandex.cloud.smartwebsecurity.v1.security_profile_pb2.Condition:
        """The condition for matching traffic."""

    @property
    def exclude_rules(self) -> global___WafProfileExclusionRule.ExcludeRules:
        """Exclude rules."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        condition: yandex.cloud.smartwebsecurity.v1.security_profile_pb2.Condition | None = ...,
        exclude_rules: global___WafProfileExclusionRule.ExcludeRules | None = ...,
        log_excluded: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["condition", b"condition", "exclude_rules", b"exclude_rules"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["condition", b"condition", "description", b"description", "exclude_rules", b"exclude_rules", "log_excluded", b"log_excluded", "name", b"name"]) -> None: ...

global___WafProfileExclusionRule = WafProfileExclusionRule

@typing.final
class RuleSet(google.protobuf.message.Message):
    """A RuleSet object. Determines name and version of rule set."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of rule set."""
    version: builtins.str
    """Version of rule set."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "version", b"version"]) -> None: ...

global___RuleSet = RuleSet
