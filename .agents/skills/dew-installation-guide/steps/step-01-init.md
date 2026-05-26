# Step 01 — Installation Guide Initialization

## Mandatory Rules

- Do not create install guide before package release context exists.
- Do not approve documentation in this step.

## Task

Initialize installation guide workflow.

## Sequence

1. Detect existing install docs.

Look for:
- `{workflow.install_docs_output_path}/**/installation-guide.md`
- `{implementation_artifacts}/**/*install*.md`

2. Validate prerequisite:
- packaging-report.md
- final-release-notes.md

If missing:
- return to `dew-package-release`

3. Create workspace:

`{workflow.install_docs_output_path}/{workflow.run_folder_pattern}/`

Create:
- `installation-guide.md`
- `usage-guide.md`
- `command-reference.md`
- `troubleshooting.md`

4. Continue checkpoint:

`[C] Continue to load package context`
