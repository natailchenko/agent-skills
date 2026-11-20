#!/usr/bin/env python3
"""Build dashboard documents from the project files.

Reads drafts/, published/, ready/, ideas/idea-bank.md and ideas/priorities.json
and writes one JSON file per dashboard document into tools/.dashboard-out/:
  posts/<slug>.json, ideas/<no>.json, meta/summary.json
Claude then pushes them to the dashboard artifact with ArtifactData (batch, file_path).
"""
import json, os, re, glob, datetime

# Set these once for the board header.
OWNER_NAME = "Your Name"
SIGNATURE = ""  # their own slogan, or leave empty

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tools", ".dashboard-out")
COVERS = os.path.join(ROOT, "tools", "dashboard-covers.json")  # slug -> uploaded asset url

STATUS_ORDER = ["draft", "approved", "scheduled", "published", "on_hold"]


def field(text, name):
    m = re.search(r"^- \*\*" + re.escape(name) + r":\*\*\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def section_after(text, label):
    m = re.search(r"^" + re.escape(label) + r":\s*\n((?:- .*\n?)+)", text, re.M)
    return [l[2:].strip() for l in m.group(1).strip().split("\n")] if m else []


def norm_status(raw):
    r = raw.lower()
    if r.startswith("published"):
        return "published"
    if r.startswith("scheduled"):
        return "scheduled"
    if r.startswith("approved"):
        return "approved"
    if r.startswith("on hold"):
        return "on_hold"
    return "draft"


def parse_post(path, folder):
    s = open(path, encoding="utf-8").read()
    slug = os.path.basename(path)[:-3]
    title = re.search(r"^# (.+)$", s, re.M).group(1).strip()
    a = s.index("## Post\n") + len("## Post\n")
    b = s.index("\n---\n", a)
    body = s[a:b].strip()
    hashtags = " ".join(l for l in body.split("\n") if l.startswith("#"))
    text = "\n".join(l for l in body.split("\n") if not l.startswith("#")).strip()
    tail = s[b + 5:]
    pillar_line = field(s, "Pillar")
    parts = [p.strip() for p in pillar_line.split("·")]
    pillar = parts[0] if parts else ""
    series = next((p.split(":**")[-1].strip() for p in parts if p.startswith("**Series")), "")
    fmt = next((p.split(":**")[-1].strip() for p in parts if p.startswith("**Format")), "")
    m = re.search(r"^First comment:\s*(.*)$", tail, re.M)
    first_comment = m.group(1).strip() if m else ""
    if first_comment in ("—", "-") or first_comment.startswith("— ("):
        first_comment = ""
    date_iso = slug[:10]
    status = norm_status(field(s, "Status"))
    ready_dir = os.path.join(ROOT, "ready", slug)
    if not os.path.isdir(ready_dir):
        cands = glob.glob(os.path.join(ROOT, "ready", slug[:10] + "-*"))
        ready_dir = cands[0] if cands else ""
    has_cover = bool(ready_dir) and os.path.exists(os.path.join(ready_dir, "cover.png"))
    covers = json.load(open(COVERS)) if os.path.exists(COVERS) else {}
    needs = []
    if status == "draft":
        needs.append("Approve text")
    if status in ("draft", "approved") and not has_cover:
        needs.append("Cover")
    if status == "approved" and has_cover:
        needs.append("Schedule in LinkedIn")
    notes = tail.split("\n", 1)[-1].strip() if tail else ""
    return {
        "slug": slug,
        "date": date_iso,
        "dateLabel": field(s, "Date").split(" (")[0],
        "title": title,
        "pillar": pillar,
        "series": series,
        "format": fmt,
        "ideaNo": field(s, "Idea #"),
        "status": status,
        "statusRaw": field(s, "Status"),
        "text": text,
        "hashtags": hashtags,
        "firstComment": first_comment,
        "words": len(text.split()),
        "draftPath": os.path.relpath(path, ROOT),
        "readyPath": (os.path.relpath(ready_dir, ROOT) + "/") if ready_dir else "",
        "hasCover": has_cover,
        "coverUrl": covers.get(slug) or covers.get(os.path.basename(ready_dir) if ready_dir else "", ""),
        "needs": needs,
        "notes": notes[:6000],
    }


def parse_ideas():
    s = open(os.path.join(ROOT, "ideas", "idea-bank.md"), encoding="utf-8").read()
    pillar = ""
    ideas = []
    for line in s.split("\n"):
        if line.startswith("## "):
            pillar = re.sub(r"^## (\d\.\s*)?", "", line).strip()
            continue
        m = re.match(r"^\| (\d+) \| (.+?) \| (.+?) \| (\w[\w ]*) \|$", line)
        if m:
            no, title, fmt, st = m.groups()
            ideas.append({
                "no": int(no),
                "title": re.sub(r"\*\*", "", title).strip(),
                "format": fmt.strip(),
                "needsInput": "⭐" in fmt,
                "status": st.strip(),
                "pillar": pillar,
            })
    pri = json.load(open(os.path.join(ROOT, "ideas", "priorities.json"), encoding="utf-8"))
    by_no = {p["no"]: p for p in pri["top"]}
    for i in ideas:
        p = by_no.get(i["no"])
        if p:
            i.update({"priority": p["rank"], "why": p["why"], "ask": p["ask"]})
    return ideas, pri


def main():
    os.makedirs(OUT, exist_ok=True)
    for sub in ("posts", "ideas", "meta"):
        os.makedirs(os.path.join(OUT, sub), exist_ok=True)
        for f in glob.glob(os.path.join(OUT, sub, "*.json")):
            os.remove(f)
    posts = []
    for folder in ("drafts", "published"):
        for p in sorted(glob.glob(os.path.join(ROOT, folder, "*.md"))):
            if os.path.basename(p).startswith("20"):
                posts.append(parse_post(p, folder))
    for p in posts:
        json.dump(p, open(os.path.join(OUT, "posts", p["slug"] + ".json"), "w"), ensure_ascii=False)
    ideas, pri = parse_ideas()
    json.dump({"items": ideas}, open(os.path.join(OUT, "ideas", "all.json"), "w"), ensure_ascii=False)
    counts = {k: sum(1 for p in posts if p["status"] == k) for k in STATUS_ORDER}
    summary = {
        "updatedAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "ownerName": OWNER_NAME,
        "signature": SIGNATURE,
        "counts": counts,
        "totalPosts": len(posts),
        "ideasOpen": sum(1 for i in ideas if i["status"] in ("idea", "planned")),
        "cadence": pri.get("cadence", ""),
        "nextActions": pri.get("nextActions", []),
    }
    json.dump(summary, open(os.path.join(OUT, "meta", "summary.json"), "w"), ensure_ascii=False)
    # Local mode (no artifact, e.g. Codex or a plain browser): dashboard/data.js next to dashboard/index.html
    os.makedirs(os.path.join(ROOT, "dashboard"), exist_ok=True)
    with open(os.path.join(ROOT, "dashboard", "data.js"), "w", encoding="utf-8") as f:
        f.write("window.BOARD_DATA = " + json.dumps({"posts": posts, "ideas": {"items": ideas}, "meta": summary}, ensure_ascii=False) + ";\n")
    print(json.dumps({"posts": len(posts), "ideas": len(ideas), "counts": counts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
