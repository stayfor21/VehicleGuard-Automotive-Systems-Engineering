# VehicleGuard Requirements

This directory contains the structured requirements management data and the V1 configuration specification for VehicleGuard.

The main system requirements specification is documented in:

`docs/03-system-requirements.md`

The artifacts in this directory support requirements management, traceability, verification planning, and controlled configuration of the VehicleGuard V1 prototype.

---

## Contents

### requirements.xlsx

The `requirements.xlsx` workbook is the central structured requirements register for VehicleGuard V1.

It is used to maintain information related to:

- system requirements;
- requirement categories;
- requirement sources;
- requirement priorities;
- verification methods;
- architecture allocation;
- test case relationships;
- requirements traceability;
- verification planning;
- verification status.

The workbook currently contains:

```text
Requirements
Summary
Verification Matrix
```

The `Verification Matrix` connects system requirements with their planned architecture allocation and verification activities.

Before prototype test execution, verification-related fields remain in states such as:

```text
NOT RUN
TBD
NOT VERIFIED
```

Actual verification results will only be added after the applicable prototype tests have been executed.

The workbook complements the Markdown documentation and is not intended to replace it.

---

### v1-configuration.md

The `v1-configuration.md` document defines the initial engineering configuration for the VehicleGuard V1 prototype.

It defines configuration information for the five monitored parameters:

```text
Coolant Temperature
Battery Voltage
Oil Pressure
Engine RPM
Brake Pad Remaining
```

The specification includes:

- engineering units;
- data types;
- supported input ranges;
- diagnostic thresholds;
- severity criteria;
- boundary behaviour;
- parameter dependencies;
- engineering rationale.

The values defined in this document are demonstration values for the VehicleGuard V1 engineering prototype.

They must not be interpreted as universal OEM calibration values or production vehicle diagnostic thresholds.

The configuration specification provides the human-readable engineering definition for the machine-readable configuration that will later be implemented in:

```text
prototype/config/vehicleguard-v1.json
```

---

## Requirements Management Approach

VehicleGuard uses the following general traceability structure:

```text
Stakeholder Need
        |
        v
System Requirement
        |
        v
Architecture Element
        |
        v
Implementation
        |
        v
Test Case
        |
        v
Verification Evidence
```

Each system requirement has a unique identifier such as:

```text
SYS-VAL-001
SYS-DIAG-001
SYS-WRN-001
```

These identifiers are used consistently across project documentation, architecture, implementation, and verification activities.

Structured traceability information is maintained in:

```text
requirements.xlsx
```

---

## Configuration Relationship

Requirements define what VehicleGuard must do.

The V1 configuration defines the controlled engineering values used to implement and verify that behaviour.

The intended relationship is:

```text
System Requirements
        |
        v
V1 Configuration Specification
        |
        v
Machine-Readable Configuration
        |
        v
Prototype Implementation
        |
        v
Verification
```

More specifically:

```text
docs/03-system-requirements.md
        |
        v
requirements/requirements.xlsx
        |
        v
requirements/v1-configuration.md
        |
        v
prototype/config/vehicleguard-v1.json
        |
        v
VehicleGuard Prototype
        |
        v
Test Execution
        |
        v
Verification Evidence
```

The prototype implementation should use the machine-readable configuration rather than introduce independent hard-coded diagnostic thresholds.

---

## Verification Planning

Verification relationships are prepared before prototype execution.

The Verification Matrix provides relationships between:

```text
SYS-xxx
   |
   v
COMP-xxx
   |
   v
TC-xxx
   |
   v
RESULT-xxx
```

At the current project stage:

```text
Test Execution       NOT RUN
Verification Evidence TBD
Verification Status   NOT VERIFIED
```

These states are intentional.

No requirement should be marked as verified until the applicable verification activity has actually been executed and supporting evidence exists.

---

## Current Status

The VehicleGuard V1 requirements are currently:

```text
Draft - Under Engineering Review
```

The initial V1 demonstration configuration is:

```text
Defined - Implementation Pending
```

Prototype implementation and executable verification have not yet been completed.

Requirements and configuration may be refined if implementation or verification identifies an inconsistency.

Once the applicable baselines are established, significant technical modifications will be handled through the project change management process.

---

## Related Documentation

Additional requirements-related information is available in:

- `../docs/01-project-overview.md` - project scope, system purpose, assumptions, and system boundary
- `../docs/02-stakeholders.md` - stakeholders and stakeholder needs
- `../docs/03-system-requirements.md` - complete system requirements specification
- `../docs/04-system-architecture.md` - system architecture and requirement allocation
- `../docs/05-interfaces.md` - logical interface definitions
- `../docs/06-risk-analysis.md` - technical system risk analysis
- `../docs/07-verification-validation.md` - verification and validation approach
- `../docs/08-change-management.md` - controlled change management process
- `../project-management/risk-register.md` - project development risks
- `../tests/test-cases.md` - requirement-based test specification
- `../tests/test-report.md` - verification results after test execution

---

## Maintenance

The requirements artifacts will be maintained as VehicleGuard progresses through implementation and verification.

Requirement identifiers should remain stable throughout the project.

If a requirement is modified, its relationships to stakeholder needs, architecture elements, interfaces, configuration, test cases, and verification activities should be reviewed.

If the V1 configuration changes, affected boundary tests and expected results must also be reviewed.

Removed requirement identifiers should not be reused for unrelated requirements.

Significant changes after baseline establishment should follow the process defined in:

```text
docs/08-change-management.md
```
