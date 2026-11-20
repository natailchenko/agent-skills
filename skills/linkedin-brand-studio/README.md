# LinkedIn Brand Studio — a Claude skill

Turns Claude into a small content studio for your LinkedIn: you dictate ideas and approve, Claude does the rest.

What you get at the end:
- a project folder with your strategy, voice guide, idea bank and calendar
- posts drafted in your own voice, fact-checked and made to sound human
- cover images in your colors (memes, your photos or question cards)
- copy-paste kits for each post, ready to schedule in LinkedIn
- a private live board: every post by status, its text and files, your next steps and top topics

## Install

**Claude Code or the Claude desktop app (recommended, needed for files, covers and the board)**
Unzip into your skills folder so you have `~/.claude/skills/linkedin-brand-studio/SKILL.md`. Restart the session.

**claude.ai**
Customize → Skills → upload `linkedin-brand-studio.zip` (the zip must contain the `linkedin-brand-studio` folder with `SKILL.md` inside). On Team/Enterprise plans an admin can also share it with the whole organization.

**OpenAI Codex or another agent that supports Agent Skills**
Put the `linkedin-brand-studio` folder into that tool's skills folder (for Codex see developers.openai.com/codex/skills). The board then runs in local mode: a file you open in your browser. See `references/portability.md` for what differs.

## Start
Open Claude in an empty folder (for example `~/projects/LinkedIn`) and say:
> Set up my LinkedIn personal brand project.

Claude will ask questions in small groups, check which tools you have, and walk you through 10 steps.

## Prepare (10 minutes)
- your CV/resume (PDF or DOCX)
- your LinkedIn profile link
- 5–10 texts you wrote yourself (posts, emails, Slack messages, voice notes)
- a few photos of yourself in one folder
- colors you like, if any

## Optional add-ons (Claude checks and tells you)
| Add-on | What for | Without it |
|---|---|---|
| [humanizer](https://github.com/blader/humanizer) | Makes posts sound less AI-written | Built-in checklist is used |
| [meme-factory](https://skills.sh/softaworks/agent-toolkit/meme-factory) | Memes from 100+ templates | Memes come from memegen.link directly |
| Claude in Chrome or the built-in browser | Reads your LinkedIn profile | You send screenshots |
| Google Chrome + Node | Renders cover images | Make covers in Canva |
| Postiz (paid, from ~$29/month, 7-day trial) | Automatic scheduling and stats | You schedule in LinkedIn by hand (free, ~2 min per post) |

Install commands for each add-on are in `references/tools.md`; Claude shows them to you during setup.

Start free with manual scheduling. Move to Postiz only if you post 3+ times a week or on several networks.
