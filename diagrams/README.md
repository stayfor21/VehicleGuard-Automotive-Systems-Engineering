# VehicleGuard Engineering Diagrams

This directory contains the engineering diagrams used to support the VehicleGuard V1 system documentation.

The diagrams provide visual representations of the system context, stakeholder relationships, architecture, functional decomposition, interfaces, requirements traceability, risk analysis, and verification approach.

They are supporting engineering artifacts and should be interpreted together with the corresponding documents in the `docs/` and `project-management/` directories.

---

## Diagram Index

| Diagram | Purpose | Related Document |
|---|---|---|
| `system-context.png` | Defines the VehicleGuard system boundary and its interaction with external actors and systems. | `docs/01-project-overview.md` |
| `stakeholder-map.png` | Shows the main VehicleGuard stakeholder groups and their relationship to the system. | `docs/02-stakeholders.md` |
| `requirements-traceability.png` | Shows the traceability chain from stakeholder needs through system requirements and architecture to verification evidence. | `docs/03-system-requirements.md` |
| `system-architecture.png` | Shows the logical VehicleGuard architecture, major system elements, and their relationships. | `docs/04-system-architecture.md` |
| `functional-decomposition.png` | Decomposes the VehicleGuard system into its primary engineering functions and responsibilities. | `docs/04-system-architecture.md` |
| `interface-data-flow.png` | Shows the primary information flow between external data sources and internal VehicleGuard functions. | `docs/05-interfaces.md` |
| `system-failure-analysis.png` | Shows how selected technical failure scenarios may propagate through the VehicleGuard processing chain. | `docs/06-risk-analysis.md` |
| `verification-v-model.png` | Shows the relationship between system definition, implementation, verification, and validation using the VehicleGuard V-model. | `docs/07-verification-validation.md` |
| `project-risk-matrix.png` | Provides a visual representation of the probability and impact method used for project risk classification. | `project-management/risk-register.md` |

---

## System Context

### `system-context.png`

The System Context Diagram defines VehicleGuard as a system and shows its relationship with external entities.

Its main purpose is to establish:

- the VehicleGuard system boundary;
- external sources of vehicle data;
- driver-oriented outputs;
- diagnostic-oriented outputs;
- interactions that are inside or outside the VehicleGuard scope.

This diagram provides the highest-level view of the system.

---

## Stakeholder Map

### `stakeholder-map.png`

The Stakeholder Map identifies the main groups that interact with, depend on, or influence VehicleGuard.

It supports the definition of stakeholder needs and provides context for the requirements development process.

The stakeholder relationships shown in this diagram are further described in:

```text
docs/02-stakeholders.md
```

---

## Requirements Traceability

### `requirements-traceability.png`

The Requirements Traceability Diagram shows how engineering information is connected across the project.

The intended traceability direction is:

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
Test Case
      |
      v
Verification Evidence
```

The corresponding identifier families are:

```text
SN-xxx
SYS-xxx
COMP-xxx
TC-xxx
RESULT-xxx
```

The diagram also illustrates that relationships are not necessarily one-to-one.

For example:

- one stakeholder need may result in multiple system requirements;
- one system requirement may be allocated to multiple architecture elements;
- one architecture element may implement several requirements;
- multiple test cases may contribute to verification of a requirement.

Detailed traceability data is maintained separately in:

```text
requirements/requirements.xlsx
```

---

## System Architecture

### `system-architecture.png`

The System Architecture Diagram defines the logical structure of VehicleGuard V1.

It shows the major architecture elements responsible for:

- vehicle data input;
- input validation;
- parameter monitoring;
- diagnostic processing;
- severity classification;
- driver warning generation;
- diagnostic event generation;
- configuration.

Architecture elements use the project identifier convention:

```text
COMP-xxx
```

The diagram represents logical engineering responsibilities rather than production ECU deployment.

---

## Functional Decomposition

### `functional-decomposition.png`

The Functional Decomposition Diagram provides a function-oriented view of VehicleGuard.

While the System Architecture Diagram focuses on system elements and their relationships, the Functional Decomposition Diagram focuses on the functions that VehicleGuard must perform.

The decomposition helps connect system requirements with specific engineering responsibilities before implementation.

---

## Interface Data Flow

### `interface-data-flow.png`

The Interface Data Flow Diagram shows how information moves through VehicleGuard.

The primary processing direction is:

```text
Vehicle Data Source
        |
        v
