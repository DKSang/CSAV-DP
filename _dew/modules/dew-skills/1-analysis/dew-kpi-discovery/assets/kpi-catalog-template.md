# KPI Catalog Template

```markdown
---
title: "{Project Name} KPI Catalog"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "1-analysis"
decisionGates:
  GATE-03-kpi-definition:
    status: pending
  GATE-04-kpi-grain:
    status: pending
evidence: []
assumptions: []
caveats:
  - "KPIs are hypotheses until validated by dew-kpi-feasibility."
---

# KPI Catalog: {Project Name}

## 0. Important Status Note

All KPIs in this document are candidate KPIs.

They are not verified until Batch 3 KPI Feasibility validates them with real source/sample data.

## 1. KPI Summary

| KPI ID | KPI Name | Business Question | Consumer | Status |
|---|---|---|---|---|
| KPI-001 | | | | Hypothesis |

## 2. KPI Details

## KPI-001 — {KPI Name}

### Business Question

### Decision Supported

### Consumer

### Formula

### Grain

One row represents:

### Dimensions

- Time:
- Geography:
- Entity:
- Category:

### Required Fields

| Field | Meaning | Required? | Candidate Source | Verified? |
|---|---|---|---|---|
| | | Yes/No | | No |

### Candidate Sources

| Source ID | Source Name | Source Type | Dependency Type | Verified? |
|---|---|---|---|---|
| SRC-001 | | API/File/DB | Required/Optional | No |

### Feasibility Status

Choose one:

- Hypothesis
- Needs source validation
- Needs field validation
- Deferred
- Rejected

Current status: Hypothesis

### Assumptions

- [ASSUMPTION] ...

### Caveats

- ...

### Evidence Links

Do not add evidence unless it exists.

- Field availability:
- Sample computation:
- Sample output:
- Validation report:

## 3. Open KPI Questions

## 4. Next Workflow

Recommended next:

`dew-data-product-prd`

Required later:

`dew-kpi-feasibility`