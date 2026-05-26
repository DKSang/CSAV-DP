# Step 01 — Data Quality Design Initialization

## Mandatory Rules

- Do not design DQ before data model spec exists.
- Do not proceed if transformation design is missing.
- DQ must be tied to source/model/KPI.

## Task

Initialize Data Quality Design workflow.

## Sequence

### 1. Detect existing workflow

Look for:
- `{workflow.dq_output_path}/**/data-quality-rules.md`
- `{planning_artifacts}/**/*quality*.md`

If unfinished DQ design exists, offer to resume.

### 2. Validate prerequisites

Look for:
- `data-model-spec.md`
- `transformation-design.md`
- `source-validation-report.md`
- `kpi-feasibility-report.md`

If missing:
- missing model → return to `dew-data-model-design`
- missing transformation → return to `dew-transformation-design`
- missing source validation → `HALT-06`
- missing KPI feasibility → `HALT-03`

### 3. Create workspace

Bind `{doc_workspace}` to:

`{workflow.dq_output_path}/{workflow.run_folder_pattern}/`

Create:
- `data-quality-rules.md`
- `dq-rule-catalog.md`
- `dq-gate-policy.md`

Use templates.

### 4. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-18-data-quality-rule:
    status: pending
```

### 5. Continue checkpoint

Ask:

`[C] Continue to load model and source context`
