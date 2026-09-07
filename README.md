# Facet

**Start with a company, exact wording, material, or only a symptom. Facet finds the published promise that governs the question and verifies whether it holds, or exactly where it stops.**

> Simple and intuitive on the front. Obsessive about verification underneath.

Facet is a verification-first Agent Skill. Its first public skill, **Facet Core**, audits one company at a time and returns a plain-language verdict backed by current evidence.

**회사명, 문구, 자료 또는 증상으로 시작하면 회사가 실제로 내건 약속을 먼저 찾습니다. 그 약속이 제품 경험에서 지켜지는지, 아니라면 정확히 어디서 끊어지는지 검증합니다.**

## See what Facet finds in 20 seconds

### TikTok · a verified break

> **Product problem in the recommendation feed's defaults: Trust & Safety and Recommendation stop meeting there.**

**English**

```text
"Serious about Safety"
        ↓ holds
content removal · screen-time limits · Family Pairing
        ↓ breaks here
how the recommendation feed chooses and continues the next video
        ↓
infinite scroll · autoplay · personalized recommendation
```

**한국어**

```text
"안심에 진심"
        ↓ 유지됨
콘텐츠 삭제 · 사용 시간 제한 · 패밀리 페어링
        ↓ 여기서 끊김
추천 피드가 다음 영상을 선택하고 계속 이어가는 방식
        ↓
무한 스크롤 · 자동 재생 · 개인화 추천
```

**Why it may be this way**

Hard to discover + setup burden + easy-to-dismiss controls. The safety features can pause viewing or ask people to manage limits, while the recommendation feed continues choosing the next video from viewing behavior. Public evidence does not show how strongly wellbeing measures constrain that decision.

[Read the complete TikTok audit in English](examples/tiktok-safety-priority.en.md) · [한국어 전체 감사 보기](examples/tiktok-safety-priority.md)

## Start with what you have

You do not need to know the message.

| What you have | Example | What Facet does first |
|---|---|---|
| A company name | `$facet-core Toss`<br>`$facet-core 토스` | Finds the most central current proposition, names it, then audits it |
| Exact wording | `$facet-core Check whether OpenAI's "one system, one identity" holds in the product experience`<br>`$facet-core OpenAI의 "one system, one identity"가 제품 경험에서도 유지되는지 봐줘` | Establishes what the wording governed before testing it |
| A page, ad, deck, or screen | `$facet-core Check whether this landing page creates the same expectation as the product`<br>`$facet-core 이 랜딩페이지가 실제 제품과 같은 기대를 만드는지 봐줘` | Extracts the material's claim and compares it with the relevant experience |
| Only a symptom | `$facet-core Customers say they cannot tell what makes us different. Find where the problem is`<br>`$facet-core 고객들이 우리 차이를 모르겠다고 하는데 어디가 문제인지 봐줘` | Uses the symptom to find the company's own wording, discloses the selection, then audits it |

A symptom starts the search; it never becomes the claim under audit. Facet does not promote the user's summary into the company's promise. When no governing published wording can be established from the reviewed evidence, that absence is reported without claiming the company never made such a promise.

If several propositions are equally central and the choice would materially change the result, Facet asks which one to trace. If material evidence is inaccessible, it requests at most two items in two lines or fewer.

## [What's new in v0.6.1](https://github.com/jovelove7/facet/releases/latest)

- **A break begins with a diagnosis.** Facet names the kind of problem, its location in the product, and the public-facing functions that stop meeting.
- **A promise that holds is a result.** The audit no longer invents a failure when the evidence supports the stated objective.
- **Scope comes before judgment.** A design brief is judged against design; a launch claim is judged against that launch. Adjacent issues cannot lower an unrelated verdict.
- **You can start with a symptom.** Facet first locates and discloses the company's actual published wording.
- **A divided structure is not automatically a divided experience.** Facet checks the route a user can actually take before calling the split a break.
- **Safety and priority claims receive stronger checks.** Discoverability, setup burden, default strength, dismissal cost, reversibility, coverage, and measured outcomes are tested separately.
- **Competing hypotheses now point in two directions.** Every verified break is tested against both a constraint explanation and a deliberate-choice explanation.

## What Facet Core returns

Every default answer follows one fixed reader-facing order:

1. a plain-language verdict;
2. `Where the message travels` - the path from promise to observed reality;
3. `What the company says` - the current proposition and its scope;
4. `What the product shows` - concrete product or service moments;
5. `Where it changes` - the diagnosis, or a direct statement that the promise held;
6. `Why it may be this way` - the evidence behind a held result, the best-surviving explanation for a break, or an explicit unknown.

Facet answers in the language used in the request. The order never changes; the labels are localized. In Korean, the same sections read `메시지 이동 경로`, `회사가 하는 말`, `제품에서 보이는 것`, `어디서 틀어지나`, and `왜 그런 것으로 보이나`.

