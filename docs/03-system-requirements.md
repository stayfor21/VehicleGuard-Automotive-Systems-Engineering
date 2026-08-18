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

