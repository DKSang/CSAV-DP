# Step 05 — Incident, Backfill, and Change Process

## Mandatory Rules

- Incidents must have owner/action path or caveat.
- Backfill must respect idempotency and raw retention.
- Change process must cover schema, KPI, business rules, DQ, serving contract.

## Task

Define operational processes.

## Incident process

Define:
- detection
- severity
- owner
- response
- communication
- serving caveat/update
- resolution evidence

## Backfill process

Define:
- source of truth
- raw availability
- date range selection
- rerun behavior
- downstream recomputation
- DQ validation
- serving refresh

## Change process

Define for:
- source schema change
- source freshness/access change
- KPI formula change
- business rule change
- DQ rule change
- serving contract change
- access policy change

## Update

Update:
- dataops-runbook.md
- operational-readiness-report.md

## Continue checkpoint

Ask:

`[C] Continue to CI CD environments and handoff`
