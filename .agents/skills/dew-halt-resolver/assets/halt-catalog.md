# DEW HALT Catalog

## HALT-00 — Project Scope Missing

Triggered when the project scope is not clear enough to start the workflow.

Type: Hard Halt

Resume when:
- scope is defined
- MVP boundary is clear
- user approves scope

---

## HALT-01 — Business Decision Unclear

Triggered when the workflow cannot identify what decision the data product supports.

Type: Hard Halt

Resume when:
- target decision is defined
- consumer is identified
- business question is clear

---

## HALT-02 — KPI Definition Unverified

Triggered when a KPI is proposed but lacks formula, grain, dimensions, or required fields.

Type: Hard Halt

Resume when:
- KPI formula is defined
- grain is defined
- required fields are listed
- user approves definition

---

## HALT-03 — KPI Feasibility Not Proven

Triggered when primary KPI feasibility has not been tested with real source/sample data.

Type: Hard Halt

Resume when:
- sample computation exists
- or KPI is explicitly deferred/caveated by user decision

---

## HALT-04 — Source Not Identified

Triggered when the workflow needs source systems but none are identified.

Type: Hard Halt

Resume when:
- candidate sources are listed
- source owner/access method is recorded

---

## HALT-05 — Source Access Not Verified

Triggered when a source is listed but access has not been tested.

Type: Hard Halt

Resume when:
- API call/download/query succeeds
- or access limitation is documented and approved

---

## HALT-06 — Source Trust Not Established

Triggered when a source is being promoted to P1 without enough evidence.

Type: Hard Halt

Resume when:
- source sample exists
- schema snapshot exists
- profiling or quality notes exist
- user approves source trust level

---

## HALT-07 — Grain Undefined

Triggered when the workflow cannot define what one row represents.

Type: Hard Halt

Resume when:
- source grain is defined
- target KPI/product grain is defined
- bridging/mapping need is documented

---

## HALT-08 — Trust Expectation Required

Triggered when product trust level is not defined.

Type: Soft Halt

Resume when user chooses:
A. Exploratory only
B. Internal decision-support with documented limitations
C. Trusted shared product with quality checks
D. Production-grade with contracts and monitoring

---

## HALT-09 — Freshness Unverified

Triggered when source/product freshness is assumed but not verified.

Type: Hard Halt

Resume when:
- observed source freshness is documented
- required freshness is approved
- caveat is recorded if mismatch exists

---

## HALT-10 — Architecture Before Validation

Triggered when the workflow attempts to create final architecture before KPI/source validation is complete.

Type: Readiness Halt

Resume when:
- KPI feasibility report exists
- source validation report exists
- requirement gate is approved

---

## HALT-11 — Storage Layer Unclear

Triggered when storage zones/layers are not defined.

Type: Hard Halt

Resume when:
- raw/bronze/silver/gold or equivalent layers are defined
- metadata expectations are approved

---

## HALT-12 — Ingestion Pattern Unclear

Triggered when source access pattern is known but ingestion pattern is not chosen.

Type: Hard Halt

Resume when:
- ingestion mode is chosen
- batch/streaming decision is made
- failure handling is defined

---

## HALT-13 — Schema Evolution Undefined

Triggered when source schema may change but handling policy is missing.

Type: Hard Halt

Resume when user chooses:
A. Strict schema contract
B. Schema snapshot + drift detection
C. Flexible rescued fields
D. Manual review on change

---

## HALT-14 — DQ Rules Missing

Triggered when transformation/serving is planned without data quality rules.

Type: Hard Halt

Resume when:
- minimum DQ rule set is defined
- blocking/warning behavior is approved

---

## HALT-15 — Serving Consumer Unclear

Triggered when the serving layer is designed without a known consumer.

Type: Hard Halt

Resume when:
- consumer is defined
- serving mode is selected
- success criteria are known

---

## HALT-16 — Security Privacy Unreviewed

Triggered when data may include sensitive, personal, regulated, or access-controlled data but privacy/security posture is missing.

Type: Safety Halt

Resume when:
- privacy classification is complete
- access control approach is approved
- sensitive data handling is documented

---

## HALT-17 — Implementation Not Ready

Triggered when stories are requested before core artifacts are validated.

Type: Readiness Halt

Resume when:
- PRD exists
- KPI feasibility exists
- source validation exists
- architecture is approved
- storage/ingestion/transformation designs are sufficiently complete

---

## HALT-18 — No Validation Evidence

Triggered when a phase is marked done without evidence.

Type: Hard Halt

Resume when:
- required evidence is produced
- or user explicitly approves caveated continuation

---

## HALT-19 — Learning Capture Missing

Triggered when an epic/project is being closed without learning notes.

Type: Soft Halt

Resume when:
- `.learning-log.md` is updated
- reusable pattern is extracted if applicable
- unresolved lessons are recorded

---

## HALT-20 — Release Not Ready

Triggered when E2E validation fails or critical release readiness items are missing.

Type: Hard Halt

Resume when:
- E2E validation passes
- critical evidence gaps are filled
- user approves release with caveats

---

## HALT-21 — Documentation Incomplete

Triggered when required documentation (user-facing or technical) is missing before final closure.

Type: Soft Halt

Resume when:
- README, Data Dictionary, or Runbook is completed
- or user accepts documentation gaps

---

## HALT-22 — Skill Pack QA Failed

Triggered when the DEW skill pack itself fails structural or logical consistency checks.

Type: Hard Halt

Resume when:
- missing files are created
- broken links are fixed
- inconsistencies are resolved

---

## HALT-23 — Package Release Not Ready

Triggered when packaging scope, version, or release notes are missing.

Type: Hard Halt

Resume when:
- version is selected
- release notes are drafted
- user approves package release

---

## HALT-24 — Installation Documentation Incomplete

Triggered when onboarding guides, command references, or troubleshooting steps are missing.

Type: Soft Halt

Resume when:
- installation guide is completed
- verification steps are included