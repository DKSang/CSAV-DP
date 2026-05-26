# Step 05 — Package Release Gate

## Mandatory Rules

- Stop at this gate.
- User must approve package release.
- Critical QA finding blocks package release.
- Version must be selected.

## Decision options

A. Package release approved  
B. Package release approved with caveats  
C. Fix required before package release  
D. Block package release  

## Required summary

| Area | Status | Release Impact |
|---|---|---|
| QA | | |
| Module catalog | | |
| Skill folders | | |
| Version | | |
| Release notes | | |
| Caveats | | |

## Recommendation

Recommend one option.

## User decision

Ask user to choose A/B/C/D.

Do not continue until user chooses.

## Record

Update:
- packaging-report.md
- final-release-notes.md
- .decision-log.md
- .learning-log.md if enabled

## Continue checkpoint

Ask:

`[C] Continue to finalize package release`
