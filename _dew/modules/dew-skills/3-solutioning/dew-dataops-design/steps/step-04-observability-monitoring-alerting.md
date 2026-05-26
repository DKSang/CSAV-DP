# Step 04 — Observability, Monitoring, and Alerting

## Mandatory Rules

- Monitoring must match operational mode and trust expectation.
- Critical DQ rules require observable evidence.
- Freshness must be monitored if it is part of the trust statement.

## Task

Define observability plan.

## Required monitors

Consider:
- source access success
- ingestion row count
- schema drift
- freshness
- critical DQ failures
- transformation success
- Gold output availability
- serving asset refresh
- access/security events
- cost/resource usage if relevant

## Required table

| Monitor ID | Area | Signal | Threshold | Severity | Action |
|---|---|---|---|---|---|

## Update

Update:
- observability-plan.md
- dataops-runbook.md

## Continue checkpoint

Ask:

`[C] Continue to incident backfill and change process`
