# Step 01 — Source Validation Initialization

## Mandatory Rules

- Do not promote any source to P1 in this step.
- Do not proceed if source inventory is missing unless user explicitly provides source context.
- Read the complete step before acting.
- Initialize document state before moving to next step.

## Task

Initialize source validation workflow.

## Sequence

### 1. Detect existing workflow

Look for existing source validation report in:

- `{workflow.validation_output_path}/**/source-validation-report.md`
- `{planning_artifacts}/**/*source*validation*.md`

If an unfinished report exists, offer to resume.

### 2. Create workspace

If fresh workflow, bind `{doc_workspace}` to:

`{workflow.validation_output_path}/{workflow.run_folder_pattern}/`

Create:

- `source-validation-report.md`

Use:

- `{workflow.validation_report_template}`

### 3. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-07-source-access:
    status: pending
  GATE-08-source-trust:
    status: pending