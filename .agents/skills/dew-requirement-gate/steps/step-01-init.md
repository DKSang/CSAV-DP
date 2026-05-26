# Step 01 — Requirement Gate Initialization

## Mandatory Rules

- Do not create architecture in this step.
- Do not approve architecture readiness in this step.
- Read the complete step before acting.
- Initialize document state before moving to next step.

## Task

Initialize the Requirement Gate workflow.

## Sequence

### 1. Detect existing workflow

Look for existing requirement gate report in:

- `{workflow.gate_output_path}/**/requirement-gate-report.md`
- `{planning_artifacts}/**/*requirement*gate*.md`

If an unfinished report exists, offer to resume.

### 2. Create workspace

If fresh workflow, bind `{doc_workspace}` to:

`{workflow.gate_output_path}/{workflow.run_folder_pattern}/`

Create:

- `requirement-gate-report.md`
- `caveat-register.md`
- `architecture-readiness-matrix.md`

Use:
- `{workflow.gate_report_template}`
- `{workflow.caveat_register_template}`
- `{workflow.architecture_readiness_matrix_template}`

### 3. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-05-trust-expectation:
    status: pending
  GATE-04-kpi-grain:
    status: pending
  GATE-10-source-freshness:
    status: pending
  GATE-12-architecture-readiness:
    status: pending
architectureReadiness:
  status: pending