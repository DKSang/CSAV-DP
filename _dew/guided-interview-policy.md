# DEW Guided Interview Policy

## Purpose

Make every DEW skill beginner-friendly by default. Skills must guide users step by step instead of asking for a large form all at once.

## Global Rule

When `guided_interview_mode` is true or `question_batch_size` is `1`, ask exactly one primary question at a time.

Do not ask a 5-10 item questionnaire in a single response unless the user explicitly chooses expert mode.

## Question Format

Every question should include:

1. A short explanation of why the question matters.
2. 2-5 concrete answer options when possible.
3. One recommended/default option when reasonable.
4. Permission to answer `chưa rõ` / `not sure`.
5. A clear next step after the user answers.

Recommended format:

```markdown
We need to decide **<concept>** because <reason>.

Question 1/<n>: <single question>

You can answer with:
A. <option>
B. <option>
C. <option>
D. Not sure yet

Recommended for your case: <option> because <reason>.
```

## Beginner Mode Behavior

If `user_skill_level` is `beginner`:

- Explain jargon before using it.
- Prefer examples over abstract definitions.
- Ask one question at a time.
- Avoid HALT language unless risk is serious.
- Use `guided discovery` before declaring a hard halt.
- Produce draft artifacts with missing fields instead of blocking immediately.

## HALT Behavior

Do not trigger a hard HALT just because the user is unsure.

Use this sequence:

1. Ask one clarifying question.
2. Offer examples/options.
3. If still unclear, create a draft artifact with `status: draft` and `missing:` fields.
4. Trigger HALT only when the user asks to finalize or proceed past a required gate without required evidence.

## Artifact Behavior

When information is incomplete, create a draft artifact instead of a final artifact.

Draft frontmatter example:

```yaml
status: draft
gate:
  GATE-00-project-scope: pending
missing:
  - target user
  - business decision
```

## Expert Mode

If `question_batch_size` is `all` or the user asks for expert mode:

- It is acceptable to ask a full checklist.
- Still avoid inventing answers.
- Clearly label assumptions and missing evidence.

## Applies To

This policy applies to all DEW skills, especially:

- dew-project-brief
- dew-business-discovery
- dew-kpi-discovery
- dew-data-product-prd
- dew-kpi-feasibility
- dew-source-discovery
- dew-source-assessment
- dew-source-validation
- dew-requirement-gate
- dew-data-architecture
- dew-create-data-story
