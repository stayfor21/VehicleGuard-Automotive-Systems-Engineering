from prototype.diagnostics import VehicleGuard
from prototype.models import Severity

from .helpers import sample, severity_for


def test_tc_diag_001_normal_condition_is_identified_as_normal():
    """TC-DIAG-001"""
    result = VehicleGuard().process(sample())

    assert all(condition.severity is Severity.NORMAL for condition in result.classified_conditions)
    assert result.events == []


def test_tc_diag_002_abnormal_condition_detection_identifies_parameter_and_condition():
    """TC-DIAG-002"""
    result = VehicleGuard().process(sample(coolant_temperature=110.0))

    assert severity_for(result, "coolant_temperature") is Severity.WARNING
    event = next(event for event in result.events if event.parameter == "coolant_temperature")
    assert event.condition_id == "COOLANT_TEMPERATURE_WARNING_HIGH"


def test_tc_diag_003_multiple_simultaneous_abnormal_conditions_are_not_suppressed():
    """TC-DIAG-003"""
    result = VehicleGuard().process(
        sample(
            coolant_temperature=120.0,
            battery_voltage=10.9,
            oil_pressure=69.9,
            engine_rpm=7500,
            brake_pad_remaining=5.0,
        )
    )

    assert {event.parameter for event in result.events} == {
        "coolant_temperature",
        "battery_voltage",
        "oil_pressure",
        "engine_rpm",
        "brake_pad_remaining",
    }


def test_tc_diag_004_recovery_to_normal_clears_active_abnormal_condition():
    """TC-DIAG-004"""
    guard = VehicleGuard()

    normal = guard.process(sample(timestamp=1.0))
    abnormal = guard.process(sample(timestamp=2.0, coolant_temperature=120.0))
    recovered = guard.process(sample(timestamp=3.0, coolant_temperature=90.0))
    stable_normal = guard.process(sample(timestamp=4.0, coolant_temperature=90.0))

    assert normal.events == []
    assert any(event.parameter == "coolant_temperature" for event in abnormal.events)
    assert any(event.event_type == "RECOVERY" for event in recovered.events)
    assert not recovered.warnings
    assert stable_normal.events == []


def test_oil_pressure_monitoring_is_inactive_when_engine_is_stopped():
    result = VehicleGuard().process(sample(engine_rpm=0, oil_pressure=0.0, battery_voltage=12.6))

    assert severity_for(result, "oil_pressure") is Severity.NORMAL
    assert not any(event.parameter == "oil_pressure" for event in result.events)
