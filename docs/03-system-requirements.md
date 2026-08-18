# VehicleGuard System Requirements

## 1. Document Purpose

This document defines the system requirements for VehicleGuard V1.

The requirements describe the behaviour and capabilities that VehicleGuard must provide within the system boundary defined in `01-project-overview.md`.

System requirements are derived from stakeholder needs documented in `02-stakeholders.md` and provide the basis for system architecture, prototype implementation, and verification.

Each requirement is assigned a unique identifier to support traceability throughout the project.

---

## 2. Requirements Development Approach

VehicleGuard requirements are developed from identified stakeholder needs.

The general requirements flow is:

```text
Stakeholder
     |
     v
Stakeholder Need
     |
     v
System Requirement
     |
     v
System Architecture
     |
     v
Implementation
     |
     v
Verification
```

A stakeholder need may result in multiple system requirements.

A system requirement may also support more than one stakeholder need.

These relationships will be maintained through requirements traceability.

---

## 3. Requirement Identification

Each VehicleGuard system requirement uses the following identifier structure:

```text
SYS-[CATEGORY]-[NUMBER]
```

Example:

```text
SYS-VAL-003
```

where:

* `SYS` identifies a system-level requirement;
* `VAL` identifies the requirement category;
* `003` identifies the individual requirement within that category.

Requirement identifiers are unique and remain stable after they have been assigned.

If a requirement is removed during later development, its identifier should not be reused for an unrelated requirement.

---

## 4. Requirement Categories

VehicleGuard V1 requirements are organized into the following categories:

| Prefix     | Category                | Purpose                                                       |
| ---------- | ----------------------- | ------------------------------------------------------------- |
| `SYS-INP`  | Input                   | Reception of vehicle operating data                           |
| `SYS-VAL`  | Validation              | Validation and plausibility checking of received data         |
| `SYS-MON`  | Monitoring              | Monitoring of configured vehicle parameters                   |
| `SYS-DIAG` | Diagnostics             | Detection of defined abnormal operating conditions            |
| `SYS-SEV`  | Severity Classification | Classification of detected conditions according to severity   |
| `SYS-WRN`  | Driver Warning          | Generation of driver-oriented warnings and status information |
| `SYS-EVT`  | Diagnostic Event        | Generation of structured diagnostic event information         |
| `SYS-CFG`  | Configuration           | Management of configurable thresholds and related parameters  |

Additional categories should only be introduced when a clear system-level need has been identified.

---

## 5. Requirement Writing Rules

VehicleGuard system requirements should be written so that they can be understood, implemented, and verified.

The following rules are used throughout this document.

### 5.1 Use Mandatory Language

Mandatory system behaviour is expressed using the word `shall`.

Example:

```text
VehicleGuard shall validate received vehicle data before diagnostic evaluation.
```

The words `should`, `could`, and `may` are avoided when defining mandatory system behaviour.

### 5.2 Define One Main Requirement per Statement

A requirement should describe one primary system obligation.

Multiple independent behaviours should not be combined into a single requirement when they can be verified separately.

### 5.3 Avoid Ambiguous Terms

Requirements should avoid undefined expressions such as:

```text
fast
appropriate
high temperature
low voltage
as soon as possible
user-friendly
normally
```

If such a concept affects system behaviour, it should be defined through measurable criteria, configuration data, or another referenced requirement.

### 5.4 Keep Requirements Verifiable

Each requirement should allow a verification activity to determine whether the required behaviour is satisfied.

A requirement that cannot be objectively verified should be reviewed and refined.

### 5.5 Separate Requirements from Implementation

System requirements should primarily describe required behaviour rather than unnecessarily defining how that behaviour must be implemented.

Implementation details should only be included when they represent an actual system constraint.

### 5.6 Maintain Traceability

Each relevant system requirement should identify the stakeholder need or engineering source from which it was derived.

Later project phases will extend this traceability to architecture elements and test cases.

---

## 6. Requirement Attributes

The following information will be maintained for each system requirement:

