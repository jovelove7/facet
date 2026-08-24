# Contributing to Facet

Facet should improve by changing the rule that produced a weak judgment, not by hand-fixing one answer.

## Before proposing a change

1. Identify the exact claim, evidence, relationship, hypothesis, or output rule that failed.
2. Show a case where the current rule produces an unsupported, inconsistent, or unclear result.
3. Change the narrowest reusable rule that fixes the failure.
4. Add or update a regression case without hard-coding the desired company verdict.
5. Run `python3 scripts/check_skill.py`.

## Design constraints

- Keep the reader-facing output simple, intuitive, and stable.
- Keep verification exhaustive behind the output.
- Do not add a visible confidence score or methodology block.
- Do not convert missing public evidence into evidence of absence.
- Do not let a first-party claim or feature prove its own outcome.
- Do not force one causal hypothesis when several still fit.
- Do not add rankings or recommendations to Facet Core.

## Regression philosophy

Tests should assert invariants such as scope control, concrete evidence, competing-hypothesis checks, explicit uncertainty, and output order. They should not require Facet to preserve a conclusion after the underlying evidence changes.

Add regression prompts to `tests/facet-core-regression.md` and explain which reusable rule the case exercises.
