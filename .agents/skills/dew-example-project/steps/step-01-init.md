# Step 01 — Example Project Initialization

## Mandatory Rules

- Example project is optional.
- Do not create huge example.
- Do not approve example in this step.

## Task

Initialize example project workflow.

## Sequence

1. Detect existing example project docs.

Look for:
- `{workflow.example_output_path}/**/example-project-walkthrough.md`
- `{implementation_artifacts}/**/*example*.md`

2. Validate prerequisite:
- installation guide
- usage guide

If missing:
- return to `dew-installation-guide`

3. Create workspace:

`{workflow.example_output_path}/{workflow.run_folder_pattern}/`

Create:
- `example-project-walkthrough.md`
- `quickstart-scenario.md`
- `example-artifact-map.md`

4. Continue checkpoint:

`[C] Continue to select example scenario`
