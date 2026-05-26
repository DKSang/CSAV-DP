# Source Scorecard Template

```markdown
---
title: "{Project Name} Source Scorecard"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "2-plan-workflows"
decisionGates:
  GATE-08-source-trust:
    status: pending
evidence: []
assumptions: []
caveats:
  - "Source priority here is assessment priority, not final acceptance."
---

# Source Scorecard: {Project Name}

## 0. Status Note

This scorecard prioritizes source validation.

It does not accept sources as P1/P2. Final source acceptance happens in `dew-source-validation`.

## 1. Source Assessment Summary

| Source ID | Source Name | KPI Relevance | Risk | Validation Priority |
|---|---|---|---|---|
| SRC-001 | | High/Medium/Low | High/Medium/Low | Validate first |

## 2. Source Scorecards

## SRC-001 — {Source Name}

### Expected Role

### Related KPI(s)

### Access Risk

Low / Medium / High / Unknown

Notes:

### Ownership / Provider Clarity

Clear / Partial / Unknown

Notes:

### Field Coverage

Expected coverage:
- Full
- Partial
- Unknown
- Weak

Notes:

### Grain Compatibility

Expected:
- Compatible
- Requires aggregation
- Requires bridge
- Incompatible
- Unknown

Notes:

### Freshness Fit

Expected:
- Meets requirement
- Might meet requirement
- Does not meet requirement
- Unknown

Notes:

### Schema Stability Risk

Low / Medium / High / Unknown

Notes:

### Privacy / Security Risk

Low / Medium / High / Unknown

Notes:

### License / Usage Risk

Low / Medium / High / Unknown

Notes:

### Operational Reliability

Low / Medium / High / Unknown

Notes:

### Validation Effort

Low / Medium / High

Notes:

### Recommended Validation Priority

- Validate first
- Validate later
- Exploration only
- Reject early
- Blocked

### Rationale

### Evidence Needed

- Access check
- Sample
- Schema snapshot
- Profiling
- Freshness observation
- Contract test

## 3. Validation Plan

| Source ID | Priority | Required Evidence | Next Skill |
|---|---|---|---|
| SRC-001 | Validate first | Access, sample, schema | dew-source-validation |

## 4. Open Questions

## 5. Next Workflow

Recommended next:

`dew-source-validation`s