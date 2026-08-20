# VehicleGuard V1 Configuration Specification

## 1. Purpose

This document defines the baseline parameter configuration used by the VehicleGuard V1 engineering prototype.

The configuration provides controlled values for:

- supported input ranges;
- diagnostic monitoring criteria;
- severity classification;
- boundary behaviour;
- parameter-specific diagnostic rules.

The purpose of separating these values from the diagnostic implementation is to ensure that configurable engineering criteria are not hard-coded into the processing logic.

The configuration defined here will later be represented in machine-readable form in:

```text
prototype/config/vehicleguard-v1.json
```

---

## 2. Configuration Scope

VehicleGuard V1 monitors the following vehicle parameters:

| Parameter | Configuration ID | Unit | Data Type |
|---|---|---|---|
| Coolant Temperature | `CFG-COOLANT` | °C | float |
| Battery Voltage | `CFG-BATTERY` | V | float |
| Oil Pressure | `CFG-OIL` | kPa | float |
| Engine RPM | `CFG-RPM` | rpm | integer |
| Brake Pad Remaining | `CFG-BRAKE` | % | float |

These parameters correspond to the initial VehicleGuard V1 scope.

Adding another monitored parameter after the V1 configuration baseline has been established should be evaluated through the project change management process.

---

## 3. Important Engineering Limitation

The values defined in this document are **VehicleGuard V1 demonstration values**.

They are used to provide deterministic and testable behaviour for the engineering prototype.

They must not be interpreted as:

- universal automotive limits;
- OEM calibration values;
- service specifications for a particular vehicle;
- safety-certified thresholds;
- diagnostic thresholds suitable for production vehicles.

Real automotive thresholds depend on the vehicle, engine, operating state, sensor characteristics, ECU calibration, environmental conditions, and manufacturer requirements.

VehicleGuard V1 intentionally uses a simplified configuration so that the systems engineering concept can be implemented and verified in a controlled environment.

---

## 4. Severity Levels

VehicleGuard V1 uses four severity levels.

| Severity | Meaning |
|---|---|
| `NORMAL` | Parameter does not satisfy an abnormal diagnostic condition. |
| `INFO` | Condition should be recorded or communicated but does not currently represent a significant abnormal state. |
| `WARNING` | Abnormal condition requires driver or diagnostic attention. |
| `CRITICAL` | Severe abnormal condition requiring immediate attention within the demonstration model. |

Severity is assigned only after the input has passed validation.

Invalid input is not classified as a genuine vehicle operating condition.

Therefore:

```text
Invalid Input != CRITICAL Vehicle Condition
```

Invalid input is handled separately by the validation and diagnostic event functions.

---

## 5. Processing Order

Configuration values are applied according to the VehicleGuard processing sequence:

```text
Vehicle Data
     |
     v
Input Validation
     |
     | valid
     v
Parameter Monitoring
     |
     v
Condition Detection
     |
     v
Severity Classification
     |
     +----------------+
     |                |
     v                v
Driver Warning   Diagnostic Event
```

If a value fails input validation, normal diagnostic threshold evaluation for that value is not performed.

---

# 6. Coolant Temperature

## 6.1 Parameter Definition

| Property | Value |
|---|---|
| Configuration ID | `CFG-COOLANT` |
| Parameter | `coolant_temperature` |
| Unit | °C |
| Data Type | float |
| Supported Minimum | -40.0 °C |
| Supported Maximum | 150.0 °C |

The supported input range defines values that the V1 prototype is able to accept as technically valid input.

A supported value is not necessarily a normal operating value.

---

## 6.2 Diagnostic Criteria

VehicleGuard V1 uses the following demonstration criteria:

| Coolant Temperature | Classification |
|---:|---|
| `< 110.0 °C` | `NORMAL` |
| `>= 110.0 °C and < 120.0 °C` | `WARNING` |
| `>= 120.0 °C` | `CRITICAL` |

Values outside the supported input range are classified as invalid input before diagnostic evaluation.

---

## 6.3 Boundary Behaviour

The important diagnostic boundaries are:

```text
110.0 °C
120.0 °C
```

Planned boundary verification should therefore include values immediately below, exactly at, and immediately above each boundary.

Example:

