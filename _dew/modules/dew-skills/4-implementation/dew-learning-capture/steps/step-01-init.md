# Step 01 — Learning Capture Initialization

## Mandatory Rules

- Do not skip learning capture.
- Do not produce shallow learning summary only.

## Task

Initialize learning capture.

## Sequence

1. Detect existing learning capture.

Look for:
- `{workflow.learning_output_path}/**/learning-retrospective.md`
- `{learning_artifacts}/**/*learning*.md`

2. Validate prerequisite:
- project documentation or release readiness
- decision log
- learning log

3. Create workspace:

`{workflow.learning_output_path}/{workflow.run_folder_pattern}/`

Create:
- `learning-retrospective.md`
- `fde-learning-map.md`
- `mistake-pattern-log.md`

4. Continue checkpoint:

`[C] Continue to load learning context`
