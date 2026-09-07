# Facet Core v0.6.1 Regression Cases

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

## Test 8 — Answer language

Prompts:

`Use $facet-core to trace where Patagonia's repair promise stops matching the buying experience.`

`$facet-core 파타고니아의 수선 약속이 구매 경험에서 어디서 틀어지는지 추적해줘.`

Expected behavior:

- answers each prompt in the language it was written in
- uses the localized label set for that language and no other
- keeps the same five steps in the same order in both answers
- localizes the table headers with the labels
- does not append an English label to a translated one, and does not mix languages inside one answer
- keeps quoted company wording in its original language, marking any translation as a translation

## Test 9 — Diagnosis

Prompt:

`Use $facet-core to test TikTok's claim that safety is its top priority.`

Expected behavior:

- `어디서 틀어지나` opens with a diagnosis, not with description
- the diagnosis is one declarative sentence with no conditional clause, and no `~것으로 보인다`, `may`, or `appears`
- exactly one category is chosen from the list in `references/diagnosis.md`
- three noun-phrase lines follow: main problem location, where the connection breaks, and a second problem only if the evidence exposed one
- `Connection` is chosen only when both areas are shown to work on their own
- the answer names where the problem sits and never says what to build

## Test 10 — Naming and unsupported numbers

Prompt:

`$facet-core 틱톡의 부모 통제 기능이 실제 보호로 이어지는지 검증해줘.`

Expected behavior:

- names functions using the company's own public wording, such as `신뢰와 안전 ↔ 추천 시스템`
- makes no claim about how teams coordinate, who decided something, or any individual
- states that what public evidence establishes is two functions moving separately in the finished product
- gives an adoption or awareness figure only with a source and an owner, such as `2024년 2월 영국 청소년 월간 이용자의 4~5%, Ofcom`
- when the company's own figure is not public, may carry a published figure for the same kind of feature while saying whose figure it is
- never converts an absent figure into `이용률이 낮다`

## Test 11 — A promise that holds

Prompt:

`$facet-core 오픈에이아이의 "one system, one identity"를 검증해줘.`

Expected behavior:

- judges the wording only against the surface it governed, which here is the visual identity system
- reports `지켜짐` as a result, with the same force used for a break
- does not import product naming, entry points, or model names as evidence that this promise failed
- names an out-of-scope observation under `별도 고려사항`, with the wording that would govern it, and passes no verdict on it
- carries the `주의` line naming the observation that must not be read as failure
- explains why the promise held instead of building a hypothesis about a failure that did not occur
- uses `판정:` rather than a problem category for the held branch
- keeps adjacent observations out of the message path and evidence table

## Test 12 — Company name only

Prompt:

`$facet-core 토스`

Expected behavior:

- finds the strongest current first-party proposition and states the selected wording before analysis
- when two are equally central, names both, says which one it is taking, and continues
- asks only when the choice would decide the answer

## Test 13 — Material as the entry

Prompt:

`$facet-core 이 광고 문구와 제품 화면이 같은 기대를 만드는지 검증해줘.`

Expected behavior:

- asks for at most two items, in two lines or fewer, and does not open with a questionnaire
- says whether it is auditing this material's claim or the company's durable promise
- treats material the user received, rather than the company published, as evidence of what one audience was told

## Test 14 — Symptom as the entry

Prompt:

`$facet-core 우리 회사는 기능이 많은데 고객이 차이를 모르겠다고 해.`

Expected behavior:

- does not audit the user's phrasing as if it were the company's promise
- asks for the company or site, then finds first-party wording and states it before auditing
- bounds the search by the surface the symptom points at
- when no wording in the reviewed materials governs the symptom, says so and stops, and reports that no governing promise could be established rather than that none exists
- discloses the selected wording and why it was selected before the audit begins

## Test 15 — A divided structure

Prompt:

`$facet-core 토스의 "금융부터 일상까지, 마침내 토스 하나로"를 검증해줘.`

Expected behavior:

- generates one constraint hypothesis and one choice hypothesis, not two that both attribute the pattern to external constraints
- checks whether the divided parts are named by the company's internal divisions or by the user's task, and whether a catch-all route exists
- does not treat a count of separate touchpoints as evidence that the experience is divided
- leaves the unmeasured resolution experience as a separate consideration rather than a second verdict

## Test 16 — A request for permission

Prompt:

`$facet-core 이 출시 문구를 그대로 광고에 써도 될까?`

Expected behavior:

- does not refuse the request, and does not answer it as asked
- restates the work as verifying how far the evidence supports each claim, and says the advertising decision is not judged
- separates claims confirmed in the product, claims that hold only under a condition, claims with no public evidence, and wording that describes something other than the experience
- never outputs an approval, replacement wording, a campaign decision, or a statement that something is legally safe
- when asked whether a claim is legally defensible, says that is out of scope and continues with the evidence audit

## Output regression

Every default answer must contain, in order:

1. a plain-language verdict title
2. `메시지 이동 경로`
3. `회사가 하는 말`
4. `제품에서 보이는 것`
5. `어디서 틀어지나`
6. `왜 그런 것으로 보이나`

The English label set carries the same five steps in the same order:

1. a plain-language verdict title
2. `Where the message travels`
3. `What the company says`
4. `What the product shows`
5. `Where it changes`
6. `Why it may be this way`

The message movement path must include one short chain and a compact two-column table with two to four material connections. It must show where the promise continues and identify either the achieved result or the exact connection where alignment changes or becomes unobservable. It describes relationships between surfaces without blaming departments or people. An adjacent observation never appears in the path or table for a held promise.

When a break survives, `어디서 틀어지나` opens with `진단:` and its three noun-phrase lines; the English form opens with `Diagnosis:`. When nothing breaks inside the audited scope, it opens with `판정:` / `Verdict:` and carries `달성한 것`, `약속 범위 내 판정`, and—only when useful—the paired `별도 고려사항` and `주의`. `왜 그런 것으로 보이나` carries two to four checks for a break or two to three evidence checks for a held result, then closes with one quoted sentence stating the surviving explanation or verified achievement.

Every verdict includes at least one concrete product moment and no unexplained jump from evidence to judgment. No visible confidence band, internal relationship label, methodology block, prescription, or separate sources section appears unless requested. Naming where a problem sits is allowed; telling the company what to build is not.
