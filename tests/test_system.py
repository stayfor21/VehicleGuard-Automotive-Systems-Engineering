from prototype.diagnostics import VehicleGuard
from prototype.models import Severity
from prototype.vehicle_simulator import run_scenarios

from .helpers import sample, sample_mapping, severity_for


def test_tc_sys_001_normal_vehicle_data_processing():
    """TC-SYS-001"""
    result = VehicleGuard().process(sample())

    assert result.validated_data is not None
    assert result.validation_issues == []
    assert all(condition.severity is Severity.NORMAL for condition in result.classified_conditions)
    assert result.warnings == []
    assert result.events == []


def test_tc_sys_002_single_abnormal_condition_end_to_end():
    """TC-SYS-002"""
    result = VehicleGuard().process(sample(coolant_temperature=120.0))

    assert result.validated_data is not None
    assert severity_for(result, "coolant_temperature") is Severity.CRITICAL
    assert len(result.warnings) == 1
    assert len(result.events) == 1
    assert result.warnings[0].condition_id == result.events[0].condition_id


def test_tc_sys_003_multiple_abnormal_conditions_end_to_end():
    """TC-SYS-003"""
    result = VehicleGuard().process(
        sample(
            coolant_temperature=120.0,
            battery_voltage=10.9,
            oil_pressure=69.9,
            engine_rpm=7500,
            brake_pad_remaining=5.0,
        )
    )

    assert len(result.events) == 5
    assert len(result.warnings) == 5
    assert {warning.parameter for warning in result.warnings} == {event.parameter for event in result.events}


def test_tc_sys_004_invalid_input_protection_end_to_end():
    """TC-SYS-004"""
    result = VehicleGuard().process(sample_mapping(engine_rpm="high"))

    assert result.validated_data is None
    assert result.parameter_conditions == []
    assert result.classified_conditions == []
    assert result.warnings == []
    assert result.events[0].event_type == "INVALID_INPUT"
    assert result.events[0].severity is None


def test_deterministic_simulator_scenarios_are_isolated():
    results = run_scenarios()

    assert results["normal_operation"]["events"] == []
    assert results["engine_stopped_with_low_oil_pressure"]["events"] == []
    assert not any(
        event["event_type"] == "RECOVERY"
        for scenario in results.values()
        for event in scenario["events"]
    )
