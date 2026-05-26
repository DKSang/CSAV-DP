---
title: SRC-CAND-006 Unblock Research Note
status: partially-unblocked
phase: "05-source-assessment"
created: 2026-05-26
source_candidate: SRC-CAND-006
result: split_into_concrete_subsources
---

# SRC-CAND-006 Unblock Research Note

## 1. Purpose

`SRC-CAND-006 — Salinity / flooding / reservoir / rainfall indicators` was previously blocked by `HALT-06 — Source Trust Not Established` because it did not identify a concrete provider, access path, license, schema, or coverage evidence.

This note breaks the broad candidate into more concrete sub-sources that can be validated separately.

## 2. Unblock Decision

Do not keep `SRC-CAND-006` as one vague source.

Split it into sub-candidates:

| New Sub-ID | Source Theme | Candidate Provider / Dataset | Validation Status |
|---|---|---|---|
| `SRC-CAND-006A` | Rainfall / drought monitoring | CHIRPS Daily precipitation | Candidate for validation |
| `SRC-CAND-006B` | Near-real-time rainfall / flood-trigger rainfall | NASA GPM IMERG | Candidate for validation |
| `SRC-CAND-006C` | River discharge / flood forecasting | Copernicus CEMS GloFAS forecast/reforecast | Candidate for validation |
| `SRC-CAND-006D` | Mekong hydrological observations | Mekong River Commission Data Portal | Candidate but access/API details need validation |
| `SRC-CAND-006E` | Salinity intrusion / station salinity | Official Vietnam/SIWRR/DARD/MARD or Mekong Delta salinity datasets | Still blocked until concrete data access is found |

## 3. Candidate Details

### SRC-CAND-006A — CHIRPS Daily Precipitation

Expected role:

- rainfall anomaly;
- drought monitoring;
- historical precipitation baseline;
- support for `risk_driver_type = rainfall_anomaly` or `drought`.

Assessment:

- Strong candidate for rainfall/drought component.
- Public-domain terms appear favorable.
- Needs sample extraction and Vietnam/MRD clipping validation.

### SRC-CAND-006B — NASA GPM IMERG

Expected role:

- near-real-time rainfall;
- flood-trigger rainfall monitoring;
- short latency precipitation signal.

Assessment:

- Strong candidate for rainfall/flood trigger.
- Requires Earthdata/PPS access validation.
- Need choose Early/Late/Final product depending latency vs research quality.

### SRC-CAND-006C — Copernicus CEMS GloFAS

Expected role:

- river discharge;
- flood forecast / flood risk signal;
- upstream hydrological condition.

Assessment:

- Strong candidate for flood/discharge component.
- Global coverage and daily/forecast products appear relevant.
- Needs EWDS access, license, sample extraction, and Vietnam/Mekong spatial matching validation.

### SRC-CAND-006D — Mekong River Commission Data Portal

Expected role:

- hydrological observations for Mekong basin;
- potential water level/discharge station data.

Assessment:

- Relevant institutionally.
- Data portal exists but requires JavaScript; API/download details were not verified in this pass.
- Keep as candidate but not yet validated.

### SRC-CAND-006E — Salinity Intrusion / Station Salinity

Expected role:

- direct salinity intrusion signal;
- `risk_driver_type = salinity`;
- advisory rules for prepare_for_salinity, crop shift, or avoid rice cultivation.

Assessment:

- Still the most important gap for MRD advisory logic.
- No concrete open machine-readable dataset was validated in this pass.
- Keep `HALT-06` for salinity-specific operational data until provider/access/license/sample is found.

Potential provider categories to investigate:

- Vietnam official hydro-meteorological sources;
- MARD/DARD salinity bulletins;
- Southern Institute of Water Resources Research / related projects;
- provincial salinity monitoring portals;
- Mekong Delta research/open data repositories.

## 4. Revised Status for SRC-CAND-006

`SRC-CAND-006` is now **partially unblocked**:

- rainfall component: unblocked into CHIRPS and IMERG candidates;
- flood/discharge component: unblocked into GloFAS and MRC candidates;
- salinity component: still blocked pending concrete source discovery.

## 5. Recommended Next Validation Order

1. Validate `SRC-CAND-006A` CHIRPS access and sample extraction.
2. Validate `SRC-CAND-006C` GloFAS access and sample extraction.
3. Validate `SRC-CAND-006B` IMERG access and product choice.
4. Investigate `SRC-CAND-006D` MRC data portal access/API.
5. Continue targeted search for `SRC-CAND-006E` salinity station/source data.

## 6. Decision

**Decision:** Split broad hydrology source candidate into concrete sub-candidates.

**Status:** Partially unblocked.

**Date:** 2026-05-26
