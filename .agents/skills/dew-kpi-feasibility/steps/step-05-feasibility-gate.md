# Step 05 — KPI Feasibility Gate

## Mandatory Rules

- Stop at this gate.
- Present evidence and missing evidence.
- Recommend status, but do not decide.
- User must approve final status for primary KPIs.

## Task

Run GATE-06 — KPI Feasibility Gate.

## Status options

For each KPI, choose one:

A. Verified on sample  
B. Feasible with caveats  
C. Hypothesis only  
D. Deferred  
E. Rejected  

## Gate explanation

Explain:

- why KPI feasibility matters
- how unverified KPI causes architecture hallucination
- how field availability affects transformation
- how grain mismatch affects Gold models and serving
- what evidence is still missing

## Required table

| KPI ID | Field Availability | Grain Compatibility | Prototype Ready? | Evidence | Recommended Status |
|---|---|---|---|---|---|

## User decision

Ask the user to approve status for each primary KPI.

Do not continue until user chooses.

## Decision log

Record each primary KPI decision in `.decision-log.md`.

## Learning log

If learning mode is enabled, record what was learned about KPI feasibility.

## Update frontmatter

Update:

```yaml
decisionGates:
  GATE-06-kpi-feasibility:
    status: approved / approved-with-caveats / blocked