# Step 01 — KPI Feasibility Initialization

## Mandatory Rules

- Do not create final architecture.
- Do not mark any KPI as verified in this step.
- Do not proceed if KPI catalog is missing unless the user explicitly provides KPI context.
- Read the complete step before acting.
- Initialize document state before moving to next step.

## Task

Initialize KPI feasibility workflow.

## Sequence

### 1. Detect existing workflow

Look for existing KPI feasibility report in:

- `{workflow.feasibility_output_path}/**/kpi-feasibility-report.md`
- `{planning_artifacts}/**/*kpi*feasibility*.md`

If an unfinished report exists, offer to resume.

### 2. Create workspace

If fresh workflow, bind `{doc_workspace}` to:

`{workflow.feasibility_output_path}/{workflow.run_folder_pattern}/`

Create:

- `kpi-feasibility-report.md`
- `field-availability.md`
- `sample-computation-plan.md`

Use templates:

- `{workflow.feasibility_report_template}`
- `{workflow.field_availability_template}`
- `{workflow.sample_computation_plan_template}`

### 3. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-06-kpi-feasibility:
    status: pending