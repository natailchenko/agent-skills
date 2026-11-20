# Project folder

```
LinkedIn/
├── CLAUDE.md                 rules for every session (from templates/CLAUDE.md)
├── strategy.md               goal, positioning, pillars, series, cadence, metrics
├── calendar.md               what goes out when, with status
├── brand/
│   ├── visual-style.md       palette, fonts, signature line, cover rules
│   ├── photos.md             photo shortlist and where each was used
│   ├── memes/                meme images used on covers
│   ├── photos/               cropped photos for covers
│   └── templates/            one HTML cover file per post
├── profile/
│   ├── background.md         facts about the person (🔒 = private)
│   ├── profile-audit.md      LinkedIn audit, headline/About drafts
│   └── private/              documents that must never be published (CV, contracts)
├── voice/
│   ├── voice-guide.md        how they write
│   └── samples/              their own texts and dictations, word for word
├── ideas/
│   ├── inbox.md              raw ideas, any language
│   ├── idea-bank.md          numbered ideas by pillar
│   └── priorities.json       top topics for the board
├── drafts/                   one file per post: YYYY-MM-DD-slug.md
├── ready/                    copy-paste kits: <slug>/post.txt, first-comment.txt, cover.png
├── published/                drafts move here once live
├── dashboard/index.html      the board page
├── tools/                    dashboard_sync.py, dashboard-covers.json
└── .claude/skills/linkedin-voice/SKILL.md
```

Lock `profile/private/`: `chmod 700 profile/private && chmod 600 profile/private/*`, and add an ask rule for reads of it in `.claude/settings.local.json`.
