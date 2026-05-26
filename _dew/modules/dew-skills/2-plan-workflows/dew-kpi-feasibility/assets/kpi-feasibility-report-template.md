# KPI Feasibility Report Template

```markdown
---
title: "{Project Name} KPI Feasibility Report"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "2-plan-workflows"
stepsCompleted: []
decisionGates:
  GATE-06-kpi-feasibility:
    status: pending
evidence: []
assumptions: []
caveats:
  - "A KPI is not verified unless field availability, grain compatibility, and sample computation are supported by evidence."
---

# KPI Feasibility Report: {Project Name}

## 0. Document Purpose

This report evaluates whether candidate KPIs can be computed from available data.

It does not design architecture.

Architecture may start only after primary KPI feasibility is verified or explicitly caveated.

## 1. Input Artifacts

| Artifact | Path | Loaded? | Notes |
|---|---|---|---|
| Project Brief | | Yes/No | |
| Business Discovery | | Yes/No | |
| KPI Catalog | | Yes/No | |
| KPI Source Matrix | | Yes/No | |
| Data Product PRD | | Yes/No | |
| Decision Log | | Yes/No | |
| Evidence Index | | Yes/No | |

## 2. KPI Feasibility Summary

| KPI ID | KPI Name | Priority | Current Status | Recommended Status | Decision Needed |
|---|---|---|---|---|---|
| KPI-001 | | Primary/Secondary | Hypothesis | | Yes/No |

## 3. KPI Detail

## KPI-001 — {KPI Name}

### Business Question

### Decision Supported

### Consumer

### Formula

### Target Grain

### Required Fields

| Required Field | Meaning | Candidate Source | Source Field | Field Available? | Evidence |
|---|---|---|---|---|---|
| | | | | Unknown/Yes/No | |

### Grain Compatibility

Target KPI grain:

Candidate source grain:

Compatibility:
- Compatible
- Requires aggregation
- Requires join/bridge
- Incompatible
- Unknown

Evidence:

### Sample Computation Requirement

Required prototype type:
- SQL
- Python
- Notebook
- Manual calculation
- Not possible yet

Prototype path:

Sample output path:

### Data Quality Checks Needed

- not_null:
- valid_range:
- duplicate check:
- freshness:
- referential integrity:
- business rule consistency:

### Feasibility Status

Choose one:

- Verified on sample
- Feasible with caveats
- Hypothesis only
- Deferred
- Rejected

Current:

### Caveats

### Decision Required

A. Accept as feasible on sample  
B. Accept with caveats  
C. Keep as hypothesis  
D. Defer from MVP  
E. Reject KPI  

### User Decision

## 4. KPI Feasibility Matrix

| KPI ID | Required Fields Verified? | Grain Compatible? | Sample Computed? | Output Reviewed? | Final Status |
|---|---|---|---|---|---|
| KPI-001 | No | Unknown | No | No | Hypothesis only |

## 5. Architecture Readiness Impact

Can architecture proceed?

A. Yes  
B. Yes, with caveats  
C. No, return to KPI feasibility  
D. Reduce MVP scope  

Decision:

## 6. Open Issues

## 7. Evidence Links

| Evidence ID | Type | Path | Related KPI | Status |
|---|---|---|---|---|
| EVD-001 | | | | |

## 8. Next Workflow

Required next:
- `dew-kpi-prototype`
- `dew-kpi-validation-review`

Then:
- `dew-source-validation`
- `dew-requirement-gate`