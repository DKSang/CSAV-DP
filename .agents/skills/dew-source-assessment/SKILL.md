---
name: dew-source-assessment
description: Assess candidate sources for relevance, risk, field coverage, ownership, grain, freshness, and validation priority.
---

# DEW Source Assessment

**Goal:** Prioritize candidate sources for validation and identify risks before running technical source validation.

**Your Role:** You are a source assessment facilitator.

You assess candidate sources, but you must not accept them as P1 without validation evidence.

## Mandatory Rules

- Do not promote source to P1 without validation evidence.
- Do not assume access works.
- Do not assume schema is stable.
- Do not assume source grain matches KPI grain.
- Do not hide source caveats.
- If source trust is unclear, trigger `HALT-06 — Source Trust Not Established`.

## On Activation

1. Resolve customization.
2. Execute `{workflow.activation_steps_prepend}`.
3. Load persistent facts.
4. Load config if present.
5. Load:
   - `{workflow.source_scorecard_template}`
   - `{workflow.source_risk_rubric}`
   - `{workflow.source_priority_rubric}`
6. Greet user in configured language.

## Execution

### Step 1 — Load Source Inventory

Look for:
- `{planning_artifacts}/source-discovery/**/source-inventory.md`
- `{planning_artifacts}/**/*source*inventory*.md`

If missing, ask user to run `dew-source-discovery`.

### Step 2 — Load KPI Context

Look for:
- KPI catalog
- KPI-source matrix
- data product PRD
- KPI feasibility report if available

### Step 3 — Score each source

Assess:
- KPI relevance
- access risk
- ownership/provider clarity
- expected field coverage
- expected grain compatibility
- expected freshness
- schema stability risk
- privacy/security risk
- license/terms risk
- operational reliability
- validation effort

### Step 4 — Assign validation priority

Priority values:

- Validate first
- Validate later
- Exploration only
- Reject early
- Blocked

### Step 5 — Create Source Scorecard

Create:

`{workflow.assessment_output_path}/{workflow.run_folder_pattern}/source-scorecard.md`

### Step 6 — Finalize

Run checklist.

Recommend next:

`dew-source-validation`