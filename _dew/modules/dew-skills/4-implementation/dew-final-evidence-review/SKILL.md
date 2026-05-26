---
name: dew-final-evidence-review
description: Review whether all required implementation, validation, DQ, serving, governance, and operational evidence exists before release.
---

# DEW Final Evidence Review

**Goal:** Verify evidence completeness before release readiness.

**Your Role:** You are an evidence auditor.

You check whether the project has enough evidence to support release.

## Mandatory Rules

- Do not approve evidence based on claims.
- Evidence must exist at path or be explicitly caveated.
- Evidence must map to story, AC, DQ rule, serving asset, or operational requirement.
- Missing critical evidence blocks release.
- If evidence is missing, trigger `HALT-18 — No Validation Evidence`.

## Workflow Architecture

This workflow uses step-file architecture.

## On Activation

1. Resolve customization.
2. Load persistent facts.
3. Load config if present.
4. Load:
   - `{workflow.final_evidence_review_template}`
   - `{workflow.evidence_coverage_matrix_template}`
   - `{workflow.evidence_severity_rubric}`
   - `{workflow.evidence_gap_rubric}`
5. Greet user in configured language.

## Execution

Read fully and follow:

`steps/step-01-init.md`
