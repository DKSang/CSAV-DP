# Step 02 — Load Pipeline, Serving, and Governance Context

## Mandatory Rules

- Load all operationally relevant designs before readiness decision.
- Do not invent owners, schedules, or monitoring that are not supported by design.

## Task

Extract DataOps context.

## Extract

From ingestion:
- source plans
- frequency
- schema evolution
- failure handling
- replay/backfill

From transformation/model:
- model dependencies
- Gold outputs
- KPI calculations

From DQ:
- critical rules
- evidence requirements
- DQ gate policy

From serving:
- serving assets
- freshness expectation
- trust limitations

From governance:
- access controls
- privacy posture
- ownership/audit requirements

## Update

Update:
- dataops-runbook.md
- observability-plan.md
- operational-readiness-report.md

## Continue checkpoint

Ask:

`[C] Continue to operational readiness gate`