```text
109.9 °C
110.0 °C
110.1 °C

119.9 °C
120.0 °C
120.1 °C
```

Expected classifications:

```text
109.9 °C -> NORMAL
110.0 °C -> WARNING
110.1 °C -> WARNING

119.9 °C -> WARNING
120.0 °C -> CRITICAL
120.1 °C -> CRITICAL
```

---

## 6.4 Engineering Rationale

Coolant temperature is used as a simple example of a parameter where increasing values can represent increasing diagnostic severity.

The V1 model intentionally uses two upper thresholds to demonstrate transition between:

```text
NORMAL
  |
  v
WARNING
  |
  v
CRITICAL
```

The thresholds are demonstration values and are not intended to represent a specific engine or vehicle.

---

# 7. Battery Voltage

## 7.1 Parameter Definition

| Property | Value |
|---|---|
| Configuration ID | `CFG-BATTERY` |
| Parameter | `battery_voltage` |
| Unit | V |
| Data Type | float |
| Supported Minimum | 0.0 V |
| Supported Maximum | 20.0 V |

---

## 7.2 Operating Assumption

Battery voltage depends strongly on vehicle operating state.

A stationary vehicle with the engine off and a vehicle with an active charging system cannot be evaluated using exactly the same interpretation.

VehicleGuard V1 does not currently model a complete ignition and charging-system state machine.

For this reason, battery voltage monitoring uses a simplified demonstration assumption:

```text
Engine running:
engine_rpm > 0
```

The diagnostic thresholds below apply when:

```text
engine_rpm > 0
```

---

## 7.3 Diagnostic Criteria

| Battery Voltage | Classification |
|---:|---|
| `< 11.0 V` | `CRITICAL` |
| `>= 11.0 V and < 12.0 V` | `WARNING` |
| `>= 12.0 V and <= 15.0 V` | `NORMAL` |
| `> 15.0 V and <= 16.0 V` | `WARNING` |
| `> 16.0 V` | `CRITICAL` |

These criteria are evaluated only for values inside the supported input range.

---

## 7.4 Boundary Behaviour

Important boundaries are:

```text
11.0 V
12.0 V
15.0 V
16.0 V
```

Representative boundary tests should include:

```text
10.9 / 11.0 / 11.1 V
11.9 / 12.0 / 12.1 V
14.9 / 15.0 / 15.1 V
15.9 / 16.0 / 16.1 V
```

---

## 7.5 Engineering Rationale

Battery voltage demonstrates a parameter with both lower and upper abnormal conditions.

This allows VehicleGuard to verify behaviour such as:

```text
CRITICAL LOW
     |
     v
WARNING LOW
     |
     v
NORMAL
     |
     v
WARNING HIGH
     |
     v
CRITICAL HIGH
```

The values are intentionally simplified and must not be treated as production charging-system specifications.

---

# 8. Oil Pressure

## 8.1 Parameter Definition

| Property | Value |
|---|---|
| Configuration ID | `CFG-OIL` |
| Parameter | `oil_pressure` |
| Unit | kPa |
| Data Type | float |
| Supported Minimum | 0.0 kPa |
| Supported Maximum | 1000.0 kPa |

---

## 8.2 Context-Dependent Monitoring

Oil pressure should not be evaluated independently from engine operating state.

A simple rule such as:

```text
oil_pressure < X
```

would produce misleading diagnostic behaviour when the engine is not running.

VehicleGuard V1 therefore uses engine RPM as a monitoring condition.

The first decision is:

```text
engine_rpm == 0
        |
        v
Oil pressure diagnostic evaluation inactive
```

When:

```text
engine_rpm > 0
```

oil pressure evaluation becomes active.

---

## 8.3 Diagnostic Criteria

For the V1 demonstration configuration:

| Condition | Classification |
|---|---|
| `engine_rpm == 0` | Oil pressure monitoring inactive |
| `engine_rpm > 0` and `oil_pressure < 70.0 kPa` | `CRITICAL` |
| `engine_rpm > 0` and `oil_pressure >= 70.0 kPa and < 150.0 kPa` | `WARNING` |
| `engine_rpm > 0` and `oil_pressure >= 150.0 kPa` | `NORMAL` |

---

