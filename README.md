# Facet

Facet is a verification-first Agent Skill for tracing where a company's message changes between what it says and what people actually encounter.

> Simple and intuitive on the front. Obsessive about verification underneath.

The first public skill is **Facet Core**. It audits one company at a time and finds the exact connection where a core promise is preserved, weakened, contradicted, or no longer verifiable.

한국어로는 이렇게 설명할 수 있습니다: **회사가 하는 말이 실제 제품 경험으로 이동하면서 어디서, 어떻게 달라지는지 검증하는 스킬**입니다.

## What Facet Core returns

Every default answer follows one fixed reader-facing order:

1. a one-sentence verdict;
2. `메시지 이동 경로` — the path from promise to observed reality;
3. `회사가 하는 말` — the company's current proposition;
4. `제품에서 보이는 것` — concrete product or service moments;
5. `어디서 틀어지나` — the exact change in meaning;
6. `왜 그런 것으로 보이나` — the best-surviving explanation, or an explicit unknown.

The visible answer stays compact. Behind it, the skill verifies claim scope, evidence directness, surface relationships, competing hypotheses, and falsification conditions.

## Where to use it

Any work that starts with desk research.

- **Product marketing** - Keep expectations and market intelligence current and validated. Check whether a competitor's strength is product-backed or messaging-heavy, and pressure-test launch language against the experience it describes.
- **Brand and messaging** - Maintain narrative coherence across product pillars. Find where a story goes quiet between touchpoints, and tell a messaging problem apart from a real experience gap.
- **Audience and positioning** - Attach a dated source to every claim, so launch, sales, and campaigns share the same evidence.
- **User research** - Compress the desk research before primary research, so interviews start by testing which competing explanation best fits actual behaviour, rather than from scratch.

## Install

### Codex

Clone this repository, then copy the skill into your personal skills directory:

```bash
git clone https://github.com/jovelove7/facet.git
cp -R facet/skills/facet-core ~/.codex/skills/facet-core
```

Restart Codex if the skill does not appear immediately.

### Other Agent Skills clients

Use the `skills/facet-core` directory as the skill package. `SKILL.md` is the entry point and the files in `references/` are loaded only when needed.

To make an uploadable ZIP:

```bash
cd skills
zip -r facet-core.zip facet-core
```

## Use

Invoke the skill explicitly:

```text
$facet-core 메타의 메시지가 실제 제품 경험에서 어디서 틀어지는지 분석해줘
```

You can also name a specific promise:

```text
$facet-core OpenAI의 "one system, one identity"가 제품 경험에서도 유지되는지 검증해줘
```

If no promise is supplied, Facet Core identifies the strongest current first-party proposition before starting the audit.

## Verification principles

- Observe brand, marketing, product, UX, policy, outcomes, and independent evidence separately before judging the whole.
- Treat a feature as evidence of capability, not automatic proof of priority or outcome.
- Compare the same claim dimensions across surfaces.
- Keep product, market, audience, geography, and time scope attached to the evidence.
- Preserve uncertainty when public evidence cannot support a relationship or cause.
- Attack competing explanations before presenting a likely cause.
- Let evidence strength control the verb instead of displaying a confidence badge.
- Hide internal calculations, not the reasoning bridge the reader needs.

## Example

[TikTok, safety as a priority claim](examples/tiktok-safety-priority.md) is an unedited answer with its sources, run date, and scope attached. It shows the default output contract, and it shows what the skill does when a promise holds on one surface and stops holding on another.

## Repository layout

```text
facet/
├── skills/facet-core/          # installable Agent Skill
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── examples/                   # unedited answers with sources and run dates
├── tests/                      # regression prompts and output invariants
├── scripts/check_skill.py      # structural and output-contract checks
├── CONTRIBUTING.md
└── LICENSE
```

## Validate

```bash
python3 scripts/check_skill.py
```

The regression suite is intentionally conclusion-agnostic. It checks the method and output contract rather than freezing a historical answer.

## Scope

Facet Core is for a **single-company message-integrity audit**. It does not rank companies or recommend vendors. Those tasks belong in a separate comparison workflow.

## License

[MIT](LICENSE)
