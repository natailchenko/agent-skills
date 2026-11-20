# Prompt Upgrade — a Claude skill

Turns a rough idea into a clear, complete brief and then does the work.

The trick: an expert committee, picked for your task, sets the quality bar **before** anything is produced, not after. The experts decide what "excellent" means here, name the main risks, and ask only the questions that would change the result. Then Claude writes the brief and delivers against it.

Works for ideas, scripts, sites and features, plans, analyses and documents. Small tasks get a light pass; big or vague ones get the full process.

## Install

With Node.js:
```bash
npx skills add natailchenko/agent-skills --skill prompt-upgrade
```

Or by hand: copy the `prompt-upgrade` folder into `~/.claude/skills/` and start a new session. For claude.ai, zip the folder and upload it in Customize → Skills.

## Use
Start any non-trivial task with it, for example:
> Upgrade this prompt: I want a landing page for my side project.

Other triggers: "write a brief", "expert committee".
- "Just the prompt" / "for another AI" → you get the brief as a copyable block, nothing is run.
- "Quick" / "no questions" → light committee, zero questions, assumptions labeled.

## License
MIT
