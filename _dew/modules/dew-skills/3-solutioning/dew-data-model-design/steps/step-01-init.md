# Step 01 — Data Model Design Initialization

## Mandatory Rules

- Do not design models before transformation design exists.
- Do not proceed if transformation design is missing.

## Task

Initialize Data Model Design workflow.

## Sequence

### 1. Detect existing workflow

Look for:
- `{workflow.model_output_path}/**/data-model-spec.md`
- `{planning_artifacts}/**/*data*model*.md`

If unfinished model design exists, offer to resume.

### 2. Validate prerequisites

Look for:
- `transformation-design.md`
- `business-rule-catalog.md`
- `kpi-feasibility-report.md`

If missing:
- missing transformation → return to `dew-transformation-design`
- missing KPI feasibility → `HALT-03`

### 3. Create workspace

Bind `{doc_workspace}` to:

`{workflow.model_output_path}/{workflow.run_folder_pattern}/`

Create:
- `data-model-spec.md`
- `kpi-to-model-mapping.md`

Use templates.

### 4. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-24-modeling-grain:
    status: pending
  GATE-history-scd:
    status: pending
```

### 5. Continue checkpoint

Ask:

`[C] Continue to load transformation context`
