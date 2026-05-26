# Source Validation Report Template

```markdown
---
title: "{Project Name} Source Validation Report"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "2-plan-workflows"
stepsCompleted: []
decisionGates:
  GATE-07-source-access:
    status: pending
  GATE-08-source-trust:
    status: pending
  GATE-09-source-grain:
    status: pending
  GATE-10-source-freshness:
    status: pending
  GATE-11-schema-evolution:
    status: pending
evidence: []
assumptions: []
caveats:
  - "A source is not accepted as P1 unless access, sample, schema, grain/freshness, and trust evidence are documented."
---

# Source Validation Report: {Project Name}

## 0. Document Purpose

This report validates whether candidate sources can be used for the data product.

It must be completed before final architecture.

## 1. Input Artifacts

| Artifact | Path | Loaded? | Notes |
|---|---|---|---|
| Source Inventory | | Yes/No | |
| Source Scorecard | | Yes/No | |
| KPI Catalog | | Yes/No | |
| KPI Source Matrix | | Yes/No | |
| KPI Feasibility Report | | Yes/No | |
| Data Product PRD | | Yes/No | |
| Decision Log | | Yes/No | |
| Evidence Index | | Yes/No | |

## 2. Source Validation Summary

| Source ID | Source Name | Access | Sample | Schema | Grain | Freshness | DQ Profile | Recommended Status |
|---|---|---|---|---|---|---|---|---|
| SRC-001 | | Unknown | Missing | Missing | Unknown | Unknown | Missing | Candidate |

## 3. Source Detail

## SRC-001 — {Source Name}

### Source Role

### Related KPI(s)

| KPI ID | Dependency Type | Required Fields |
|---|---|---|
| KPI-001 | Required/Optional | |

### Access Validation

Status:
- Verified
- Blocked
- Manual only
- Unknown
- Failed

Evidence:
- access log:
- notes:

### Sample Validation

Status:
- Sample available
- Sample missing
- Sample invalid
- Sample stale

Evidence:
- sample path:
- row count:
- file size:
- sample date:

### Schema Snapshot

Status:
- Captured
- Missing
- Unstable
- Unknown

Evidence:
- schema path:
- field count:
- schema date:

### Field Coverage

| Required Field | Candidate Source Field | Available? | Notes |
|---|---|---|---|
| | | Yes/No/Unknown | |

### Grain Validation

Expected grain:

Observed grain:

Status:
- Confirmed
- Requires aggregation
- Requires bridge/mapping
- Incompatible
- Unknown

### Freshness Validation

Required freshness:

Observed freshness:

Status:
- Meets requirement
- Acceptable with caveat
- Does not meet requirement
- Unknown

### Profiling / Data Quality Notes

- nulls:
- duplicates:
- invalid ranges:
- unexpected values:
- row count:
- time coverage:
- geography/entity coverage:

### Schema Evolution Behavior

Choose one:

A. Strict schema contract  
B. Schema snapshot + drift detection  
C. Flexible rescued fields  
D. Manual review on change  

Selected:

### Privacy / Security Notes

### Source Validation Status

Choose one:

- P1 — Use in MVP
- P2 — Use later
- Exploration only
- Rejected
- Blocked

### Caveats

### Decision Required

A. Promote to P1  
B. Keep as P2  
C. Exploration only  
D. Reject  
E. Block pending access/evidence  

### User Decision

## 4. KPI-Source Coverage After Validation

| KPI ID | Required Source | Validated Source? | Coverage | Caveat |
|---|---|---|---|---|
| KPI-001 | SRC-001 | Yes/No | Full/Partial/None | |

## 5. Architecture Readiness Impact

Can architecture proceed?

A. Yes  
B. Yes, with caveats  
C. No, source validation unresolved  
D. Reduce MVP scope  

Decision:

## 6. Evidence Links

| Evidence ID | Type | Path | Related Source | Status |
|---|---|---|---|---|
| EVD-001 | source-sample | | SRC-001 | |

## 7. Open Issues

## 8. Next Workflow

Recommended next:

`dew-requirement-gate`