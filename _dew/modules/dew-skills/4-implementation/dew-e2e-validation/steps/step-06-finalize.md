# Step 06 — Finalize E2E Validation

## Mandatory Rules

- Do not finalize as passed if E2E gate is blocked.
- Run checklist.
- Preserve caveats.

## Required outputs

- e2e-validation-report.md
- e2e-validation-matrix.md
- decision log entry
- learning log entry if enabled

## Final status

Set:

```yaml
status: final
stepsCompleted:
  - step-01-init
  - step-02-load-implemented-context
  - step-03-build-e2e-validation-path
  - step-04-run-or-review-e2e-validation
  - step-05-e2e-validation-gate
  - step-06-finalize
```

## Next workflow

Recommend:

`dew-final-evidence-review`
