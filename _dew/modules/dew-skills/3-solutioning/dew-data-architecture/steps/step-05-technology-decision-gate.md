# Step 05 — Technology Decision Gate

## Mandatory Rules

- Stop at this gate.
- Do not choose technology silently.
- Do not choose tools because they are trendy.
- Every technology decision must include alternatives, rationale, risk, reversibility, and revisit trigger.

## Task

Run GATE-14 — Technology Choice Gate.

## Decision areas

Evaluate at architecture level:

1. Local development environment
2. Storage direction
3. Compute engine
4. Orchestration direction
5. Transformation framework
6. Data quality/testing direction
7. Serving direction
8. Documentation/catalog direction

## Required technology decision table

| Decision Area | Option A | Option B | Option C | Recommended | Rationale |
|---|---|---|---|---|---|
| Local development | | | | | |
| Storage | | | | | |
| Compute | | | | | |
| Orchestration | | | | | |
| Transformation | | | | | |
| Quality/testing | | | | | |
| Serving | | | | | |
| Documentation/catalog | | | | | |

## Minimum decision quality

For each selected direction, record:
- selected option
- alternatives considered
- why selected
- why alternatives rejected
- evidence used
- risk
- reversibility
- revisit trigger

## User decision

Ask user to approve technology direction:

A. Approve recommended stack direction  
B. Approve with caveats  
C. Revise one or more technology choices  
D. Defer technology decision to detailed design  
E. Return to architecture pattern gate  

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
  GATE-14-technology-choice:
    status: approved / approved-with-caveats / deferred
technologyDecisions:
  status: approved / approved-with-caveats / deferred