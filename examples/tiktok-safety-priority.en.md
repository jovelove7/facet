# Example - TikTok, safety as a priority claim

An unedited Facet Core answer, kept as a reference for the output contract and the verification rules behind it.

The same audit in Korean: [tiktok-safety-priority.md](tiktok-safety-priority.md). The labels differ because the output contract localizes them; the five steps and their order do not.

- **Prompt:** `$facet-core Test TikTok's claim that safety is its top priority.`
- **Run date:** 2026-08-24
- **Scope:** globally announced product features, one UK figure, and one EU-scoped regulatory assessment. TikTok's Korean-market messaging is the promise under audit.
- **Sources verified:** 2026-08-24, read directly except where noted. The Ofcom figure is carried from search coverage of Ofcom's report; ofcom.org.uk blocks automated reading, so the primary page was not opened.
- **Note:** the EU assessment is preliminary and does not prejudge the outcome of the investigation. Treat this answer as accurate to its run date, not as a standing claim.

---

## TikTok · "Serious about Safe" weakens at the product step where safety features have to become protection

**Where the message travels**

Safety presented as a core value → real protective features follow → **it weakens where safety features meet the recommendation feed** → the features exist and the default watching experience is unchanged

| Connection | What is actually there |
|---|---|
| Message → safety features | Content removal, teen defaults, and Family Pairing genuinely exist |
| Safety features → actual use | Stronger protection requires a parent to know about it, link an account, and set it up |
| Default UX → actual protection | The prompt can be passed, and the same recommendation feed resumes after it |

**What the company says**

In Korea TikTok runs the line "안심에 진심", carried in English as "Serious about Safe", and describes trust and safety as a core value. It says it invests over two billion dollars a year, that in Q2 2025 more than 99% of removed content was detected before any user reported it, and that more than 90% was taken down before anyone saw it. Teen accounts get age-based protections and Family Pairing. [TikTok 2025 Media Day](https://newsroom.tiktok.com/2025mediaday?lang=ko-KR)

**What the product shows**

The words reach real features. Accounts under 18 have a 60-minute daily limit by default. When someone under 16 opens TikTok after 10pm, the For You feed is interrupted by a full-screen prompt. Parents can set stricter time and content limits through Family Pairing. [TikTok teen protections](https://newsroom.tiktok.com/new-ways-we-are-supporting-parents-and-helping-teens-build-balanced-digital-habits?lang=en)

Raising the level of protection, though, requires a parent to link accounts and adjust the settings themselves. In February 2024, accounts with Family Pairing active came to 4-5% of TikTok's UK teen monthly users. [Ofcom, protecting children report](https://www.ofcom.org.uk/online-safety/protecting-children/how-tiktok-snap-twitch-protect-children-from-harmful-videos)

**Where it changes**

> **Diagnosis: this is a product problem, not a messaging problem.**

- **Main problem location:** the recommendation feed's defaults and its screen-time controls
- **Where the connection breaks:** Trust & Safety ↔ Recommendation
- **Also visible:** feature launches and removal counts ↔ measurement of actual protection

"Serious about Safe" carries all the way to the features. What breaks is the moment those features would have to change how the recommendation feed behaves.

Safety features pause the feed. Past the prompt, infinite scroll and autoplay and personalized recommendation resume. Sharpening the wording would not change that. It turns on whether safety reaches the feed's default behavior.

**Why it may be this way**

**Known but rarely switched on**
Family Pairing was active on 4-5% of UK teen accounts as of February 2024. A feature existing does not carry itself into use.

**Setup burden**
Stronger protection requires a parent to create a TikTok account, link it to the teen's, and set the limits by hand. The European Commission also noted that parental controls demand extra time and skill from parents.

**A default prompt that is easy to pass**
The default screen-time limit does not end the session. At the limit, entering a passcode the user set themselves returns them to the feed, and the limit itself can be switched off. [TikTok screen time](https://support.tiktok.com/en/account-and-privacy/account-information/screen-time)

In February 2026 the European Commission preliminarily found that infinite scroll, autoplay, and personalized recommendation can create a risk of compulsive use, and that screen-time tools are easy to dismiss and introduce limited friction. [European Commission preliminary findings](https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act)

> **TikTok built safety as protective features that users and parents operate around the feed, rather than as a rule that constrains the feed itself.**

What public evidence establishes is not how the company coordinates internally, but that safety features and the recommendation system move separately in the finished product.
