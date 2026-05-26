# Step 06 — Finalize Ingestion Design

## Mandatory Rules

- Do not finalize if ingestion pattern is unresolved.
- Do not finalize if schema evolution is unresolved.
- Do not finalize if idempotency/replay/failure handling are missing.
- Run checklist.

## Task

Finalize ingestion design.

## Required outputs

- ingestion-design.md
- ingestion-decision-record.md
- ingestion-source-plan.md
- decision log entries
- learning log entries if enabled

## Final status

Set:

```yaml
status: final
stepsCompleted:
  - step-01-init
  - step-02-load-source-and-storage-context
  - step-03-ingestion-pattern-gate
  - step-04-snapshot-incremental-and-frequency-gates
  - step-05-schema-evolution-failure-replay-design
  - step-06-finalize