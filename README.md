# Facet

[![Release](https://img.shields.io/github/v/release/jovelove7/facet)](https://github.com/jovelove7/facet/releases/latest)
[![Validate](https://github.com/jovelove7/facet/actions/workflows/validate.yml/badge.svg)](https://github.com/jovelove7/facet/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[English](README.md) | [한국어](README.ko.md)

**Facet verifies whether a brand's promise holds in the customer experience. When it does not, it shows where the break begins.**

Facet is a verification-first Agent Skill. Facet compares what a brand says with what customers actually experience. It traces the message across marketing, product, default UX, and observed outcomes, then returns a source-backed verdict.

Works with Claude Code, Codex, and any Agent Skills client.

## "Is this a copy problem, or a product problem?"

- Customers keep saying they cannot tell what makes you different.
- The ad copy reads well, and you are not sure the product carries it.
- The feature shipped, and users still do not feel it.
- A competitor claims a strength and you want to know whether it is real.
- Something is off across brand, marketing, product, and UX, and you cannot tell where it started.
- Interviews are coming up and you need to know what to ask first.

Facet checks whether what a company says still holds by the time it reaches the product. When it does not, Facet finds where it first changes - marketing, product, or UX. When nothing is wrong, it says the promise held instead of inventing a flaw.

## Start with whatever you have

A company name is enough.

```text
$facet-core Toss
```

A page or an ad works too.

```text
$facet-core Check whether this landing page creates the same expectation as the product
```

So does a vague symptom.

```text
$facet-core Customers say they cannot tell what makes us different. Find where the problem is
```

Facet locates the company's own published wording first, states which promise it is auditing, and then shows the result.

## See what Facet finds in 20 seconds

### TikTok · a verified break

> **Product problem in the recommendation feed's defaults: Trust & Safety and Recommendation stop meeting there.**

TikTok's safety message reached real protective features. The break came after that, at the point where Trust & Safety meets the recommendation product. The safety features existed, but they did not extend to constraining how the recommendation feed behaves by default.

```text
"Serious about Safety"
        ↓ holds
content removal · screen-time limits · Family Pairing
        ↓ breaks here
how the recommendation feed chooses and continues the next video
        ↓
infinite scroll · autoplay · personalized recommendation
```

**Why it may be this way**

Hard to discover + setup burden + easy-to-dismiss controls. The safety features can pause viewing or ask people to manage limits, while the recommendation feed continues choosing the next video from viewing behavior. Public evidence does not show how strongly wellbeing measures constrain that decision.

[Read the complete TikTok audit in English](examples/tiktok-safety-priority.en.md) · [한국어 전체 감사 보기](examples/tiktok-safety-priority.md)

### A sample of the returned answer

This is how the same audit arrives, in the fixed output order.

> **Diagnosis: this is a product problem, not a messaging problem.**

- **Main problem location:** the recommendation feed's defaults and its screen-time controls
- **Where the connection breaks:** Trust & Safety ↔ Recommendation
- **Also visible:** feature launches and removal counts ↔ measurement of actual protection

**Where the message travels**

| Connection | What is actually there |
|---|---|
| Message → safety features | Content removal, teen defaults, and Family Pairing genuinely exist |
| Safety features → actual use | Stronger protection requires a parent to know about it, link an account, and set it up |
| Default UX → actual protection | The prompt can be passed, and the same recommendation feed resumes after it |

**What the product shows**

Accounts under 18 have a 60-minute daily limit by default. When someone under 16 opens TikTok after 10pm, the For You feed is interrupted by a full-screen prompt. Raising the level of protection requires a parent to link accounts and adjust the settings themselves. In February 2024, accounts with Family Pairing active came to 4-5% of TikTok's UK teen monthly users. [TikTok teen protections](https://newsroom.tiktok.com/new-ways-we-are-supporting-parents-and-helping-teens-build-balanced-digital-habits?lang=en) · [Ofcom](https://www.ofcom.org.uk/online-safety/protecting-children/how-tiktok-snap-twitch-protect-children-from-harmful-videos)

**Why it may be this way**

**Known but rarely switched on.** Family Pairing was active on 4-5% of UK teen accounts as of February 2024.

**Setup burden.** Stronger protection requires a parent to create an account, link it to the teen's, and set the limits by hand.

**A default prompt that is easy to pass.** At the limit, entering a passcode the user set themselves returns them to the feed, and the limit itself can be switched off.

> **TikTok built safety as protective features that users and parents operate around the feed, rather than as a rule that constrains the feed itself.**

Every claim above carries its source in the full audit, with the run date and the scope it was verified against.

## Install

Facet Core is a standard Agent Skill directory. Copy it into your client's personal skills folder.

### Claude Code

```bash
git clone https://github.com/jovelove7/facet.git
cp -R facet/skills/facet-core ~/.claude/skills/facet-core
```

The skill is available as `facet-core`. Restart Claude Code if it does not appear immediately.

### Codex

```bash
git clone https://github.com/jovelove7/facet.git
cp -R facet/skills/facet-core ~/.codex/skills/facet-core
```

Restart Codex if the skill does not appear immediately, then call it as `$facet-core`.

### From a release

Download the latest package from [Releases](https://github.com/jovelove7/facet/releases/latest), then unpack it into your client's skills directory.

```bash
unzip facet-core-v0.6.1.zip -d ~/.claude/skills/   # or ~/.codex/skills/
```

Every release publishes a SHA-256 checksum next to the package.

### Other Agent Skills clients

Use the `skills/facet-core` directory as the skill package. `SKILL.md` is the entry point; files in `references/` are loaded only when needed.

## What Facet is for

A company knows how it describes itself. It rarely knows how it is actually understood - by its customers, through its product, in search results, or by the AI systems now answering questions about it.

```text
what the company believes it is
    -> what the company says
    -> what the product makes people experience
    -> how search and AI classify it
    -> what the market remembers
```

One question runs the length of that chain: is the positioning we intended the one that actually arrives?

**Today, Facet Core verifies the first half.** It checks whether a company's stated message survives contact with its own product experience, and shows with evidence where the meaning holds and where it changes.

**Where it is going.** The same method applied further along the chain: whether a competitor's claimed strength holds when audited on its own terms, how search results classify a company, and how AI systems describe and recommend it. None of that ships yet. Facet Core is the message-to-product segment, and the rest is the direction, not the current feature set.

## Before you launch what you just built

**You tested whether it works. Now test whether what it says is true.**

The moment right after a product is built fast is when the gap opens, because the copy and the product were generated separately and nothing compared them:

- The hero copy claims more than the feature does.
- The positioning you started with is not the product you finished with.
- Features, pricing, and terms of service each promise something different.
- The numbers and testimonials added for credibility have nothing behind them.
- The value the user came for disappears after onboarding or payment.
- Every page describes the same product differently.

Point Facet at your own site before launch.

```text
$facet-core I built this. Check whether the hero copy is true of the actual product
https://example.com
```

```text
$facet-core Check whether the homepage, the working features, the pricing, and the terms of service all say the same thing
```

You do not have to name the promise yourself. Facet finds the most central wording on the page, tells you which one it is auditing, and then traces it through onboarding, the core feature, the output, pricing, and terms.

Facet does not rewrite the copy. It establishes how much of the current copy is true, which is the thing you need before rewriting any of it.

**This use needs a client that can actually reach your site.** Facet reasons over evidence it can open. Without web access it can only work from what you paste into the conversation.

## What Facet does with each kind of input

| Start with | Example | What Facet does first |
|---|---|---|
| A company name | `$facet-core Toss` | Finds the most central current message and explains why it was selected |
| Exact wording | `$facet-core Check whether OpenAI's "one system, one identity" holds in the product experience` | Defines what the wording promises, then checks it against the relevant experience |
| A page, ad, deck, or screen | `$facet-core Check whether this landing page creates the same expectation as the product` | Extracts the core claim and compares it with the product experience |
| A problem symptom | `$facet-core Customers say they cannot tell what makes us different. Find where the problem is` | Uses the symptom to find the company's own published message before auditing it |

A symptom starts the search. It never becomes the company's promise. When no governing published wording can be established from the reviewed evidence, that absence is reported without claiming the company never made such a promise.

If several propositions are equally central and the choice would materially change the result, Facet asks which one to trace. If material evidence is inaccessible, it requests at most two items in two lines or fewer.

## How Facet verifies

| Step | What happens |
|---|---|
| 1. Establish the promise | Confirms the company's published wording and the scope it actually governs |
| 2. Trace the experience | Follows the message through marketing, product, default UX, and observed outcome |
| 3. Test the evidence | Determines whether the promise holds, breaks, or cannot yet be established |

## Questions Facet can answer

| Use case | Question |
|---|---|
| Launch claim | How far does the actual product experience support this claim? |
| Positioning | Can customers see the difference the company says it offers? |
| Product experience | Does the mismatch begin in messaging, product, or UX? |
| Customer complaints | Which published promise does a recurring complaint conflict with? |
| Trust and safety | Does the feature shape the default experience and the actual outcome? |
| Sales promise | Does the promise survive implementation and operation? |

## What you can take forward

| Output | What it tells you |
|---|---|
| A one-line verdict | Whether the promise holds, and where it stops if it does not |
| The point of failure | The product behavior or customer touchpoint where the mismatch first appears |
| What remains unknown | What cannot be established from the available evidence |
| The next verification question | What to investigate in interviews or internal data |
| Evidence that would change the verdict | What could disprove or strengthen the current hypothesis |

Facet does not prescribe a fix or approve a claim for use. It makes clear what the evidence supports and what should be checked next.

![How Facet works](assets/facet-use-map-en.png)

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
├── README.ko.md                        # Korean version of the front half
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
