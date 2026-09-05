# Example - TikTok, safety as a priority claim

An unedited Facet Core answer, kept as a reference for the output contract and the verification rules behind it.

The same audit in English: [tiktok-safety-priority.en.md](tiktok-safety-priority.en.md).

- **Prompt:** `$facet-core 틱톡의 "안심에 진심"이 실제 제품 경험에서도 유지되는지 검증해줘`
- **Run date:** 2026-08-24
- **Scope:** globally announced product features, one UK figure, and one EU-scoped regulatory assessment. TikTok's Korean-market messaging is the promise under audit.
- **Sources verified:** 2026-08-24, read directly except where noted. The Ofcom figure is carried from search coverage of Ofcom's report; ofcom.org.uk blocks automated reading, so the primary page was not opened.
- **Note:** the EU assessment is preliminary and does not prejudge the outcome of the investigation. Treat this answer as accurate to its run date, not as a standing claim.

---

## 틱톡 · "안심에 진심"은 안전 기능이 실제 보호로 넘어가는 프로덕트 단계에서 약해진다

**메시지 이동 경로**

안전을 핵심 가치로 제시 → 실제 보호 기능으로 이어짐 → **안전 기능과 추천 피드가 연결되는 단계에서 약해짐** → 보호 기능이 있어도 기본 시청 경험은 그대로 유지

| 연결 지점 | 실제 상태 |
|---|---|
| 메시지 → 안전 기능 | 콘텐츠 삭제, 청소년 기본 설정, 패밀리 페어링이 실제로 존재한다 |
| 안전 기능 → 실제 사용 | 더 강한 보호는 부모가 알고 계정을 연결해 직접 설정해야 한다 |
| 기본 UX → 실제 보호 | 알림은 넘길 수 있고, 이후에는 같은 추천 피드가 다시 이어진다 |

**회사가 하는 말**

틱톡은 한국에서 "안심에 진심"을 내세우며 신뢰와 안전을 핵심 가치로 설명한다. 연간 20억 달러 이상을 투자하고, 2025년 2분기 삭제 콘텐츠의 99% 이상을 신고 전에 발견했으며 90% 이상은 노출 전에 제거했다고 발표했다. 청소년 계정에는 연령별 보호 장치와 패밀리 페어링도 제공한다. [틱톡 2025 미디어데이](https://newsroom.tiktok.com/2025mediaday?lang=ko-KR)

**제품에서 보이는 것**

말은 실제 기능으로 이어진다. 18세 미만 계정에는 하루 60분 제한이 기본 적용된다. 16세 미만 이용자가 밤 10시 이후 틱톡을 보면 'For You' 피드가 전체 화면 알림으로 중단된다. 부모는 패밀리 페어링으로 시간과 콘텐츠 제한을 더 강하게 설정할 수 있다. [틱톡 청소년 보호 기능](https://newsroom.tiktok.com/new-ways-we-are-supporting-parents-and-helping-teens-build-balanced-digital-habits?lang=en)

하지만 보호 수준을 높이려면 부모가 계정을 연결하고 여러 설정을 직접 조정해야 한다. 영국에서는 2024년 2월 패밀리 페어링이 활성화된 계정이 청소년 월간 이용자의 4~5%였다. [Ofcom, 아동 보호 보고서](https://www.ofcom.org.uk/online-safety/protecting-children/how-tiktok-snap-twitch-protect-children-from-harmful-videos)

**어디서 틀어지나**

> **진단: 메시징 문제가 아니라 프로덕트 문제다.**

- **주된 문제 위치:** 추천 피드의 기본값과 사용시간 제어
- **연결이 끊긴 영역:** 신뢰와 안전 ↔ 추천 시스템
- **함께 드러난 문제:** 기능 출시와 삭제 지표 ↔ 실제 보호 효과 측정

"안심에 진심"이라는 메시지는 기능까지는 제대로 전달된다. 끊어지는 곳은 그 기능이 추천 피드의 작동 방식을 바꿔야 하는 순간이다.

안전 기능은 피드를 잠시 멈추지만, 알림을 넘긴 뒤에는 무한 스크롤과 자동 재생과 개인화 추천이 다시 이어진다. 문구를 더 정확하게 고치는 것으로는 달라지지 않는다. 안전 기능이 추천 피드의 기본 행동까지 바꾸는 지점에서 갈린다.

**왜 그런 것으로 보이나**

**알아도 잘 쓰이지 않음**
영국 청소년 계정에서 패밀리 페어링 활성화 비율은 2024년 2월 기준 4~5%였다. 기능의 존재가 사용으로 자동 연결되지는 않는다.

**설정 부담**
더 강한 보호를 적용하려면 부모가 틱톡 계정을 만들고 청소년 계정과 연결한 뒤 제한 수준을 직접 조정해야 한다. EU 집행위원회도 부모 통제가 추가적인 시간과 역량을 요구한다고 지적했다.

**쉽게 넘기는 기본 알림**
기본 화면시간 제한은 시청을 영구히 멈추는 장치가 아니다. 한도에 닿아도 본인이 정한 패스코드를 입력하면 피드로 돌아가고, 제한 자체도 본인이 끌 수 있다. [틱톡 스크린타임 안내](https://support.tiktok.com/en/account-and-privacy/account-information/screen-time)

EU 집행위원회는 2026년 2월 무한 스크롤과 자동 재생, 개인화 추천이 강박적 사용 위험을 만들 수 있고, 화면시간 도구는 넘기기 쉬워 마찰이 거의 없다고 예비 판단했다. [EU 집행위원회 예비 판단](https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act)

> **틱톡은 안전을 추천 피드 자체를 제한하는 원칙이 아니라, 피드 주변에서 사용자와 부모가 작동시키는 보호 기능으로 구현했다.**

공개 자료로 확인되는 것은 조직의 협업 구조가 아니라, 최종 제품에서 안전 기능과 추천 시스템이 따로 움직인다는 결과다.
