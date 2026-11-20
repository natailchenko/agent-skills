# Running this skill outside Claude

This skill follows the open Agent Skills format (a folder with `SKILL.md`), so tools that support that format can load it. What works everywhere and what is Claude-only:

| Part | Claude (Code / desktop app) | Codex or another agent with file access | Plain chat (ChatGPT, claude.ai without files) |
|---|---|---|---|
| Intake, strategy, voice guide, idea bank | ✅ | ✅ | ✅ in the chat, no files |
| Drafts, ready kits, calendar as files | ✅ | ✅ | ❌ copy from the chat |
| Fact check with web search | ✅ | ✅ if the agent has web access | depends |
| Sounding human | humanizer skill, if installed, else checklist | checklist in `post-rules.md` (or a humanizer skill if their tool has one) | checklist |
| Memes | meme skill, else memegen.link | memegen.link | memegen.link link only |
| Cover images (HTML → PNG) | ✅ with Chrome | ✅ with Chrome | ❌ (use Canva) |
| Reading the LinkedIn profile | browser tools, else screenshots | screenshots | screenshots |
| Content board | Artifact with database, auto-updating | local mode: `dashboard/index.html` + `data.js` | ❌ |
| Publishing | manual (free) or Postiz CLI (paid) | same | manual |

Where to put the folder:
- Claude Code / desktop app: `~/.claude/skills/linkedin-brand-studio/`
- claude.ai: upload the zip in Customize → Skills
- Codex: its skills folder (OpenAI's docs currently name `~/.agents/skills/` for personal skills and `.agents/skills/` inside a project; check developers.openai.com/codex/skills if that changed)
- Any other agent: point it at `SKILL.md` as instructions, or paste `SKILL.md` and the references it needs into a project's instructions.

When a step names a Claude tool (Artifact, ArtifactData, a browser tool) and you don't have it, use the fallback in this table and tell the person in one line what is different.
