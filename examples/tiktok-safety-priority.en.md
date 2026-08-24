# Example - TikTok, safety as a priority claim

An unedited Facet Core answer, kept as a reference for the output contract and the verification rules behind it.

The same audit in Korean: [tiktok-safety-priority.md](tiktok-safety-priority.md). The labels differ because the output contract localizes them; the five steps and their order do not.

- **Prompt:** `$facet-core Test TikTok's claim that safety is its top priority.`
- **Run date:** 2026-08-24
- **Scope:** globally announced product features, plus one EU-scoped regulatory assessment. TikTok's Korean-market messaging is the promise under audit.
- **Sources verified:** 2026-08-24. Three of the four cited sources were re-read at their original URLs. The `support.tiktok.com` recommendation page returned an empty response on re-check; the same claim is supported by TikTok's newsroom explanation of For You ranking (2020-06-18), which states that finishing a longer video carries greater weight.
- **Note:** the EU assessment is preliminary and does not prejudge the outcome of the investigation. Company positions and product behavior change; treat this answer as accurate to its run date, not as a standing claim.

---

## TikTok · "serious about peace of mind" weakens where screen-time safety meets the teen recommendation feed

**Where the message travels**

Safety presented as a core value → content moderation and teen protections follow → **screen-time safety is built only as guards outside the feed** → the feed keeps infinite scroll and personalized recommendation

| Connection | What is actually there |
|---|---|
| Message → content moderation | The investment and the proactive removal system genuinely exist |
| Safety features → teen UX | A 60-minute limit for under-18s and a late-night interruption for under-16s are on by default |
| Teen UX → actual protection | The guards stop the feed; the feed itself is unchanged. EU regulators preliminarily found these guards insufficient |

**What the company says**

In Korea TikTok presents "serious about peace of mind," describing trust and safety as a core value. It says it invests over two billion dollars a year, that in Q2 2025 more than 99% of removed content was detected before any user reported it, and that more than 90% was taken down before anyone saw it. Teen accounts get age-based protections and Family Pairing. [TikTok 2025 Media Day, December 2025](https://newsroom.tiktok.com/2025mediaday?lang=ko-KR)

**What the product shows**

The words do reach real features. Accounts under 18 have a 60-minute daily limit by default, and when someone under 16 uses TikTok after 10pm, the For You feed is interrupted by a full-screen takeover with calming music. Keep going and a second, harder-to-dismiss prompt appears. [TikTok teen protections, March 2025](https://newsroom.tiktok.com/new-ways-we-are-supporting-parents-and-helping-teens-build-balanced-digital-habits?lang=en)

Past the prompt, though, the personalized stream resumes. TikTok explains that the For You feed uses signals such as whether you watched a video through to the end or skipped it, and keeps recommending what you are likely to be interested in. [How TikTok recommends content](https://support.tiktok.com/en/using-tiktok/exploring-videos/how-tiktok-recommends-content)

**Where it changes**

At the stage of reducing harmful content, "serious about peace of mind" carries through into features and operations. The meaning shifts once safety is taken to include **limiting the default experience itself so people do not stay long**.

Every protection TikTok has published stops the feed from outside it. The 60-minute limit and the late-night prompt break the flow, while infinite scroll, autoplay, and personalized recommendation stay exactly as they are. Safety enters content through removal and suppressed distribution; it does not enter screen time by changing how the feed works.

Outside evidence questions how well that structure performs. In February 2026 the European Commission preliminarily found that infinite scroll, autoplay, and personalized recommendation can create a risk of compulsive use, and that TikTok had not adequately assessed the effect of that risk on minors and vulnerable adults. Screen-time management tools, it said, are easy to dismiss and introduce limited friction, and parental controls demand extra time and skill from parents, so neither appears to reduce the risk in practice. This is not a final decision, and it concerns TikTok's EU service. [European Commission preliminary findings, 6 February 2026](https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act)

**Why it may be this way**

TikTok's safety is not built one way. Content safety runs deep inside the feed through removal, blocking, and exclusion from recommendation, while screen-time safety sits around the feed as prompts, limits, and parental settings.

The recommendation system, meanwhile, is centered on reading watching behavior and handing over the next piece of content. TikTok itself explains that finishing a video carries greater weight. So the message "safety is built into the design" narrows in the actual product to **"the recommendation experience stays, and users are given ways to stop."**

Why TikTok drew the line there cannot be established from public material. An explanation that reducing time on app conflicts with the revenue structure, and an explanation that screen-time safety started later than content safety and has not yet reached the feed itself, both fit what can be observed. Internal targets or design discussions would have to be public to separate them.
