# Data Quality Rules Template

```markdown
---
title: "{Project Name} Data Quality Rules"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-18-data-quality-rule:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# Data Quality Rules: {Project Name}

## 0. Document Purpose

This document defines data quality rules, severity, action policy, evidence requirements, and implementation handoff.

## 1. Input Context

| Input | Path | Status | Notes |
|---|---|---|---|
| Data Model Spec | | Loaded/Missing | |
| Transformation Design | | Loaded/Missing | |
| Source Validation | | Loaded/Missing | |
| KPI Feasibility | | Loaded/Missing | |
| PRD | | Loaded/Missing | |

## 2. Trust Expectation

Selected trust level:

DQ implication:

## 3. DQ Rule Summary

| Rule ID | Layer | Dataset | Field/Key | Rule Type | Severity | Action | Related KPI |
|---|---|---|---|---|---|---|---|
| DQ-001 | Silver | | | not_null | High | fail/quarantine/warn | KPI-001 |

## 4. Source-Level DQ Rules

## 5. Bronze / Ingestion DQ Rules

## 6. Silver DQ Rules

## 7. Gold / KPI DQ Rules

## 8. Serving DQ Rules

## 9. DQ Gate Policy

| Severity | Default Action | Can Proceed? | Requires User Approval? |
|---|---|---|---|
| Critical | fail | No | Yes |
| High | fail/quarantine | Usually no | Yes |
| Medium | warn/caveat | Maybe | Maybe |
| Low | warn/log | Yes | No |

## 10. DQ Evidence Requirements

Evidence to produce during implementation:
- test result
- row count
- null report
- duplicate report
- range check report
- referential integrity report
- freshness check
- KPI plausibility result

## 11. Handoff to Implementation

Implementation stories must include:
- DQ rule IDs
- expected test files
- pass/fail behavior
- evidence output paths
- caveats
```
