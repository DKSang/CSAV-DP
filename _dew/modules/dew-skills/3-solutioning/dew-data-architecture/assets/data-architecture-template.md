# Data Architecture Template

```markdown
---
title: "{Project Name} Data Architecture"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-13-architecture-pattern:
    status: pending
  GATE-14-technology-choice:
    status: pending
evidence: []
assumptions: []
caveats: []
architecturePattern:
  status: pending
technologyDecisions:
  status: pending
---

# Data Architecture: {Project Name}

## 0. Document Purpose

This architecture translates validated/caveated requirements into a data engineering architecture.

It is grounded in:
- Requirement Gate Report
- KPI Feasibility Report
- Source Validation Report
- Evidence Index
- Decision Log
- Caveat Register

This document does not replace detailed storage, ingestion, transformation, serving, or governance designs.

Those are created in later DEW skills.

## 1. Validated Context

### Data Product

### Data Consumers

### Decisions Supported

### Trust Expectation

### MVP Scope

### Explicit Non-Goals

## 2. Evidence-Grounded Inputs

| Input | Status | Evidence | Caveat |
|---|---|---|---|
| Primary KPI feasibility | Ready/Caveated/Blocked | | |
| P1 source validation | Ready/Caveated/Blocked | | |
| Product grain | Ready/Caveated/Blocked | | |
| Freshness | Ready/Caveated/Blocked | | |
| Trust expectation | Ready/Caveated/Blocked | | |
| Requirement gate | Ready/Caveated/Blocked | | |

## 3. Data Engineering Lifecycle Architecture

### 3.1 Generation / Source Systems

Validated sources:

| Source ID | Source Name | Role | Validation Status | Caveat |
|---|---|---|---|---|

Source constraints:
- access:
- schema stability:
- grain:
- freshness:
- quality:
- privacy/security:

### 3.2 Storage

Architecture-level storage intent:

- Raw/Bronze:
- Silver:
- Gold:
- Metadata:
- Evidence retention:

Detailed storage design deferred to:

`dew-storage-design`

### 3.3 Ingestion

Architecture-level ingestion intent:

- ingestion mode:
- batch/streaming assumption:
- snapshot/incremental direction:
- replay/backfill expectation:
- schema drift direction:

Detailed ingestion design deferred to:

`dew-ingestion-design`

### 3.4 Transformation

Architecture-level transformation intent:

- grain transformations:
- KPI computation layer:
- conformance logic:
- business rule ownership:
- bridge/mapping needs:

Detailed transformation design deferred to:

`dew-transformation-design`

### 3.5 Serving

Architecture-level serving intent:

- serving mode:
- consumers:
- freshness:
- trust statement:
- limitations:

Detailed serving design deferred to:

`dew-serving-design`

## 4. Architecture Pattern Decision

Options considered:
- Local-first
- Warehouse-first
- Lakehouse
- Hybrid
- Streaming-first
- Application-integrated

Selected pattern:

Rationale:

Trade-offs:

Rejected alternatives:

Revisit trigger:

## 5. Technology Decision Summary

| Decision Area | Selected Direction | Alternatives | Rationale | Revisit Trigger |
|---|---|---|---|---|
| Local development | | | | |
| Storage format | | | | |
| Compute engine | | | | |
| Orchestration | | | | |
| Transformation tool | | | | |
| Quality/testing | | | | |
| Serving layer | | | | |
| Documentation/catalog | | | | |

## 6. Caveat Carryover

| Caveat ID | Area | Description | Architecture Impact | Later Skill Responsible |
|---|---|---|---|---|
| CAV-001 | | | | |

## 7. DataOps, Security, and Governance Undercurrents

### Security

### Privacy

### Access Control

### Observability

### Orchestration

### Data Management

### Software Engineering Practices

### Cost / FinOps

## 8. Architecture Risks

| Risk ID | Risk | Severity | Mitigation | Owner / Later Skill |
|---|---|---|---|---|

## 9. Reversible vs Hard-to-Reverse Decisions

| Decision | Reversibility | Why | Revisit Trigger |
|---|---|---|---|

## 10. Open Questions

## 11. Architecture Handoff

Next skills:

- `dew-storage-design`
- `dew-ingestion-design`
- `dew-transformation-design`
- `dew-serving-design`
- `dew-governance-security-design`