# Decision Gate Frontmatter Schema

Artifacts that participate in DEW decision gates should include frontmatter.

## Minimal schema

```yaml
---
title: "{Artifact Title}"
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
phase: "{phase-id}"
workflow: dew
stepsCompleted: []
decisionGates: {}
evidence: []
assumptions: []
caveats: []
---