# Output Contract

## Front-end principle

Keep the front end simple and intuitive while the back end remains exhaustive.

> Hide the calculation, not the reasoning bridge.

The reader must be able to see, without knowing the rubric:

1. where the message travels and where alignment changes;
2. what the company says;
3. what the product actually does;
4. how the meaning changes;
5. why that change may exist.

Do not compress these five steps into an unexplained verdict.

## Default output

Use this exact order:

```markdown
## <COMPANY> · “<PROMISE IN PLAIN LANGUAGE>”는 <CONCRETE LOCATION OR EXPERIENCE>에서 <지켜진다/흐려진다/틀어진다/판단하기 어렵다>

**메시지 이동 경로**
<MARKETING OR BRAND PROMISE> → <PRODUCT CAPABILITY> → **<EXACT CONNECTION WHERE ALIGNMENT CHANGES>** → <OBSERVED OUTCOME OR INDEPENDENT EVIDENCE>

| 연결 지점 | 실제 상태 |
|---|---|
| <SURFACE A> → <SURFACE B> | <WHAT CONTINUES OR CHANGES IN PLAIN LANGUAGE> |
| <SURFACE B> → <SURFACE C> | <WHAT CONTINUES OR CHANGES IN PLAIN LANGUAGE> |
| <SURFACE C> → <OUTCOME OR EVIDENCE> | <WHAT IS OBSERVED, DISPUTED, OR UNKNOWN> |

**회사가 하는 말**
<The current first-party promise in one plain sentence with an inline source.>

**제품에서 보이는 것**
<One or two concrete product moments the reader can picture. Explain what is default, separated, required, recommended, or experienced. Include inline sources.>

**어디서 틀어지나**
<Explain in ordinary language how the promise becomes a materially different product reality. If it holds, explain what stays consistent.>

**왜 그런 것으로 보이나**
<State the best-surviving causal hypothesis in plain language, or Unknown. Include the observable business or product mechanism that supports it.>
```

Do not add a preamble, methodology, confidence label, recommendation, action plan, source appendix, or generic company summary by default.

## 메시지 이동 경로

Make this a mandatory orientation block, not a second analysis. Use one short chain followed by a compact two-column table.

Normally trace only the material surfaces:

`Marketing or Brand → Product capability → Default UX or journey → Observed outcome or independent evidence`

Adapt the surface names when another route is more truthful, such as `Policy → Support → Resolution` or `Sales → Service delivery → Customer outcome`. Do not force an irrelevant surface into the chain.

The block must:

- show where the promise continues before showing where it changes;
- bold the exact connection or surface where alignment first materially weakens, breaks, or becomes unobservable;
- use plain descriptions such as `기능으로 이어짐`, `기본 UX에서 약해짐`, or `실제 효과는 확인되지 않음`;
- describe relationships between surfaces, not blame a marketing, product, UX, or leadership team;
- use `확인하기 어려움` when evidence cannot resolve a connection;
- keep the table to two to four material rows.

Do not print internal labels such as `Reinforced`, `Divergent`, `Deep`, or `Unknown` in this block. Translate them into ordinary language.

Example:

```markdown
**메시지 이동 경로**
마케팅의 약속 → 제품 기능으로 이어짐 → **기본 UX에서 약해짐** → 실제 보호 효과에 외부 문제 제기

| 연결 지점 | 실제 상태 |
|---|---|
| 마케팅 → 제품 | 약속한 보호 기능이 실제로 존재한다 |
| 제품 → 기본 UX | 강한 보호는 사용자가 직접 찾아 설정해야 한다 |
| 기본 UX → 실제 효과 | 현재 보호 장치의 효과가 충분하지 않다는 예비 판단이 있다 |
```

## Verdict title

Write the verdict as a sentence a non-specialist can understand. Do not print internal status labels such as `THE PROMISE BREAKS DEEP`, `Divergent`, or `Promise ↔ Core Product Architecture`.

Use natural forms such as:

- `<Company> · “안전이 최우선”이라는 말은 추천 피드에서 틀어진다`
- `<Company> · “누구나 접근 가능하다”는 약속은 지원 국가에서 좁아진다`
- `<Company> · “사용자가 통제한다”는 약속은 설정 경험에서도 대체로 지켜진다`
- `<Company> · 공개 자료만으로는 “개인정보 우선” 약속을 판단하기 어렵다`

Depth remains an internal classification. The title names the concrete location instead.

## 회사가 하는 말

Preserve the company's intended meaning and cite the current first-party surface where it deliberately presents the proposition. Translate when helpful, but do not silently strengthen the wording.

## 제품에서 보이는 것

This is the mandatory evidence-to-judgment bridge. Include at least one concrete moment, control, default, screen, flow, ranking behavior, product boundary, or measured outcome.

Prefer:

`친구 글만 보는 기능은 별도 Friends 탭에 있고, 기본 피드는 추천 콘텐츠를 함께 보여준다.`

Avoid:

`관계 중심 가치가 핵심 제품 아키텍처에서 지배적 제약조건으로 작동하지 않는다.`

Use technical terms only when no ordinary equivalent exists, and explain them immediately.

## 어디서 틀어지나

State the semantic change as a simple contrast:

`“사람과 연결한다”가 제품에서는 “계속 볼 콘텐츠를 찾아준다”로 바뀐다.`

Do not merely repeat the observation. Explain why the difference materially changes the expectation created by the promise.

If no material leak survives verification, explain what remains consistent. If evidence is insufficient, say which product behavior cannot be observed.

## 왜 그런 것으로 보이나

Translate the best-surviving hypothesis into plain language. Connect it to an observable mechanism without claiming hidden intent.

- Supported indirect cause: `광고 노출이 사용시간과 연결돼 있어, 추천 시스템이 직접적인 관계보다 시청을 먼저 최적화하는 것으로 보인다.`
- Multiple survivors: `사용자 행동 변화와 광고 구조가 모두 설명에 들어맞는다. 내부 목표지표가 공개돼야 둘을 가를 수 있다.`
- Unknown: `공개 자료는 차이가 생기는 지점은 보여주지만 원인까지 가르지는 못한다.`

## Expanded output on request

Reveal only the requested layer:

- **Evidence chain:** claim, source, date, scope, observation
- **Surface graph:** verified edges and relationship labels
- **Competing hypotheses:** support, contradiction, and survivor status
- **Unknowns:** material gaps without absence claims
- **Falsification:** evidence that would change the result

Keep the reader-facing verdict and message movement path first even when expanding.
