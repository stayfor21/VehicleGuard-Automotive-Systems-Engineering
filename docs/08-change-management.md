# VehicleGuard Change Management

## 1. Purpose

This document defines how controlled changes are introduced into VehicleGuard V1.

Changes may affect requirements, architecture, interfaces, configuration, implementation, verification activities, or other engineering artifacts.

The purpose of change management is to ensure that a modification is understood before it is introduced and that related project artifacts remain consistent after the change.

The process is intended to prevent situations where one part of the project is modified while related requirements, interfaces, tests, or documentation remain outdated.

---

## 2. Scope

The change management process applies to controlled VehicleGuard engineering artifacts, including:

- stakeholder needs;
- system requirements;
- system architecture;
- interface definitions;
- system risk analysis;
- verification and validation documentation;
- requirements and traceability data;
- prototype configuration;
- prototype implementation;
- test cases;
- verification evidence.

Minor corrections that do not change technical meaning may be handled without a formal Change Request.

Examples include:

- spelling corrections;
- formatting corrections;
- broken Markdown links;
- wording improvements that do not change requirement intent;
- diagram alignment corrections that do not change engineering content.

A change that modifies technical meaning, behaviour, interfaces, acceptance criteria, or traceability should be evaluated through the change management process.

---

## 3. Change Management Principles

VehicleGuard uses the following change management principles.

### 3.1 Changes Must Be Traceable

Significant technical changes should have an identifiable reason and documented impact.

### 3.2 Impact Must Be Considered Before Implementation

A change should not be implemented only because it appears simple in one file.

Related requirements, architecture elements, interfaces, configuration, tests, and risks must also be considered.

### 3.3 Existing Identifiers Should Remain Stable

Existing identifiers should not be reused for unrelated engineering items.

This applies to identifiers such as:

```text
SN-xxx
SYS-xxx
COMP-xxx
IF-xxx
SCN-xx
TC-xxx
RESULT-xxx
CR-xxx
```

### 3.4 Traceability Must Be Maintained

When an engineering artifact changes, related traceability information must be reviewed.

### 3.5 Verification Must Follow Relevant Changes

A change affecting verified behaviour may require existing tests to be repeated.

### 3.6 Project History Should Be Preserved

Removed or replaced engineering items should remain understandable through repository history and change records.

---

## 4. Change Request Identification

Controlled changes use the identifier format:

```text
CR-XXX
```

Examples:

```text
CR-001
CR-002
CR-003
```

Each Change Request receives a unique identifier.

An existing Change Request identifier must not be reused for an unrelated change.

Change Requests are stored in:

```text
project-management/change-requests/
```

A recommended filename is:

```text
CR-001-short-description.md
```

For example:

```text
CR-001-add-transmission-temperature.md
```

---

## 5. When a Change Request Is Required

A Change Request should be created when a proposed modification affects technical project content.

Examples include:

- adding a new monitored vehicle parameter;
- removing an existing parameter;
- modifying a system requirement;
- introducing a new system requirement;
- changing requirement acceptance criteria;
- changing architecture responsibilities;
- adding or removing an architecture element;
- changing an interface field;
- changing an interface data type;
- changing an engineering unit;
- modifying supported input ranges;
- modifying diagnostic behaviour;
- changing severity classification behaviour;
- modifying output structures;
- changing configuration behaviour;
- modifying an existing test acceptance criterion;
- changing the intended VehicleGuard V1 scope.

A Change Request is not normally required for purely editorial corrections that do not alter engineering meaning.

---

## 6. Change Request Structure

Each Change Request should contain the following information:

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
Verification Impact
Risk Impact
Decision
Implementation Status
Verification Status
Notes
```

Not every field must be complete when the Change Request is first created.

Information may be added as the change progresses.

---

## 7. Change Request Status

The following status values are used.

### Proposed

The change has been identified but has not yet been evaluated or approved.

### Under Review

The impact of the proposed change is being analysed.

### Approved

The change has been accepted for implementation.

### Rejected

The proposed change will not be implemented.

### Implemented

The approved modification has been introduced into the affected engineering artifacts.

### Verified

Required verification after implementation has been completed successfully.

### Closed

The Change Request is complete and no further action is required.

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

Not every change requires all states.

For example, a documentation-only technical change may not require executable verification.

---

## 8. Change Management Process

The standard VehicleGuard change process consists of the following stages.

### Step 1 - Identify the Change

A required or proposed modification is identified.

The source may be:

- requirements review;
- architecture review;
- implementation;
- test planning;
- failed verification;
- risk analysis;
- interface review;
- scope review;
- new engineering information.

### Step 2 - Create the Change Request

A `CR-XXX` identifier is assigned.

The reason and proposed modification are documented.

### Step 3 - Perform Impact Analysis

Affected project artifacts are identified before implementation.

### Step 4 - Make a Decision

The change is approved, rejected, or returned for further analysis.

### Step 5 - Implement the Change

Approved project artifacts are updated.

### Step 6 - Update Traceability

Relationships between affected needs, requirements, architecture elements, interfaces, tests, and evidence are reviewed and updated.

### Step 7 - Verify the Change

Affected verification activities are executed or repeated where required.

### Step 8 - Close the Change

The Change Request is closed when required implementation and verification activities are complete.

---

## 9. Impact Analysis

Impact analysis determines which parts of VehicleGuard may be affected by a proposed change.

The following areas should be considered:

| Area | Impact Question |
|---|---|
| Stakeholder Needs | Does the change modify or introduce a stakeholder expectation? |
| Requirements | Which `SYS-xxx` requirements are affected? |
| Architecture | Which `COMP-xxx` elements are affected? |
| Interfaces | Does any `IF-xxx` structure or data flow change? |
| Risk Analysis | Does the change introduce or modify a failure scenario? |
| Configuration | Are ranges, thresholds, or criteria affected? |
| Prototype | Which implementation elements must change? |
| Test Cases | Which `TC-xxx` tests must be added or modified? |
| Evidence | Does existing verification evidence remain valid? |
| Traceability | Which relationships must be updated? |
| Scope | Does the change remain within VehicleGuard V1? |

The purpose of impact analysis is not to create unnecessary documentation.

It is used to prevent incomplete changes.

---

## 10. Example Impact Analysis

Assume a proposed change introduces:

```text
transmission_temperature
```

as a new monitored VehicleGuard parameter.

The change may initially appear to affect only the vehicle data input.

However, the complete impact may include:

```text
Stakeholder Need
      |
      v
