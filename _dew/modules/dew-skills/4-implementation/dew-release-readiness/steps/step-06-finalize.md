# Step 06 — Finalize Release Readiness

## Mandatory Rules

- Do not finalize as release if gate is blocked.
- Run checklist.
- Preserve caveats.

## Required outputs

- release-readiness-report.md
- release-checklist.md
- release-notes.md
- decision log entry
- learning log entry if enabled

## Final status

Set:

```yaml
status: final
stepsCompleted:
  - step-01-init
  - step-02-load-validation-and-evidence
  - step-03-release-scope-review
  - step-04-release-risk-review
  - step-05-release-readiness-gate
  - step-06-finalize
```

## Next workflow

Recommend:

`dew-project-documentation`
