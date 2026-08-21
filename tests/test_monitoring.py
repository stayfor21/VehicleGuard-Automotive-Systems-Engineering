import pytest

from prototype.diagnostics import VehicleGuard
from prototype.models import Severity

from .helpers import sample, severity_for


def test_tc_mon_001_all_configured_parameters_are_monitored():
    """TC-MON-001"""
    result = VehicleGuard().process(sample())

    assert {condition.parameter for condition in result.parameter_conditions} == {
        "coolant_temperature",
        "battery_voltage",
        "oil_pressure",
        "engine_rpm",
        "brake_pad_remaining",
    }


@pytest.mark.parametrize(
    ("field", "value", "expected"),
    [
        ("coolant_temperature", 109.9, Severity.NORMAL),
        ("coolant_temperature", 110.0, Severity.WARNING),
        ("coolant_temperature", 110.1, Severity.WARNING),
        ("coolant_temperature", 119.9, Severity.WARNING),
        ("coolant_temperature", 120.0, Severity.CRITICAL),
        ("coolant_temperature", 120.1, Severity.CRITICAL),
        ("battery_voltage", 10.9, Severity.CRITICAL),
        ("battery_voltage", 11.0, Severity.WARNING),
        ("battery_voltage", 11.1, Severity.WARNING),
        ("battery_voltage", 11.9, Severity.WARNING),
        ("battery_voltage", 12.0, Severity.NORMAL),
        ("battery_voltage", 12.1, Severity.NORMAL),
        ("battery_voltage", 14.9, Severity.NORMAL),
        ("battery_voltage", 15.0, Severity.NORMAL),
        ("battery_voltage", 15.1, Severity.WARNING),
        ("battery_voltage", 15.9, Severity.WARNING),
        ("battery_voltage", 16.0, Severity.WARNING),
        ("battery_voltage", 16.1, Severity.CRITICAL),
        ("oil_pressure", 69.9, Severity.CRITICAL),
        ("oil_pressure", 70.0, Severity.WARNING),
        ("oil_pressure", 70.1, Severity.WARNING),
        ("oil_pressure", 149.9, Severity.WARNING),
        ("oil_pressure", 150.0, Severity.NORMAL),
        ("oil_pressure", 150.1, Severity.NORMAL),
        ("engine_rpm", 6499, Severity.NORMAL),
        ("engine_rpm", 6500, Severity.WARNING),
        ("engine_rpm", 6501, Severity.WARNING),
        ("engine_rpm", 7499, Severity.WARNING),
        ("engine_rpm", 7500, Severity.CRITICAL),
        ("engine_rpm", 7501, Severity.CRITICAL),
        ("brake_pad_remaining", 4.9, Severity.CRITICAL),
        ("brake_pad_remaining", 5.0, Severity.CRITICAL),
        ("brake_pad_remaining", 5.1, Severity.WARNING),
        ("brake_pad_remaining", 14.9, Severity.WARNING),
        ("brake_pad_remaining", 15.0, Severity.WARNING),
        ("brake_pad_remaining", 15.1, Severity.INFO),
        ("brake_pad_remaining", 24.9, Severity.INFO),
        ("brake_pad_remaining", 25.0, Severity.INFO),
        ("brake_pad_remaining", 25.1, Severity.NORMAL),
    ],
)
def test_tc_mon_002_diagnostic_threshold_boundaries(field, value, expected):
    """TC-MON-002"""
    result = VehicleGuard().process(sample(**{field: value}))

    assert severity_for(result, field) is expected
