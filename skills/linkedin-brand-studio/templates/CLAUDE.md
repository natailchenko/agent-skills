# LinkedIn personal brand — {{NAME}}

Goal: {{GOAL}}. Talk to {{NAME}} in {{CHAT_LANGUAGE}}; posts are in {{POST_LANGUAGE}}.
Strategy: [strategy.md](strategy.md). Folder map: see the linkedin-brand-studio skill, `templates/folder-structure.md`.

## Start of every session
- Posts with status `scheduled` whose date and time have passed → `published`: update the draft header, `calendar.md`, `ideas/idea-bank.md`, move the draft to `published/`, sync the board.
- Re-read `voice/voice-guide.md` before writing anything.

## Posts
Use the `linkedin-voice` skill for every idea and every round of feedback. Rules: see the linkedin-brand-studio skill, `references/post-rules.md`.
Default time: {{POST_TIME}} ({{AUDIENCE_TZ}}). Cadence: {{CADENCE}}.

## Confidentiality
- Private facts are marked 🔒 in `profile/background.md`. Never use them.
- Employer name in posts: {{EMPLOYER_RULE}}.
- Never: {{NEVER_LIST}}.
- `profile/private/`: read only to extract facts; never quote, upload or publish.

## Visuals
Palette, fonts and signature line in `brand/visual-style.md`. Signature: "{{NAME}} · {{SIGNATURE}}".

## Publishing
{{PUBLISHING}} (manual + LinkedIn scheduler by default). For each approved post make `ready/<slug>/` with post.txt, first-comment.txt, cover.png.

## Dashboard
Board URL: {{BOARD_URL}}. After any change to drafts/, published/, ready/ or ideas/: upload new covers, run `python3 tools/dashboard_sync.py`, batch-write `tools/.dashboard-out/` to the board (see `references/dashboard.md`).

## Never
- Write, post or schedule comments for {{NAME}}.
- Enter passwords, card details or API keys.
- Publish anything without {{NAME}}'s approval.
