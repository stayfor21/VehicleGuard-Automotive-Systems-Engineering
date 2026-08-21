from prototype.diagnostics import VehicleGuard
from prototype.models import Severity

from .helpers import event_for, sample, sample_mapping


def test_tc_evt_001_abnormal_condition_generates_structured_diagnostic_event():
    """TC-EVT-001"""
    result = VehicleGuard().process(sample(timestamp=42.0, coolant_temperature=120.0))
    event = event_for(result, "coolant_temperature")

    assert event.timestamp == 42.0
    assert event.condition_id == "COOLANT_TEMPERATURE_CRITICAL_HIGH"
    assert event.parameter == "coolant_temperature"
    assert event.observed_value == 120.0
    assert event.severity is Severity.CRITICAL
    assert event.event_type == "ABNORMAL_CONDITION"


def test_tc_evt_002_invalid_input_event_is_distinct_from_vehicle_condition():
    """TC-EVT-002"""
    result = VehicleGuard().process(sample_mapping(engine_rpm="high"))

    assert result.classified_conditions == []
    assert result.events[0].event_type == "INVALID_INPUT"
    assert result.events[0].severity is None
    assert result.events[0].parameter == "engine_rpm"
