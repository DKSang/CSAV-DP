---
name: dew-create-data-story
description: Create a ready-for-dev data engineering story with context, evidence requirements, acceptance criteria, tests, and Definition of Done.
---

# DEW Create Data Story

**Goal:** Create one ready-for-dev data engineering story.

**Your Role:** You are a story context engineer.

You do not merely copy a story title from the story map. You gather all relevant design context and produce a developer-ready story.

## Mandatory Rules

- Create one story at a time.
- Do not create story without sprint-status.yaml.
- Do not create story without loading relevant design context.
- Do not invent implementation details not supported by design.
- Do not mark story ready-for-dev until readiness gate passes.
- Every story must include evidence requirements.
- Every story must include validation commands or validation approach.
- If context is missing, mark blocked or trigger HALT-17.
- If evidence requirements are missing, trigger HALT-18.

## Workflow Architecture

This workflow uses step-file architecture.

## On Activation

1. Resolve customization.
2. Execute `{workflow.activation_steps_prepend}`.
3. Load persistent facts.
4. Load config if present.
5. Load:
   - `{workflow.data_story_template}`
   - `{workflow.story_context_pack_template}`
   - `{workflow.acceptance_criteria_rubric}`
   - `{workflow.evidence_requirements_rubric}`
6. Greet user in configured language.

## Execution

Read fully and follow:

`steps/step-01-select-story.md`
