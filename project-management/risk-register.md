# Project Risk Register

## 1. Purpose

This document identifies and tracks project risks that may affect the development of VehicleGuard.

The purpose of the risk register is to identify potential problems early, evaluate their possible impact on the project, and define actions that reduce the probability or consequences of these risks.

This register focuses on **project and development risks**, such as unclear requirements, uncontrolled scope growth, insufficient traceability, or problems with verification.

Technical hazards and failure scenarios related to the behaviour of the VehicleGuard system itself are handled separately in the system risk analysis.

The risk register will be reviewed and updated as the project develops.

---

## 2. Risk Assessment Method

Each identified project risk is evaluated using two factors:

* **Probability** — how likely the risk is to occur.
* **Impact** — how strongly the risk could affect the project if it occurs.

Both factors use a three-level scale.

### Probability

| Level  | Rating | Description                                                    |
| ------ | -----: | -------------------------------------------------------------- |
| Low    |      1 | The risk is unlikely to occur during the project.              |
| Medium |      2 | The risk could occur under realistic project conditions.       |
| High   |      3 | The risk is likely to occur unless preventive action is taken. |

### Impact

| Level  | Rating | Description                                                                                          |
| ------ | -----: | ---------------------------------------------------------------------------------------------------- |
| Low    |      1 | Limited effect. Minor rework may be required.                                                        |
| Medium |      2 | Noticeable effect on requirements, documentation, implementation, testing, or schedule.              |
| High   |      3 | Significant effect that may require major rework or prevent a project objective from being achieved. |

The overall risk score is calculated as:

**Risk Score = Probability × Impact**

This produces a score between **1 and 9**.

---

## 3. Risk Classification

The calculated score is used to determine the overall risk level.

| Score | Risk Level | Expected Action                                 |
| ----: | ---------- | ----------------------------------------------- |
|   1–2 | Low        | Accept and monitor                              |
|   3–4 | Medium     | Monitor and define mitigation where appropriate |
|   6–9 | High       | Mitigation action required                      |

The score is used to support prioritization. Engineering judgement is still required when evaluating individual risks.

A low numerical score does not automatically mean that a risk can be ignored.

---

## 4. Risk Register

| ID     | Risk                                                                                                                           | Probability | Impact | Score | Mitigation                                                                                                                                                                                          | Status |
| ------ | ------------------------------------------------------------------------------------------------------------------------------ | ----------: | -----: | ----: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| PR-001 | Project scope becomes too large and introduces functionality that is not necessary for VehicleGuard V1.                        |           3 |      2 |     6 | Keep the V1 scope limited to the defined vehicle parameters and core diagnostic functions. New functionality must be evaluated before being added and may be introduced through a change request.   | Open   |
| PR-002 | System requirements are ambiguous or not sufficiently measurable.                                                              |           2 |      3 |     6 | Review requirements before implementation. Use clear terminology, defined conditions and measurable criteria where applicable.                                                                      | Open   |
| PR-003 | Requirements are created without a practical method of verification.                                                           |           2 |      3 |     6 | Define the intended verification method when important system requirements are created. Requirements that cannot be verified must be reviewed and refined.                                          | Open   |
| PR-004 | Prototype implementation begins to determine the requirements instead of being based on previously defined system behaviour.   |           2 |      3 |     6 | Establish an initial requirements baseline before implementing the diagnostic prototype. Changes discovered during implementation must be documented instead of silently changing the requirements. | Open   |
| PR-005 | Automotive assumptions or demonstration thresholds are presented as if they were valid for real production vehicles.           |           2 |      3 |     6 | Clearly document assumptions and distinguish conceptual or simulated behaviour from production automotive behaviour. Demonstration thresholds should be configurable where practical.               | Open   |
| PR-006 | Changes to requirements, architecture or implementation are not reflected in related tests and documentation.                  |           2 |      3 |     6 | Maintain unique requirement IDs and traceability between requirements, architecture elements and test cases. Review affected items whenever a controlled change is introduced.                      | Open   |
| PR-007 | The prototype becomes unnecessarily complex and shifts the project focus from systems engineering toward software development. |           2 |      2 |     4 | Keep the prototype limited to functionality required to demonstrate and verify the system concept. Additional software features must have a clear engineering purpose.                              | Open   |

---

## 5. Risk Status

The following status values are used in the register:

**Open**
The risk is currently relevant and requires monitoring or mitigation.

**Monitoring**
Mitigation measures have been introduced, but the risk remains relevant and continues to be observed.

**Closed**
The risk is no longer considered active or has been sufficiently addressed.

**Accepted**
The risk is understood and intentionally accepted because additional mitigation is not considered necessary or proportionate.

---

## 6. Risk Review and Maintenance

The risk register is a living project document and will be updated throughout the development of VehicleGuard.

A review should be performed when:

* important requirements are added or modified;
* the system architecture changes;
* prototype implementation reveals a new technical or project limitation;
* a change request is introduced;
* verification identifies an unexpected problem;
* the project scope changes;
* an existing mitigation action significantly changes the probability or impact of a risk.

New risks will receive the next available `PR-XXX` identifier.

Existing risk identifiers will not be reused for unrelated risks.

When mitigation actions have been implemented, the probability and impact may be reassessed. If the risk is no longer relevant, its status can be changed to `Closed` rather than deleting it from the register.

Keeping closed risks in the project history makes it possible to understand how risks and engineering decisions evolved during development.

---

## 7. Current Risk Summary

At the current project stage, the main risks are related to requirements quality, project scope and maintaining the intended systems engineering focus.

Several risks currently have a high score because the project is still in the early definition phase. These risks are expected to decrease as the requirements, architecture, traceability model and verification strategy become more mature.

The risk assessment will therefore be reviewed after the initial system requirements and system architecture have been defined.

