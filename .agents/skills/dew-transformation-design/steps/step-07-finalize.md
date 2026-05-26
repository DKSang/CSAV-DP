# Step 07 — Finalize Transformation Design

## Mandatory Rules

- Do not finalize if grain gate is unresolved.
- Do not finalize if business rule gate is unresolved.
- Do not finalize if primary KPI Gold logic is unresolved unless user approved caveat.
- Run checklist.

## Task

Finalize transformation design.

## Required outputs

- transformation-design.md
- business-rule-catalog.md
- transformation-decision-record.md
- decision log entries
- learning log entries if enabled

## Final status

Set:

```yaml
status: final
stepsCompleted:
  - step-01-init
  - step-02-load-storage-ingestion-context
  - step-03-grain-transformation-gate
  - step-04-bronze-to-silver-rules
  - step-05-silver-to-gold-rules
  - step-06-business-rule-gate
  - step-07-finalize
```

## Next workflow

Recommend:

`dew-data-model-design`
