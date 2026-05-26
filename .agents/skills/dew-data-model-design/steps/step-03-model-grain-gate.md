# Step 03 — Model Grain Gate

## Mandatory Rules

- Stop at this gate.
- Every model must have explicit grain.
- User must approve modeling grain strategy.
- If grain is unclear, trigger HALT-07.

## Required table

| Model | Layer | Proposed Grain | Keys | Related KPI | Risk |
|---|---|---|---|---|---|

## Options

A. One grain per model  
B. Multiple models for multiple grains  
C. Bridge table between grains  
D. Aggregate to serving grain in Gold  
E. Return to transformation design  

## User decision

Ask user to choose A/B/C/D/E.

Do not continue until user chooses.

## Record

Update:
- data-model-spec.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-24-modeling-grain:
    status: approved / approved-with-caveats / blocked
```

## Continue checkpoint

Ask:

`[C] Continue to Silver model design`
