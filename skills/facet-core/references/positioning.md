# Positioning

Read this only when the promise names who the product is for, what kind of product it is, or how it differs from an alternative. Otherwise skip it.

## Three dimensions

| Dimension | What the wording claims | Surfaces checked in Core |
|---|---|---|
| audience | Who the product is for | First screen, app or store description the company wrote, onboarding |
| category | What kind of product it is | Title, H1, meta description, first screen, core feature behavior |
| differentiation | How it differs from a named or clearly implied alternative | The product surface where the difference would have to show, and the alternative on that same dimension |

Extract only what the wording states. Do not infer an audience or a category the company never named. When the wording is silent on a dimension, that dimension is not audited.

## Category has three layers

| Layer | Question | Where it is judged |
|---|---|---|
| Chosen | What does the company call the product in its title, H1, and meta description? | Core |
| Shown | Do the first screen and the core feature behave like that kind of product? | Core |
| Perceived | How do search results and AI systems classify the company? | A Search or GEO audit, never Core |

A gap between the chosen category and how search or AI systems describe the company is never evidence against a Core verdict. Name it as a separate consideration for a Search or GEO audit.

## Differentiation

- Run only when the company states the difference explicitly. `Unlike a general map, we plan the walk around weather and shade` qualifies. A feature list does not.
- The alternative is a reference surface, not a second subject. Observe what it does on the same dimension and nothing else.
- Pass no verdict on the alternative, and never conclude which product is better. That is a comparison workflow.
- The finding is limited to four outcomes: the claimed difference exists, exists only in part, does not exist, or cannot be established from public evidence.
- If the company claims no difference, do not construct one.

## The positioning dimension in a diagnosis

Positioning is not a failure category. It is an optional tag recording which positioning dimension a break affected. The category still says where and how the promise failed.

```yaml
diagnosis:
  category: product               # where the promise failed
  positioning_dimension: audience # which positioning dimension it affected
```

- The tag can sit on any category: messaging, product, ux, policy, operations, measurement, connection.
- Add it only when a break survives. A promise that held has no diagnosis, so the audited dimensions stay in the claim record and never appear as a tag.
- Values are `audience`, `category`, and `differentiation`. Add a value only after real audits need it.

| Situation | category | positioning_dimension |
|---|---|---|
| The copy calls a different user than the product serves | messaging | audience |
| The default experience does not fit the user the copy names | product | audience |
| The feature is right, but people cannot tell what kind of product it is | ux | category |
| The claimed difference is not built into the product | product | differentiation |
| Each surface holds, and the category shifts between them | connection | category |

## The reader-facing sentence

The diagnosis sentence keeps its rules: one declarative sentence, twenty words or fewer, no conditional clause. Name the failing category, and describe the affected dimension in plain words. The word "positioning" may qualify the category; it never replaces it.

- messaging + audience: `진단: 제품이 아니라, 첫 화면이 다른 사용자를 부르는 메시지 문제다.`
- product + audience: `진단: 문구가 아니라, 제품 경험이 주장한 사용자에게 맞지 않는 제품 문제다.`
- messaging + category: `진단: 기능은 맞지만, 첫 화면이 제품을 다른 종류로 소개하는 메시지 문제다.`
- product + differentiation: `Diagnosis: the claimed difference is not built into the product, which makes this a product problem.`
