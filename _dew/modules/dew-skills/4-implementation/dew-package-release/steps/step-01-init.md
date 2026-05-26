# Step 01 — Package Release Initialization

## Mandatory Rules

- Do not package before Skill QA exists.
- Do not approve release in this step.

## Task

Initialize package release workflow.

## Sequence

1. Detect existing package release workflow.

Look for:
- `{workflow.package_output_path}/**/packaging-report.md`
- `{implementation_artifacts}/**/*package*.md`

2. Validate prerequisite:
- `skill-qa-report.md`
- `module-catalog-audit.md`

If missing:
- return to `dew-skill-qa`

3. Create workspace:

`{workflow.package_output_path}/{workflow.run_folder_pattern}/`

Create:
- `packaging-report.md`
- `release-package-checklist.md`
- `final-release-notes.md`

4. Continue checkpoint:

`[C] Continue to load QA results`