System Requirement
      |
      v
Input Interface
      |
      v
Validation
      |
      v
Monitoring
      |
      v
Diagnostic Logic
      |
      v
Severity Classification
      |
      v
Warning / Event
      |
      v
Test Cases
      |
      v
Verification Evidence
```

Potentially affected artifacts could therefore include:

```text
docs/02-stakeholders.md
docs/03-system-requirements.md
docs/04-system-architecture.md
docs/05-interfaces.md
docs/06-risk-analysis.md
docs/07-verification-validation.md
requirements/requirements.xlsx
prototype/
tests/test-cases.md
```

This example demonstrates why implementation should not be changed independently from the system definition.

---

## 11. Requirement Changes

When an existing system requirement changes, the following must be reviewed:

- requirement wording;
- requirement rationale;
- stakeholder need relationship;
- architecture allocation;
- interface impact;
- risk impact;
- verification method;
- related test cases;
- existing verification evidence.

If the meaning of an existing requirement changes significantly, the project should preserve enough history to understand the previous definition.

Requirement IDs should not be casually replaced or renumbered because they are used for traceability.

---

## 12. Architecture Changes

Architecture changes may include:

- adding an architecture element;
- removing an architecture element;
- changing element responsibility;
- changing allocation of requirements;
- modifying information flow;
- changing component relationships.

An architecture change requires review of:

```text
SYS-xxx
COMP-xxx
IF-xxx
TC-xxx
```

Architecture diagrams must also be updated when their technical content is affected.

---

## 13. Interface Changes

Interface changes require particular attention because they may affect several architecture elements simultaneously.

Examples include:

- adding a field;
- removing a field;
- changing a field name;
- changing a data type;
- changing an engineering unit;
- changing interface direction;
- changing data semantics.

For example:

```text
battery_voltage: float [V]
```

must not be changed to another unit or meaning without reviewing all consumers of that information.

Affected implementation and tests must be reviewed together with the interface definition.

---

## 14. Configuration Changes

VehicleGuard uses configuration to separate adjustable diagnostic criteria from processing logic.

Configuration changes may include:

- supported input ranges;
- monitoring thresholds;
- severity criteria;
- parameter-specific settings.

A configuration change does not automatically require a system requirement change.

However, the effect of the new value must still be evaluated.

The following should be considered:

- whether the value remains within the intended V1 scope;
- whether related tests remain valid;
- whether expected test results change;
- whether new boundary tests are required;
- whether the change introduces a new technical risk.

Configuration used for verification should be identifiable so that test results can be reproduced.

---

## 15. Test Case Changes

Test cases may change because:

- a requirement changes;
- an interface changes;
- configuration behaviour changes;
- an incorrect test assumption is discovered;
- acceptance criteria require clarification;
- a new failure scenario is identified.

A failed test must not be made to pass simply by changing the expected result to match incorrect implementation behaviour.

Before changing an expected result after a failure, the project must determine whether the problem is in:

```text
Requirement
Architecture
Interface
Configuration
Implementation
or
Test Definition
```

Only then should the appropriate artifact be modified.

---

## 16. Verification Impact

A technical change may invalidate previous verification evidence.

For each implemented change, the project should determine whether:

- a new test is required;
- an existing test must be modified;
- an existing test must be repeated;
- existing evidence remains valid;
- additional validation is required.

The relationship is:

```text
Change
   |
   v
Affected Requirement
   |
   v
Affected Test
   |
   v
Re-Test
   |
   v
