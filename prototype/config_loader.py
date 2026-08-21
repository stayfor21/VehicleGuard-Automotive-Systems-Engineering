"""Configuration loading and validation for VehicleGuard V1."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import (
    ConditionCriterion,
    ConditionRule,
    ParameterConfiguration,
    Severity,
    VehicleGuardConfiguration,
)

DEFAULT_CONFIG_PATH = Path(__file__).parent / "config" / "vehicleguard-v1.json"
SUPPORTED_DATA_TYPES = {"float", "integer"}
SUPPORTED_OPERATORS = {"<", "<=", ">", ">=", "=="}


class ConfigurationError(ValueError):
    """Raised when the VehicleGuard configuration is missing or malformed."""


def load_config(path: str | Path = DEFAULT_CONFIG_PATH) -> VehicleGuardConfiguration:
    config_path = Path(path)
    try:
        raw = json.loads(config_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigurationError(f"Configuration file not found: {config_path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigurationError(f"Configuration file is not valid JSON: {config_path}") from exc

    return parse_config(raw)


def parse_config(raw: dict[str, Any]) -> VehicleGuardConfiguration:
    if not isinstance(raw, dict):
        raise ConfigurationError("Configuration root must be a JSON object.")

    version = _require_str(raw, "version")
    input_fields = _require_dict(raw, "input_fields")
    parameters_raw = _require_dict(raw, "parameters")

    if not parameters_raw:
        raise ConfigurationError("Configuration must define at least one monitored parameter.")

    for field_name, field_config in input_fields.items():
        _validate_input_field(field_name, field_config)

    parameters: dict[str, ParameterConfiguration] = {}
    for parameter, parameter_raw in parameters_raw.items():
        parameter_config = _parse_parameter(parameter, parameter_raw)
        parameters[parameter] = parameter_config

        if parameter not in input_fields:
            raise ConfigurationError(f"Parameter {parameter!r} is missing from input_fields.")

    return VehicleGuardConfiguration(
        version=version,
        input_fields=input_fields,
        parameters=parameters,
    )


def _parse_parameter(parameter: str, raw: Any) -> ParameterConfiguration:
    if not isinstance(raw, dict):
        raise ConfigurationError(f"Configuration for {parameter!r} must be an object.")

    parameter_id = _require_str(raw, "parameter_id")
    unit = _require_str(raw, "unit")
    data_type = _require_str(raw, "data_type")
    if data_type not in SUPPORTED_DATA_TYPES:
        raise ConfigurationError(f"{parameter!r} has unsupported data_type {data_type!r}.")

    supported_min = _require_number(raw, "supported_min")
    supported_max = _require_number(raw, "supported_max")
    if supported_min > supported_max:
        raise ConfigurationError(f"{parameter!r} supported_min must be <= supported_max.")

    conditions_raw = _require_list(raw, "conditions")
    conditions = [_parse_condition(parameter, item) for item in conditions_raw]
    if not conditions:
        raise ConfigurationError(f"{parameter!r} must define at least one condition.")
    if not any(condition.severity == Severity.NORMAL.value for condition in conditions):
        raise ConfigurationError(f"{parameter!r} must define a NORMAL condition.")

    activation_rules = [
        _parse_rule(item) for item in raw.get("activation_rules", [])
    ]
    inactive_condition = None
    if "inactive_condition" in raw:
        inactive_condition = _parse_condition(parameter, raw["inactive_condition"])

    return ParameterConfiguration(
        parameter_id=parameter_id,
        parameter=parameter,
        unit=unit,
        data_type=data_type,
        supported_min=supported_min,
        supported_max=supported_max,
        conditions=conditions,
        activation_rules=activation_rules,
        inactive_condition=inactive_condition,
        recovery_condition_id=raw.get("recovery_condition_id"),
    )


def _parse_condition(parameter: str, raw: Any) -> ConditionCriterion:
    if not isinstance(raw, dict):
        raise ConfigurationError(f"Condition for {parameter!r} must be an object.")

    severity = _require_str(raw, "severity")
    if severity not in Severity.__members__:
        raise ConfigurationError(f"{parameter!r} condition has unsupported severity {severity!r}.")

    return ConditionCriterion(
        condition_id=_require_str(raw, "condition_id"),
        condition_type=_require_str(raw, "condition_type"),
        severity=severity,
        event_type=_require_str(raw, "event_type"),
        message=_require_str(raw, "message"),
        rules=[_parse_rule(item) for item in raw.get("rules", [])],
    )


def _parse_rule(raw: Any) -> ConditionRule:
    if not isinstance(raw, dict):
        raise ConfigurationError("Condition rule must be an object.")

    field = _require_str(raw, "field")
    operator = _require_str(raw, "operator")
    if operator not in SUPPORTED_OPERATORS:
        raise ConfigurationError(f"Unsupported rule operator {operator!r}.")

    return ConditionRule(
        field=field,
        operator=operator,
        value=_require_number(raw, "value"),
    )


def _validate_input_field(field_name: str, field_config: Any) -> None:
    if not isinstance(field_config, dict):
        raise ConfigurationError(f"Input field {field_name!r} must be an object.")

    data_type = _require_str(field_config, "data_type")
    if data_type not in SUPPORTED_DATA_TYPES:
        raise ConfigurationError(f"Input field {field_name!r} has unsupported data_type.")

    _require_bool(field_config, "required")
    supported_min = _require_number(field_config, "supported_min")
    supported_max = field_config.get("supported_max")
    if supported_max is not None:
        supported_max = _require_number(field_config, "supported_max")
        if supported_min > supported_max:
            raise ConfigurationError(f"Input field {field_name!r} supported_min must be <= supported_max.")


def _require_str(raw: dict[str, Any], key: str) -> str:
    value = raw.get(key)
    if not isinstance(value, str) or not value:
        raise ConfigurationError(f"Required string field missing or invalid: {key}")
    return value


def _require_bool(raw: dict[str, Any], key: str) -> bool:
    value = raw.get(key)
    if not isinstance(value, bool):
        raise ConfigurationError(f"Required boolean field missing or invalid: {key}")
    return value


def _require_dict(raw: dict[str, Any], key: str) -> dict[str, Any]:
    value = raw.get(key)
    if not isinstance(value, dict):
        raise ConfigurationError(f"Required object field missing or invalid: {key}")
    return value


def _require_list(raw: dict[str, Any], key: str) -> list[Any]:
    value = raw.get(key)
    if not isinstance(value, list):
        raise ConfigurationError(f"Required list field missing or invalid: {key}")
    return value


def _require_number(raw: dict[str, Any], key: str) -> int | float:
    value = raw.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ConfigurationError(f"Required numeric field missing or invalid: {key}")
    return value
