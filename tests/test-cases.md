# VehicleGuard Test Cases

## 1. Purpose

This document defines the planned verification test cases for VehicleGuard V1.

The test cases are derived from the system requirements, architecture, interface specification, and system risk analysis.

The purpose of this document is to define:

- what behaviour will be tested;
- which requirements are covered by each test;
- required test preconditions;
- controlled test inputs;
- expected system behaviour;
- acceptance criteria for determining PASS or FAIL.

At the current project stage, the test cases are defined before prototype verification has been executed.

Therefore:

```text
Actual Result: NOT RUN
Status: NOT RUN
Evidence: TBD
```

These fields will only be updated after the corresponding test has been executed against the VehicleGuard prototype.

---

## 2. Test Approach

VehicleGuard uses requirement-based testing.

The basic relationship is:

```text
System Requirement
        |
        v
Test Case
        |
        v
Controlled Input
        |
        v
VehicleGuard
        |
        v
Observed Output
        |
        v
Expected vs Actual
        |
        v
PASS / FAIL
```

Test cases are defined from expected system behaviour rather than from the behaviour of the implementation.

This allows the prototype to be evaluated against the specification instead of adapting the expected result to the implemented behaviour.

---

## 3. Test Case Identification

Test cases use the following identifier format:

```text
TC-<CATEGORY>-XXX
```

The following categories are used:

| Prefix | Area |
|---|---|
| `TC-INP` | Input handling |
| `TC-VAL` | Data validation |
| `TC-MON` | Parameter monitoring |
| `TC-DIAG` | Diagnostic processing |
| `TC-SEV` | Severity classification |
| `TC-WRN` | Driver warning generation |
| `TC-EVT` | Diagnostic event generation |
| `TC-CFG` | Configuration behaviour |
| `TC-SYS` | Integrated system behaviour |

Test case identifiers must remain unique.

Existing identifiers should not be reused for unrelated test cases.

---

## 4. Test Status

The following status values are used:

**NOT RUN**

The test case has been defined but has not yet been executed.

**PASS**

The observed behaviour satisfies all acceptance criteria.

**FAIL**

One or more acceptance criteria are not satisfied.

**BLOCKED**

The test cannot currently be executed because a required dependency or implementation is unavailable.

At the current project stage, all executable test cases have the status:

`NOT RUN`

---

# 5. Input Interface Tests

## TC-INP-001 - Complete Vehicle Data Sample

**Related Requirements**

- `SYS-INP-001`
- `SYS-INP-002`
- `SYS-INP-003`
- `SYS-INP-004`
- `SYS-INP-005`
- `SYS-INP-006`

**Related Architecture Element**

`COMP-INP-001`

**Related Interface**

`IF-EXT-001`

### Objective

Verify that VehicleGuard can receive a complete vehicle data sample containing all monitored V1 parameters.

### Preconditions

- VehicleGuard prototype is available.
- The standard V1 input interface is active.

### Test Input

```text
timestamp = 10.0 s
coolant_temperature = 90.0 °C
battery_voltage = 13.8 V
oil_pressure = 350.0 kPa
engine_rpm = 2000 rpm
brake_pad_remaining = 80.0 %
```

### Test Steps

1. Create a `VehicleData` sample containing all required fields.
2. Submit the sample through the VehicleGuard input interface.
3. Observe whether the input is accepted for further processing.

### Expected Result

The complete vehicle data sample is received and made available to the validation function.

### Acceptance Criteria

- all required fields are received;
- field values remain associated with the correct parameters;
- the sample is passed to the validation stage.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-INP-002 - Timestamp Preservation

**Related Requirement**

`SYS-INP-007`

**Related Architecture Element**

`COMP-INP-001`

### Objective

Verify that the timestamp associated with an input sample remains associated with that sample during processing.

### Test Input

```text
timestamp = 25.5 s
```

with otherwise valid vehicle data.

### Test Steps

1. Submit a valid vehicle data sample with timestamp `25.5`.
2. Process the sample.
3. Observe timestamp information in the resulting diagnostic data where applicable.

### Expected Result

The timestamp associated with the processed sample remains `25.5 s`.

### Acceptance Criteria

The resulting information refers to the same timestamp as the originating vehicle data sample.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

# 6. Data Validation Tests

## TC-VAL-001 - Valid Vehicle Data

**Related Requirements**

- `SYS-VAL-001`
- `SYS-VAL-004`

**Related Architecture Element**

