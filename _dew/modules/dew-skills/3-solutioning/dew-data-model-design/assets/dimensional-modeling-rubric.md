# Dimensional Modeling Rubric

## Fact table

Use when:
- model represents measurements/events
- metrics are calculated
- dimensions provide context

## Dimension table

Use when:
- model represents descriptive entity attributes
- attributes are used to filter/group facts

## Aggregate mart

Use when:
- serving layer needs precomputed KPI/summary
- dashboard/report performance matters
- grain is consumer-oriented

## Wide reporting table

Use when:
- dashboard/report needs simple consumption
- project scope is small
- semantic layer is lightweight

Risk:
- duplication
- harder reuse

## Bridge table

Use when:
- two grains/entities must be mapped
- many-to-many relation exists
- source grain differs from target grain

Risk:
- bridge assumptions affect KPI meaning

## Snapshot table

Use when:
- point-in-time state matters
- history tracking is needed
