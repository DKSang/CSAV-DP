# Epics Template

```markdown
---
title: "{Project Name} Epics"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-23-implementation-readiness:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# Epics: {Project Name}

## 0. Document Purpose

This document converts approved DEW designs into implementation epics.

Each epic must map back to validated design artifacts and define evidence expected from implementation.

## 1. Input Design Artifacts

| Artifact | Path | Loaded? | Status |
|---|---|---|---|
| Data Product PRD | | Yes/No | |
| Requirement Gate | | Yes/No | |
| Data Architecture | | Yes/No | |
| Storage Design | | Yes/No | |
| Ingestion Design | | Yes/No | |
| Transformation Design | | Yes/No | |
| Data Model Spec | | Yes/No | |
| Data Quality Rules | | Yes/No | |
| Serving Design | | Yes/No | |
| Governance Security Review | | Yes/No | |
| DataOps Runbook | | Yes/No | |

## 2. Epic Summary

| Epic ID | Epic Name | Purpose | Depends On | Status |
|---|---|---|---|---|
| EPIC-01 | Foundation and Project Setup | | | backlog |

## 3. Epics

## EPIC-01 — Foundation and Project Setup

### Goal

Set up project structure, configuration, environment, and evidence folders needed for data engineering implementation.

### Design Inputs

- Data Architecture:
- DataOps Runbook:
- Governance/Security:
- Storage Design:

### Scope

In:
- repo/project structure
- config management
- environment setup
- evidence folder setup
- logging conventions

Out:
- actual source ingestion
- actual transformations

### Story Candidates

| Story ID | Story Title | Layer | Depends On | Evidence Required |
|---|---|---|---|---|
| 1.1 | Initialize project structure | foundation | | repo structure evidence |

### Acceptance Criteria

- project structure matches design
- config files exist
- evidence paths exist
- README/run instructions exist

### Evidence Expected

- file list
- setup log
- config sample
- run command output

### Risks / Caveats

## EPIC-02 — Source Access and Bronze Ingestion

### Goal

Implement access and ingestion for validated P1 sources into Raw/Bronze storage.

### Design Inputs

- Source Validation:
- Storage Design:
- Ingestion Design:
- Source Contract Tests:

### Story Candidates

| Story ID | Story Title | Source | Depends On | Evidence Required |
|---|---|---|---|---|
| 2.1 | Implement source access for SRC-001 | SRC-001 | 1.1 | access log |
| 2.2 | Ingest SRC-001 into Bronze | SRC-001 | 2.1 | run log, row count, schema snapshot |

## EPIC-03 — Source Contract and DQ Prechecks

### Goal

Implement source contract tests and ingestion-level DQ checks.

## EPIC-04 — Silver Transformation

### Goal

Implement Bronze → Silver transformation rules.

## EPIC-05 — Gold Modeling and KPI Computation

### Goal

Implement Gold models and KPI computation.

## EPIC-06 — Data Quality Evidence

### Goal

Implement DQ rule catalog tests and evidence outputs.

## EPIC-07 — Serving Data Product

### Goal

Implement dashboard/mart/API/report/web app serving layer.

## EPIC-08 — Governance, Documentation, and Trust Statement

### Goal

Implement documentation, access notes, lineage metadata, and user-facing trust/limitations statement.

## EPIC-09 — DataOps, Observability, and Runbook

### Goal

Implement operational runbook, monitoring, logging, incident/backfill process, and evidence generation.

## 4. Dependency Map

## 5. Implementation Risks

## 6. Open Questions

## 7. Next Workflow

`dew-sprint-planning`
```
