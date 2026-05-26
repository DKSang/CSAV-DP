# Step 04 — Architecture Pattern Gate

## Mandatory Rules

- Stop at this gate.
- Recommend, but do not decide.
- User must approve the architecture pattern.
- Explain trade-offs.
- Record decision in ADR and decision log.

## Task

Run GATE-13 — Architecture Pattern Gate.

## Pattern options

A. Local-first  
B. Warehouse-first  
C. Lakehouse  
D. Hybrid local-first + cloud/lakehouse  
E. Streaming-first  
F. Application-integrated  

## Evaluate using

- project type
- user skill level
- trust expectation
- source types
- data volume
- freshness requirement
- KPI complexity
- serving mode
- governance/security needs
- cost/complexity
- local feedback speed
- deployment target

## Required comparison table

| Pattern | Pros | Cons | Fit | Risk | When to choose |
|---|---|---|---|---|---|

## Recommendation

Recommend one pattern.

Label it clearly as recommendation.

## User decision

Ask user to choose A/B/C/D/E/F.

Do not continue until user chooses.

## Record

Update:
- `data-architecture.md`
- `architecture-decision-record.md`
- `.decision-log.md`
- `.learning-log.md` if learning mode is enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-13-architecture-pattern:
    status: approved / approved-with-caveats
architecturePattern:
  selected: "{selected pattern}"
  status: approved