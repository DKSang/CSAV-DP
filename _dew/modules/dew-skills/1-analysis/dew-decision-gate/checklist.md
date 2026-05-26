# Decision Gate Checklist

Use this checklist before closing any DEW decision gate.

## Required

- [ ] Gate ID is identified.
- [ ] Phase is identified.
- [ ] Trigger is explained.
- [ ] Concept is explained.
- [ ] Current evidence is shown.
- [ ] Missing evidence is shown.
- [ ] Options are provided.
- [ ] Recommendation is provided.
- [ ] Trade-offs are explained.
- [ ] User explicitly chooses an option.
- [ ] `.decision-log.md` is updated.
- [ ] `.learning-log.md` is updated when learning mode is enabled.
- [ ] Artifact frontmatter is updated when applicable.
- [ ] Evidence index is updated when applicable.
- [ ] Resume condition is satisfied.

## Failure conditions

Fail the checklist if:
- agent chose silently
- no user confirmation exists
- no decision log entry exists
- missing evidence is hidden
- assumptions are presented as facts
- next phase begins before required gate is resolved