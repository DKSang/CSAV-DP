# Step 06 — Readiness and Dependency Review

## Mandatory Rules

- Implementation readiness must be explicit.
- Blockers must not be hidden.
- Every story must have evidence requirement.
- Missing evidence requirement triggers HALT-18.

## Task

Review epic/story readiness.

## Review table

| Epic | Ready? | Blocker | Caveat | Next Action |
|---|---|---|---|---|

## Dependency review

Check:
- no story depends on missing design
- no transformation story before ingestion story
- no Gold story before Silver story
- no serving story before Gold/DQ story
- no operational story without DataOps design

## Implementation readiness gate

Options:

A. Ready for sprint planning  
B. Ready with caveats  
C. Return to design phase  
D. Reduce MVP scope  
E. Block implementation  

Ask user to choose.

Do not continue until user chooses.

## Record

Update:
- epics.md
- story-map.md
- .decision-log.md
- .learning-log.md if enabled

## Continue checkpoint

Ask:

`[C] Continue to finalize epics and stories`
