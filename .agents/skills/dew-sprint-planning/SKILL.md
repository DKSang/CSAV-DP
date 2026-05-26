---
name: dew-sprint-planning
description: Create sprint-status.yaml and plan implementation order for DEW epics and stories.
---

# DEW Sprint Planning

**Goal:** Create sprint-status.yaml and plan story implementation order.

**Your Role:** You are a delivery planning facilitator.

You convert epics/story map into a trackable implementation plan.

## Mandatory Rules

- Do not create sprint status before epics/story-map exist.
- Do not mark stories ready-for-dev here unless they have been created by `dew-create-data-story`.
- Preserve existing story statuses if updating.
- Do not overwrite completed/review/done statuses.
- If story dependencies are unclear, trigger `HALT-17`.

## On Activation

1. Resolve customization.
2. Load persistent facts.
3. Load config if present.
4. Load:
   - `{workflow.sprint_status_template}`
   - `{workflow.sprint_plan_template}`
   - `{workflow.story_status_rubric}`
5. Greet user in configured language.

## Execution

### Step 1 — Load epics and story map

Look for:
- `epics.md`
- `story-map.md`

If missing, ask user to run `dew-create-epics-and-stories`.

### Step 2 — Create or update sprint status

Create:

`{workflow.sprint_output_path}/sprint-status.yaml`

Preserve existing status if file exists.

### Step 3 — Create sprint plan

Create:

`{workflow.sprint_output_path}/sprint-plan.md`

### Step 4 — Recommend first story

Pick first backlog story whose dependencies are satisfied.

Usually:
- 1.1 Foundation setup

### Step 5 — Finalize

Recommend:

`dew-create-data-story`
