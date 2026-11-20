---
name: prompt-upgrade
description: Turns a rough idea into a clear, complete brief and then does the work. An expert committee, picked for the task, sets the quality bar before anything is produced. Use at the start of any non-trivial task (an idea, a script, a site or feature, a plan, an analysis, a document) and for "upgrade this prompt", "write a brief", "expert committee".
---

# Prompt Upgrade

Turn a rough request into a strong brief, then deliver a result that meets it.

The core idea is that **the expert committee works at the start**, while the idea, script or spec is still being shaped. It does not review a finished product. The experts decide what "excellent" means for this specific task, and the work is produced against those criteria from the start, so fewer rounds of revision are needed.

This is a scaffold, not a cage. If a better path is obvious (different experts, a different tool, fewer steps), take it and say so in one line.

## Principles

- **Reply in the user's language.** Write deliverables in the language the task calls for (the audience's language, or whatever the user asked for).
- **Read messy input generously.** Dictated or stream-of-consciousness requests contain repeats, false starts and self-corrections. Extract the intent and don't ask again about anything the user already said.
- **Use what you already know.** Before asking a question, check the conversation, attached files, project context and any stored user preferences.
- **Proportion.** A small task gets a light pass and a large or ambiguous one gets the full process. Never put on a show of process.

## Process

### 1. Understand
In 2–3 lines, restate what you understood: the goal, the audience or user, and the expected output.

### 2. Convene the committee (always, scaled to the task)
Pick **3–4 experts** that someone would really hire for this task. Work them out from the task's signals:

- **Domain keywords**: "landing page" → product, frontend, conversion copywriter; "pitch deck" → investor, storyteller, designer; "lesson plan" → teacher, instructional designer, student advocate.
- **Output type**: code, text, visual, video, data, decision, plan.
- **Audience**: who will use or judge the result, and who represents them.
- **Risk**: whoever catches the most expensive mistake (security, legal, accuracy, budget, feasibility).

Always include one **skeptic**, someone who argues for the user or audience or names the risk. Keep the roles concrete ("senior React engineer", not "tech expert").

Each expert adds to the brief:
- **one quality criterion**, what "excellent" means from their angle;
- **one main risk** or typical mistake;
- **one question** for the user, only if the work cannot go on without the answer.

Then a short **synthesis**: where the experts disagree and which call we take.

**Scale:**
- *Light* (clear, small task): the committee works internally and you show one line, e.g. "Committee: UX writer → plain language; QA → edge cases".
- *Full* (a new idea, a creative piece, a build, a strategy, high stakes, ambiguity): show it compactly, 1–2 bullets per expert plus the synthesis.

### 3. Pick the tools
Before working, see what this session has: skills, connected tools or apps, artifact or file types, search, code execution. Pick the best fit, chain several if needed, and name them in the brief. If a missing tool or connection would make a big difference to the result, say so in one line.

### 4. Ask (0–5 questions)
Ask only the questions the committee raised that would really change the result. Use a multiple-choice question tool when one is available, with the recommended option first. A clear task gets zero questions. If the user is not around to answer, go with reasonable assumptions and label them.

### 5. Write the brief
Skip any section that would be empty:

```
# Task
# Context (who, project, what already exists)
# Steps
# Quality criteria (from the committee)
# Constraints and things to avoid (risks from the committee)
# Output format
# Tools / skills to use
```

Add a reasoning technique where it helps, and combine them freely:
- **Step-by-step reasoning** for logic, math, debugging and architecture.
- **Self-refine** for writing, scripts and copy: draft → check against the criteria → improve.
- **Step-back** for tangled or overly narrow problems: state the underlying goal or principle first.

Never invent facts. Mark unknowns as `[to confirm]` or as explicit assumptions.

### 6. Deliver
- **By default, run it.** Do the work right after the brief (or after the answers, if there were questions), with no separate "shall I proceed?".
- **"Just the prompt"**, "for another AI", "to copy": give the brief as a copyable code block and don't run it.
- **"Quick"**, "no questions": light committee, zero questions, assumptions labeled.
- **Self-check before handing over.** Check the result against the committee's criteria and fix the gaps yourself. This is a final pass, not a new review round with the user.
- If a later result misses, fix the **brief** (what was missing) as well as the output.

## Example committees (starting points, not fixed lists)

| Task type | Possible committee |
|---|---|
| Website / app feature | Product manager, senior engineer, UX designer, QA or security skeptic |
| Short video / social post | Content strategist, short-form scriptwriter, native-speaker editor, editor or motion designer |
| Marketing copy / landing page | Conversion copywriter, brand strategist, target customer, legal/claims checker |
| Business plan / strategy | Strategist, operator, finance lead, skeptical investor |
| Data analysis / research | Domain expert, statistician, data engineer, decision-maker who uses the result |
| Writing / documents | Editor, subject expert, target reader |
| Teaching / training | Teacher, instructional designer, learner advocate |
| AI agents / automation | Agent architect, security and privacy reviewer, skeptical end user |
| Personal decision | Pragmatist, risk manager, someone who knows the user's values, devil's advocate |

## Don'ts
- Don't convene the committee only after the work is done.
- Don't turn the committee into theater. Its value is in the criteria, not the discussion.
- Don't ask more than 5 questions, or anything already answered.
- Don't pad the brief. Every line should change the result.
