# Content board

A private artifact that shows every post by status (Drafts → Approved → Scheduled → Published), opens each post's text, cover and file paths on click, lists "your next steps", the top topics by priority and the whole idea bank. The page never changes; its data lives in the artifact's database and you refresh it after every change.

## Create it (once)
1. Copy `assets/dashboard.html` to `<project>/dashboard/index.html`.
2. Publish it with the Artifact tool: icon `board`, description "Content board for <Name>'s LinkedIn", capabilities `{"db": {"rules": [{"path": "", "read": "view", "write": "admin"}]}, "assets": {}}`.
3. Copy `scripts/dashboard_sync.py` to `<project>/tools/` and create `tools/dashboard-covers.json` with `{}`.
4. Write the board URL into the project's `CLAUDE.md` (Dashboard section).
5. Offer to pin it in their sidebar.

## Sync (after every change to drafts/, published/, ready/, ideas/)
1. New `cover.png` in ready/? Upload it: Artifact publish with `url`, `asset: true`, `file_paths: [...]`. Add `"<slug>": "/_blob/<id>"` to `tools/dashboard-covers.json`.
2. Run `python3 tools/dashboard_sync.py` (set OWNER_NAME and SIGNATURE at the top of the script once).
3. `ArtifactData list` on `posts` to read versions, then one `batch` of `set` writes with `file_path` from `tools/.dashboard-out/`: `posts/<slug>`, `ideas/all`, `meta/summary`. Pin existing documents with `if_version`; omit it for new ones. Delete board docs for posts whose files are gone.
4. Check once with `ArtifactData list` (`as_level: "view"`). Don't loop.

The idea bank parser expects `ideas/idea-bank.md` with `## <pillar>` headings and rows `| <no> | <idea> | <format> | <status> |`.

## Local mode (no Artifacts: Codex, other agents, or by choice)
1. Copy `assets/dashboard.html` to `<project>/dashboard/index.html`.
2. Run `python3 tools/dashboard_sync.py`. Besides `tools/.dashboard-out/` it writes `dashboard/data.js`.
3. The person opens `dashboard/index.html` in their browser (double-click). It reads `data.js` and shows the same board. After each sync they refresh the tab.
Covers show on cards only in Artifact mode; in local mode the card shows a "Cover ready" chip and the modal shows the file path.
