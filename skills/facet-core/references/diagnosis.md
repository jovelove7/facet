# Diagnosis

Every default answer names what kind of problem this is before explaining it. A reader who stops after one line should still know which part of the company has to move.

## Categories

Choose exactly one.

| Category | Assign when |
|---|---|
| Messaging | The wording claims more, or more broadly, than the product does. The product already does the narrower thing well. |
| Product | The feature exists, but the default behavior or the core logic does not carry the promise out. |
| UX | The logic is right, but people do not reach it, notice it, or understand it. |
| Policy | Rules, eligibility, or terms narrow the promise. |
| Operations | Staffing, turnaround, or support quality cannot keep up with the promise. |
| Measurement | The company does not measure the outcome it promised, or measures something else. |
| Connection | Each area works on its own, and the promise breaks between them. |
| Not determinable | Public evidence cannot separate the areas. |

Rules:

- One category. If two fit, take the one the user meets first.
- `Connection` requires evidence that both areas work independently. Without it, name the weaker area instead.
- `Not determinable` is a real answer, not a fallback. Use it when the evidence genuinely cannot separate areas, never to avoid committing.

## The block

The section opens with the diagnosis, then three noun phrases:

```markdown
> **Diagnosis: this is a product problem, not a messaging problem.**

- **Main problem location:** <the point in the product that has to change>
- **Where the connection breaks:** <function A> ↔ <function B>
- **Also visible:** <a second problem the evidence exposed, if any>
```

`Also visible` is optional. Drop the line rather than filling it.

## Location, not prescription

Name where the problem sits. Do not say what to build.

- Allowed: `the default behavior of the recommendation feed`
- Not allowed: `change the default to a chronological feed`

The reader decides what to do. The audit decides where to look.

## Naming the functions

Use the names the company itself uses in public for those functions. If TikTok publicly describes trust and safety and a recommendation system, write `Trust & Safety ↔ Recommendation`.

What is forbidden is a claim, not a vocabulary:

- Do not assert that teams do not coordinate, that a department decided something, or that anyone is responsible.
- Do not name individuals.
- What public evidence supports is that two functions move separately in the finished product. Write that, and stop there.

## No evasion

- The diagnosis is one declarative sentence, twenty words or fewer.
- No conditional clauses in it. No `may`, `appears`, or `is consistent with`.
- Hedged verbs belong in the causal section only, and only for causes.
- The three lines are noun phrases. Not sentences.

## The closing hypothesis

The causal section ends with one quoted sentence that states the surviving explanation in full.

```markdown
> **<The company implements X as A rather than B.>**
```

State it. Then, in one plain sentence, separate what public evidence establishes from what it does not. That sentence is a boundary, not a retreat: it says what is known, not that nothing is.
