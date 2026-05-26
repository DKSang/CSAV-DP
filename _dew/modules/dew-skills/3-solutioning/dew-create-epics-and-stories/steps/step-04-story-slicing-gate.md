# Step 04 — Story Slicing Gate

## Mandatory Rules

- Stop at this gate.
- User must approve story slicing strategy.
- Stories must be small enough to implement and validate.
- Stories must not mix unrelated lifecycle layers.

## Story slicing options

A. Slice by lifecycle layer  
B. Slice by source  
C. Slice by KPI/data product output  
D. Slice by vertical path source→serving  
E. Hybrid slicing  

## Recommendation guide

- Use lifecycle slicing for learning clarity.
- Use source slicing when sources are independent.
- Use KPI slicing when data product is metric-centric.
- Use vertical slicing when proving E2E value quickly.
- Use hybrid when project is complex.

## Required table

| Option | Pros | Cons | Fit | Risk |
|---|---|---|---|---|

## User decision

Ask user to choose A/B/C/D/E.

Do not continue until user chooses.

## Record

Update:
- epics.md
- story-map.md
- .decision-log.md
- .learning-log.md if enabled

## Continue checkpoint

Ask:

`[C] Continue to create story map`
