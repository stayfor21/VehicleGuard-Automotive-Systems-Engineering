import json
from copy import deepcopy
from pathlib import Path

import pytest

from prototype.config_loader import ConfigurationError, load_config, parse_config
from prototype.diagnostics import VehicleGuard
from prototype.models import Severity

from .helpers import sample, severity_for


def test_tc_cfg_001_supported_input_range_is_loaded_from_json():
    """TC-CFG-001"""
    config = load_config()
    guard = VehicleGuard(config)

    assert config.parameters["coolant_temperature"].supported_min == -40.0
    assert guard.process(sample(coolant_temperature=-40.0)).validation_issues == []
    assert guard.process(sample(coolant_temperature=-40.1)).validation_issues


def test_tc_cfg_002_diagnostic_threshold_change_follows_configuration(tmp_path):
    """TC-CFG-002"""
    source = json.loads(Path("prototype/config/vehicleguard-v1.json").read_text(encoding="utf-8"))
    modified = deepcopy(source)
    coolant_conditions = modified["parameters"]["coolant_temperature"]["conditions"]
    coolant_conditions[1]["rules"][0]["value"] = 100.0
    coolant_conditions[2]["rules"][0]["value"] = 100.0

    config_path = tmp_path / "vehicleguard-v1-modified.json"
    config_path.write_text(json.dumps(modified), encoding="utf-8")

    default_result = VehicleGuard(load_config()).process(sample(coolant_temperature=105.0))
    modified_result = VehicleGuard(load_config(config_path)).process(sample(coolant_temperature=105.0))

    assert severity_for(default_result, "coolant_temperature") is Severity.NORMAL
    assert severity_for(modified_result, "coolant_temperature") is Severity.WARNING


def test_tc_cfg_003_parameter_configuration_independence():
    """TC-CFG-003"""
    source = json.loads(Path("prototype/config/vehicleguard-v1.json").read_text(encoding="utf-8"))
    modified = deepcopy(source)
    coolant_conditions = modified["parameters"]["coolant_temperature"]["conditions"]
    coolant_conditions[1]["rules"][0]["value"] = 100.0
    coolant_conditions[2]["rules"][0]["value"] = 100.0

    result = VehicleGuard(parse_config(modified)).process(
        sample(coolant_temperature=105.0, engine_rpm=6499)
    )

    assert severity_for(result, "coolant_temperature") is Severity.WARNING
    assert severity_for(result, "engine_rpm") is Severity.NORMAL


def test_configuration_loader_fails_clearly_on_missing_structure():
    broken = {"version": "broken"}

    with pytest.raises(ConfigurationError):
        parse_config(broken)


def test_diagnostic_thresholds_are_not_independently_hardcoded_in_diagnostics_py():
    source = Path("prototype/diagnostics.py").read_text(encoding="utf-8")

    for threshold in ["109.9", "110.0", "120.0", "70.0", "150.0", "6500", "7500"]:
        assert threshold not in source
