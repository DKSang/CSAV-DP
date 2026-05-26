# Step 01 — Load Ready Story

## Mandatory Rules

- Do not work on story unless status is `ready-for-dev`.
- Do not proceed if sprint-status.yaml is missing.
- Do not skip dependency check.

## Task

Load selected story.

## Sequence

1. Load `sprint-status.yaml`.
2. Select story:
   - user-specified story, or
   - first `ready-for-dev` story.
3. Load story file.
4. Load story context pack.
5. Load implementation readiness review if available.
6. Verify dependencies are done or not required.

## If invalid

- no ready story → recommend `dew-create-data-story`
- missing context → `HALT-17`
- missing evidence requirements → `HALT-18`
- dependency not done → `HALT-17`

## Continue checkpoint

Ask:

`[C] Continue to plan implementation`
