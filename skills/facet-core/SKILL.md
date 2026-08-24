---
name: facet-core
description: Trace where a single company's core promise changes, weakens, disappears, or conflicts across brand, marketing, product, UX, policy, support, outcomes, and independent evidence, then present only the best-supported causal hypothesis. Use when a user asks where a company's message breaks or leaks, whether a brand promise holds through the actual product or experience, why narrative and reality diverge, or requests a message-integrity audit. Also use for desk research in product marketing, brand and messaging, audience and positioning, and user research, such as testing whether a competitor's strength is product-backed or messaging-heavy, pressure-testing launch language against the experience it describes, finding where a story goes quiet between touchpoints, attaching a dated source to a claim, or narrowing competing explanations before primary research. Do not use for company comparisons, rankings, vendor selection, or generic brand summaries.
---

# Facet Core

Facet Core is a verification-first message-integrity audit for one company. Find the exact surface or relationship where a promise stops holding, then offer a causal explanation only after competing hypotheses have been attacked.

## Required input

Accept:

- one company, organization, product, or service;
- one core promise, proposition, or priority claim when supplied;
- optional product, market, audience, geography, or time scope.

If the user does not name a promise, identify the strongest explicit proposition in current first-party materials and state the selected wording before analysis. Establish centrality through intentional prominence or repetition on a current homepage, About or mission page, product proposition, investor material, or brand manifesto. Do not promote wording found only in legal boilerplate, a privacy policy, a footer, an archived campaign, or a third-party paraphrase into the company's core promise. Do not invent an implicit mission. If several propositions are equally central and choosing one would materially change the audit, ask the user which one to trace.

For multiple companies, do not rank or synthesize them. Analyze one independently or route comparison requests to a comparison workflow.

## Non-negotiable rules

1. Observe surfaces independently before forming an overall judgment.
2. Treat a capability as evidence of capability, not automatically of outcome, priority, or organizational intent.
3. Compare the same claim dimension across surfaces.
4. Preserve `Unknown` when public evidence cannot support a relationship or cause.
5. Treat missing evidence as omission or uncertainty, not contradiction.
6. Keep product-, branch-, market-, and time-specific evidence at that scope.
7. Describe the structural pattern before explaining it.
8. Generate competing explanations before selecting a likely cause.
9. Let evidence strength control the verb. Do not display confidence bands.
10. Keep the default output compact, but never remove the evidence-to-judgment bridge.
11. Include at least one concrete product moment that a reader can picture. Hide internal labels and calculations, not the observations needed to understand the verdict.
12. Show the message movement path in every default answer. Name where the promise continues and the exact connection where alignment first weakens, breaks, or becomes unobservable.

## Workflow

### 1. Define the promise contract

Quote or closely preserve the company's wording and cite the first-party surface where the company intentionally presents it as a proposition. Verify that the wording is current for the audited period. When the user supplies wording you cannot immediately locate, read `references/evidence-protocol.md` and search again from another angle before calling it unverifiable. A failed search is not evidence that the wording was never said. Atomize the promise into the dimensions that determine whether it holds:

- capability
- scope
- effort
- time
- cost
- condition
- outcome
- priority

For a priority claim, also inspect default behavior, friction, architecture, trade-offs, and what happens when the stated priority conflicts with growth, engagement, cost, or speed.

### 2. Observe surfaces in parallel

Research relevant surfaces independently:

- Corporate / Brand
- Marketing / Sales
- Product / Service
- UX / Customer journey
- Docs / Policy / Support
- Outcomes / Cases
- Independent / Regulatory / Review evidence

Capture the claim, evidence, source, date, first-party or independent status, scope, and supported dimensions. Read `references/evidence-protocol.md` before evaluating material evidence.

### 3. Verify claim against evidence

For each material observation, ask:

- Does the evidence support the whole claim or only one dimension?
- Is a feature being mistaken for effectiveness?
- Is investment being mistaken for priority?
- Is a first-party description being mistaken for independent confirmation?
- Is the evidence current and scoped to the same product, market, or period?

Narrow the observation whenever the evidence is narrower than the claim.

### 4. Build the surface graph

Do not assume a linear funnel. Compare only meaningful edges, such as Promise ↔ Product, Marketing ↔ UX, Product ↔ Outcome, or Claim ↔ Independent evidence.

Read `references/relationship-rubric.md` and assign a relationship only after verification. A normal surface-specific simplification is not automatically divergence.

### 5. Locate the leak

Identify the earliest and deepest material edge where meaning changes. Name the exact surface, mechanism, audience, geography, or stage—not a vague department.

Depth describes structural location, not moral severity:

- **Edge:** distribution, access, support, localization, or another boundary condition.
- **Deep:** core product architecture, default behavior, decision mechanism, or outcome mechanism that the promise claims to govern.

If no material divergence survives verification, say the promise holds or mostly holds within the reviewed scope. If evidence cannot resolve the edge, use `Unknown`.

### 6. Attack competing hypotheses

For every material leak, generate at least two plausible explanations. Read `references/hypothesis-protocol.md`, then run support, contradiction, alternative-explanation, scope, and falsifiability tests.

Present one likely cause only when it explains the pattern better than its competitors. Otherwise list the surviving explanations in one compact sentence and state what evidence would separate them.

### 7. Run the final verification loop

Before responding, confirm:

- the promise wording is traceable;
- every decisive observation has a current source;
- the named leak compares the same claim dimensions;
- `Compressed` and `Divergent` pass the materiality test;
- omission is not presented as contradiction;
- the likely cause does not exceed the observed pattern;
- a competing explanation has not been ignored;
- the language distinguishes observed fact from inference;
- the reader can move from promise to product observation to judgment without an unexplained leap;
- the message movement path names the material surfaces and the exact connection where alignment changes;
- at least one concrete product moment appears in plain language;
- internal terms such as surface graph, governing constraint, architecture edge, or relationship label are absent unless immediately explained;
- no comparison, ranking, recommendation, or remediation plan has leaked into the default output.

## Output

Read `references/output-contract.md` and follow it exactly.

Default to the reader-facing contract:

1. a plain-language verdict title;
2. the message movement path;
3. what the company says;
4. what the product shows;
5. where it changes;
6. why it may be this way.

Answer in the language the user wrote in. The order above never changes; the labels are localized. `references/output-contract.md` carries the Korean and English label sets and the rule for other languages.

In the message movement path, show a one-line chain and a compact two-column table covering only the material connections, normally Marketing → Product → default UX → observed outcome or independent evidence. State which connections continue and where alignment changes. Describe relationships between surfaces; do not assign blame to departments or people.

Keep evidence links inline. Translate internal analysis into ordinary language. Do not expose internal relationship labels, confidence scores, methodology, generic company summaries, action plans, or a separate sources section by default.

When the user asks for proof, expand only the requested layer: evidence chain, surface graph, competing hypotheses, unknowns, or falsification conditions.

## Tone

- Simple but not thin: compact, plain, and sufficiently explained.
- Analytical without sounding prosecutorial.
- Use `may`, `appears`, or `is consistent with` for inferred causes.
- Prefer `Unknown` to an interesting but unsupported explanation.
