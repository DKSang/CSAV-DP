---
title: SRC-CAND-002 Access Check
status: partially_verified
phase: "source-access-check"
created: 2026-05-26
source_id: SRC-CAND-002
source_name: CS-MAP / Climate-Smart Mapping and Adaptation Planning risk maps
skill: dew-source-access-check
next_recommended_workflow: dew-source-sampler
---

# SRC-CAND-002 — Access Check

## 1. Source

| Field | Value |
|---|---|
| Source ID | `SRC-CAND-002` |
| Source name | CS-MAP / Climate-Smart Mapping and Adaptation Planning risk maps |
| Source type | Map image / metadata / possible geospatial planning artifact |
| KPI dependencies | `KPI-MON-001`, `SIG-EXP-001`, `ADV-OUT-001`, `KPI-DQ-001` |

## 2. Access Method

| Field | Value |
|---|---|
| Access method | Web access / map image and metadata retrieval |
| Evidence type | Map image access and metadata access |
| Timestamp | 2026-05-26 |
| Result | Access verified for JPEG map image and metadata |
| Status | Partially verified |

## 3. Verified Access

The following access was verified:

- JPEG map image is reachable/obtainable.
- Associated metadata is reachable/obtainable.

This is enough to prove that the source is not completely blocked at the access level.

## 4. Caveat

Access is **not fully verified for implementation**.

Current caveat:

- Access has been verified for map image JPEG and metadata only.
- GIS vector data has not been verified.
- Shapefile access has not been verified.
- Raster/georeferenced data has not been verified.
- Machine-readable schema has not been verified.
- Coordinate reference system has not been verified.
- Geometry grain has not been verified.
- Attribute fields for risk level, risk type, season, scenario, crop, and adaptation options have not been verified.

Therefore, this access check does **not** prove that the source can be directly used in an automated pipeline.

## 5. Status Interpretation

`SRC-CAND-002` should move from:

```text
blocked_by_access_unknown
```

to:

```text
partially_accessible_image_and_metadata_only
```

It should **not** be promoted to accepted, P1, or implementation-ready.

## 6. Recommended Next Step

Recommended next workflow:

```text
dew-source-sampler
```

Sampling should check:

1. whether the JPEG image can be downloaded consistently;
2. whether metadata includes useful spatial, temporal, and thematic information;
3. whether metadata contains source version/date/provider/license;
4. whether map legend can be interpreted safely;
5. whether there is any linked GIS/shapefile/raster source;
6. whether the image can support manual evidence only or can be transformed into structured data;
7. whether OCR/manual digitization would be required and whether that is acceptable for the MVP.

## 7. Decision

**Decision:** Access is partially verified for JPEG map image and metadata.

**Status:** Partially verified; not implementation-ready.

**Next workflow:** `dew-source-sampler`.
