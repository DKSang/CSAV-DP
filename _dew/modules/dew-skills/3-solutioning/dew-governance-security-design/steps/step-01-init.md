# Step 01 — Governance Security Initialization

## Mandatory Rules

- Do not proceed if serving design is missing.
- Do not assume privacy posture.
- Read the complete step before acting.

## Task

Initialize Governance Security Design workflow.

## Sequence

### 1. Detect existing workflow

Look for:
- `{workflow.governance_output_path}/**/governance-security-review.md`
- `{planning_artifacts}/**/*governance*.md`
- `{planning_artifacts}/**/*security*.md`

If unfinished workflow exists, offer to resume.

### 2. Validate prerequisites

Look for:
- `serving-data-product-spec.md`
- `trust-and-limitations-statement.md`
- `data-model-spec.md`
- `source-validation-report.md`

If missing:
- missing serving → return to `dew-serving-design`
- missing source validation → `HALT-06`

### 3. Create workspace

Bind `{doc_workspace}` to:

`{workflow.governance_output_path}/{workflow.run_folder_pattern}/`

Create:
- `governance-security-review.md`
- `access-control-matrix.md`
- `governance-decision-record.md`

Use templates.

### 4. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-21-privacy-posture:
    status: pending
  GATE-access-control:
    status: pending
```