`COMP-VAL-001`

### Objective

Verify that vehicle parameter values inside their supported input ranges are accepted as valid.

### Test Input

```text
coolant_temperature = 90.0 °C
battery_voltage = 13.8 V
oil_pressure = 350.0 kPa
engine_rpm = 2000 rpm
brake_pad_remaining = 80.0 %
```

### Expected Result

All supplied parameter values are classified as valid input and are eligible for diagnostic processing.

### Acceptance Criteria

No valid parameter is rejected by the validation function.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-VAL-002 - Missing Required Parameter

**Related Requirements**

- `SYS-VAL-002`
- `SYS-VAL-005`
- `SYS-VAL-006`

**Related Risk Scenario**

`SCN-01`

### Objective

Verify that VehicleGuard detects a missing required parameter.

### Test Input

A `VehicleData` sample without:

```text
oil_pressure
```

All other required parameters contain valid values.

### Expected Result

VehicleGuard identifies the input sample as incomplete.

The missing parameter is not silently interpreted as a valid operating value.

### Acceptance Criteria

- the missing required parameter is detected;
- the incomplete input is distinguishable from an abnormal oil pressure condition;
- no fabricated oil pressure value enters normal diagnostic processing.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-VAL-003 - Incorrect Data Type

**Related Requirements**

- `SYS-VAL-003`
- `SYS-VAL-005`
- `SYS-VAL-006`

### Objective

Verify that a parameter with an unsupported data type is detected.

### Test Input

```text
engine_rpm = "high"
```

instead of an integer value.

### Expected Result

The parameter is rejected as invalid input.

### Acceptance Criteria

The value `"high"` is not processed as a valid engine RPM value.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-VAL-004 - Value Below Supported Range

**Related Requirements**

- `SYS-VAL-004`
- `SYS-VAL-005`
- `SYS-VAL-006`

**Related Risk Scenarios**

- `SCN-01`
- `SCN-03`

### Objective

Verify detection of a numeric value below its configured supported input range.

### Test Input

Using the defined V1 supported range:

```text
battery_voltage = -0.1 V
```

### Expected Result

The value is classified as invalid input.

It is not evaluated as a genuine low-voltage vehicle condition.

### Acceptance Criteria

- validation rejects the value;
- the invalid value does not enter normal monitoring;
- invalid input remains distinguishable from a valid abnormal condition.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-VAL-005 - Value Above Supported Range

**Related Requirements**

- `SYS-VAL-004`
- `SYS-VAL-005`
- `SYS-VAL-006`

### Objective

Verify detection of a numeric value above its configured supported input range.

### Test Input

```text
brake_pad_remaining = 100.1 %
```

### Expected Result

The value is classified as invalid input.

### Acceptance Criteria

The value does not enter normal diagnostic processing as valid brake data.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-VAL-006 - Supported Range Boundary

**Related Requirements**

- `SYS-VAL-001`
- `SYS-VAL-004`

### Objective

Verify correct handling of values exactly at supported input boundaries.

### Test Inputs

Examples:

```text
coolant_temperature = -40.0 °C
coolant_temperature = 150.0 °C

engine_rpm = 0 rpm
engine_rpm = 10000 rpm

brake_pad_remaining = 0.0 %
brake_pad_remaining = 100.0 %
```

### Expected Result

Values exactly equal to defined inclusive supported boundaries are accepted as valid input.

### Acceptance Criteria

Each boundary value is processed according to:

```text
supported_min <= value <= supported_max
```

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

# 7. Monitoring Tests

## TC-MON-001 - Monitor All Configured Parameters

**Related Requirements**

- `SYS-MON-001`
- `SYS-MON-002`
- `SYS-MON-003`
- `SYS-MON-004`
- `SYS-MON-005`
- `SYS-MON-006`

**Related Architecture Element**

`COMP-MON-001`

### Objective

Verify that all configured V1 vehicle parameters are evaluated by the monitoring function.

### Test Input

A complete valid `VehicleData` sample containing:

```text
coolant_temperature
battery_voltage
oil_pressure
engine_rpm
brake_pad_remaining
```

### Expected Result

Each configured parameter is evaluated using its applicable monitoring criteria.

### Acceptance Criteria

No configured monitored parameter is omitted from processing.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-MON-002 - Diagnostic Threshold Boundary

**Related Requirements**

- `SYS-MON-001`
- applicable `SYS-MON-xxx`
- `SYS-DIAG-001`

