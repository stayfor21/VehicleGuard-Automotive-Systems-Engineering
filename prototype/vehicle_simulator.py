"""Deterministic vehicle data scenarios for VehicleGuard V1."""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import Callable

from .diagnostics import VehicleGuard
from .models import DiagnosticEvent, DriverWarning, VehicleData


def normal_operation() -> VehicleData:
    return VehicleData(
        timestamp=10.0,
        coolant_temperature=90.0,
        battery_voltage=13.8,
        oil_pressure=350.0,
        engine_rpm=2000,
        brake_pad_remaining=80.0,
    )


def high_coolant_temperature() -> VehicleData:
    data = asdict(normal_operation())
    data.update(timestamp=11.0, coolant_temperature=120.0)
    return VehicleData(**data)


def low_battery_voltage() -> VehicleData:
    data = asdict(normal_operation())
    data.update(timestamp=12.0, battery_voltage=11.0)
    return VehicleData(**data)


def low_oil_pressure_with_engine_running() -> VehicleData:
    data = asdict(normal_operation())
    data.update(timestamp=13.0, oil_pressure=69.9, engine_rpm=1800)
    return VehicleData(**data)


def engine_stopped_with_low_oil_pressure() -> VehicleData:
    data = asdict(normal_operation())
    data.update(timestamp=14.0, oil_pressure=0.0, engine_rpm=0, battery_voltage=12.6)
    return VehicleData(**data)


def high_engine_rpm() -> VehicleData:
    data = asdict(normal_operation())
    data.update(timestamp=15.0, engine_rpm=7500)
    return VehicleData(**data)


def low_brake_pad_remaining() -> VehicleData:
    data = asdict(normal_operation())
    data.update(timestamp=16.0, brake_pad_remaining=5.0)
    return VehicleData(**data)


def multiple_simultaneous_faults() -> VehicleData:
    data = asdict(normal_operation())
    data.update(
        timestamp=17.0,
        coolant_temperature=120.0,
        battery_voltage=10.9,
        oil_pressure=69.9,
        engine_rpm=7500,
        brake_pad_remaining=5.0,
    )
    return VehicleData(**data)


def invalid_input() -> dict[str, object]:
    data = asdict(normal_operation())
    data.update(timestamp=18.0, engine_rpm="high")
    return data


SCENARIOS: dict[str, Callable[[], VehicleData | dict[str, object]]] = {
    "normal_operation": normal_operation,
    "high_coolant_temperature": high_coolant_temperature,
    "low_battery_voltage": low_battery_voltage,
    "low_oil_pressure_with_engine_running": low_oil_pressure_with_engine_running,
    "engine_stopped_with_low_oil_pressure": engine_stopped_with_low_oil_pressure,
    "high_engine_rpm": high_engine_rpm,
    "low_brake_pad_remaining": low_brake_pad_remaining,
    "multiple_simultaneous_faults": multiple_simultaneous_faults,
    "invalid_input": invalid_input,
}


def run_scenarios() -> dict[str, dict[str, object]]:
    results: dict[str, dict[str, object]] = {}

    for name, scenario in SCENARIOS.items():
        guard = VehicleGuard()
        result = guard.process(scenario())
        results[name] = {
            "warnings": [_warning_to_dict(warning) for warning in result.warnings],
            "events": [_event_to_dict(event) for event in result.events],
            "validation_issues": [
                {
                    "parameter": issue.parameter,
                    "issue_type": issue.issue_type.value,
                    "observed_value": issue.observed_value,
                }
                for issue in result.validation_issues
            ],
        }

    return results


def _warning_to_dict(warning: DriverWarning) -> dict[str, object]:
    data = asdict(warning)
    data["severity"] = warning.severity.value
    return data


def _event_to_dict(event: DiagnosticEvent) -> dict[str, object]:
    data = asdict(event)
    data["severity"] = event.severity.value if event.severity is not None else None
    return data


if __name__ == "__main__":
    print(json.dumps(run_scenarios(), indent=2, sort_keys=True))
