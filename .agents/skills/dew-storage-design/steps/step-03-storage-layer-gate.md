# Step 03 — Storage Layer Gate

## Mandatory Rules

- Stop at this gate.
- Recommend, but do not decide.
- User must approve storage layer strategy.
- Record decision.

## Task

Run GATE-15 — Storage Layer Gate.

## Options

A. Minimal raw + curated outputs  
B. Bronze/Silver/Gold medallion  
C. Warehouse staging + marts  
D. Lakehouse tables with medallion convention  
E. Local-first files with promotion path  

## Evaluation criteria

- project type
- trust expectation
- source count
- source variety
- KPI complexity
- need for lineage
- DQ expectations
- serving mode
- local vs cloud architecture
- cost/complexity

## Required comparison table

| Option | Pros | Cons | Fit | Risk |
|---|---|---|---|---|

## User decision

Ask user to choose A/B/C/D/E.

Do not continue until user chooses.

## Record

Update:
- storage-design.md
- storage-decision-record.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-15-storage-layer:
    status: approved / approved-with-caveats