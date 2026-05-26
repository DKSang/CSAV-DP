# Step 01 — E2E Validation Initialization

## Mandatory Rules

- Do not run E2E validation before implementation stories exist.
- Do not proceed if sprint-status.yaml is missing.
- Read the complete step before acting.

## Task

Initialize E2E validation workflow.

## Sequence

1. Detect existing workflow.

Look for:
- `{workflow.e2e_output_path}/**/e2e-validation-report.md`
- `{implementation_artifacts}/**/*e2e*.md`

If unfinished workflow exists, offer to resume.

2. Validate prerequisite:
   - `sprint-status.yaml`
   - story validation reports
   - completion notes
   - evidence index

If missing:
- missing sprint status → `HALT-17`
- missing evidence → `HALT-18`

3. Create workspace:

`{workflow.e2e_output_path}/{workflow.run_folder_pattern}/`

Create:
- `e2e-validation-report.md`
- `e2e-validation-matrix.md`

Use templates.

4. Initialize frontmatter:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-25-e2e-validation:
    status: pending
```

5. Continue checkpoint:

`[C] Continue to load implemented context`
