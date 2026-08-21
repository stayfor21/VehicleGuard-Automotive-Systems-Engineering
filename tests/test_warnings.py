from prototype.diagnostics import VehicleGuard
from prototype.models import Severity

from .helpers import sample, warning_for


def test_tc_wrn_001_warning_condition_generates_driver_warning():
    """TC-WRN-001"""
    result = VehicleGuard().process(sample(coolant_temperature=110.0))
    warning = warning_for(result, "coolant_temperature")

    assert warning.condition_id == "COOLANT_TEMPERATURE_WARNING_HIGH"
    assert warning.severity is Severity.WARNING
    assert warning.message == "Coolant temperature high."


def test_tc_wrn_002_critical_condition_generates_driver_warning():
    """TC-WRN-002"""
    result = VehicleGuard().process(sample(coolant_temperature=120.0))
    warning = warning_for(result, "coolant_temperature")

    assert warning.severity is Severity.CRITICAL


def test_tc_wrn_003_normal_condition_does_not_generate_abnormal_warning():
    """TC-WRN-003"""
    result = VehicleGuard().process(sample())

    assert result.warnings == []


def test_info_condition_generates_event_but_not_driver_warning():
    result = VehicleGuard().process(sample(brake_pad_remaining=25.0))

    assert result.events[0].severity is Severity.INFO
    assert result.warnings == []
