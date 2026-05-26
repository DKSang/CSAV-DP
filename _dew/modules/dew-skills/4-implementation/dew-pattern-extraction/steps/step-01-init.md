# Step 01 — Pattern Extraction Initialization

## Mandatory Rules

- Do not extract patterns before learning capture exists.
- Do not approve patterns in this step.

## Task

Initialize pattern extraction.

## Sequence

1. Detect existing pattern extraction workflow.

Look for:
- `{workflow.pattern_output_path}/**/reusable-patterns.md`
- `{learning_artifacts}/**/*pattern*.md`

2. Validate prerequisite:
- learning-retrospective.md
- fde-learning-map.md
- mistake-pattern-log.md

If missing:
- return to `dew-learning-capture`
- or trigger `HALT-19`

3. Create workspace:

`{workflow.pattern_output_path}/{workflow.run_folder_pattern}/`

Create:
- `reusable-patterns.md`
- `pattern-catalog.md`
- `anti-patterns.md`

4. Continue checkpoint:

`[C] Continue to load project outcomes`
