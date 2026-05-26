# Step 05 — DQ Severity and Action Policy

## Mandatory Rules

- Every DQ rule must have severity.
- Every DQ rule must have action.
- Blocking rules must be explicit.

## Task

Assign severity and actions.

## Severity

- Critical
- High
- Medium
- Low

## Actions

- fail pipeline
- quarantine records
- warn and continue
- log only
- require user review

## Required table

| Rule ID | Severity | Action | Pipeline Continues? | Data Served? |
|---|---|---|---|---|

## Update

Update:
- dq-rule-catalog.md
- dq-gate-policy.md
- data-quality-rules.md

## Continue checkpoint

Ask:

`[C] Continue to DQ evidence and test handoff`
