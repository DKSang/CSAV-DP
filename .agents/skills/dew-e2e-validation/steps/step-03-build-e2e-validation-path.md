# Step 03 — Build E2E Validation Path

## Mandatory Rules

- E2E path must include all relevant lifecycle stages.
- Do not call story-level validation E2E unless it covers full path.
- Missing lifecycle stage must be flagged.

## Required stages

- source access
- Bronze ingestion
- schema snapshot
- Silver transformation
- Gold model / KPI
- DQ
- serving
- trust/limitations
- observability/logging

## Required table

| Stage | Expected Evidence | Actual Evidence | Status |
|---|---|---|---|

## Validation method options

A. Run E2E command  
B. Review existing story evidence  
C. Manual walkthrough  
D. Hybrid  

Recommend one.

## Update

Update e2e report.

## Continue checkpoint

Ask:

`[C] Continue to run or review E2E validation`