| Attribute           | Description                                   |
| ------------------- | --------------------------------------------- |
| Requirement ID      | Unique system requirement identifier          |
| Requirement         | Required system behaviour                     |
| Source              | Stakeholder need or engineering source        |
| Priority            | Importance within VehicleGuard V1             |
| Verification Method | Planned method used to verify the requirement |
| Status              | Current requirement lifecycle status          |

The complete requirements register will later be maintained in:

`requirements/requirements.xlsx`

This document provides the readable system specification, while the requirements register supports structured management and traceability.

---

## 7. Requirements Traceability

VehicleGuard maintains traceability between stakeholder needs, system requirements, architecture elements, verification activities, and verification evidence.

The purpose of traceability is to ensure that each system requirement has a defined engineering source and can later be connected to the system elements that implement it and the test cases that verify it.

Traceability is maintained in both directions. This makes it possible to determine:

- which stakeholder need resulted in a system requirement;
- which architecture elements are responsible for realizing a requirement;
- which test cases verify a requirement;
- which verification results provide evidence that the requirement has been satisfied.

A stakeholder need may result in multiple system requirements. Similarly, one system requirement may be allocated to multiple architecture elements when its implementation requires more than one system function or component.

The traceability concept used throughout VehicleGuard is shown below.

![VehicleGuard Requirements Traceability](../diagrams/requirements-traceability.png)

<p align="center">
  <em>Figure 1 - VehicleGuard Requirements Traceability</em>
</p>

Detailed traceability relationships will be maintained as the corresponding requirements, architecture elements, and test cases are defined.

---

## 8. Input Requirements

VehicleGuard receives vehicle operating data through its defined input interface.

The input requirements define which information must be available to the system before validation and diagnostic processing can take place.

Detailed data types, units, ranges, and interface structures will be defined in `05-interfaces.md`.

### SYS-INP-001 - Vehicle Data Reception

**Requirement:**
VehicleGuard shall receive vehicle operating data through a defined input interface.

**Source:** `SN-DEV-002`
**Priority:** High
**Verification Method:** Test

### SYS-INP-002 - Coolant Temperature Input

**Requirement:**
VehicleGuard shall accept coolant temperature as a monitored vehicle parameter.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-INP-003 - Battery Voltage Input

**Requirement:**
VehicleGuard shall accept battery voltage as a monitored vehicle parameter.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-INP-004 - Oil Pressure Input

**Requirement:**
VehicleGuard shall accept oil pressure as a monitored vehicle parameter.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-INP-005 - Engine RPM Input

**Requirement:**
VehicleGuard shall accept engine speed as a monitored vehicle parameter.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-INP-006 - Brake Condition Input

**Requirement:**
VehicleGuard shall accept brake condition information as a monitored vehicle parameter.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-INP-007 - Input Timestamp

**Requirement:**
VehicleGuard shall receive or associate a timestamp with each vehicle data sample used for diagnostic evaluation.

**Source:** `SN-SRV-002`
**Priority:** Medium
**Verification Method:** Test

---

## 9. Validation Requirements

Input data must be validated before it is interpreted as representing an actual vehicle condition.

Validation prevents invalid or unsupported input values from automatically being treated as real vehicle faults.

### SYS-VAL-001 - Input Validation

**Requirement:**
VehicleGuard shall validate received vehicle data before using the data for diagnostic evaluation.

**Source:** `SN-DRV-003`, `SN-SRV-003`
**Priority:** High
**Verification Method:** Test

### SYS-VAL-002 - Missing Input Detection

**Requirement:**
VehicleGuard shall detect when a required monitored parameter is missing from the received vehicle data.

**Source:** `SN-SRV-003`
**Priority:** High
**Verification Method:** Test

### SYS-VAL-003 - Invalid Data Type Detection

**Requirement:**
VehicleGuard shall detect received parameter values that do not conform to the defined input data type.

**Source:** `SN-DEV-002`, `SN-TST-002`
**Priority:** High
**Verification Method:** Test

### SYS-VAL-004 - Supported Range Validation

