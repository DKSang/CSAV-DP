# Step 01 — Release Readiness Initialization

## Mandatory Rules

- Do not start release readiness before E2E and final evidence review exist.
- Do not approve release in this step.

## Task

Initialize release readiness workflow.

## Sequence

1. Detect existing release readiness workflow.

Look for:
- `{workflow.release_output_path}/**/release-readiness-report.md`
- `{implementation_artifacts}/**/*release*.md`

2. Validate prerequisite:
- `e2e-validation-report.md`
- `final-evidence-review.md`

If missing:
- missing E2E → return to `dew-e2e-validation`
- missing evidence review → return to `dew-final-evidence-review`

3. Create workspace:

`{workflow.release_output_path}/{workflow.run_folder_pattern}/`

Create:
- `release-readiness-report.md`
- `release-checklist.md`
- `release-notes.md`

4. Initialize frontmatter:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-27-release-readiness:
    status: pending
releaseDecision:
  status: pending
```

5. Continue checkpoint:

`[C] Continue to load validation and evidence`
