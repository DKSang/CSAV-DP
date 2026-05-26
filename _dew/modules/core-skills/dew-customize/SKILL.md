---
name: dew-customize
description: 'Authors and updates customization overrides for installed DEW skills.'
---

# DEW Customize

**Goal:** Translate user intent into correctly placed TOML override files under `{project-root}/_dew/custom/`.

## Scope

This skill supports:
- per-skill `[agent]` overrides
- per-skill `[workflow]` overrides
- sparse TOML override files
- team overrides and user overrides

## Preflight

- If `{project-root}/_dew/` does not exist, say DEW is not installed and stop.
- If `{project-root}/_dew/scripts/resolve_customization.py` exists, use it for verification.
- If resolver is missing, continue with manual merge explanation.

## Execution

### Step 1 — Classify Intent

Classify as:
- Directed — specific skill and change requested.
- Exploratory — user asks what can be customized.
- Audit/iterate — user wants to inspect or update existing overrides.
- Cross-cutting — change may affect multiple skills.

### Step 2 — Discover Customizable Skills

Scan installed skill roots for `customize.toml`.

For each customizable skill, report:
- skill name
- surface: `[agent]` or `[workflow]`
- exposed fields
- existing team/user override if present

### Step 3 — Determine Surface

Read target skill's `customize.toml`.

Heuristics:
- Workflow-level: template swap, output path, activation hooks, persistent facts for one workflow.
- Agent-level: persona, communication style, principles, behavior across workflows.

If ambiguous, present both options and ask user to choose.

### Step 4 — Compose Override

Write sparse TOML only for fields being changed.

Merge semantics:
- scalars override
- arrays append unless keyed merge is documented
- tables deep-merge
- keyed arrays merge by `code` or `id` when applicable

Never copy entire `customize.toml` into override.

### Step 5 — Placement

Use:
- `{skill-name}.toml` for team/shared override
- `{skill-name}.user.toml` for personal override

Confirm placement before writing.

### Step 6 — Show, Confirm, Write, Verify

1. Show full TOML.
2. If file exists, show diff.
3. Wait for explicit approval.
4. Write file under `{project-root}/_dew/custom/`.
5. Verify using resolver if available.

If resolver is unavailable, manually explain base → team → user merge.

## Completion

Complete only when:
- override file is written, or user explicitly aborts
- user has seen verification or manual merge summary
- next iteration path is clear

## Cannot Help When

- requested field is not exposed in `customize.toml`
- user wants to change hidden step logic directly
- skill has no `customize.toml`