**Related Risk Scenario**

`SCN-04`

### Objective

Verify correct monitoring behaviour around a configured diagnostic threshold.

### Test Input

For a configured threshold `X`:

```text
X - Δ
X
X + Δ
```

The actual values will be taken from the active V1 test configuration.

### Expected Result

Each value is classified according to the comparison rule defined by the active configuration.

### Acceptance Criteria

No off-by-one or incorrect comparison behaviour occurs at the configured threshold.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

# 8. Diagnostic Processing Tests

## TC-DIAG-001 - Normal Condition

**Related Requirement**

`SYS-DIAG-002`

**Related Architecture Element**

`COMP-DIAG-001`

### Objective

Verify that a valid parameter that does not satisfy any configured abnormal condition is identified as normal.

### Test Input

A valid parameter value within the configured normal operating condition.

### Expected Result

No abnormal diagnostic condition is reported for the parameter.

### Acceptance Criteria

The parameter is identified as normal according to the active configuration.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-DIAG-002 - Abnormal Condition Detection

**Related Requirements**

- `SYS-DIAG-001`
- `SYS-DIAG-003`

### Objective

Verify that VehicleGuard detects a configured abnormal operating condition and identifies the affected parameter.

### Test Input

A valid parameter value satisfying a configured abnormal condition.

### Expected Result

VehicleGuard detects the abnormal condition and identifies the parameter responsible for it.

### Acceptance Criteria

- abnormal condition is detected;
- correct parameter is identified;
- a valid condition identifier is associated with the detected condition.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-DIAG-003 - Multiple Simultaneous Abnormal Conditions

**Related Requirement**

`SYS-DIAG-004`

### Objective

Verify that VehicleGuard can detect multiple abnormal conditions within one vehicle data sample.

### Test Input

A sample containing at least two valid parameters that simultaneously satisfy configured abnormal conditions.

### Expected Result

VehicleGuard detects each abnormal condition independently.

### Acceptance Criteria

- both conditions are detected;
- each condition identifies the correct parameter;
- one condition does not suppress the other.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-DIAG-004 - Recovery to Normal

**Related Requirement**

`SYS-DIAG-005`

### Objective

Verify that VehicleGuard recognizes recovery from an abnormal condition.

### Test Sequence

```text
Sample 1 - Normal
Sample 2 - Abnormal
Sample 3 - Normal
```

### Expected Result

The condition is detected during Sample 2 and is no longer treated as active after Sample 3 has been processed.

### Acceptance Criteria

The previous abnormal state does not remain active after valid recovery to the configured normal condition.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

# 9. Severity Classification Tests

## TC-SEV-001 - NORMAL Classification

**Related Requirements**

- `SYS-SEV-002`
- `SYS-SEV-003`

**Related Architecture Element**

`COMP-SEV-001`

### Objective

Verify assignment of `NORMAL` to a valid condition that does not satisfy abnormal severity criteria.

### Expected Result

```text
severity = NORMAL
```

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-SEV-002 - INFO Classification

**Related Requirements**

- `SYS-SEV-001`
- `SYS-SEV-002`
- `SYS-SEV-004`

### Objective

Verify assignment of `INFO` when the active configuration defines the detected condition at INFO level.

### Expected Result

```text
severity = INFO
```

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-SEV-003 - WARNING Classification

**Related Requirements**

- `SYS-SEV-001`
- `SYS-SEV-002`
- `SYS-SEV-004`

### Objective

Verify assignment of `WARNING` for a condition configured at WARNING severity.

### Expected Result

```text
severity = WARNING
```

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-SEV-004 - CRITICAL Classification

**Related Requirements**

- `SYS-SEV-001`
- `SYS-SEV-002`
- `SYS-SEV-004`

**Related Risk Scenario**

`SCN-05`

### Objective

Verify assignment of `CRITICAL` for a condition configured at CRITICAL severity.

### Expected Result

```text
severity = CRITICAL
```

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-SEV-005 - Independent Severity Classification

**Related Requirement**

`SYS-SEV-005`

### Objective

Verify that multiple detected conditions are classified independently.

### Test Input

A vehicle data sample containing multiple abnormal conditions configured with different severity levels.

### Expected Result

Each condition receives the severity defined by its own configuration criteria.

### Acceptance Criteria

The severity assigned to one condition does not incorrectly determine the severity of another condition.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

# 10. Driver Warning Tests

## TC-WRN-001 - WARNING Generates Driver Warning

