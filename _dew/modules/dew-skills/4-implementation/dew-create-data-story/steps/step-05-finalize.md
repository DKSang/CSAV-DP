# Step 05 — Finalize Story

## Mandatory Rules

- Do not finalize as ready-for-dev unless readiness gate approved.
- Preserve blocked/caveated status if applicable.
- Run checklist.

## Final updates

If approved:
- story frontmatter `storyStatus: ready-for-dev`
- story status section `Ready for Dev`
- sprint-status story status `ready-for-dev`

If blocked:
- story frontmatter `storyStatus: blocked`
- sprint-status story status `blocked`
- blocker documented

## Next workflow

Recommend:

`dew-implementation-readiness-review`

Or if ready:

`dew-dev-story`