**Requirement:**
VehicleGuard shall determine whether received numeric parameter values are within the configured supported input range for the corresponding parameter.

**Source:** `SN-DRV-003`, `SN-SRV-003`
**Priority:** High
**Verification Method:** Test

### SYS-VAL-005 - Invalid Input Classification

**Requirement:**
VehicleGuard shall distinguish an invalid input condition from an abnormal vehicle operating condition.

**Source:** `SN-SRV-003`
**Priority:** High
**Verification Method:** Test

### SYS-VAL-006 - Invalid Data Diagnostic Evaluation

**Requirement:**
VehicleGuard shall prevent an invalid parameter value from being evaluated as a valid vehicle operating value.

**Source:** `SN-DRV-003`, `SN-SRV-003`
**Priority:** High
**Verification Method:** Test

---

## 10. Monitoring Requirements

VehicleGuard monitors validated vehicle parameters and evaluates their current operating condition.

Monitoring requirements define which parameters participate in the diagnostic process.

### SYS-MON-001 - Valid Data Monitoring

**Requirement:**
VehicleGuard shall monitor each valid configured vehicle parameter received through the input interface.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-MON-002 - Coolant Temperature Monitoring

**Requirement:**
VehicleGuard shall evaluate valid coolant temperature values against the configured coolant temperature operating conditions.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-MON-003 - Battery Voltage Monitoring

**Requirement:**
VehicleGuard shall evaluate valid battery voltage values against the configured battery voltage operating conditions.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-MON-004 - Oil Pressure Monitoring

**Requirement:**
VehicleGuard shall evaluate valid oil pressure values against the configured oil pressure operating conditions.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-MON-005 - Engine RPM Monitoring

**Requirement:**
VehicleGuard shall evaluate valid engine speed values against the configured engine speed operating conditions.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

### SYS-MON-006 - Brake Condition Monitoring

**Requirement:**
VehicleGuard shall evaluate valid brake condition information against the configured brake condition criteria.

**Source:** Project Scope
**Priority:** High
**Verification Method:** Test

---

## 11. Diagnostic Requirements

Diagnostic requirements define how VehicleGuard identifies abnormal conditions after input data has passed validation.

### SYS-DIAG-001 - Abnormal Condition Detection

**Requirement:**
VehicleGuard shall detect when a valid monitored parameter satisfies a configured abnormal operating condition.

**Source:** `SN-DRV-001`, `SN-SRV-001`
**Priority:** High
**Verification Method:** Test

### SYS-DIAG-002 - Normal Condition Recognition

**Requirement:**
VehicleGuard shall identify a monitored parameter as normal when its valid value does not satisfy any configured abnormal condition.

**Source:** `SN-DRV-004`
**Priority:** High
**Verification Method:** Test

### SYS-DIAG-003 - Parameter Identification

**Requirement:**
VehicleGuard shall identify which monitored parameter caused each detected abnormal condition.

**Source:** `SN-SRV-001`
**Priority:** High
**Verification Method:** Test

### SYS-DIAG-004 - Multiple Condition Detection

**Requirement:**
VehicleGuard shall support detection of abnormal conditions affecting more than one monitored parameter within the same vehicle data sample.

**Source:** Engineering Requirement
**Priority:** Medium
**Verification Method:** Test

### SYS-DIAG-005 - Condition Recovery

**Requirement:**
VehicleGuard shall recognize when a previously abnormal monitored parameter returns to its configured normal operating condition.

**Source:** Engineering Requirement
**Priority:** Medium
**Verification Method:** Test

---

## 12. Severity Classification Requirements

VehicleGuard uses severity classification to distinguish between conditions with different levels of importance.

The exact threshold values associated with each severity level are configuration data and are not defined in this document.

### SYS-SEV-001 - Condition Classification

**Requirement:**
VehicleGuard shall assign a defined severity level to each detected abnormal vehicle condition.

**Source:** `SN-DRV-002`, `SN-SRV-002`
**Priority:** High
**Verification Method:** Test

