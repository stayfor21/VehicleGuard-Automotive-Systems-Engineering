"""Explicit data structures for the VehicleGuard V1 prototype."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Severity(Enum):
    NORMAL = "NORMAL"
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


class ValidationIssueType(Enum):
    MISSING_REQUIRED_INPUT = "MISSING_REQUIRED_INPUT"
    UNSUPPORTED_DATA_TYPE = "UNSUPPORTED_DATA_TYPE"
    VALUE_BELOW_SUPPORTED_RANGE = "VALUE_BELOW_SUPPORTED_RANGE"
    VALUE_ABOVE_SUPPORTED_RANGE = "VALUE_ABOVE_SUPPORTED_RANGE"
    MALFORMED_INPUT = "MALFORMED_INPUT"


@dataclass(frozen=True)
class VehicleData:
    timestamp: float
    coolant_temperature: float
    battery_voltage: float
    oil_pressure: float
    engine_rpm: int
    brake_pad_remaining: float


@dataclass(frozen=True)
class ReceivedVehicleData:
    timestamp: float | None
    values: dict[str, Any]


@dataclass(frozen=True)
class ValidatedVehicleData:
    timestamp: float
    values: dict[str, int | float]
    validation_status: str = "VALID"


@dataclass(frozen=True)
class ValidationIssue:
    timestamp: float | None
    parameter: str
    observed_value: Any
    issue_type: ValidationIssueType
    message: str


@dataclass(frozen=True)
class ConditionRule:
    field: str
    operator: str
    value: int | float


@dataclass(frozen=True)
class ConditionCriterion:
    condition_id: str
    condition_type: str
    severity: str
    event_type: str
    message: str
    rules: list[ConditionRule] = field(default_factory=list)


@dataclass(frozen=True)
class ParameterConfiguration:
    parameter_id: str
    parameter: str
    unit: str
    data_type: str
    supported_min: int | float
    supported_max: int | float
    conditions: list[ConditionCriterion]
    activation_rules: list[ConditionRule] = field(default_factory=list)
    inactive_condition: ConditionCriterion | None = None
    recovery_condition_id: str | None = None


@dataclass(frozen=True)
class VehicleGuardConfiguration:
    version: str
    input_fields: dict[str, dict[str, Any]]
    parameters: dict[str, ParameterConfiguration]


@dataclass(frozen=True)
class ParameterCondition:
    timestamp: float
    parameter: str
    observed_value: int | float
    condition_id: str
    condition_type: str
    severity_name: str
    event_type: str
    message: str
    active: bool = True


@dataclass(frozen=True)
class DiagnosticCondition:
    timestamp: float
    condition_id: str
    parameter: str
    observed_value: int | float | None
    condition_type: str
    severity_name: str
    event_type: str
    message: str
    active: bool = True


@dataclass(frozen=True)
class ClassifiedCondition:
    timestamp: float
    condition_id: str
    parameter: str
    observed_value: int | float | None
    severity: Severity
    event_type: str
    message: str
    condition_type: str
    active: bool = True


@dataclass(frozen=True)
class DriverWarning:
    timestamp: float
    condition_id: str
    parameter: str
    severity: Severity
    message: str


@dataclass(frozen=True)
class DiagnosticEvent:
    timestamp: float | None
    condition_id: str
    parameter: str
    observed_value: Any
    severity: Severity | None
    event_type: str


@dataclass(frozen=True)
class DiagnosticResult:
    received_data: ReceivedVehicleData
    validated_data: ValidatedVehicleData | None
    validation_issues: list[ValidationIssue]
    parameter_conditions: list[ParameterCondition]
    diagnostic_conditions: list[DiagnosticCondition]
    classified_conditions: list[ClassifiedCondition]
    warnings: list[DriverWarning]
    events: list[DiagnosticEvent]
