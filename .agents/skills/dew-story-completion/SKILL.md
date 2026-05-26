---
name: dew-story-completion
description: Finalize story completion notes, learning capture, file list, evidence index, and sprint status after validation passes.
---

# DEW Story Completion

**Goal:** Close a validated story cleanly and capture learning.

**Your Role:** You are a completion and learning capture facilitator.

## Mandatory Rules

- Do not complete story unless validation report marks story done or done-with-caveats.
- Do not skip learning capture.
- Do not skip evidence index update.
- Do not overwrite sprint statuses incorrectly.
- If learning capture is missing, trigger `HALT-19`.

## On Activation

1. Resolve customization.
2. Load persistent facts.
3. Load config if present.
4. Load:
   - `{workflow.completion_notes_template}`
   - `{workflow.learning_capture_template}`
   - `{workflow.sprint_status_update_rubric}`
5. Greet user in configured language.

## Execution

### Step 1 — Load validated story

Load:
- story file
- validation report
- code review report
- dev notes
- evidence manifest
- sprint-status.yaml

### Step 2 — Verify completion status

Proceed only if validation decision is:
- done
- done-with-caveats

### Step 3 — Create completion notes

Create:

`{workflow.completion_output_path}/{story_id}-completion-notes.md`

### Step 4 — Capture learning

Update:
- `.learning-log.md`
- story completion notes

### Step 5 — Update sprint status

Ensure:
- story status = done
- epic status updated if all stories done

### Step 6 — Finalize

Recommend next backlog story or sprint review.
