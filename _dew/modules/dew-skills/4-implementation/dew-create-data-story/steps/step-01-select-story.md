# Step 01 — Select Story

## Mandatory Rules

- Create one story at a time.
- Do not create story if sprint-status.yaml is missing.
- Respect dependency order.

## Task

Select next story.

## Sequence

1. Load `sprint-status.yaml`.
2. Load `story-map.md`.
3. Find first story with status `backlog` whose dependencies are done or not required.
4. If user named a specific story, validate dependencies first.
5. If dependencies are missing, mark blocked or recommend dependency story first.

## Continue checkpoint

Ask:

`[C] Continue to load story context`