**Related Requirements**

- `SYS-WRN-001`
- `SYS-WRN-002`
- `SYS-WRN-003`
- `SYS-WRN-004`

**Related Architecture Element**

`COMP-WRN-001`

### Objective

Verify generation of driver warning information for a `WARNING` condition.

### Expected Result

A `DriverWarning` is generated containing:

- condition identifier;
- affected parameter;
- severity `WARNING`;
- driver-oriented message;
- associated timestamp.

### Acceptance Criteria

All required warning information is present and associated with the correct condition.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-WRN-002 - CRITICAL Generates Driver Warning

**Related Requirement**

`SYS-WRN-001`

### Objective

Verify generation of driver warning information for a `CRITICAL` condition.

### Expected Result

A driver warning is generated for the detected critical condition.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-WRN-003 - NORMAL Does Not Generate Abnormal Warning

**Related Requirement**

`SYS-WRN-005`

### Objective

Verify that a parameter classified as `NORMAL` does not generate an active abnormal-condition warning.

### Expected Result

No active abnormal-condition `DriverWarning` is generated.

### Acceptance Criteria

Normal system behaviour does not produce a false warning.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

# 11. Diagnostic Event Tests

## TC-EVT-001 - Diagnostic Event Generation

**Related Requirements**

- `SYS-EVT-001`
- `SYS-EVT-002`
- `SYS-EVT-003`
- `SYS-EVT-004`
- `SYS-EVT-005`
- `SYS-EVT-006`

**Related Architecture Element**

`COMP-EVT-001`

### Objective

Verify that a detected abnormal condition generates a structured diagnostic event.

### Expected Result

A `DiagnosticEvent` is generated containing:

```text
timestamp
condition_id
parameter
observed_value
severity
event_type
```

### Acceptance Criteria

- required event fields are present;
- values correspond to the originating detected condition;
- severity matches the classified condition;
- timestamp corresponds to the processed sample.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-EVT-002 - Invalid Input Diagnostic Event

**Related Requirement**

`SYS-EVT-007`

### Objective

Verify that invalid input can be represented separately from an abnormal vehicle operating condition.

### Test Input

An intentionally invalid vehicle parameter value.

### Expected Result

Diagnostic information identifies an invalid input condition.

It is distinguishable from a genuine abnormal vehicle condition.

### Acceptance Criteria

The resulting event does not incorrectly represent the invalid input as a real vehicle operating fault.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

# 12. Configuration Tests

## TC-CFG-001 - Configuration-Based Input Range

**Related Requirements**

- `SYS-CFG-001`
- `SYS-CFG-002`
- `SYS-CFG-003`

**Related Architecture Element**

`COMP-CFG-001`

### Objective

Verify that supported input ranges are obtained from the active parameter configuration.

### Test Approach

1. Define a known supported range for a selected parameter.
2. Provide a value inside the range.
3. Provide a value outside the range.
4. Compare validation behaviour.

### Expected Result

Validation behaviour follows the active configuration.

### Acceptance Criteria

The configured supported range determines whether the value is accepted as valid input.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-CFG-002 - Configuration-Based Diagnostic Threshold

**Related Requirements**

- `SYS-CFG-001`
- `SYS-CFG-002`
- `SYS-CFG-004`

**Related Risk Scenario**

`SCN-02`

### Objective

Verify that diagnostic behaviour follows the configured monitoring and severity criteria.

### Test Approach

1. Define threshold configuration `A`.
2. Process a controlled input value.
3. Record the expected classification.
4. Change the applicable threshold to configuration `B`.
5. Process the same input value again.

### Expected Result

The resulting condition or severity changes according to the active configuration where the changed threshold affects the input.

### Acceptance Criteria

Diagnostic behaviour can be changed through configuration without changing the diagnostic processing implementation.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-CFG-003 - Parameter Configuration Independence

**Related Requirements**

- `SYS-CFG-002`
- `SYS-CFG-005`

### Objective

Verify that configuration associated with one monitored parameter does not incorrectly modify another parameter's diagnostic behaviour.

### Test Approach

1. Establish a known configuration for two monitored parameters.
2. Change the configuration of only one parameter.
3. Process controlled input data.
4. Compare the behaviour of both parameters.

### Expected Result

Only behaviour associated with the modified configuration is affected.

### Acceptance Criteria

Configuration remains correctly associated with the intended parameter.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

# 13. Integrated System Tests

## TC-SYS-001 - Normal Vehicle Data Processing

