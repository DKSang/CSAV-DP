# Review Finding Rubric

## Critical

Blocks approval.

Use when:
- AC not met
- required evidence missing
- DQ critical rule ignored
- KPI formula changed without approval
- grain changed silently
- sensitive/security issue introduced
- output is misleading

## High

Usually blocks approval unless explicitly caveated.

Use when:
- partial evidence
- important validation missing
- idempotency/failure handling missing for pipeline story
- source/schema caveat ignored

## Medium

Can approve with caveats.

Use when:
- documentation incomplete
- minor operational issue
- non-critical DQ evidence weak

## Low

Does not block.

Use when:
- naming
- formatting
- minor clarity issue
