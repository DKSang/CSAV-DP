# Step 06 — Finalize Serving Design

## Mandatory Rules

- Do not finalize if serving mode gate is unresolved.
- Do not finalize if trust/limitations statement is unresolved.
- Run checklist.

## Required outputs

- serving-data-product-spec.md
- metric-serving-contract.md
- trust-and-limitations-statement.md
- decision log entries
- learning log entries if enabled

## Final status

Set:

```yaml
status: final
stepsCompleted:
  - step-01-init
  - step-02-load-model-dq-context
  - step-03-serving-mode-gate
  - step-04-metric-contract-and-consumer-experience
  - step-05-trust-limitations-and-feedback
  - step-06-finalize
```

## Next workflow

Recommend:

`dew-governance-security-design`
