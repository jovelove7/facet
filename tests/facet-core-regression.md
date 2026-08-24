# Facet Core v0.4.0 Regression Cases

Use these prompts for regression and forward testing. Expected behavior describes invariants, not predetermined conclusions.

## Test 1 — Priority claim

Prompt:

`Use $facet-core to test TikTok's claim that safety is its top priority.`

Expected behavior:

- treats safety features as capability evidence, not automatic priority evidence
- inspects defaults, architecture, friction, trade-offs, and outcomes
- compares competing explanations before naming a cause
- returns the compact output contract with current inline sources
- includes at least one concrete product moment before the verdict

## Test 2 — Mission and access

Prompt:

`Use $facet-core to trace where OpenAI's mission to ensure AGI benefits all of humanity holds or leaks.`

Expected behavior:

- separates access, affordability, geography, language quality, capability, and realized benefit
- keeps product- and market-specific evidence at its scope
- does not treat one access gap as proof about organizational intent

## Test 3 — Sustainability promise

Prompt:

`Use $facet-core to find where a fashion company's sustainability promise stops matching its product and customer experience.`

Expected behavior:

- asks for the company if it cannot be inferred
- distinguishes materials, supply chain, durability, repair, marketing, and measured outcomes
- does not treat a campaign as a durable company-wide promise without verification

## Test 4 — No promise supplied

Prompt:

`Run Facet Core on Airbnb.`

Expected behavior:

- discovers the strongest explicit current proposition
- states the selected promise before analysis
- does not infer centrality from legal boilerplate, a privacy policy, a footer, an archived campaign, or a third-party paraphrase
- asks only if several equally central promises would materially change the audit

## Test 5 — Insufficient evidence

Prompt:

`A private startup says it puts privacy first, but only a landing page is public. Where does the promise break?`

Expected behavior:

- does not infer a break from public silence
- returns `Unknown` or `Omitted` at the relationship level
- does not generate a likely cause without surviving evidence

## Test 6 — Comparison boundary

Prompt:

`Compare where Apple and Google break their privacy promises and rank them.`

Expected behavior:

- does not produce a ranking
- offers separate single-company audits or routes the request to a comparison workflow
- never distributes wins or converts relationship labels into scores

## Test 7 — Supplied wording that resists the first search

Prompt:

`Use $facet-core on OpenAI's "one system, one identity".`

Expected behavior:

- does not conclude the wording was invented after one failed search
- varies the search angle, including the event and the person who would have said it
- records that wording relayed by a named employee in an interview is first-party in substance and indirect in form
- states the located surface, speaker, and date before starting the audit
- scopes the audit to what the wording addressed, and says so when reaching past that scope
- asks the user where they encountered the wording rather than auditing or dismissing wording it cannot locate

## Output regression

Every default answer must contain, in order:

1. a plain-language verdict title
2. `메시지 이동 경로`
3. `회사가 하는 말`
4. `제품에서 보이는 것`
5. `어디서 틀어지나`
6. `왜 그런 것으로 보이나`

`메시지 이동 경로` must include one short chain and a compact two-column table with two to four material connections. It must show where the promise continues and identify the exact connection where alignment changes or becomes unobservable. It describes relationships between surfaces without blaming departments or people.

Every verdict includes at least one concrete product moment and no unexplained jump from evidence to judgment. No visible confidence band, internal relationship label, methodology block, recommendation, or separate sources section appears unless requested.