### SYS-SEV-002 - Supported Severity Levels

**Requirement:**
VehicleGuard shall support the following condition levels:

* `NORMAL`
* `INFO`
* `WARNING`
* `CRITICAL`

**Source:** `SN-DRV-002`, `SN-DRV-004`
**Priority:** High
**Verification Method:** Test

### SYS-SEV-003 - Normal Classification

**Requirement:**
VehicleGuard shall assign `NORMAL` when a valid monitored condition does not meet any configured abnormal condition.

**Source:** `SN-DRV-004`
**Priority:** High
**Verification Method:** Test

### SYS-SEV-004 - Severity Determination

**Requirement:**
VehicleGuard shall determine severity using the configured condition criteria associated with the affected monitored parameter.

**Source:** `SN-DRV-002`, `SN-DEV-003`
**Priority:** High
**Verification Method:** Test

### SYS-SEV-005 - Independent Severity Evaluation

**Requirement:**
VehicleGuard shall determine the severity of each detected abnormal condition independently when multiple abnormal conditions are present.

**Source:** Engineering Requirement
**Priority:** Medium
**Verification Method:** Test

---

## 13. Driver Warning Requirements

Driver warning requirements define the information VehicleGuard provides when a detected condition requires driver attention.

VehicleGuard V1 generates warning information as a system output. Implementation of a production vehicle HMI is outside the project scope.

### SYS-WRN-001 - Warning Generation

**Requirement:**
VehicleGuard shall generate driver warning information when a detected condition is classified as `WARNING` or `CRITICAL`.

**Source:** `SN-DRV-001`
**Priority:** High
**Verification Method:** Test

### SYS-WRN-002 - Warning Severity

**Requirement:**
VehicleGuard shall include the severity level of the detected condition in the generated driver warning information.

**Source:** `SN-DRV-002`
**Priority:** High
**Verification Method:** Test

### SYS-WRN-003 - Warning Source

**Requirement:**
VehicleGuard shall identify the monitored vehicle parameter associated with the generated warning.

**Source:** `SN-DRV-001`
**Priority:** High
**Verification Method:** Test

### SYS-WRN-004 - Warning Message

**Requirement:**
VehicleGuard shall provide a driver-oriented message describing the detected condition without requiring interpretation of raw diagnostic data.

**Source:** `SN-DRV-002`
**Priority:** Medium
**Verification Method:** Inspection and Test

### SYS-WRN-005 - Normal Operation

**Requirement:**
VehicleGuard shall not generate an active abnormal-condition warning for a monitored parameter classified as `NORMAL`.

**Source:** `SN-DRV-004`
**Priority:** High
**Verification Method:** Test

---

## 14. Diagnostic Event Requirements

Diagnostic events provide structured technical information about conditions detected by VehicleGuard.

These events are intended to support diagnostic analysis and verification.

### SYS-EVT-001 - Diagnostic Event Generation

**Requirement:**
VehicleGuard shall generate a diagnostic event for each detected abnormal vehicle condition.

**Source:** `SN-SRV-001`, `SN-SRV-002`
**Priority:** High
**Verification Method:** Test

### SYS-EVT-002 - Event Identifier

**Requirement:**
VehicleGuard shall associate each diagnostic event with a defined fault or condition identifier.

**Source:** `SN-SRV-004`
**Priority:** High
**Verification Method:** Test

### SYS-EVT-003 - Affected Parameter

**Requirement:**
VehicleGuard shall include the affected monitored parameter in each diagnostic event.

**Source:** `SN-SRV-001`
**Priority:** High
**Verification Method:** Test

### SYS-EVT-004 - Observed Value

**Requirement:**
VehicleGuard shall include the observed parameter value associated with the detected condition when such a value is available.

**Source:** `SN-SRV-002`
**Priority:** High
**Verification Method:** Test

### SYS-EVT-005 - Event Severity

**Requirement:**
VehicleGuard shall include the assigned severity level in each diagnostic event.

**Source:** `SN-SRV-002`
**Priority:** High
**Verification Method:** Test

