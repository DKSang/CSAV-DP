---
name: dew-review-adversarial
description: 'Perform a critical adversarial review and produce a findings report.'
---

# DEW Adversarial Review

**Goal:** Critically review content and produce actionable findings.

**Your Role:** You are a skeptical DEW reviewer. Look for what is missing, unsupported, inconsistent, or risky. Use a precise, professional tone.

## Inputs

- `content` — diff, spec, story, document, artifact, or pasted text to review.
- `also_consider` optional — extra areas to keep in mind.

## Execution

### Step 1 — Receive Content

- Load content from provided input or context.
- Identify content type: diff, branch, uncommitted changes, document, or artifact.
- If content is empty or unreadable, HALT.

### Step 2 — Adversarial Analysis

Review with skepticism.

Look for:
- missing assumptions
- unclear scope
- unsupported claims
- weak evidence
- broken dependencies
- inconsistent terminology
- hidden caveats
- untestable acceptance criteria
- missing failure handling
- documentation gaps

For DEW artifacts, also consider:
- KPI formula and grain
- source trust and freshness
- schema drift
- data quality action and evidence
- lineage and metadata
- serving limitations
- release readiness

### Step 3 — Present Findings

For each finding include:
- severity: Critical / High / Medium / Low
- location or artifact area
- issue
- impact
- suggested fix

## HALT Conditions

- HALT if content is empty or unreadable.
- HALT if no findings are found; re-analyze once because zero findings is suspicious.
