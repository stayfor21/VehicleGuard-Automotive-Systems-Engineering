from prototype.diagnostics import VehicleGuard

from .helpers import sample


def test_tc_inp_001_complete_vehicle_data_sample_is_received_and_validated():
    """TC-INP-001"""
    result = VehicleGuard().process(sample())

    assert result.received_data.values["coolant_temperature"] == 90.0
    assert result.received_data.values["battery_voltage"] == 13.8
    assert result.received_data.values["oil_pressure"] == 350.0
    assert result.received_data.values["engine_rpm"] == 2000
    assert result.received_data.values["brake_pad_remaining"] == 80.0
    assert result.validated_data is not None
    assert result.validation_issues == []


def test_tc_inp_002_timestamp_is_preserved_in_outputs():
    """TC-INP-002"""
    result = VehicleGuard().process(sample(timestamp=25.5, coolant_temperature=120.0))

    assert result.events
    assert all(event.timestamp == 25.5 for event in result.events)
    assert all(warning.timestamp == 25.5 for warning in result.warnings)