Updated Evidence
```

A requirement should not remain marked as verified if the supporting evidence is no longer valid after a significant change.

---

## 17. Risk Impact

Each significant technical change should be reviewed against:

`docs/06-risk-analysis.md`

The review should determine whether the change:

- introduces a new failure scenario;
- changes an existing failure scenario;
- changes a mitigation measure;
- changes failure propagation;
- affects verification intended to detect a failure.

If necessary, a new `SCN-xx` identifier should be created.

Project execution risks should also be reviewed in:

`project-management/risk-register.md`

when the change affects project scope, complexity, schedule, or development quality.

---

## 18. Traceability Update

Traceability must be reviewed whenever a controlled technical change is implemented.

The intended VehicleGuard traceability chain is:

```text
SN-xxx
   |
   v
SYS-xxx
   |
   v
COMP-xxx
   |
   v
IF-xxx
   |
   v
TC-xxx
   |
   v
RESULT-xxx
```

A change affecting one item may require updates to relationships elsewhere in the chain.

The structured traceability information maintained in:

```text
requirements/requirements.xlsx
```

must therefore be reviewed after relevant changes.

---

## 19. Baseline Concept

A baseline represents a reviewed project state used as a reference for subsequent development.

Before a baseline is established, engineering artifacts may change relatively frequently as the system definition matures.

After a baseline is established, significant technical modifications should be introduced through controlled change.

VehicleGuard may use baselines such as:

```text
Requirements Baseline
Architecture Baseline
Interface Baseline
Verification Baseline
V1 Release Baseline
```

The project does not require a complex enterprise configuration management system.

Git repository history and documented Change Requests provide the primary change history for VehicleGuard V1.

---

## 20. Git and Change Management

Git provides version history for project files.

However, a Git commit and a Change Request serve different purposes.

A commit answers:

```text
What changed in the repository?
```

A Change Request answers:

```text
Why was the technical change introduced,
what does it affect,
and how was its impact controlled?
```

Significant Change Requests should therefore be referenced in related commit messages where practical.

Example:

```text
CR-003: Add transmission temperature monitoring
```

This creates a direct relationship between engineering decision history and repository history.

---

## 21. Change Request Example

An example Change Request may look like:

```text
Change Request ID:
CR-001

Title:
Add transmission temperature monitoring

Status:
Proposed

Reason for Change:
Extend VehicleGuard monitoring to include transmission temperature.

Current Situation:
VehicleGuard V1 does not currently receive or evaluate transmission temperature.

Proposed Change:
Add transmission_temperature to the vehicle data interface and define the required validation, monitoring, diagnostic, configuration, and verification behaviour.

Affected Artifacts:
SYS requirements
System architecture
Interface specification
Configuration
Prototype
Test cases
Requirements traceability

Risk Impact:
To be reviewed.

Verification Impact:
New validation, monitoring, diagnostic, severity, and integrated system tests may be required.

Decision:
Pending
```

This example demonstrates the expected level of information.

A Change Request should remain concise while providing enough information to understand and review the modification.

---

## 22. Change Request Storage

Change Requests are stored in:

```text
project-management/change-requests/
```

The recommended structure is:

```text
change-requests/
|
+-- README.md
+-- CR-001-short-description.md
+-- CR-002-short-description.md
+-- CR-003-short-description.md
```

The directory may initially contain only `README.md` until the first real technical change is proposed.

Change Requests should not be invented only to populate the folder.

---

## 23. Change Approval

VehicleGuard is currently an individual engineering project.

Therefore, formal organizational approval roles such as:

```text
Change Control Board
Project Manager
Safety Manager
System Architect
Customer Representative
```

are not artificially assigned.

For the current project, approval means that the proposed change has been reviewed for engineering impact and intentionally accepted into the VehicleGuard scope.

If the project later involves additional contributors, explicit review and approval responsibilities may be introduced.

---

## 24. Emergency Changes

VehicleGuard V1 does not currently define a separate emergency change process.

If a critical defect is discovered, the required correction may be implemented quickly, but the technical impact and affected verification must still be documented.

Urgency does not remove the need to maintain consistency between:

```text
Requirements
Architecture
Interfaces
Implementation
Tests
Evidence
```

---

## 25. Change Completion Criteria

A technical change may be considered complete when:

- the Change Request contains sufficient information;
- the impact has been reviewed;
- the change has been approved where required;
- affected engineering artifacts have been updated;
- traceability has been reviewed;
- affected tests have been updated;
- required verification has been performed;
- verification evidence has been updated where applicable;
- no known inconsistent project artifact remains;
- the Change Request status has been updated.

For changes made before prototype verification exists, verification-related actions may remain pending until the applicable implementation becomes available.

---

## 26. Current Change Management Status

The current VehicleGuard change management status is:

```text
Process Defined - Initial Development
```

The project is still in the initial engineering definition and implementation phase.

No artificial Change Requests are created for work that is already part of the planned initial V1 development.

The `CR-xxx` process will be used when a genuine modification to the established VehicleGuard definition is proposed.

As requirements, architecture, interfaces, implementation, and verification become more mature, change control will become increasingly important for maintaining consistency across the project.
