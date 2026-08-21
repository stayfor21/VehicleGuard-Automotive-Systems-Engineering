from prototype.diagnostics import VehicleGuard
from prototype.models import Severity

from .helpers import sample, severity_for


def test_tc_sev_001_normal_classification():
    """TC-SEV-001"""
    result = VehicleGuard().process(sample())

    assert severity_for(result, "coolant_temperature") is Severity.NORMAL


def test_tc_sev_002_info_classification():
    """TC-SEV-002"""
    result = VehicleGuard().process(sample(brake_pad_remaining=25.0))

    assert severity_for(result, "brake_pad_remaining") is Severity.INFO


def test_tc_sev_003_warning_classification():
    """TC-SEV-003"""
    result = VehicleGuard().process(sample(coolant_temperature=110.0))

    assert severity_for(result, "coolant_temperature") is Severity.WARNING


def test_tc_sev_004_critical_classification():
    """TC-SEV-004"""
    result = VehicleGuard().process(sample(engine_rpm=7500))

    assert severity_for(result, "engine_rpm") is Severity.CRITICAL


def test_tc_sev_005_independent_severity_classification():
    """TC-SEV-005"""
    result = VehicleGuard().process(
        sample(
            coolant_temperature=110.0,
            battery_voltage=10.9,
            brake_pad_remaining=25.0,
        )
    )

    assert severity_for(result, "coolant_temperature") is Severity.WARNING
    assert severity_for(result, "battery_voltage") is Severity.CRITICAL
    assert severity_for(result, "brake_pad_remaining") is Severity.INFO
