"""VehicleGuard V1 diagnostic processing pipeline."""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any, Mapping

from .config_loader import load_config
from .models import (
    ClassifiedCondition,
    ConditionCriterion,
    ConditionRule,
    DiagnosticCondition,
    DiagnosticEvent,
    DiagnosticResult,
    DriverWarning,
    ParameterCondition,
    ParameterConfiguration,
    ReceivedVehicleData,
    Severity,
    ValidatedVehicleData,
    ValidationIssue,
    ValidationIssueType,
    VehicleData,
    VehicleGuardConfiguration,
)


class VehicleGuard:
    """Small implementation of the documented VehicleGuard processing stages."""

    def __init__(self, configuration: VehicleGuardConfiguration | None = None) -> None:
        self.configuration = configuration if configuration is not None else load_config()
        self._active_abnormal_conditions: dict[str, DiagnosticCondition] = {}

    def process(self, sample: VehicleData | Mapping[str, Any]) -> DiagnosticResult:
        received = self.receive_input(sample)
        validated, validation_issues = self.validate(received)

        if validation_issues:
            events = self.generate_invalid_input_events(validation_issues)
            return DiagnosticResult(
                received_data=received,
                validated_data=None,
                validation_issues=validation_issues,
                parameter_conditions=[],
                diagnostic_conditions=[],
                classified_conditions=[],
                warnings=[],
                events=events,
            )

        if validated is None:
            raise RuntimeError("Validation completed without data or issues.")

        parameter_conditions = self.monitor(validated)
        diagnostic_conditions = self.detect_conditions(parameter_conditions)
        classified_conditions = self.classify_severity(diagnostic_conditions)
        warnings = self.generate_warnings(classified_conditions)
        events = self.generate_events(classified_conditions)

        return DiagnosticResult(
            received_data=received,
            validated_data=validated,
            validation_issues=[],
            parameter_conditions=parameter_conditions,
            diagnostic_conditions=diagnostic_conditions,
            classified_conditions=classified_conditions,
            warnings=warnings,
            events=events,
        )

    def receive_input(self, sample: VehicleData | Mapping[str, Any]) -> ReceivedVehicleData:
        if isinstance(sample, VehicleData):
            values = asdict(sample)
        elif is_dataclass(sample):
            values = asdict(sample)
        elif isinstance(sample, Mapping):
            values = dict(sample)
        else:
            return ReceivedVehicleData(
                timestamp=None,
                values={"sample": sample},
            )

        timestamp = values.get("timestamp")
        if isinstance(timestamp, bool) or not isinstance(timestamp, (int, float)):
            timestamp = None

        return ReceivedVehicleData(timestamp=float(timestamp) if timestamp is not None else None, values=values)

    def validate(
        self,
        received: ReceivedVehicleData,
    ) -> tuple[ValidatedVehicleData | None, list[ValidationIssue]]:
        issues: list[ValidationIssue] = []
        valid_values: dict[str, int | float] = {}

        for field, field_config in self.configuration.input_fields.items():
            if field_config["required"] and field not in received.values:
                issues.append(
                    ValidationIssue(
                        timestamp=received.timestamp,
                        parameter=field,
                        observed_value=None,
                        issue_type=ValidationIssueType.MISSING_REQUIRED_INPUT,
                        message=f"{field} is missing.",
                    )
                )
                continue

            value = received.values.get(field)
            if not self._has_supported_type(value, field_config["data_type"]):
                issues.append(
                    ValidationIssue(
                        timestamp=received.timestamp,
                        parameter=field,
                        observed_value=value,
                        issue_type=ValidationIssueType.UNSUPPORTED_DATA_TYPE,
                        message=f"{field} has unsupported data type.",
                    )
                )
                continue

            numeric_value = int(value) if field_config["data_type"] == "integer" else float(value)
            supported_min = field_config["supported_min"]
            supported_max = field_config.get("supported_max")

            if numeric_value < supported_min:
                issues.append(
                    ValidationIssue(
                        timestamp=received.timestamp,
                        parameter=field,
                        observed_value=value,
                        issue_type=ValidationIssueType.VALUE_BELOW_SUPPORTED_RANGE,
                        message=f"{field} is below the supported input range.",
                    )
                )
                continue

            if supported_max is not None and numeric_value > supported_max:
                issues.append(
                    ValidationIssue(
                        timestamp=received.timestamp,
                        parameter=field,
                        observed_value=value,
                        issue_type=ValidationIssueType.VALUE_ABOVE_SUPPORTED_RANGE,
                        message=f"{field} is above the supported input range.",
                    )
                )
                continue

            valid_values[field] = numeric_value

        if issues:
            return None, issues

        timestamp = float(valid_values["timestamp"])
        return ValidatedVehicleData(timestamp=timestamp, values=valid_values), []

    def monitor(self, validated: ValidatedVehicleData) -> list[ParameterCondition]:
        conditions: list[ParameterCondition] = []

        for parameter, parameter_config in self.configuration.parameters.items():
            if not self._activation_rules_match(parameter_config.activation_rules, validated.values):
                inactive = parameter_config.inactive_condition
                if inactive is None:
                    continue
                conditions.append(
                    self._parameter_condition(validated, parameter, inactive, active=False)
                )
                continue

            criterion = self._matching_condition(parameter_config.conditions, validated.values)
            conditions.append(self._parameter_condition(validated, parameter, criterion))

        return conditions

    def detect_conditions(
        self,
        parameter_conditions: list[ParameterCondition],
    ) -> list[DiagnosticCondition]:
        diagnostic_conditions: list[DiagnosticCondition] = []

        for condition in parameter_conditions:
            diagnostic_condition = DiagnosticCondition(
                timestamp=condition.timestamp,
                condition_id=condition.condition_id,
                parameter=condition.parameter,
                observed_value=condition.observed_value,
                condition_type=condition.condition_type,
                severity_name=condition.severity_name,
                event_type=condition.event_type,
                message=condition.message,
                active=condition.active,
            )
            diagnostic_conditions.append(diagnostic_condition)

            previous = self._active_abnormal_conditions.get(condition.parameter)
            if self._is_active_abnormal(diagnostic_condition):
                self._active_abnormal_conditions[condition.parameter] = diagnostic_condition
            elif previous is not None:
                diagnostic_conditions.append(self._recovery_condition(condition, previous))
                del self._active_abnormal_conditions[condition.parameter]

        return diagnostic_conditions

    def classify_severity(
        self,
        diagnostic_conditions: list[DiagnosticCondition],
    ) -> list[ClassifiedCondition]:
        return [
            ClassifiedCondition(
                timestamp=condition.timestamp,
                condition_id=condition.condition_id,
                parameter=condition.parameter,
                observed_value=condition.observed_value,
                severity=Severity[condition.severity_name],
                event_type=condition.event_type,
                message=condition.message,
                condition_type=condition.condition_type,
                active=condition.active,
            )
            for condition in diagnostic_conditions
        ]

    def generate_warnings(
        self,
        classified_conditions: list[ClassifiedCondition],
    ) -> list[DriverWarning]:
        warning_severities = {Severity.WARNING, Severity.CRITICAL}
        return [
            DriverWarning(
                timestamp=condition.timestamp,
                condition_id=condition.condition_id,
                parameter=condition.parameter,
                severity=condition.severity,
                message=condition.message,
            )
            for condition in classified_conditions
            if condition.active and condition.severity in warning_severities
        ]

    def generate_events(
        self,
        classified_conditions: list[ClassifiedCondition],
    ) -> list[DiagnosticEvent]:
        events: list[DiagnosticEvent] = []

        for condition in classified_conditions:
            if condition.severity == Severity.NORMAL and condition.event_type != "RECOVERY":
                continue
            if not condition.active and condition.event_type != "RECOVERY":
                continue

            events.append(
                DiagnosticEvent(
                    timestamp=condition.timestamp,
                    condition_id=condition.condition_id,
                    parameter=condition.parameter,
                    observed_value=condition.observed_value,
                    severity=condition.severity,
                    event_type=condition.event_type,
                )
            )

        return events

    def generate_invalid_input_events(
        self,
        issues: list[ValidationIssue],
    ) -> list[DiagnosticEvent]:
        return [
            DiagnosticEvent(
                timestamp=issue.timestamp,
                condition_id=f"INVALID_INPUT_{issue.parameter.upper()}_{issue.issue_type.value}",
                parameter=issue.parameter,
                observed_value=issue.observed_value,
                severity=None,
                event_type="INVALID_INPUT",
            )
            for issue in issues
        ]

    def _parameter_condition(
        self,
        validated: ValidatedVehicleData,
        parameter: str,
        criterion: ConditionCriterion,
        active: bool = True,
    ) -> ParameterCondition:
        return ParameterCondition(
            timestamp=validated.timestamp,
            parameter=parameter,
            observed_value=validated.values[parameter],
            condition_id=criterion.condition_id,
            condition_type=criterion.condition_type,
            severity_name=criterion.severity,
            event_type=criterion.event_type,
            message=criterion.message,
            active=active,
        )

    def _matching_condition(
        self,
        conditions: list[ConditionCriterion],
        values: Mapping[str, int | float],
    ) -> ConditionCriterion:
        for condition in conditions:
            if self._activation_rules_match(condition.rules, values):
                return condition
        raise RuntimeError("Active configuration does not cover the validated sample.")

    def _activation_rules_match(
        self,
        rules: list[ConditionRule],
        values: Mapping[str, int | float],
    ) -> bool:
        return all(self._rule_matches(rule, values) for rule in rules)

    def _rule_matches(self, rule: ConditionRule, values: Mapping[str, int | float]) -> bool:
        observed = values[rule.field]
        if rule.operator == "<":
            return observed < rule.value
        if rule.operator == "<=":
            return observed <= rule.value
        if rule.operator == ">":
            return observed > rule.value
        if rule.operator == ">=":
            return observed >= rule.value
        if rule.operator == "==":
            return observed == rule.value
        raise RuntimeError(f"Unsupported operator after configuration validation: {rule.operator}")

    def _recovery_condition(
        self,
        condition: ParameterCondition,
        previous: DiagnosticCondition,
    ) -> DiagnosticCondition:
        parameter_config = self.configuration.parameters[condition.parameter]
        condition_id = parameter_config.recovery_condition_id or f"RECOVERY_{condition.parameter.upper()}"
        return DiagnosticCondition(
            timestamp=condition.timestamp,
            condition_id=condition_id,
            parameter=condition.parameter,
            observed_value=condition.observed_value,
            condition_type="RECOVERY",
            severity_name=Severity.NORMAL.value,
            event_type="RECOVERY",
            message=f"{previous.parameter} returned to normal.",
            active=False,
        )

    def _is_active_abnormal(self, condition: DiagnosticCondition) -> bool:
        return condition.active and condition.severity_name != Severity.NORMAL.value

    def _has_supported_type(self, value: Any, data_type: str) -> bool:
        if isinstance(value, bool):
            return False
        if data_type == "integer":
            return isinstance(value, int)
        if data_type == "float":
            return isinstance(value, (int, float))
        return False


def process_vehicle_data(sample: VehicleData | Mapping[str, Any]) -> DiagnosticResult:
    return VehicleGuard().process(sample)
