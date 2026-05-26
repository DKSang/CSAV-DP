# DEW Decision Gate Catalog

## Phase 00 — Project Framing

### GATE-00 — Project Scope Gate

Decision:
- learning project
- portfolio project
- internal decision-support
- production-grade

Required before:
- Data Product PRD

Related HALT:
- HALT-00
- HALT-01

---

## Phase 01 — Business, KPI & Data Product Discovery

### GATE-01 — Data Consumer Gate

Decision:
- who consumes the data product

Required before:
- KPI discovery
- source discovery

Related HALT:
- HALT-01
- HALT-15

### GATE-02 — Business Decision Gate

Decision:
- what decision the data product supports

Required before:
- KPI definition

Related HALT:
- HALT-01

### GATE-03 — KPI Definition Gate

Decision:
- accepted KPI definition
- formula
- grain
- dimensions
- required fields

Required before:
- KPI feasibility validation

Related HALT:
- HALT-02

### GATE-04 — KPI Grain Gate

Decision:
- one row represents what

Required before:
- KPI feasibility
- data model design

Related HALT:
- HALT-07

### GATE-05 — Trust Expectation Gate

Decision:
A. Exploratory only
B. Internal decision-support with documented limitations
C. Trusted shared product with quality checks
D. Production-grade with contracts and monitoring

Required before:
- source priority
- architecture
- serving design

Related HALT:
- HALT-08

---

## Phase 02 — KPI Feasibility Validation

### GATE-06 — KPI Feasibility Gate

Decision:
- verified
- feasible with caveats
- hypothesis only
- rejected
- deferred

Required before:
- architecture

Related HALT:
- HALT-03
- HALT-18

---

## Phase 03 — Source Discovery & Validation

### GATE-07 — Source Access Gate

Decision:
- access verified
- access blocked
- manual only
- reject source

Required before:
- source validation
- source priority

Related HALT:
- HALT-05

### GATE-08 — Source Trust Gate

Decision:
A. P1 — Use in MVP
B. P2 — Use later
C. Exploration only
D. Reject

Required before:
- architecture
- ingestion design

Related HALT:
- HALT-06

### GATE-09 — Source Grain Gate

Decision:
- source grain approved
- needs bridge/mapping
- incompatible with target KPI grain
- reject/defer source

Required before:
- transformation design

Related HALT:
- HALT-07

### GATE-10 — Source Freshness Gate

Decision:
- freshness sufficient
- freshness insufficient but acceptable with caveat
- source needs alternate update process
- reject source

Required before:
- ingestion frequency design

Related HALT:
- HALT-09

### GATE-11 — Schema Evolution Gate

Decision:
A. Strict schema contract
B. Schema snapshot + drift detection
C. Flexible rescued fields
D. Manual review on change

Required before:
- ingestion design

Related HALT:
- HALT-13

---

## Phase 04 — Requirement Gate

### GATE-12 — Architecture Readiness Gate

Decision:
A. Proceed to architecture
B. Proceed with caveats
C. Return to KPI validation
D. Return to source validation
E. Reduce MVP scope

Required before:
- data architecture

Related HALT:
- HALT-10

---

## Phase 05 — Data Architecture

### GATE-13 — Architecture Pattern Gate

Decision:
- local-first
- warehouse-first
- lakehouse
- hybrid
- streaming-first

Required before:
- storage design

Related HALT:
- HALT-10

### GATE-14 — Technology Choice Gate

Decision:
- tool/platform choice
- rejected alternatives
- revisit trigger

Required before:
- implementation stories

Related HALT:
- HALT-17

---

## Phase 06 — Storage & Ingestion Design

### GATE-15 — Storage Layer Gate

Decision:
- raw/bronze/silver/gold shape
- metadata expectations
- retention

Required before:
- ingestion implementation

Related HALT:
- HALT-11

### GATE-16 — Ingestion Pattern Gate

Decision:
- pull API
- file drop
- database export
- CDC
- stream
- manual

Required before:
- ingestion story

Related HALT:
- HALT-12

### GATE-17 — Batch vs Streaming Gate

Decision:
- batch
- micro-batch
- streaming
- event-driven

Required before:
- orchestration design

Related HALT:
- HALT-12

---

## Phase 07 — Transformation, Modeling & DQ Design

### GATE-18 — Data Quality Rule Gate

Decision:
- minimum DQ rules
- warning vs blocking
- quarantine behavior

Required before:
- gold modeling
- serving

Related HALT:
- HALT-14

### GATE-19 — Transformation Rule Gate

Decision:
- business rules approved
- rule caveats
- deferred logic

Required before:
- data story implementation

Related HALT:
- HALT-14

---

## Phase 08 — Serving, Governance & DataOps

### GATE-20 — Serving Mode Gate

Decision:
- dashboard
- data mart
- API
- ML feature table
- notebook/report
- reverse ETL

Required before:
- serving implementation

Related HALT:
- HALT-15

### GATE-21 — Privacy Posture Gate

Decision:
- no sensitive data
- low-risk internal
- PII present with controls
- high-risk requires governance review

Required before:
- implementation

Related HALT:
- HALT-16

### GATE-22 — Operational Readiness Gate

Decision:
- minimal logs
- monitored internal pipeline
- SLA-backed production pipeline
- not operationally ready

Required before:
- production-like serving

Related HALT:
- HALT-17

---

## Phase 09 — Epics, Stories & Readiness

### GATE-23 — Implementation Readiness Gate

Decision:
A. Ready for stories
B. Ready with caveats
C. Return to architecture
D. Return to source/KPI validation

Required before:
- sprint planning

Related HALT:
- HALT-17

---

## Phase 10 — Build, Review & Retrospective

### GATE-24 — Validation Evidence Gate

Decision:
- evidence accepted
- evidence incomplete
- rerun validation
- revise story

Required before:
- story done

Related HALT:
- HALT-18

### GATE-25 — Learning Capture Gate

Decision:
- learning captured
- pattern extracted
- needs retrospective
- close epic

Required before:
- epic closure

Related HALT:
- HALT-19