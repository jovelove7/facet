# Example - TikTok, safety as a priority claim

An unedited Facet Core answer, kept as a reference for the output contract and the verification rules behind it.

- **Prompt:** `$facet-core 틱톡의 "안심에 진심"이 실제 제품 경험에서도 유지되는지 검증해줘`
- **Run date:** 2026-08-24
- **Scope:** globally announced product features, plus one EU-scoped regulatory assessment. Korean-market messaging is the promise under audit.
- **Sources verified:** 2026-08-24. Three of the four cited sources were re-read at their original URLs. The `support.tiktok.com` recommendation page returned an empty response on re-check; the same claim is supported by TikTok's newsroom explanation of For You ranking (2020-06-18), which states that finishing a longer video carries greater weight.
- **Note:** the EU assessment is preliminary and does not prejudge the outcome of the investigation. Company positions and product behavior change; treat this answer as accurate to its run date, not as a standing claim.

---

## 틱톡 · "안심에 진심"은 청소년 추천 피드의 사용시간 보호에서 약해진다

**메시지 이동 경로**

안전을 핵심 가치로 제시 → 콘텐츠 관리와 청소년 보호 기능으로 이어짐 → **사용시간 안전은 피드 바깥의 장치로만 구현됨** → 피드 자체는 무한 스크롤과 개인화 추천을 유지

| 연결 지점 | 실제 상태 |
|---|---|
| 메시지 → 콘텐츠 관리 | 투자와 선제적 삭제 체계가 실제로 존재한다 |
| 안전 기능 → 청소년 UX | 18세 미만 60분 제한과 16세 미만 야간 알림이 기본 적용된다 |
| 청소년 UX → 실제 보호 | 보호 장치는 피드를 멈추는 방식이고 피드 자체는 그대로다. EU 규제기관은 이 장치들의 효과가 충분하지 않다고 예비 판단했다 |

**회사가 하는 말**

틱톡은 한국에서 "안심에 진심"을 내세우며 '신뢰와 안전'을 핵심 가치로 설명한다. 연간 20억 달러 이상을 투자하고, 2025년 2분기 삭제 콘텐츠의 99% 이상을 신고 전에 발견했으며 90% 이상은 노출 전에 제거했다고 발표했다. 청소년 계정에도 연령별 보호 장치와 패밀리 페어링을 제공한다. [틱톡 2025 미디어데이, 2025년 12월](https://newsroom.tiktok.com/2025mediaday?lang=ko-KR)

**제품에서 보이는 것**

말은 실제 기능으로 이어진다. 18세 미만 계정에는 하루 60분 제한이 기본 적용되고, 16세 미만 이용자가 밤 10시 이후 틱톡을 보면 'For You' 피드가 차분한 음악이 나오는 전체 화면 알림으로 중단된다. 계속 보기를 선택하면 더 넘기기 어려운 두 번째 알림도 표시된다. [틱톡 청소년 보호 기능, 2025년 3월](https://newsroom.tiktok.com/new-ways-we-are-supporting-parents-and-helping-teens-build-balanced-digital-habits?lang=en)

하지만 알림을 지나면 다시 개인화된 영상 흐름으로 돌아간다. 틱톡은 'For You' 피드에서 이용자가 영상을 끝까지 보거나 넘기는 행동 등을 사용해 관심 가능성이 높은 콘텐츠를 계속 추천한다고 설명한다. [틱톡 추천 시스템 설명](https://support.tiktok.com/en/using-tiktok/exploring-videos/how-tiktok-recommends-content)

**어디서 틀어지나**

콘텐츠 유해성을 줄이는 단계에서는 "안심에 진심"이 기능과 운영으로 이어진다. 그러나 안전을 **이용자가 오래 머무르지 않도록 기본 경험 자체를 제한하는 것**까지 포함하면 의미가 달라진다.

틱톡이 공개한 보호 장치는 모두 피드를 바깥에서 멈추는 방식이다. 60분 제한과 야간 알림은 흐름을 끊지만, 무한 스크롤과 자동 재생, 개인화 추천이라는 기본 경험은 그대로 유지된다. 안전이 콘텐츠에는 삭제와 노출 차단으로 들어가 있는 반면, 사용시간에는 피드 구조를 바꾸는 방식으로 들어가 있지 않다.

이 구조의 효과에는 외부 문제 제기가 있다. EU 집행위원회는 2026년 2월 무한 스크롤과 자동 재생, 개인화 추천이 강박적 사용 위험을 만들 수 있고, 틱톡이 이 위험을 미성년자와 취약한 성인에게 미치는 영향까지 충분히 평가하지 않았다고 예비 판단했다. 화면시간 관리 도구는 넘기기 쉬워 마찰이 거의 없고 부모 통제는 부모의 추가 시간과 역량을 요구해, 위험을 실질적으로 줄이지 못하는 것으로 보인다고 밝혔다. 확정 결론이 아니며 EU 서비스에 대한 판단이다. [EU 집행위원회 예비 판단, 2026년 2월 6일](https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act)

**왜 그런 것으로 보이나**

틱톡의 안전은 하나의 방식으로 구현되지 않는다. 콘텐츠 안전은 삭제·차단·추천 제외처럼 피드 안으로 깊게 들어가 있지만, 사용시간 안전은 알림·시간 제한·부모 설정처럼 피드 주변의 보호 장치로 구현돼 있다.

반면 추천 시스템의 중심은 이용자의 시청 행동을 읽어 다음 콘텐츠를 이어주는 데 있다. 틱톡 자신도 영상을 끝까지 본 행동에 더 큰 가중치를 둔다고 설명한다. 그래서 "안전을 기본 설계에 넣는다"는 메시지가 실제 제품에서는 **"추천 경험은 유지하면서 사용자가 멈출 수 있는 장치를 제공한다"**로 좁아진다.

왜 틱톡이 이 경계를 택했는지는 공개 자료로 확인하기 어렵다. 사용시간을 줄이는 설계가 수익 구조와 충돌한다는 설명과, 사용시간 안전이 콘텐츠 안전보다 늦게 시작돼 아직 피드 구조까지 들어가지 못했다는 설명이 모두 관찰된 사실에 들어맞는다. 내부 목표지표나 설계 논의가 공개돼야 둘을 가를 수 있다.
