# Step 08 — Finalize Data Architecture

## Mandatory Rules

- Do not finalize if architecture pattern gate is unresolved.
- Do not finalize if technology decision gate is unresolved unless explicitly deferred by user.
- Do not hide caveats.
- Do not mark detailed storage/ingestion/transformation/serving complete here.
- Run checklist before finalizing.

## Task

Finalize data architecture.

## Run checklist

Use:

`{workflow.checklist}`

## Required final outputs

- `data-architecture.md`
- `architecture-decision-record.md`
- `architecture-caveat-carryover.md`
- decision log entries
- learning log entries if enabled

## Final status

Set:

```yaml
status: final
updated: {date}
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context
  - step-03-lifecycle-architecture
  - step-04-architecture-pattern-gate
  - step-05-technology-decision-gate
  - step-06-risk-caveat-and-reversibility
  - step-07-dataops-security-governance-undercurrents
  - step-08-finalize