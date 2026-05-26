# Step 01 — Skill QA Initialization

## Mandatory Rules

- Do not approve QA in this step.
- Do not proceed if module root is missing.

## Task

Initialize skill QA.

## Sequence

1. Detect existing QA workflow.

Look for:
- `{workflow.qa_output_path}/**/skill-qa-report.md`
- `{implementation_artifacts}/**/*qa*.md`

2. Validate prerequisite:
- `src/dew-skills/module.yaml`
- `src/dew-skills/module-help.csv`

If missing, trigger:

`HALT-22 — Skill Pack QA Failed`

3. Create workspace:

`{workflow.qa_output_path}/{workflow.run_folder_pattern}/`

Create:
- `skill-qa-report.md`
- `module-catalog-audit.md`

4. Continue checkpoint:

`[C] Continue to scan skill pack`
