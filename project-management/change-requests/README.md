# Change Requests

This directory contains formal Change Requests for controlled technical changes to VehicleGuard.

The Change Request process is used when a proposed modification affects the established system definition, including requirements, architecture, interfaces, configuration, implementation, verification, or other related engineering artifacts.

The complete change management process is defined in:

`docs/08-change-management.md`

---

## Purpose

A Change Request documents why a technical change is required, what parts of the project may be affected, and how the change will be introduced and verified.

The purpose is to prevent isolated modifications that create inconsistencies between:

```text
Requirements
Architecture
Interfaces
Configuration
Implementation
Tests
Verification Evidence
```

Change Requests also provide a traceable engineering history for significant project decisions.

---

## Change Request Identification

Each Change Request uses a unique identifier:

```text
CR-XXX
```

Examples:

```text
CR-001
CR-002
CR-003
```

The identifier must not be reused for an unrelated change.

---

## File Naming

Change Request files use the following naming convention:

```text
CR-XXX-short-description.md
```

Examples:

```text
CR-001-add-transmission-temperature.md
CR-002-update-severity-classification.md
CR-003-modify-diagnostic-event-interface.md
```

File names should remain short while clearly identifying the proposed change.

---

## When to Create a Change Request

A Change Request should be created when a proposed modification changes technical project content.

Examples include:

- adding or removing a monitored vehicle parameter;
- adding or modifying a system requirement;
- changing architecture responsibilities;
- modifying an interface;
- changing an engineering unit or data type;
- changing diagnostic behaviour;
- modifying severity classification behaviour;
- changing configuration behaviour;
- changing test acceptance criteria;
- introducing a new technical failure scenario;
- modifying the established VehicleGuard V1 scope.

A Change Request is normally not required for changes that do not affect engineering meaning, such as:

- spelling corrections;
- formatting corrections;
- Markdown cleanup;
- broken link corrections;
- diagram alignment corrections;
- minor wording improvements without technical impact.

---

## Change Request Structure

Each Change Request should contain:

```text
Change Request ID
Title
Date
Status
Reason for Change
Current Situation
Proposed Change
Affected Artifacts
Impact Analysis
Risk Impact
Verification Impact
Decision
Implementation Status
Verification Status
Notes
```

Fields that cannot yet be completed may remain pending while the change is under review.

---

## Status

The following status values may be used:

| Status | Meaning |
|---|---|
| `Proposed` | The change has been identified |
| `Under Review` | The technical impact is being evaluated |
| `Approved` | The change has been accepted for implementation |
| `Rejected` | The change will not be implemented |
| `Implemented` | The approved modification has been introduced |
| `Verified` | Required verification has been completed |
| `Closed` | No further action is required |

A typical lifecycle is:

```text
Proposed
   |
   v
Under Review
   |
   +------> Rejected
   |
   v
Approved
   |
   v
Implemented
   |
   v
Verified
   |
   v
Closed
```

---

## Impact Analysis

Before an approved technical change is implemented, the following areas should be reviewed where applicable:

| Area | Examples |
|---|---|
| Stakeholder Needs | `SN-xxx` |
| System Requirements | `SYS-xxx` |
| Architecture | `COMP-xxx` |
| Interfaces | `IF-xxx` |
| Failure Analysis | `SCN-xx` |
| Configuration | ranges, thresholds, severity criteria |
| Prototype | affected implementation |
| Test Cases | `TC-xxx` |
| Verification Evidence | `RESULT-xxx` |
| Traceability | affected relationships |

Not every change affects every area.

The impact analysis should identify only the artifacts that are actually relevant to the proposed modification.

---

## Verification After Change

A technical change may require existing verification activities to be repeated.

After implementation, the affected test cases should be reviewed to determine whether:

- an existing test remains valid;
- an existing test must be updated;
- a test must be repeated;
- a new test is required;
- previous verification evidence remains valid.

A requirement should not remain marked as verified if the supporting evidence has been invalidated by a significant technical change.

---

## Current Status

VehicleGuard V1 is currently in the initial development phase.

No Change Requests are stored in this directory yet.

Changes that are part of the planned initial V1 development are not treated as Change Requests.

The first `CR-XXX` file will be created when a genuine modification to the established VehicleGuard definition requires controlled impact analysis and implementation.

Change Requests will not be created only to populate this directory.
