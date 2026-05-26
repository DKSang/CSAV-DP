# Step 06 — Finalize Storage Design

## Mandatory Rules

- Do not finalize if storage layer gate is unresolved.
- Do not finalize if metadata/retention decisions are unresolved.
- Do not hide caveats.
- Run checklist.

## Task

Finalize storage design.

## Required outputs

- storage-design.md
- storage-decision-record.md
- source-to-storage-mapping.md
- decision log entry
- learning log entry if enabled

## Final status

Set:

```yaml
status: final
stepsCompleted:
  - step-01-init
  - step-02-load-architecture-context
  - step-03-storage-layer-gate
  - step-04-metadata-retention-schema-gates
  - step-05-source-to-storage-mapping
  - step-06-finalize