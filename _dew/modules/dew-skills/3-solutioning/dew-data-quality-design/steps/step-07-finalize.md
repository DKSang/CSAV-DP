# Step 07 — Finalize Data Quality Design

## Mandatory Rules

- Do not finalize if DQ rule gate is unresolved.
- Do not finalize if critical datasets have no DQ rules.
- Run checklist.

## Required outputs

- data-quality-rules.md
- dq-rule-catalog.md
- dq-gate-policy.md
- decision log entries
- learning log entries if enabled

## Final status

Set:

```yaml
status: final
stepsCompleted:
  - step-01-init
  - step-02-load-model-and-source-context
  - step-03-dq-rule-discovery
  - step-04-dq-rule-gate
  - step-05-dq-severity-and-action-policy
  - step-06-dq-evidence-and-test-handoff
  - step-07-finalize
```

## Next workflow

Recommend:

`dew-serving-design`