**Related Requirements**

Multiple requirements across input, validation, monitoring, diagnostics, severity, warning, and event processing.

### Objective

Verify end-to-end VehicleGuard behaviour for a complete valid sample representing normal operating conditions.

### Test Input

A complete `VehicleData` sample in which all monitored values satisfy the active normal operating criteria.

### Expected Result

```text
Input accepted
      |
      v
Validation successful
      |
      v
Parameters monitored
      |
      v
No abnormal conditions detected
      |
      v
Severity = NORMAL
      |
      v
No abnormal driver warning
```

### Acceptance Criteria

The complete processing chain handles the sample without generating a false abnormal-condition warning.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-SYS-002 - Single Abnormal Condition

### Objective

Verify end-to-end behaviour when one monitored parameter satisfies an abnormal condition.

### Test Input

A complete valid sample containing one parameter value configured to produce an abnormal condition.

### Expected Result

VehicleGuard:

1. accepts the sample;
2. validates the input;
3. detects the abnormal parameter;
4. creates the correct diagnostic condition;
5. assigns the configured severity;
6. generates the required driver warning where applicable;
7. generates the required diagnostic event.

### Acceptance Criteria

All outputs correspond to the same originating condition and input sample.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-SYS-003 - Multiple Abnormal Conditions

### Objective

Verify end-to-end behaviour when multiple abnormal conditions occur within one vehicle data sample.

### Expected Result

Each condition is independently:

- detected;
- identified;
- classified;
- represented in diagnostic output;
- represented in driver warning output where required.

### Acceptance Criteria

No valid detected condition is lost because another condition is processed simultaneously.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

## TC-SYS-004 - Invalid Input Protection

**Related Risk Scenarios**

- `SCN-01`
- `SCN-03`

### Objective

Verify end-to-end protection against invalid vehicle data.

### Expected Result

```text
Invalid VehicleData
        |
        v
Validation detects problem
        |
        +-> Invalid input information
        |
        X
Normal diagnostic processing
```

### Acceptance Criteria

Invalid data does not produce a normal diagnostic evaluation based on the invalid value.

**Actual Result:** `NOT RUN`

**Status:** `NOT RUN`

**Evidence:** `TBD`

---

# 14. Planned Boundary Test Expansion

The initial test cases define the verification structure.

During prototype implementation, parameter-specific boundary cases will be expanded using the actual active V1 configuration.

For each applicable diagnostic threshold `X`, the planned pattern is:

```text
X - Δ
X
X + Δ
```

For supported input ranges:

```text
minimum - Δ
minimum
minimum + Δ

maximum - Δ
maximum
maximum + Δ
```

These cases will be assigned individual test identifiers where separate execution evidence is required.

No expected result will be derived from undocumented assumptions.

The active configuration used during the test will determine the expected boundary behaviour.

---

# 15. Test Evidence

Test evidence does not currently exist because prototype verification has not yet been executed.

After execution, evidence may include:

- automated test output;
- structured result records;
- execution logs;
- expected and actual value comparisons;
- test report entries.

Evidence identifiers will follow the project convention:

```text
RESULT-xxx
```

Evidence identifiers will only be assigned to actual verification evidence.

They will not be created for tests that have not been executed.

---

# 16. Current Test Status

The current test specification status is:

`Defined - Execution Pending`

At the current project stage:

- test objectives are defined;
- requirement relationships are identified;
- controlled test inputs are partially defined;
- expected behaviour is defined;
- acceptance criteria are defined;
- prototype execution has not yet been performed;
- actual results are not available;
- PASS / FAIL status has not been assigned;
- verification evidence has not yet been generated.

All executable test cases therefore remain:

```text
Status: NOT RUN
```

until the corresponding VehicleGuard implementation is available and the test has been executed.

---

# 17. Next Test Activities

After the VehicleGuard prototype has been implemented, the following activities will be performed:

1. review test cases against the final active V1 configuration;
2. finalize parameter-specific boundary values;
3. implement automated tests where appropriate;
4. execute the defined test cases;
5. record actual results;
6. assign `PASS`, `FAIL`, or `BLOCKED`;
7. generate verification evidence;
8. update the Requirements Verification Matrix;
9. investigate failed tests;
10. re-test corrected behaviour where required.

The final execution results will be summarized in:

`tests/test-report.md`

Until execution occurs, `test-cases.md` remains the VehicleGuard V1 test specification rather than evidence of successful verification.
