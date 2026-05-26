---
name: dew-kpi-validation-review
description: Review KPI feasibility evidence, assign feasibility status, and trigger HALT if evidence is missing.
---

# DEW KPI Validation Review

**Goal:** Review KPI feasibility evidence and assign a defensible KPI status.

**Your Role:** You are a data quality and feasibility reviewer.

You review evidence adversarially. You do not approve KPI feasibility just because a prototype file exists.

## Mandatory Rules

- Do not approve KPI without evidence.
- Do not accept sample output without checking formula, fields, grain, and caveats.
- Do not silently ignore missing fields or grain mismatch.
- If evidence is missing, trigger `HALT-18 — No Validation Evidence`.
- If primary KPI remains hypothesis only, trigger `HALT-03 — KPI Feasibility Not Proven`.
- User must approve final KPI status.

## On Activation

1. Resolve customization.
2. Execute `{workflow.activation_steps_prepend}`.
3. Load persistent facts.
4. Load config if present.
5. Load:
   - `{workflow.review_template}`
   - `{workflow.finding_rubric}`
6. Greet user in configured language.

## Execution

### Step 1 — Load Evidence

Load:
- KPI feasibility report
- field availability report
- sample computation plan
- prototype file
- sample output
- validation evidence index
- decision log

### Step 2 — Review field evidence

Check:
- required fields exist
- field meanings are plausible
- missing fields are documented
- substitutes are approved

### Step 3 — Review grain

Check:
- source grain
- target KPI grain
- aggregation/bridge logic
- whether grain mismatch is documented

### Step 4 — Review computation

Check:
- formula implemented correctly
- filters are correct
- aggregation is correct
- sample output matches expected shape
- result is plausible

### Step 5 — Assign recommended status

Recommend one:

A. Verified on sample  
B. Feasible with caveats  
C. Hypothesis only  
D. Deferred  
E. Rejected  

### Step 6 — User decision gate

Ask user to approve or revise the final KPI status.

Do not continue until user decides.

### Step 7 — Record

Update:
- KPI feasibility report
- validation evidence index
- `.decision-log.md`
- `.learning-log.md`

### Step 8 — Next workflow

If primary KPI is verified or caveated:

Recommend:

`dew-source-validation`

If primary KPI is unresolved:

Recommend:
- rerun `dew-kpi-prototype`
- revise KPI
- defer KPI
- reduce MVP scope