Input
        |
        v
Validation
        |
        v
Monitoring
        |
        v
Diagnostics
        |
        v
Severity Classification
        |
        +------------------+
        |                  |
        v                  v
Driver Warning      Diagnostic Event
```

Configuration information supports the applicable validation, monitoring, diagnostic, and severity functions.

The detailed logical interfaces are defined in:

```text
docs/05-interfaces.md
```

---

## System Failure Analysis

### `system-failure-analysis.png`

The System Failure Analysis Diagram supports the technical risk analysis of VehicleGuard.

It shows how selected failure scenarios may originate in or propagate through the system processing chain.

Examples include problems related to:

- invalid input data;
- incorrect configuration;
- validation behaviour;
- monitoring and diagnostic logic;
- severity classification;
- output generation.

Failure scenarios use identifiers such as:

```text
SCN-01
SCN-02
SCN-03
```

The diagram is a supporting representation of the analysis documented in:

```text
docs/06-risk-analysis.md
```

It is not intended to represent a complete production automotive safety analysis.

---

## Verification and Validation V-Model

### `verification-v-model.png`

The Verification and Validation V-Model shows the relationship between system definition, implementation, verification, and validation.

The left side represents system definition and decomposition.

The bottom represents prototype implementation.

The right side represents verification and validation activities.

The diagram supports the principle that implementation should be derived from previously defined engineering artifacts and subsequently verified against them.

The complete V&V approach is defined in:

```text
docs/07-verification-validation.md
```

---

## Project Risk Matrix

### `project-risk-matrix.png`

The Project Risk Matrix supports project-level risk assessment.

Risks are evaluated using:

```text
Probability x Impact = Risk Score
```

Both probability and impact use a three-level scale.

The resulting score supports classification and prioritization of project risks.

The complete project risk register is maintained in:

```text
project-management/risk-register.md
```

The Project Risk Matrix should not be confused with the technical system failure analysis.

The two artifacts address different types of risk:

```text
project-risk-matrix.png
        |
        +-> Project and development risks

system-failure-analysis.png
        |
        +-> Technical system failure scenarios
```

---

## Diagram Conventions

VehicleGuard diagrams follow a common documentation style.

The diagrams use:

- white backgrounds;
- black text;
- black borders and connectors;
- simple engineering notation;
- consistent technical terminology;
- project identifiers where applicable;
- minimal decorative content.

The objective is readability and engineering clarity rather than presentation graphics.

---

## Relationship Between Diagrams

The diagrams describe different views of the same VehicleGuard system.

They should therefore remain consistent with each other.

At a high level:

```text
System Context
      |
      v
Stakeholders
      |
      v
Requirements
      |
      v
System Architecture
      |
      +-------------------+
      |                   |
      v                   v
Functional           Interfaces
Decomposition
      |                   |
      +---------+---------+
                |
                v
         Failure Analysis
                |
                v
        Verification and
           Validation
```

The Project Risk Matrix operates alongside this technical engineering chain and addresses project execution risks rather than system behaviour.

---

## Diagram Maintenance

A diagram should be reviewed when a controlled technical change affects the information represented by that diagram.

Examples include:

- addition or removal of a system function;
- architecture changes;
- interface changes;
- new or modified stakeholder relationships;
- changes to traceability;
- new technical failure scenarios;
- changes to the verification approach.

Diagram updates should remain consistent with the corresponding source documentation.

Significant technical changes are handled according to:

```text
docs/08-change-management.md
```

---

## Current Diagram Set

The current VehicleGuard V1 diagram set consists of:

```text
diagrams/
|
+-- README.md
+-- functional-decomposition.png
+-- interface-data-flow.png
+-- project-risk-matrix.png
+-- requirements-traceability.png
+-- stakeholder-map.png
+-- system-architecture.png
+-- system-context.png
+-- system-failure-analysis.png
+-- verification-v-model.png
```

Additional diagrams should only be introduced when they provide engineering information that is not already represented clearly by the existing artifacts.
