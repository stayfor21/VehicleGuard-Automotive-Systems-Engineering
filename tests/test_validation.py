import pytest

from prototype.diagnostics import VehicleGuard
from prototype.models import ValidationIssueType

from .helpers import sample, sample_mapping


def test_tc_val_001_valid_vehicle_data_is_accepted():
    """TC-VAL-001"""
    result = VehicleGuard().process(sample())

    assert result.validated_data is not None
    assert result.validation_issues == []


def test_tc_val_002_missing_required_parameter_is_invalid_and_not_processed():
    """TC-VAL-002"""
    data = sample_mapping()
    data.pop("oil_pressure")

    result = VehicleGuard().process(data)

    assert result.validated_data is None
    assert result.validation_issues[0].parameter == "oil_pressure"
    assert result.validation_issues[0].issue_type is ValidationIssueType.MISSING_REQUIRED_INPUT
    assert result.parameter_conditions == []
    assert result.events[0].event_type == "INVALID_INPUT"
    assert result.events[0].severity is None


def test_tc_val_003_unsupported_data_type_is_invalid():
    """TC-VAL-003"""
    result = VehicleGuard().process(sample_mapping(engine_rpm="high"))

    assert result.validated_data is None
    assert result.validation_issues[0].parameter == "engine_rpm"
    assert result.validation_issues[0].issue_type is ValidationIssueType.UNSUPPORTED_DATA_TYPE


def test_tc_val_004_value_below_supported_range_is_invalid_not_low_voltage_fault():
    """TC-VAL-004"""
    result = VehicleGuard().process(sample(battery_voltage=-0.1))

    assert result.validated_data is None
    assert result.validation_issues[0].issue_type is ValidationIssueType.VALUE_BELOW_SUPPORTED_RANGE
    assert result.classified_conditions == []
    assert result.events[0].severity is None


def test_tc_val_005_value_above_supported_range_is_invalid():
    """TC-VAL-005"""
    result = VehicleGuard().process(sample(brake_pad_remaining=100.1))

    assert result.validated_data is None
    assert result.validation_issues[0].parameter == "brake_pad_remaining"
    assert result.validation_issues[0].issue_type is ValidationIssueType.VALUE_ABOVE_SUPPORTED_RANGE


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("timestamp", 0.0),
        ("coolant_temperature", -40.0),
        ("coolant_temperature", 150.0),
        ("battery_voltage", 0.0),
        ("battery_voltage", 20.0),
        ("oil_pressure", 0.0),
        ("oil_pressure", 1000.0),
        ("engine_rpm", 0),
        ("engine_rpm", 10000),
        ("brake_pad_remaining", 0.0),
        ("brake_pad_remaining", 100.0),
    ],
)
def test_tc_val_006_supported_range_boundaries_are_inclusive(field, value):
    """TC-VAL-006"""
    result = VehicleGuard().process(sample(**{field: value}))

    assert result.validation_issues == []
    assert result.validated_data is not None


@pytest.mark.parametrize(
    ("field", "value", "issue_type"),
    [
        ("timestamp", -0.1, ValidationIssueType.VALUE_BELOW_SUPPORTED_RANGE),
        ("coolant_temperature", -40.1, ValidationIssueType.VALUE_BELOW_SUPPORTED_RANGE),
        ("coolant_temperature", 150.1, ValidationIssueType.VALUE_ABOVE_SUPPORTED_RANGE),
        ("battery_voltage", -0.1, ValidationIssueType.VALUE_BELOW_SUPPORTED_RANGE),
        ("battery_voltage", 20.1, ValidationIssueType.VALUE_ABOVE_SUPPORTED_RANGE),
        ("oil_pressure", -0.1, ValidationIssueType.VALUE_BELOW_SUPPORTED_RANGE),
        ("oil_pressure", 1000.1, ValidationIssueType.VALUE_ABOVE_SUPPORTED_RANGE),
        ("engine_rpm", -1, ValidationIssueType.VALUE_BELOW_SUPPORTED_RANGE),
        ("engine_rpm", 10001, ValidationIssueType.VALUE_ABOVE_SUPPORTED_RANGE),
        ("brake_pad_remaining", -0.1, ValidationIssueType.VALUE_BELOW_SUPPORTED_RANGE),
        ("brake_pad_remaining", 100.1, ValidationIssueType.VALUE_ABOVE_SUPPORTED_RANGE),
    ],
)
def test_supported_input_values_immediately_outside_boundaries_are_invalid(field, value, issue_type):
    result = VehicleGuard().process(sample(**{field: value}))

    assert result.validated_data is None
    assert result.validation_issues[0].parameter == field
    assert result.validation_issues[0].issue_type is issue_type
