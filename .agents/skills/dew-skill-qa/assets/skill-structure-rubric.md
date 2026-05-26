# Skill Structure Rubric

## Required structure for simple skill

A simple skill may have:

- SKILL.md
- customize.toml
- checklist.md
- assets/

## Required structure for workflow skill

A workflow skill must have:

- SKILL.md
- customize.toml
- checklist.md
- assets/
- steps/

## SKILL.md must include

- name
- description
- goal
- role
- mandatory rules
- activation logic
- execution entrypoint

## customize.toml must include

- activation steps
- persistent facts
- template paths
- checklist path
- output path
- decision/learning/evidence log paths when relevant

## assets must include

- templates referenced by SKILL.md or customize.toml
- rubrics referenced by skill
- no orphan critical template

## steps must include

- init step
- context loading step
- gate step if user decision required
- finalize step

## checklist must include

- required inputs
- required outputs
- gate completion
- failure conditions
