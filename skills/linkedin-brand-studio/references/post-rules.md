# Post rules

## Format
- First person, plain spoken, short: 80–200 words, paragraphs of 1–2 sentences with blank lines.
- First line is the hook (≤12 words): a moment, a number or an opinion. LinkedIn shows only 2–3 lines before "…see more".
- One concrete example, number or artifact in every post.
- End with a specific question to readers, not "What do you think?".
- No links in the post body (LinkedIn cuts reach). Links go in the first comment, which the person adds after the post goes live.
- 0–3 hashtags at the end.
- Emojis: 1–3 that carry meaning (🚩 red flag, ✅ done, 🙂/😅 after a joke). No emoji bullets, no emoji at every line end, no "bold" made of special unicode characters. No emojis in serious news or security posts.
- "We" for what happened to their team, "I" for their own opinion.
- Never make them sound like a beginner ("I'm still learning…"). Frame weaknesses from experience.
- Never put someone else's quote next to their photo on an image: people read it as their words.

## Sounding human
Run every draft through the humanizer skill if they have it, then check by hand. Never use:
- "Not X, but Y" / "It's not about X, it's about Y"
- One-line dramatic closers ("Let that sink in.")
- Staged openers ("Here's the thing:", "Unpopular opinion:")
- Forced triads ("faster, smarter, better")
- Em dashes (max one per post)
- Inflated words: delve, leverage, unlock, game-changer, landscape, robust, seamless, elevate, journey, empower, navigate, harness
- Hype and unbacked percentages
- Filler wrap-ups ("At the end of the day")
Do: their own phrases, specific nouns and numbers, honest admissions, simple words. Never add facts they did not give you.

## Fact check
Check every technical or factual claim before drafting (tools, security, terms, numbers, news). If something is wrong or could look wrong to an expert, fix it and explain the correction in 1–3 sentences. For news, verify with sources and leave out anything unconfirmed, even if it went viral. List corrections in the draft under `Fact check:`.

## Confidentiality
- Private facts (🔒 in `profile/background.md`) never appear in posts.
- Don't name the employer, clients, colleagues or candidates unless they approve it for that post.
- No internal numbers, unreleased features, internal tool or repo names, ticket IDs or URLs.
- Screenshots: list what to blur under `Screenshot check:`.
- Flag doubts as `⚠️ RISK:` in the draft instead of silently dropping them.

## Draft file template (`drafts/YYYY-MM-DD-slug.md`)
```
# <working title>

- **Date:** <Day DD.MM.YYYY>, 08:00 <TZ>
- **Pillar:** <pillar> · **Series:** <if any> · **Format:** <text / text + photo / carousel>
- **Idea #:** <n>
- **Status:** draft

## Post

<post text>

#Tag #Tag

---

First comment: <text or —>
Humanizer: done
Words: ~<n>

Fact check:
- <or —>

Split / expand:
- <proposal or "Single idea">
```
Statuses: draft → approved → scheduled → published (and on hold).
