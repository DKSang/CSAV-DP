# Data Story Template

```markdown
---
title: "{Story ID} {Story Title}"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "4-implementation"
storyId: "{Story ID}"
epicId: "{Epic ID}"
storyStatus: draft
dependsOn: []
evidenceRequired: []
caveats: []
---

# Story {Story ID}: {Story Title}

## Status

Draft / Ready for Dev / In Progress / Review / Done / Blocked

## Epic

{Epic ID} — {Epic Name}

## Story

As a data engineer,  
I want to {implementation goal},  
so that {data product / validation / pipeline outcome}.

## Business / Data Value

## Design Context

### Source Context

### Storage Context

### Ingestion Context

### Transformation Context

### Model Context

### DQ Context

### Serving / Governance / DataOps Context

## Scope

### In Scope

### Out of Scope

## Acceptance Criteria

1. Given ..., when ..., then ...
2. Given ..., when ..., then ...
3. Given ..., when ..., then ...

## Implementation Tasks

- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

## Evidence Requirements

| Evidence ID | Evidence Type | Required Output | Path |
|---|---|---|---|
| EVD-STORY-{id}-001 | run-log | | |
| EVD-STORY-{id}-002 | test-result | | |

## Validation Commands / Approach

```bash
# command or validation approach here
```

## Data Quality Requirements

| DQ Rule ID | Expected Behavior | Evidence |
| ---------- | ----------------- | -------- |

## Operational Requirements

* logging:
* error handling:
* idempotency:
* replay/backfill:
* monitoring:

## Files to Create / Modify

| Path | Purpose |
| ---- | ------- |

## Dependencies

## Caveats

## Definition of Done

* [ ] Implementation completed.
* [ ] Acceptance criteria satisfied.
* [ ] Required evidence produced.
* [ ] DQ/test results produced.
* [ ] File list updated.
* [ ] Run instructions documented.
* [ ] Story status updated to review.
* [ ] Sprint status updated.
```
