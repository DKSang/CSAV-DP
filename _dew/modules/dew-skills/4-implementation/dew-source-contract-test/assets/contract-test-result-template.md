# Contract Test Result Template

```markdown
---
title: "Source Contract Test Result — {Source ID}"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
relatedSource: "{Source ID}"
evidenceType: "source-contract-test-result"
---

# Source Contract Test Result: {Source ID} — {Source Name}

## Result Summary

Overall status:

- pass
- pass-with-caveats
- fail
- blocked
- not-run

## Test Results

| Test ID | Test Name | Expected | Observed | Status | Notes |
|---|---|---|---|---|---|
| SCT-001 | Required fields exist | | | pass/fail | |

## Findings

| Severity | Finding | Impact | Required Action |
|---|---|---|---|
| High/Medium/Low | | | |

## Caveats

## Downstream Impact

- KPI feasibility:
- Architecture:
- Ingestion:
- Transformation:
- Serving:

## Recommendation

A. Accept contract result  
B. Accept with caveats  
C. Rerun after fixing source/sample  
D. Reject/block source  

## User Decision