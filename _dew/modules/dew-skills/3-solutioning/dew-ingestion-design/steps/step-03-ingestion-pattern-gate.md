# Step 03 — Ingestion Pattern Gate

## Mandatory Rules

- Stop at this gate.
- Recommend, but do not decide.
- User must approve ingestion pattern for P1 sources.

## Task

Run GATE-16 — Ingestion Pattern Gate.

## Options

A. Pull API  
B. File download / file drop  
C. Database query/export  
D. CDC  
E. Stream/event ingestion  
F. Manual upload  

## Required table

| Source ID | Source Type | Access Method | Recommended Pattern | Rationale | Risk |
|---|---|---|---|---|---|

## User decision

Ask user to approve pattern by source:

A/B/C/D/E/F, or revise.

Do not continue until user chooses.

## Record

Update:
- ingestion-design.md
- ingestion-decision-record.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-16-ingestion-pattern:
    status: approved / approved-with-caveats