# Step 08 — Finalize Requirement Gate Report

## Mandatory Rules

- Do not finalize as ready if architecture readiness gate is blocked.
- Do not hide unresolved blockers.
- Do not remove caveats from the report.
- Evidence index must be referenced.

## Task

Finalize requirement gate report.

## Run checklist

Use:

`{workflow.checklist}`

## Required outputs

- `requirement-gate-report.md`
- `caveat-register.md`
- `architecture-readiness-matrix.md`
- decision log entry
- learning log entry if enabled

## Final report status

Set:

```yaml
status: final
updated: {date}
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context
  - step-03-kpi-readiness-review
  - step-04-source-readiness-review
  - step-05-trust-grain-freshness-gates
  - step-06-scope-caveat-resolution
  - step-07-architecture-readiness-gate
  - step-08-finalize