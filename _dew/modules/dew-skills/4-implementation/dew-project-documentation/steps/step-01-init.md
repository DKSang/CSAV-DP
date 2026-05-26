# Step 01 — Project Documentation Initialization

## Mandatory Rules

- Do not create release documentation before release readiness exists.
- Do not approve documentation in this step.

## Task

Initialize documentation workflow.

## Sequence

1. Detect existing documentation workflow.

Look for:
- `{workflow.documentation_output_path}/**/project-documentation.md`
- `{implementation_artifacts}/**/*documentation*.md`
- `{implementation_artifacts}/**/README*.md`

2. Validate prerequisite:
- `release-readiness-report.md`

If missing:
- return to `dew-release-readiness`
- or trigger `HALT-20 — Release Not Ready`

3. Create workspace:

`{workflow.documentation_output_path}/{workflow.run_folder_pattern}/`

Create:
- `project-documentation.md`
- `data-product-readme.md`
- `data-dictionary.md`
- `runbook-summary.md`

4. Initialize frontmatter.

5. Continue checkpoint:

`[C] Continue to load release context`
