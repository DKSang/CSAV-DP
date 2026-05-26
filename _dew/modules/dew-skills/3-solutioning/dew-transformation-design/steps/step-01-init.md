# Step 01 — Transformation Design Initialization

## Mandatory Rules

- Do not design transformation before storage and ingestion design exist.
- Do not proceed if storage or ingestion design is missing.
- Read the complete step before acting.

## Task

Initialize Transformation Design workflow.

## Sequence

### 1. Detect existing workflow

Look for:

- `{workflow.transformation_output_path}/**/transformation-design.md`
- `{planning_artifacts}/**/*transformation*design*.md`

If unfinished transformation design exists, offer to resume.

### 2. Validate prerequisites

Look for:
- `storage-design.md`
- `source-to-storage-mapping.md`
- `ingestion-design.md`
- `ingestion-source-plan.md`
- `kpi-feasibility-report.md`

If missing:
- missing storage → `HALT-11`
- missing ingestion → `HALT-12`
- missing KPI feasibility → `HALT-03`

### 3. Create workspace

Bind `{doc_workspace}` to:

`{workflow.transformation_output_path}/{workflow.run_folder_pattern}/`

Create:
- `transformation-design.md`
- `business-rule-catalog.md`
- `transformation-decision-record.md`

Use templates.

### 4. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-19-transformation-rule:
    status: pending
  GATE-transformation-grain:
    status: pending
```

### 5. Continue checkpoint

Ask:

`[C] Continue to load storage and ingestion context`
