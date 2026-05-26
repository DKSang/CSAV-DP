# Step 05 — Release Readiness Gate

## Mandatory Rules

- Stop at this gate.
- User must approve release decision.
- Critical risk blocks release.
- Critical evidence gap blocks release.
- Missing trust/governance for user-facing release blocks release.

## Decision options

A. Release  
B. Release with caveats  
C. Do not release; return to implementation  
D. Do not release; return to design  
E. Archive as learning/demo only  

## Required summary

| Area | Status | Release Impact |
|---|---|---|
| E2E validation | | |
| Evidence | | |
| DQ | | |
| Serving | | |
| Trust/limitations | | |
| Governance/security | | |
| DataOps | | |
| Learning capture | | |

## Recommendation

Recommend one option.

## User decision

Ask user to choose A/B/C/D/E.

Do not continue until user chooses.

## Record

Update:
- release-readiness-report.md
- release-checklist.md
- release-notes.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
decisionGates:
  GATE-27-release-readiness:
    status: approved / approved-with-caveats / blocked / archived
releaseDecision:
  status: release / release-with-caveats / return-to-implementation / return-to-design / archive-demo
```

## Continue checkpoint

Ask:

`[C] Continue to finalize release readiness`
