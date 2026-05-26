# Step 06 — Finalize Validation

## Mandatory Rules

- Update status based on Done Gate.
- Run checklist.
- Do not hide caveats.

## If Done / Done with caveats

Update:
- story status → Done
- sprint-status.yaml → done
- validation report → final
- evidence index → validated where applicable

## If Return to dev

Update:
- story status → In Progress
- sprint-status.yaml → in-progress
- required fixes documented

## If Block

Update:
- story status → Blocked
- sprint-status.yaml → blocked
- blocker documented

## Next workflow

If done:

`dew-story-completion`

If not done:

`dew-dev-story`
