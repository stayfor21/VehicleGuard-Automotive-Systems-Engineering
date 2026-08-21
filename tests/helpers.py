from __future__ import annotations

from dataclasses import asdict

from prototype.models import DiagnosticResult, Severity, VehicleData


def sample(**overrides: object) -> VehicleData:
    values = {
        "timestamp": 10.0,
        "coolant_temperature": 90.0,
        "battery_voltage": 13.8,
        "oil_pressure": 350.0,
        "engine_rpm": 2000,
        "brake_pad_remaining": 80.0,
    }
    values.update(overrides)
    return VehicleData(**values)


def sample_mapping(**overrides: object) -> dict[str, object]:
    values = asdict(sample())
    values.update(overrides)
    return values


def severity_for(result: DiagnosticResult, parameter: str) -> Severity:
    for condition in result.classified_conditions:
        if condition.parameter == parameter and condition.event_type != "RECOVERY":
            return condition.severity
    raise AssertionError(f"No classified condition for {parameter}")


def event_for(result: DiagnosticResult, parameter: str):
    for event in result.events:
        if event.parameter == parameter:
            return event
    raise AssertionError(f"No event for {parameter}")


def warning_for(result: DiagnosticResult, parameter: str):
    for warning in result.warnings:
        if warning.parameter == parameter:
            return warning
    raise AssertionError(f"No warning for {parameter}")