## 8.4 Boundary Behaviour

The primary oil pressure boundaries are:

```text
70.0 kPa
150.0 kPa
```

Representative tests include:

```text
69.9 kPa
70.0 kPa
70.1 kPa

149.9 kPa
150.0 kPa
150.1 kPa
```

These tests must be performed with:

```text
engine_rpm > 0
```

A separate test must verify that low oil pressure does not generate an oil-pressure operating fault when:

```text
engine_rpm == 0
```

---

## 8.5 Engineering Rationale

Oil pressure demonstrates a context-dependent diagnostic rule.

The parameter is intentionally evaluated together with engine RPM to show that VehicleGuard diagnostic behaviour can depend on more than one input.

The V1 rule remains simplified.

Production oil pressure evaluation may depend on:

- engine speed;
- oil temperature;
- engine temperature;
- engine load;
- engine design;
- sensor characteristics;
- manufacturer calibration.

These dependencies are outside the V1 prototype scope.

---

# 9. Engine RPM

## 9.1 Parameter Definition

| Property | Value |
|---|---|
| Configuration ID | `CFG-RPM` |
| Parameter | `engine_rpm` |
| Unit | rpm |
| Data Type | integer |
| Supported Minimum | 0 rpm |
| Supported Maximum | 10000 rpm |

---

## 9.2 Diagnostic Criteria

VehicleGuard V1 uses the following simplified engine speed criteria:

| Engine RPM | Classification |
|---:|---|
| `0 - 6499 rpm` | `NORMAL` |
| `6500 - 7499 rpm` | `WARNING` |
| `>= 7500 rpm` | `CRITICAL` |

Values above the supported maximum are treated as invalid input rather than as a genuine engine overspeed condition.

---

## 9.3 Boundary Behaviour

Important boundaries are:

```text
6500 rpm
7500 rpm
```

Representative boundary tests include:

```text
6499 rpm
6500 rpm
6501 rpm

7499 rpm
7500 rpm
7501 rpm
```

---

## 9.4 Engineering Rationale

Engine RPM provides a simple high-value monitoring example and also acts as contextual input for oil pressure evaluation.

The V1 RPM thresholds are demonstration criteria.

Actual permissible engine speed depends on engine design and manufacturer calibration.

---

# 10. Brake Pad Remaining

## 10.1 Parameter Definition

| Property | Value |
|---|---|
| Configuration ID | `CFG-BRAKE` |
| Parameter | `brake_pad_remaining` |
| Unit | % |
| Data Type | float |
| Supported Minimum | 0.0 % |
| Supported Maximum | 100.0 % |

---

## 10.2 Diagnostic Criteria

VehicleGuard V1 uses the following demonstration criteria:

| Brake Pad Remaining | Classification |
|---:|---|
| `> 25.0 %` | `NORMAL` |
| `> 15.0 % and <= 25.0 %` | `INFO` |
| `> 5.0 % and <= 15.0 %` | `WARNING` |
| `<= 5.0 %` | `CRITICAL` |

---

## 10.3 Boundary Behaviour

Important boundaries are:

```text
5.0 %
15.0 %
25.0 %
```

Representative tests include:

```text
4.9 / 5.0 / 5.1 %
14.9 / 15.0 / 15.1 %
24.9 / 25.0 / 25.1 %
```

---

## 10.4 Engineering Rationale

Brake pad remaining demonstrates a parameter where decreasing values correspond to increasing severity.

It also provides a useful application for the `INFO` severity level.

The intended progression is:

```text
NORMAL
  |
  v
INFO
  |
  v
WARNING
  |
  v
CRITICAL
```

The percentage values are demonstration criteria and do not represent service limits for a specific braking system.

---

# 11. Configuration Summary

The initial VehicleGuard V1 configuration is summarized below.

| Parameter | Supported Range | Primary Diagnostic Boundaries |
|---|---|---|
| Coolant Temperature | -40.0 to 150.0 °C | 110.0 °C, 120.0 °C |
| Battery Voltage | 0.0 to 20.0 V | 11.0 V, 12.0 V, 15.0 V, 16.0 V |
| Oil Pressure | 0.0 to 1000.0 kPa | 70.0 kPa, 150.0 kPa |
| Engine RPM | 0 to 10000 rpm | 6500 rpm, 7500 rpm |
| Brake Pad Remaining | 0.0 to 100.0 % | 5.0 %, 15.0 %, 25.0 % |

