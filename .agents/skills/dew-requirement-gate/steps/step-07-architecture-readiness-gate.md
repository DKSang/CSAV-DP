# Step 07 — Architecture Readiness Gate

## Mandatory Rules

- Stop at this gate.
- Recommend, but do not decide.
- User must explicitly approve architecture readiness.
- Do not approve if hard blockers remain.
- If architecture is not ready, recommend exact workflow to return to.

## Task

Run GATE-12 — Architecture Readiness Gate.

## Required readiness matrix

Complete:

| Requirement | Status | Evidence | Decision |
|---|---|---|---|
| Business decision clear | | | |
| Data consumer clear | | | |
| Primary KPI feasible or caveated | | | |
| P1 source validated or caveated | | | |
| Trust expectation approved | | | |
| Grain approved | | | |
| Freshness approved | | | |
| Schema evolution direction known | | | |
| Caveats accepted | | | |
| Evidence indexed | | | |

## Final decision options

A. Proceed to architecture  
B. Proceed to architecture with caveats  
C. Return to KPI validation  
D. Return to source validation  
E. Reduce MVP scope  

## Recommendation

Recommend one option based on readiness matrix.

## User decision

Ask user to choose A/B/C/D/E.

Do not continue until user chooses.

## Record decision

Update `.decision-log.md`.

If learning mode is enabled, update `.learning-log.md`.

Update frontmatter:

```yaml
decisionGates:
  GATE-12-architecture-readiness:
    status: approved / approved-with-caveats / blocked
architectureReadiness:
  status: ready / ready-with-caveats / blocked / scope-reduction-needed