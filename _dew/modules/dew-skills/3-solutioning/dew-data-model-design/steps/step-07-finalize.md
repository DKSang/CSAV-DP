# Step 07 — Finalize Data Model Design

## Mandatory Rules

- Do not finalize if model grain gate is unresolved.
- Do not finalize if primary KPI has no Gold model or approved deferment.
- Run checklist.

## Required outputs

- data-model-spec.md
- kpi-to-model-mapping.md
- decision log entries
- learning log entries if enabled

## Final status

Set:

```yaml
status: final
stepsCompleted:
  - step-01-init
  - step-02-load-transformation-context
  - step-03-model-grain-gate
  - step-04-silver-model-design
  - step-05-gold-model-design
  - step-06-history-and-bridge-design
  - step-07-finalize
```

## Next workflow

Recommend:

`dew-data-quality-design`
