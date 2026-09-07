# Diagnosis

Every default answer states the result before explaining it. If a material break survives the scope check, name what kind of problem it is. If nothing breaks inside scope, state that the promise held with equal force.

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

These categories apply only after a material break survives. `Held within scope` is an outcome, not a problem category.

## Finding nothing is a finding

An audit that must produce a break will invent one. The most common way to invent one is to judge wording against a surface it never addressed - a design brief against product naming, a launch claim against support, a market-specific promise against another market.

Before naming any break, confirm that the surface you are judging is one the wording actually governs. If it is not, the promise held, and the problem you can see belongs to a different promise.

## When the promise held

```markdown
> **판정: 검증한 범위에서는 약속이 지켜졌다.**

- **달성한 것:** <what the wording set out to do, and what is now true>
- **약속 범위 내 판정:** 지켜짐
- **별도 고려사항:** <an observation outside the scope, named as a separate question>
- **주의:** <that observation>을 이 약속의 실패 증거로 사용하지 않는다
```

```markdown
> **Verdict: the promise holds inside the scope this wording governed.**

- **Achieved:** <what the wording set out to do, and what is now true>
- **Verdict within the promise's scope:** holds
- **Separate consideration:** <an observation outside the scope, named as a separate question>
- **Caution:** do not use <that observation> as evidence that this promise failed
```

The opening line changes word with the branch. A break is a `진단` / `Diagnosis`, because something has to be located and fixed. A promise that held is a `판정` / `Verdict`, because there is nothing to diagnose.

Say what held with the same force used for a break. `지켜졌다` and `holds` are declarative. Do not soften a clean result into faint praise. If there is no adjacent observation worth surfacing, omit both `별도 고려사항` / `Separate consideration` and `주의` / `Caution`.

The final section then shows two or three verification points that demonstrate why the verdict holds and closes with one quoted sentence stating what the company achieved. These are evidence checks, not causal hypotheses about a failure that did not occur.

## Promises with two dimensions

Some wording claims a capability and an outcome in the same sentence. `Connect everything local, and wake the hidden value of a neighborhood` claims a connection and claims what the connection produces. The capability can be verified while the outcome cannot.

- Judge by dimension only when the wording itself carries both. Do not manufacture a second dimension to hedge.
- A verified capability is not a verified outcome, and an unmeasured outcome does not withdraw the capability.
- When the outcome cannot be measured, that is a `별도 고려사항`, not a second verdict. One verdict per audit.
- Name the evidence that would settle the unmeasured half, so the reader knows what to go get.

A verdict split across two dimensions reads as indecision. Give the verdict on the dimension the wording is mainly making a claim about, and put the other one below it.

## Adjacent promises

A problem visible outside the audited scope is not this promise's problem. When one is visible:

- name the layer;
- name the wording that governs it, if the company has published one;
- say that judging it requires a separate audit;
- pass no verdict on it here.

Naming an adjacent promise is orientation. Judging it in passing is the scope error this section exists to prevent.

## The material-break block

When a material break survives, the section opens with the diagnosis, then three noun phrases:

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

## No evasion in a break diagnosis

- The diagnosis is one declarative sentence, twenty words or fewer.
- No conditional clauses in it. No `may`, `appears`, or `is consistent with`.
- Hedged verbs belong in the causal section only, and only for causes.
- The three lines are noun phrases. Not sentences.

## The closing hypothesis for a break

The causal section ends with one quoted sentence that states the surviving explanation in full.

```markdown
> **<The company implements X as A rather than B.>**
```

State it. Then, in one plain sentence, separate what public evidence establishes from what it does not. That sentence is a boundary, not a retreat: it says what is known, not that nothing is.
