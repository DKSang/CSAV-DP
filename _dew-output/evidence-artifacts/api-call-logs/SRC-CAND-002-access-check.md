---
title: "Source Access Check - SRC-CAND-002"
status: completed
created: 2026-05-26
updated: 2026-05-26
workflow: dew
relatedSource: "SRC-CAND-002"
evidenceType: "access-check"
---

# Source Access Check: SRC-CAND-002 - CS-MAP risk maps

## Access Method

- Web extraction
- Repository API call
- File download probe

## Access Target

- CCAFS publication page: <https://ccafs.cgiar.org/resources/publications/climate-smart-maps-and-adaptation-plans-cs-map-13-provinces-vietnams>
- Permanent link: <https://hdl.handle.net/10568/100093>
- CGSpace item page after redirect: <https://cgspace.cgiar.org/items/7ad07ea7-62f5-445c-b19a-083924c54735>
- CGSpace item API: <https://cgspace.cgiar.org/server/api/core/items/7ad07ea7-62f5-445c-b19a-083924c54735>
- CGSpace bundles API: <https://cgspace.cgiar.org/server/api/core/items/7ad07ea7-62f5-445c-b19a-083924c54735/bundles>
- Sample original bitstream: <https://cgspace.cgiar.org/server/api/core/bitstreams/029fe554-308e-4d88-bebf-a0408836ae9c/content>

## Authentication / Permission Notes

No authentication was required for the checked page, item metadata API, bundle listing, or sample bitstream download.

The CCAFS page footer states Creative Commons Attribution-NonCommercial 4.0 International. The CGSpace item API returned `dcterms.license: Other`, so license/terms must be reviewed before reuse in a data product.

## Execution Timestamp

2026-05-26T23:47:10+07:00

## Result

- Verified

## Evidence

- CCAFS publication page responded with HTTP `200`, content type `text/html; charset=UTF-8`, final URI unchanged, title `Climate-Smart Maps and Adaptation Plans (CS MAP) of the 13 provinces in Vietnam's Mekong River Delta`, and response length `64213`.
- Permanent handle `https://hdl.handle.net/10568/100093` responded with HTTP `200` and redirected to `https://cgspace.cgiar.org/items/7ad07ea7-62f5-445c-b19a-083924c54735`.
- CGSpace item API responded with HTTP `200`, content type `application/hal+json;charset=UTF-8`, item name `Climate-Smart Maps and Adaptation Plans (CS MAP) of the 13 provinces in Vietnam's Mekong River Delta`, handle `10568/100093`, country `Vietnam`, and license metadata `Other`.
- CGSpace bundles API responded with HTTP `200` and exposed an `ORIGINAL` bundle.
- The `ORIGINAL` bundle query with `?size=100` returned `39` original bitstreams.
- Sample original bitstream `AnGiang_NguycoMan_CD.jpg` downloaded successfully with HTTP `200`, content type `image/jpeg;charset=UTF-8`, content disposition `inline; filename="AnGiang_NguycoMan_CD.jpg"`, length `1686868`, and first 10 bytes `FF D8 FF E1 1F AD 45 78 69 66`, consistent with a JPEG file.
- Example original bitstreams returned by the API:
  - `AnGiang_NguycoMan_CD.jpg` - `1686868` bytes
  - `AnGiang_NguycoNgap_CD.jpg` - `1811881` bytes
  - `AnGiang_NguycoNgap_TB.jpg` - `1754843` bytes
  - `BacLieu_NguyCoMan_CD.jpg` - `1200470` bytes
  - `BacLieu_NguyCoMan_TB.jpg` - `1184418` bytes

## Caveats

- Access is verified for web pages, CGSpace metadata API, bundle listing, and JPEG map bitstreams only.
- This check does not validate whether GIS/vector data, shapefiles, rasters with georeferencing, or tabular risk attributes are available.
- The discovered source appears useful for visual risk-map evidence, but may not be directly machine-readable for MVP KPI computation without manual/geospatial extraction.
- License metadata is inconsistent enough to require a license/terms review before reuse: page footer says CC BY-NC 4.0, while item API says `Other`.
- Field schema, geographic grain, risk classification definitions, scenario labels, crop/season compatibility, and administrative boundary compatibility are not validated by this access check.

## Next Step

- `dew-source-sampler`