### SYS-EVT-006 - Event Timestamp

**Requirement:**
VehicleGuard shall associate each diagnostic event with the timestamp of the vehicle data sample that resulted in the event.

**Source:** `SN-SRV-002`
**Priority:** Medium
**Verification Method:** Test

### SYS-EVT-007 - Invalid Input Event

**Requirement:**
VehicleGuard shall be capable of generating diagnostic information that identifies an invalid input condition separately from an abnormal vehicle operating condition.

**Source:** `SN-SRV-003`
**Priority:** High
**Verification Method:** Test

---

## 15. Configuration Requirements

VehicleGuard uses configurable values to separate system behaviour from demonstration-specific parameter thresholds.

This allows prototype thresholds to be changed without redefining the fundamental diagnostic processing logic.

### SYS-CFG-001 - External Threshold Configuration

**Requirement:**
VehicleGuard shall obtain configurable monitoring thresholds from defined configuration data rather than requiring threshold values to be permanently embedded in diagnostic processing logic.

**Source:** `SN-DEV-003`
**Priority:** High
**Verification Method:** Inspection and Test

### SYS-CFG-002 - Parameter-Specific Configuration

**Requirement:**
VehicleGuard shall support separate configuration criteria for each monitored vehicle parameter.

**Source:** `SN-DEV-003`
**Priority:** High
**Verification Method:** Test

### SYS-CFG-003 - Supported Input Range Configuration

**Requirement:**
VehicleGuard shall support configuration of the valid input range for each numeric monitored parameter.

**Source:** `SN-DEV-003`, `SN-TST-002`
**Priority:** High
**Verification Method:** Test

### SYS-CFG-004 - Severity Criteria Configuration

**Requirement:**
VehicleGuard shall support configuration of the condition criteria used to determine applicable severity levels for monitored parameters.

**Source:** `SN-DEV-003`
**Priority:** High
**Verification Method:** Test

### SYS-CFG-005 - Configuration Consistency

**Requirement:**
VehicleGuard shall use the active configuration consistently during monitoring, diagnostic evaluation, and severity classification.

**Source:** Engineering Requirement
**Priority:** High
**Verification Method:** Test

---

## 16. Requirements Summary

VehicleGuard V1 currently defines system requirements across eight functional categories.

| Category                | Prefix     | Requirements |
| ----------------------- | ---------- | -----------: |
| Input                   | `SYS-INP`  |            7 |
| Validation              | `SYS-VAL`  |            6 |
| Monitoring              | `SYS-MON`  |            6 |
| Diagnostics             | `SYS-DIAG` |            5 |
| Severity Classification | `SYS-SEV`  |            5 |
| Driver Warning          | `SYS-WRN`  |            5 |
| Diagnostic Event        | `SYS-EVT`  |            7 |
| Configuration           | `SYS-CFG`  |            5 |
| **Total**               |            |       **46** |

These requirements define the initial VehicleGuard V1 system baseline.

The requirements will provide input to:

* system architecture development;
* interface definition;
* prototype implementation;
* verification planning;
* test case development;
* requirements traceability.

The requirements are not considered permanently fixed.

If architecture development, risk analysis, implementation, or verification identifies a necessary change, the affected requirements may be revised through the project change management process.

Requirement identifiers should remain stable when requirements are modified.

Removed requirements should remain identifiable in the project history and their identifiers should not be reused for unrelated requirements.

---

## 17. Requirements Baseline Status

The requirements defined in this document represent the initial VehicleGuard V1 system requirements set.

At the current project stage, the requirements are considered:

`Draft - Under Engineering Review`

The requirements will be reviewed during system architecture and interface development.

The initial requirements baseline may be established once:

* the requirements have been checked for ambiguity;
* the requirements have been checked for consistency;
* the requirements have been checked for verifiability;
* required interfaces have been sufficiently defined;
* major conflicts between requirements have been resolved;
* initial traceability to stakeholder needs has been reviewed.

After the initial baseline has been established, significant requirement changes should be handled through the defined change management process.