Oil pressure monitoring additionally depends on:

```text
engine_rpm > 0
```

Battery voltage diagnostic interpretation in V1 assumes an engine-running condition when:

```text
engine_rpm > 0
```

---

# 12. Invalid Input Behaviour

Input values outside the supported range are not assigned normal operating severity levels.

For example:

```text
coolant_temperature = 160.0 °C
```

is outside the configured supported range.

VehicleGuard should therefore treat this as:

```text
INVALID INPUT
```

rather than automatically interpreting it as:

```text
CRITICAL COOLANT TEMPERATURE
```

Similarly:

```text
brake_pad_remaining = -5.0 %
```

is invalid input rather than a valid `CRITICAL` brake condition.

This distinction is important because sensor or data errors must remain distinguishable from genuine vehicle operating conditions.

---

# 13. Configuration and Validation Relationship

The supported range defines whether a value is technically accepted for further processing.

Diagnostic thresholds define how a valid value is interpreted.

The relationship is:

```text
Received Value
      |
      v
Within Supported Range?
      |
   +--+--+
   |     |
  NO    YES
   |     |
   v     v
INVALID  Diagnostic Evaluation
INPUT           |
                v
          Severity Classification
```

Validation therefore always occurs before normal diagnostic classification.

---

# 14. Configuration and Severity Relationship

The configuration provides criteria used by the severity classification function.

Conceptually:

```text
Parameter
   +
Observed Value
   +
Operating Context
   +
Active Configuration
        |
        v
Detected Condition
        |
        v
Severity
```

The diagnostic implementation should not contain independent hidden threshold values that contradict the active configuration.

---

# 15. Configuration Implementation

The machine-readable implementation of this specification will be stored in:

```text
prototype/config/vehicleguard-v1.json
```

The JSON configuration should contain the values required by the prototype without duplicating unnecessary explanatory documentation.

The Markdown specification remains the human-readable engineering definition.

The intended relationship is:

```text
v1-configuration.md
        |
        | defines
        v
vehicleguard-v1.json
        |
        | consumed by
        v
VehicleGuard Prototype
```

The implementation should load configurable values rather than reproduce the same thresholds directly in Python source code.

---

# 16. Verification Impact

The configuration directly affects planned verification activities.

Boundary tests defined in:

```text
tests/test-cases.md
```

will use the values established in this specification.

For a diagnostic threshold `X`, testing will follow the general pattern:

```text
X - Δ
X
X + Δ
```

The actual value of `Δ` depends on the data type and parameter resolution.

Examples include:

```text
Temperature:
109.9
110.0
110.1

Engine RPM:
6499
6500
6501
```

Configuration-specific expected results must be established before test execution.

---

# 17. Configuration Traceability

The configuration supports requirements related to:

```text
SYS-VAL-xxx
SYS-MON-xxx
SYS-DIAG-xxx
SYS-SEV-xxx
SYS-CFG-xxx
```

The exact requirement relationships are maintained in:

```text
requirements/requirements.xlsx
```

Verification relationships are maintained through the Verification Matrix and the test specification.

---

# 18. Configuration Control

This document defines the initial VehicleGuard V1 demonstration configuration.

During initial prototype implementation, corrections may be required if an inconsistency between the configuration and the established requirements is discovered.

After the V1 configuration is treated as baselined, significant technical changes should follow the process defined in:

```text
docs/08-change-management.md
```

A configuration change may require:

- impact analysis;
- updated expected test results;
- new boundary tests;
- repeated verification;
- updated verification evidence.

Configuration changes should remain traceable through Git history and, where applicable, a `CR-xxx` Change Request.

---

# 19. Current Configuration Status

The current configuration status is:

```text
Initial V1 Demonstration Configuration - Defined
```

The engineering values required for initial prototype implementation have been established.

Machine-readable implementation is pending.

The next configuration activity is to create:

```text
prototype/config/vehicleguard-v1.json
```

and verify that the prototype uses these values without introducing independent hard-coded diagnostic thresholds.
