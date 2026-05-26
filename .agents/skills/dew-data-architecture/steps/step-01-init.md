# Step 01 — Data Architecture Initialization

## Mandatory Rules

- Do not create architecture before checking Requirement Gate.
- Do not proceed if Requirement Gate is missing.
- Do not proceed if Requirement Gate decision is blocked.
- Read the complete step before acting.
- Initialize document state before moving to next step.

## Task

Initialize Data Architecture workflow.

## Sequence

### 1. Detect existing architecture workflow

Look for existing architecture docs in:

- `{workflow.architecture_output_path}/**/data-architecture.md`
- `{planning_artifacts}/**/*architecture*.md`

If an unfinished architecture exists, offer to resume.

### 2. Validate prerequisite

Look for:

- `requirement-gate-report.md`
- `architecture-readiness-matrix.md`
- `caveat-register.md`

The Requirement Gate must have one of:

- Proceed to architecture
- Proceed to architecture with caveats
- architectureReadiness.status = ready
- architectureReadiness.status = ready-with-caveats

If missing or blocked, trigger:

`HALT-10 — Architecture Before Validation`

### 3. Create workspace

If fresh workflow, bind `{doc_workspace}` to:

`{workflow.architecture_output_path}/{workflow.run_folder_pattern}/`

Create:

- `data-architecture.md`
- `architecture-decision-record.md`
- `architecture-caveat-carryover.md`

Use:
- `{workflow.architecture_template}`
- `{workflow.adr_template}`
- `{workflow.caveat_carryover_template}`

### 4. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-13-architecture-pattern:
    status: pending
  GATE-14-technology-choice:
    status: pending