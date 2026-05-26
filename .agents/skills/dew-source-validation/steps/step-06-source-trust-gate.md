# Step 06 — Source Trust Gate

## Mandatory Rules

- Stop at this gate.
- Present evidence and missing evidence.
- Recommend status, but do not decide.
- User must approve final status for validation-first sources.
- Do not promote to P1 without access/sample/schema evidence.

## Task

Run GATE-08 — Source Trust Gate.

## Status options

For each source, choose one:

A. P1 — Use in MVP  
B. P2 — Use later  
C. Exploration only  
D. Reject  
E. Blocked  

## Gate explanation

Explain:
- why source validation matters
- how unverified sources cause architecture hallucination
- how source grain affects transformation
- how source freshness affects ingestion/serving
- how schema stability affects ingestion and DQ
- what evidence is still missing

## Required table

| Source ID | Access | Sample | Schema | Grain | Freshness | DQ Risk | Recommended Status |
|---|---|---|---|---|---|---|---|

## User decision

Ask the user to approve status for each validation-first source.

Do not continue until user chooses.

## Decision log

Record each source decision in `.decision-log.md`.

## Learning log

If learning mode is enabled, record what was learned about source validation.

## Update frontmatter

Update:

```yaml
decisionGates:
  GATE-08-source-trust:
    status: approved / approved-with-caveats / blocked