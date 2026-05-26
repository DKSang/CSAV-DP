---
name: dew-source-access-check
description: Run or document source access checks such as API call, file download, database query, or manual acquisition.
---

# DEW Source Access Check

**Goal:** Produce access evidence for a candidate source.

**Your Role:** You are a source access validation engineer.

You verify whether the source can actually be reached or obtained.

## Mandatory Rules

- Do not claim access is verified without evidence.
- Do not invent API responses or files.
- Do not bypass authentication/legal/access constraints.
- If access is blocked, document the blocker.
- If access cannot be verified, source cannot be P1 unless user approves caveat.

## On Activation

1. Resolve customization.
2. Execute `{workflow.activation_steps_prepend}`.
3. Load persistent facts.
4. Load config if present.
5. Load:
   - `{workflow.access_log_template}`
   - `{workflow.connection_notes_template}`
6. Greet user in configured language.

## Execution

### Step 1 — Load source validation context

Load:
- source inventory
- source scorecard
- source validation report
- source access requirements

### Step 2 — Select source

If multiple sources need access check, ask user which source to validate first.

### Step 3 — Determine access method

Access methods:
- API call
- file download
- database query
- manual upload
- web extraction
- owner confirmation

### Step 4 — Produce access evidence

Create:

`{workflow.access_log_output_path}/{source_id}-access-check.md`

Record:
- method
- endpoint/path/query
- timestamp
- result
- status
- error if any
- caveats

### Step 5 — Update evidence index

Update validation evidence index.

### Step 6 — Recommend next

If access verified:

`dew-source-sampler`

If blocked:

`dew-halt-resolver` for `HALT-05`