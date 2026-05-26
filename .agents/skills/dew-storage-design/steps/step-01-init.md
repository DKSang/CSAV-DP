# Step 01 — Storage Design Initialization

## Mandatory Rules

- Do not design storage before data architecture exists.
- Do not proceed if architecture is missing or blocked.
- Read the complete step before acting.

## Task

Initialize Storage Design workflow.

## Sequence

### 1. Detect existing workflow

Look for:

- `{workflow.storage_output_path}/**/storage-design.md`
- `{planning_artifacts}/**/*storage*design*.md`

If unfinished storage design exists, offer to resume.

### 2. Validate prerequisite

Look for:

- `data-architecture.md`
- `architecture-decision-record.md`
- `architecture-caveat-carryover.md`

If missing, trigger:

`HALT-10 — Architecture Before Validation`

### 3. Create workspace

Bind `{doc_workspace}` to:

`{workflow.storage_output_path}/{workflow.run_folder_pattern}/`

Create:

- `storage-design.md`
- `storage-decision-record.md`
- `source-to-storage-mapping.md`

Use templates.

### 4. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-15-storage-layer:
    status: pending
  GATE-storage-metadata-standard:
    status: pending
  GATE-storage-retention:
    status: pending