# Step 01 — DataOps Design Initialization

## Mandatory Rules

- Do not design DataOps before serving and governance design exist.
- Do not mark implementation ready before operational readiness gate.
- Read the complete step before acting.

## Task

Initialize DataOps Design workflow.

## Sequence

### 1. Detect existing workflow

Look for:
- `{workflow.dataops_output_path}/**/dataops-runbook.md`
- `{planning_artifacts}/**/*dataops*.md`
- `{planning_artifacts}/**/*runbook*.md`

If unfinished workflow exists, offer to resume.

### 2. Validate prerequisites

Look for:
- `serving-data-product-spec.md`
- `governance-security-review.md`
- `data-quality-rules.md`
- `ingestion-design.md`

If missing:
- missing serving → return to `dew-serving-design`
- missing governance → return to `dew-governance-security-design`
- missing DQ → `HALT-14`
- missing ingestion → `HALT-12`

### 3. Create workspace

Bind `{doc_workspace}` to:

`{workflow.dataops_output_path}/{workflow.run_folder_pattern}/`

Create:
- `dataops-runbook.md`
- `observability-plan.md`
- `operational-readiness-report.md`

Use templates.

### 4. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-22-operational-readiness:
    status: pending
```
