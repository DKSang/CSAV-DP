# Installation Guide Template

```markdown
---
title: "DEW Installation Guide"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "4-implementation"
stepsCompleted: []
decisionGates:
  GATE-33-installation-docs:
    status: pending
---

# DEW Installation Guide

## 0. Purpose

This guide explains how to install the DEW skill module.

## 1. Prerequisites

## 2. Repository Layout

```text
src/dew-skills/
├── module.yaml
├── module-help.csv
├── 1-analysis/
├── 2-plan-workflows/
├── 3-solutioning/
└── 4-implementation/
```

## 3. Installation Options

### Option A — Copy module into agent skills directory

### Option B — Use repo as skill source

### Option C — Manual local usage

## 4. Configuration

Expected config:

```text
_dew/dew/config.yaml
_dew/custom/
planning_artifacts/
implementation_artifacts/
evidence_artifacts/
learning_artifacts/
```

## 5. Verify Installation

## 6. First Run

Recommended first skill:

`dew-project-brief`

## 7. Upgrade Notes

## 8. Known Caveats
```
