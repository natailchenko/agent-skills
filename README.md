# Agent Skills

Skills for Claude (Claude Code, the Claude desktop app, claude.ai) and other agents that support the Agent Skills format, such as OpenAI Codex.

## Skills

| Skill | What it does |
|---|---|
| [linkedin-brand-studio](skills/linkedin-brand-studio) | Turns Claude into a small content studio for your LinkedIn: strategy, your voice, post drafts, covers, publishing kits and a live content board. |
| [prompt-upgrade](skills/prompt-upgrade) | Turns a rough idea into a clear brief and then does the work. An expert committee picked for the task sets the quality bar before anything is produced. |

## Install one skill

With Node.js:
```bash
npx skills add natailchenko/agent-skills --skill linkedin-brand-studio
```

Or by hand: copy the skill folder (for example `skills/linkedin-brand-studio`) into `~/.claude/skills/`, then start a new session. For claude.ai, zip the skill folder and upload it in Customize → Skills.

Each skill has its own README with details.

## License
MIT
