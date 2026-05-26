# Step 03 — Grain Transformation Gate

## Mandatory Rules

- Stop at this gate.
- Do not change grain silently.
- User must approve grain transformation strategy.
- If grain is undefined, trigger HALT-07.

## Task

Run Grain Transformation Gate.

## Required table

| Input Dataset | Input Grain | Output Dataset | Output Grain | Transformation Type | Risk |
|---|---|---|---|---|---|

Transformation types:
- Preserve
- Aggregate
- Join / enrich
- Bridge
- Explode
- Filter

## Options

A. Preserve source grain through Silver, aggregate only in Gold  
B. Standardize to product/KPI grain in Silver  
C. Use bridge/mapping tables between source grain and product grain  
D. Keep multiple grains and document each model explicitly  
E. Return to KPI/source validation because grain is unclear  

## Recommendation

Recommend one option.

## User decision

Ask user to choose A/B/C/D/E.

Do not continue until user chooses.

## Record

Update:
- transformation-design.md
- transformation-decision-record.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-transformation-grain:
    status: approved / approved-with-caveats / blocked
```

## Continue checkpoint

Ask:

`[C] Continue to Bronze to Silver rules`
