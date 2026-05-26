# Step 01 — Serving Design Initialization

## Mandatory Rules

- Do not design serving before data model and DQ design exist.
- Do not proceed if consumer is unclear.
- Read the complete step before acting.

## Task

Initialize Serving Design workflow.

## Sequence

### 1. Detect existing workflow

Look for:
- `{workflow.serving_output_path}/**/serving-data-product-spec.md`
- `{planning_artifacts}/**/*serving*.md`

If unfinished serving design exists, offer to resume.

### 2. Validate prerequisites

Look for:
- `data-model-spec.md`
- `kpi-to-model-mapping.md`
- `data-quality-rules.md`
- `dq-rule-catalog.md`

If missing:
- missing model → return to `dew-data-model-design`
- missing DQ → `HALT-14`

### 3. Create workspace

Bind `{doc_workspace}` to:

`{workflow.serving_output_path}/{workflow.run_folder_pattern}/`

Create:
- `serving-data-product-spec.md`
- `metric-serving-contract.md`
- `trust-and-limitations-statement.md`

Use templates.

### 4. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-20-serving-mode:
    status: pending
  GATE-serving-trust-limitations:
    status: pending
```

### 5. Continue checkpoint

Ask:

`[C] Continue to load model and DQ context`
