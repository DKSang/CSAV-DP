# Step 01 — Load Review Story Evidence

## Mandatory Rules

- Validate only story status `review`.
- Code review must be approved or approved-with-caveats.
- Evidence manifest must exist.

## Required inputs

- story file
- dev notes
- code review report
- evidence manifest
- sprint-status.yaml

## If missing

- no review → return to `dew-code-review`
- evidence missing → `HALT-18`
- story not review → return to correct workflow

## Continue checkpoint

Ask:

`[C] Continue to validate acceptance criteria`
