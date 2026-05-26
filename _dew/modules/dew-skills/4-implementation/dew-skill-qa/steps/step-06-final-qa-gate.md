# Step 06 — Final QA Gate

## Mandatory Rules

- Stop at this gate.
- User must approve QA result.
- Critical finding blocks package release.
- High finding requires fix or explicit caveat.

## Decision options

A. QA passed  
B. QA passed with caveats  
C. Fix required before package  
D. Block release  

## Required summary

| Area | Status | Finding |
|---|---|---|
| module.yaml | | |
| module-help.csv | | |
| skill folders | | |
| assets/steps | | |
| cross-links | | |
| gates/HALTs | | |

## Recommendation

Recommend one option.

## User decision

Ask user to choose A/B/C/D.

Do not continue until user chooses.

## Record

Update:
- skill-qa-report.md
- .decision-log.md
- .learning-log.md if enabled

## Continue checkpoint

Ask:

`[C] Continue to finalize skill QA`
