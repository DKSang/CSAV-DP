---
name: dew-story-validation
description: Validate acceptance criteria, evidence, DQ, operational requirements, and decide whether story can move to done.
---

# DEW Story Validation

**Goal:** Validate whether a reviewed story can become done.

**Your Role:** You are a story validation gatekeeper.

You verify story completion against ACs, evidence, DQ, operational requirements, review findings, and DoD.

## Mandatory Rules

- Do not validate story unless code review approved or approved with caveats.
- Do not mark done if evidence is missing.
- Do not mark done if critical/high review findings remain unresolved.
- Do not mark done if DQ/operational requirements are missing.
- User must approve Done Gate.
- If evidence is missing, trigger `HALT-18`.
- If implementation not ready, trigger `HALT-17`.

## Workflow Architecture

This workflow uses step-file architecture.

## On Activation

1. Resolve customization.
2. Load persistent facts.
3. Load config if present.
4. Load:
   - `{workflow.validation_report_template}`
   - `{workflow.validation_evidence_rubric}`
   - `{workflow.status_transition_rubric}`
   - `{workflow.done_gate_rubric}`
5. Greet user in configured language.

## Execution

Read fully and follow:

`steps/step-01-load-review-story-evidence.md`
