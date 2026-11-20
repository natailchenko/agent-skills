---
name: linkedin-brand-studio
description: Set up and run a personal-brand LinkedIn project for one person, step by step. Interviews them (name, role, LinkedIn URL, CV, goals, voice samples, colors, privacy limits), checks which helper skills and tools they have, scaffolds a project folder, audits the profile, builds a voice guide, strategy, visual style and idea bank, drafts posts in their voice, makes cover images, and gives them a live content board. Use when someone wants to start posting on LinkedIn, build a personal brand, or "set up my LinkedIn project", and afterwards for every post idea and weekly planning.
---

# LinkedIn Brand Studio

You help one person run their LinkedIn personal brand like a small content studio: they dictate ideas and approve, you do the rest. Work in their language; write posts in the language they choose (usually English).

The setup has 10 phases. Do them in order, one at a time. At the end of each phase, say in one line what is done and what comes next, and wait for the person when the phase needs their input. Save everything as files in the project folder, so the next session can continue.

References (read when the phase says so):
- `references/intake.md` — every question to ask and what to do with each answer
- `references/tools.md` — optional helper skills and tools, how to check for them and what to do if missing
- `references/post-rules.md` — post format, sounding human, fact check, confidentiality
- `references/visuals.md` — palette, fonts, cover images, memes, photos
- `references/publishing.md` — manual LinkedIn scheduling (free) and optional Postiz automation (paid)
- `references/dashboard.md` — the live content board and how to keep it in sync
- `references/portability.md` — running this skill outside Claude (Codex and others)
- `templates/` — files you copy into their project; `assets/` and `scripts/` — the board page, cover template, sync script

## Phase 0. Where we work
1. If you are in Claude Code or the Claude desktop app (Code tab): ask for a folder for the project, or create `LinkedIn` in a place they name. Everything lives there.
2. If you are in a plain chat without file access: say that the full setup (files, cover images, board) needs Claude Code or the desktop app, and offer a lighter version: strategy, voice guide and posts in the chat.
3. Scaffold the folder from `templates/folder-structure.md`. Copy `templates/CLAUDE.md` into the project root and fill the placeholders as you learn things.

## Phase 1. Intake interview
Read `references/intake.md`. Ask the questions in small groups (3–5 at a time), not all at once. Accept voice-dictated, messy answers. Ask them to upload or drop into the folder: CV/resume, 5–10 texts they wrote themselves, photos of themselves. Write everything into `profile/background.md` (facts) and `voice/samples/` (raw texts). Mark anything private with 🔒 and never use it in posts.

## Phase 2. Tool check
Read `references/tools.md`. Check which helper skills, connectors and local tools are available (skills list, `which node python3`, Chrome). Tell the person in a short table: what they have, what is optional, and exactly what to install for the features they chose in the intake (memes, humanizer, Canva, automation). Never install anything that needs a password or payment yourself; give them the steps.

## Phase 3. Profile audit
Read their LinkedIn profile through a browser tool if one is available and they are signed in, otherwise ask for screenshots. Write `profile/profile-audit.md`: baseline numbers (followers, profile views, search appearances), what is strong, what to fix (headline, About, banner, photo, Featured, Experience with numbers, custom URL), and ready-to-paste drafts for headline and About. They change the profile themselves.

## Phase 4. Voice guide
From the samples and dictations, write `voice/voice-guide.md`: how they tell a story (opening, scale, turn, scene, takeaway, question), words and tone, "we" vs "I", what they never want. Copy `templates/linkedin-voice/SKILL.md.template` to the project's `.claude/skills/linkedin-voice/SKILL.md` so every later post goes through it. Update the guide each time they edit a draft (log under "What they changed").

## Phase 5. Strategy
Write `strategy.md`: goal (visibility, job search, consulting), one-sentence positioning, audience, 3–4 content pillars with shares, 2–3 recurring series, cadence (start with 2 posts a week, add a third later), best posting time for their audience's time zone, what to measure monthly. Ask them to confirm it.

## Phase 6. Visual style
Read `references/visuals.md`. Agree on a palette (their colors or a proposal), fonts, an optional short signature line for images, built from their own words (see `references/visuals.md`). Write `brand/visual-style.md`. Make one sample cover from `assets/cover-template.html` and show it.

## Phase 7. Idea bank and first calendar
Build `ideas/idea-bank.md` with 20–30 ideas from their background, goals and current news in their field, tagged by pillar and format; mark ideas that need their details with ⭐. Write `ideas/priorities.json` (top 8 with why and what you need from them). Put the first 2 weeks into `calendar.md`.

## Phase 8. First posts
For each post: their dictation → draft through the `linkedin-voice` skill → fact check → humanize (`references/post-rules.md`) → show them → edits → approval → cover image → copy-paste kit in `ready/<date-slug>/` (post.txt, first-comment.txt, cover.png). Propose splitting an idea in two when it holds two separate points or runs over 200 words.

## Phase 9. Content board
Read `references/dashboard.md`. In Claude with Artifacts: publish the board from `assets/dashboard.html` as a private artifact with a database, fill it with `scripts/dashboard_sync.py`, and offer to pin it. Anywhere else (Codex, other agents): use local mode, a `dashboard/index.html` file the person opens in their browser, refreshed by the same script. From now on, sync it after every change.

## Phase 10. Publishing
Read `references/publishing.md`. Start free: they paste the kit into LinkedIn and schedule it with LinkedIn's own clock icon. Tell them automation exists (Postiz, paid) and when it is worth it. At the start of every later session, move scheduled posts whose time has passed to published, then sync the board.

## After setup: the weekly loop
They dictate ideas any time → you process them into the idea bank → you draft the next week → they approve in one batch → you make covers and kits → they schedule → they answer comments themselves (never write or post comments for them) → once a month you review stats they screenshot and adjust the plan.
