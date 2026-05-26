# Step 01 — Epics and Stories Initialization

## Mandatory Rules

- Do not create implementation backlog before DataOps design exists.
- Do not proceed if key design artifacts are missing.
- Read the complete step before acting.

## Task

Initialize Epics and Stories workflow.

## Sequence

### 1. Detect existing workflow

Look for:
- `{workflow.epics_output_path}/**/epics.md`
- `{planning_artifacts}/**/*epics*.md`
- `{planning_artifacts}/**/*story-map*.md`

If unfinished workflow exists, offer to resume.

### 2. Validate prerequisites

Look for:
- `dataops-runbook.md`
- `serving-data-product-spec.md`
- `data-quality-rules.md`
- `data-model-spec.md`
- `transformation-design.md`
- `ingestion-design.md`
- `storage-design.md`
- `data-architecture.md`

If missing, trigger `HALT-17 — Implementation Not Ready`.

### 3. Create workspace

Bind `{doc_workspace}` to:

`{workflow.epics_output_path}/{workflow.run_folder_pattern}/`

Create:
- `epics.md`
- `story-map.md`

Use templates.

### 4. Initialize frontmatter

Set:

```yaml
status: draft
stepsCompleted:
  - step-01-init
decisionGates:
  GATE-23-implementation-readiness:
    status: pending
```

### 5. Continue checkpoint

Ask:

`[C] Continue to load design artifacts`