The visible answer stays compact. Underneath, Facet verifies claim scope, evidence directness, relationships across surfaces, competing hypotheses, and falsification conditions.

Ask for more only when you need it: the evidence chain, competing explanations, unknowns, or what evidence would change the verdict.

## Questions Facet can investigate

- **Product marketing** - Does this launch claim describe the product people will actually encounter?
- **Brand and messaging** - Is the story getting lost between touchpoints, or does the experience genuinely differ?
- **Audience and positioning** - Which parts of our claimed difference have current evidence behind them?
- **Product and UX** - Is this a messaging problem, a product-behavior problem, a usability problem, or no break inside the promise's scope?
- **User research** - Which competing explanation should interviews test first?
- **Trust and safety** - Does the protection exist only as a feature, or does it shape the default experience and measured outcome?

## Boundaries

Facet reports what the evidence supports. It does not rank companies, recommend vendors, prescribe a fix, or infer how internal teams and individuals relate.

When asked whether a line can be used in advertising, Facet converts the request into an evidence audit. It reports:

- what the product confirms;
- what holds only under a condition;
- what has no public evidence;
- what describes something other than the observed experience.

It does not approve the line, rewrite it, or determine legal defensibility.

## Verification principles

- Judge a promise only against the surface it actually governs.
- A promise that holds is a result; never manufacture a break.
- Treat a capability as evidence of capability, not automatic proof of priority, effectiveness, or outcome.
- Observe brand, marketing, product, UX, policy, support, outcomes, and independent evidence separately before judging the whole.
- Compare the same claim dimensions and keep product, market, audience, geography, and time scope attached to the evidence.
- Treat missing evidence as uncertainty or omission, not contradiction.
- Generate a constraint hypothesis and a choice hypothesis, then attack both.
- Check the user's actual route before treating a divided structure as a divided experience.
- Name where a problem sits, never what to build.
- Use the company's public wording for its functions and make no claim about its teams or people.
- Let evidence strength control the verb instead of displaying a confidence badge.
- Hide internal calculations, not the reasoning bridge the reader needs.

## Worked examples

The repository includes unedited answers with their sources, run dates, and audit scope.

- **OpenAI · a promise that held** - The "one system, one identity" design brief achieved the visual integration it governed. Product continuity is a separate consideration, not evidence that the rebrand failed. [English](examples/openai-one-system-one-identity.en.md) · [한국어](examples/openai-one-system-one-identity.md)
- **TikTok · a verified break** - "Serious about Safety" reaches real safety features, then stops where those features would have to change how the recommendation feed behaves. [English](examples/tiktok-safety-priority.en.md) · [한국어](examples/tiktok-safety-priority.md)
- **Toss · a split that was not a break** - Facet selected and disclosed the proposition itself. Separate support routes turned out to be organized by the user's task, with a catch-all route still available. [English](examples/toss-all-in-one.en.md) · [한국어](examples/toss-all-in-one.md)

The examples land on different results on purpose: a promise that held, a material break, and a structure that looked divided but did not divide the experience.

## Install

### From a release

Download the latest package from [Releases](https://github.com/jovelove7/facet/releases/latest), then unpack it into your personal skills directory.

```bash
unzip facet-core-v0.6.1.zip -d ~/.codex/skills/
```

Every release publishes a SHA-256 checksum next to the package.

### From the repository

```bash
git clone https://github.com/jovelove7/facet.git
cp -R facet/skills/facet-core ~/.codex/skills/facet-core
```

Restart Codex if the skill does not appear immediately.

### Other Agent Skills clients

Use the `skills/facet-core` directory as the skill package. `SKILL.md` is the entry point; files in `references/` are loaded only when needed.

## Repository layout

```text
facet/
├── skills/facet-core/
│   ├── SKILL.md                        # rules and workflow
│   ├── agents/openai.yaml
│   └── references/
│       ├── entry-points.md             # company, wording, material, symptom
│       ├── evidence-protocol.md        # source order and scope
│       ├── relationship-rubric.md      # preserved, compressed, divergent, unknown
│       ├── capability-to-protection.md # safety and priority checks
│       ├── hypothesis-protocol.md      # constraint and choice hypotheses
│       ├── diagnosis.md                # problem categories and held verdicts
│       └── output-contract.md          # fixed order and localized labels
├── examples/                           # unedited, sourced audit results
├── tests/                              # regression prompts and invariants
├── scripts/check_skill.py              # structural and output-contract checks
├── CONTRIBUTING.md
└── LICENSE
```

## Validate

```bash
python3 scripts/check_skill.py
```

The regression suite is conclusion-agnostic. It checks the method and output contract instead of freezing a historical answer.

## Corrections

Examples are accurate to their run date, not standing claims. Found an error or newer evidence? Open an issue with a dated source.

## License

[MIT](LICENSE)
