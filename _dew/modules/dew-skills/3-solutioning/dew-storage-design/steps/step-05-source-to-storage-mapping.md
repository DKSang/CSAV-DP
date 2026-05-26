# Step 05 — Source-to-Storage Mapping

## Mandatory Rules

- Every P1 source must have a raw/bronze target.
- Every P1 source must have schema snapshot target.
- Every source caveat must be carried forward.
- Do not create ingestion logic here.

## Task

Map sources to storage targets.

## For each source

Record:

| Source ID | Source Name | Raw/Bronze Target | Silver Target | Schema Snapshot Target | Quarantine Target | Metadata Required |
|---|---|---|---|---|---|---|

## Mapping considerations

- source type
- access method
- file/API response shape
- schema stability
- grain
- freshness
- DQ risk
- caveats

## Update

Update:
- storage-design.md
- source-to-storage-mapping.md

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-architecture-context
  - step-03-storage-layer-gate
  - step-04-metadata-retention-schema-gates
  - step-05-source-to-storage-mapping