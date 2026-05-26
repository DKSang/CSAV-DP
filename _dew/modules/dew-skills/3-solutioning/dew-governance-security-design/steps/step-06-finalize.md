# Step 06 — Finalize Governance Security Design

## Mandatory Rules

- Do not finalize if privacy posture gate is unresolved.
- Do not finalize if access control is unresolved.
- Run checklist.

## Required outputs

- governance-security-review.md
- access-control-matrix.md
- governance-decision-record.md
- decision log entries
- learning log entries if enabled

## Final status

Set:

```yaml
status: final
stepsCompleted:
  - step-01-init
  - step-02-load-serving-and-data-context
  - step-03-privacy-posture-gate
  - step-04-access-control-and-ownership
  - step-05-lineage-metadata-and-auditability
  - step-06-finalize
```

## Next workflow

Recommend:

`dew-dataops-design`
