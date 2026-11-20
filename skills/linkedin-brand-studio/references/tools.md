# Tools: what is needed, what is optional

Check each item, then show the person one short table: ✅ have it · ➕ optional, how to get it · ❌ not available here.

| Need | Required? | How to check | If missing |
|---|---|---|---|
| File access (Claude Code or desktop app, Code tab) | Yes for the full setup | You can read/write files | Offer the chat-only version (strategy, voice, posts in chat) |
| Artifacts with database | For the content board | The Artifact tool is available | Skip the board; keep `calendar.md` as the tracker |
| Browser (built-in browser or Claude in Chrome) | Optional, for reading their LinkedIn profile | Browser tools in your tool list | Ask for profile screenshots |
| Node + Google Chrome | Optional, for cover images | `which node`, Chrome in /Applications | Covers can be made in Canva instead, or skipped |
| Python 3 | For the board sync script | `which python3` | Update the board by hand with ArtifactData |
| **humanizer** skill | Strongly recommended | Skill list contains a humanizer skill | Use the built-in "Sounding human" checklist in `post-rules.md` (works, just less thorough). Install: see "How to install the optional skills" below. |
| **meme** skill (for example meme-factory) | Optional, only if they want memes | Skill list | Install: see below, or use memegen.link directly: `https://api.memegen.link/images/<template>/<top>/<bottom>.png?width=1100` (spaces as `_`). Common templates: `fine` (This is fine), `drake`, `ds` (Two Buttons), `gru` (Gru's plan), `disastergirl`. |
| Canva connector | Optional | Connector list | Covers from the HTML template are enough |
| Postiz CLI | Optional, paid automation | `postiz --help` | See `publishing.md` |

## How to install the optional skills
Show the person the commands for their tool and let them run them (or run them yourself if they ask). Re-check after install; a new session may be needed before the skill appears.

**humanizer** (rewrites AI-sounding text; open source, MIT): https://github.com/blader/humanizer
- Claude Code: `/plugin marketplace add blader/humanizer` then `/plugin install humanizer@humanizer` (Claude Code 2.1.142+). Older versions: `npx skills add blader/humanizer --global --agent claude-code`
- Codex: `npx skills add blader/humanizer --global --agent codex`
- claude.ai / Claude desktop chat: on the GitHub page, Code → Download ZIP, then upload it in Customize → Skills
- Other agents: `npx skills add blader/humanizer --global --agent '*'`

**meme-factory** (memes from 100+ templates via memegen.link; open source): https://skills.sh/softaworks/agent-toolkit/meme-factory
- Any agent with Node: `npx skills add https://github.com/softaworks/agent-toolkit --skill meme-factory` (add `--global --agent claude-code` or `--agent codex` to pick the tool)
- Without it nothing breaks: use the memegen.link URL pattern in the table above.

`npx` needs Node.js (nodejs.org). If they don't have Node, give them the GitHub link and the "Download ZIP → upload" route.

Rules:
- Never enter passwords, card details or API keys for the person. Give them the steps and wait.
- If `npm install -g` fails with permissions, install into the home folder: `npm install -g --prefix ~/.npm-global <pkg>` (add `--cache` to a temp folder if the npm cache is owned by root).
