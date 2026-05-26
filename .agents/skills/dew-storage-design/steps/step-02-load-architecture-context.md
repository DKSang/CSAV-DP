# Step 02 — Load Architecture Context

## Mandatory Rules

- Load architecture, source validation, KPI feasibility, and caveat carryover.
- Do not drop caveats.
- Do not invent source targets.

## Task

Extract storage-relevant context.

## Extract from architecture

- selected architecture pattern
- storage technology direction
- source/generation summary
- high-level storage intent
- caveats

## Extract from source validation

- P1/P2 sources
- source type
- access pattern
- source grain
- source freshness
- schema stability
- validation status
- caveats

## Extract from KPI feasibility

- KPI grain
- required fields
- Gold output needs
- caveats

## Update documents

Update:
- `storage-design.md`
- `source-to-storage-mapping.md`

## Update frontmatter

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-architecture-context