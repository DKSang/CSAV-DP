# Governance Security Review Template

```markdown
---
title: "{Project Name} Governance Security Review"
status: draft
created: {YYYY-MM-DD}
updated: YYYY-MM-DD
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-21-privacy-posture:
    status: pending
  GATE-access-control:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# Governance Security Review: {Project Name}

## 0. Document Purpose

This document defines governance, privacy, security, access control, lineage, metadata, and auditability expectations.

## 1. Input Context

| Input | Path | Status | Notes |
|---|---|---|---|
| Serving Spec | | Loaded/Missing | |
| Trust Statement | | Loaded/Missing | |
| Data Model Spec | | Loaded/Missing | |
| DQ Rules | | Loaded/Missing | |
| Source Validation | | Loaded/Missing | |
| Storage Design | | Loaded/Missing | |
| Ingestion Design | | Loaded/Missing | |

## 2. Data Sensitivity Review

| Dataset / Asset | Contains Sensitive Data? | Type | Risk | Notes |
|---|---|---|---|---|
| | Yes/No/Unknown | PII/Internal/Public/etc. | Low/Medium/High | |

## 3. Privacy Posture

Choose one:

A. No sensitive data identified  
B. Low-risk internal data  
C. PII/sensitive data present with controls  
D. High-risk data requiring governance review  
E. Unknown; block until reviewed  

Selected:

## 4. Access Control Matrix

See:

`access-control-matrix.md`

## 5. Ownership

| Asset | Owner | Steward | Technical Owner | Notes |
|---|---|---|---|---|

## 6. Lineage and Metadata

### Required Lineage

### Required Metadata

### Evidence Links

## 7. Auditability

What needs to be auditable:
- source input
- ingestion run
- transformation run
- DQ result
- metric definition
- user-facing caveat
- access decision

## 8. Governance Risks

| Risk ID | Risk | Severity | Mitigation |
|---|---|---|---|

## 9. Handoff to DataOps

DataOps must operationalize:
- monitoring
- logs
- access checks
- DQ evidence
- incident process
- change process
```
