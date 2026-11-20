# Publishing

## Start free: manual + LinkedIn's own scheduler
For each approved post you prepare `ready/<date-slug>/`: `post.txt`, `first-comment.txt` (if any), `cover.png`. The person:
1. LinkedIn → Start a post → paste `post.txt`.
2. Add `cover.png` (photo icon) or a PDF carousel (Add a document).
3. Clock icon next to "Post" → date and time (default 08:00 in the audience's time zone, Tue–Thu) → Schedule.
4. When it goes live, add the first comment from `first-comment.txt` (LinkedIn can't schedule comments) and answer comments in the first 60–90 minutes. Never write comments for them.

Time cost: about 2 minutes per post. For 2–3 posts a week this is enough.

At the start of every session: posts with status `scheduled` whose time has passed → `published` (LinkedIn posts them by itself), move the draft to `published/`, sync the board. The person only reports exceptions.

## Later: automation with Postiz (paid)
Postiz schedules posts (with images, PDFs and first comments) to LinkedIn and other networks from the command line, and gives analytics. Worth it when they post 3+ times a week, use several networks, or want stats in one place.

Price (checked Nov 2026, confirm at postiz.com/pricing before buying): Standard about $29/month for 5 channels (about $23/month billed yearly), higher tiers $39–$99. 7-day free trial. A free self-hosted version exists but needs a server and their own LinkedIn developer app, so it is only for technical people.

Setup when they decide:
1. They create an account on postiz.com, start the trial (their card, their action) and connect LinkedIn (personal profile) in Postiz.
2. You install the CLI: `npm install -g postiz` (or `--prefix ~/.npm-global` if permissions fail).
3. `postiz auth:login` → they approve the code in the browser.
4. `postiz integrations:list` → if it says "No subscription found", the trial isn't active yet.
5. Test with a draft post (`-t draft`) with a PDF before scheduling real ones.
