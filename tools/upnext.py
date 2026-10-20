#!/usr/bin/env python3
"""Build the dashboard's "Up next" file: every scheduled post that hasn't gone out yet.

Usage: python3 tools/upnext.py out.json

HARD RULE (PLAYBOOK): first pull the live schedule from Zernio and run
    python3 tools/sync_schedule.py --zernio p1.txt p2.txt
so state/schedule.json matches Zernio. This script refuses to run if the sync is older than 2 hours.

Reads state/schedule.json (status "scheduled", not Facebook, still in the future). Media come from the
slot's live_media (what Zernio will actually post). Thumbnail = first frame of the TikTok video (TikTok
covers are frame one), or the slot's _cover.jpg for an IG reel. Videos are read from this repo's queue/
or, for raw originals, from the mackygolfs-mackthegolfer repo's git history.
"""
import base64, json, subprocess, sys, tempfile, os, re
from datetime import datetime, timezone, timedelta
from urllib.parse import unquote
from zoneinfo import ZoneInfo

MT = ZoneInfo("America/Denver")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MG = os.environ.get("MG_REPO", os.path.join(os.path.dirname(ROOT), "mackygolfs-mackthegolfer"))
RAW = re.compile(r"raw\.githubusercontent\.com/mack-fitz/([^/]+)/([^/]+)/(.+)$")


def frame(src_path, width=240):
    with tempfile.NamedTemporaryFile(suffix=".jpg") as t:
        r = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", src_path, "-frames:v", "1",
                            "-vf", f"scale={width}:-2", "-q:v", "5", t.name])
        if r.returncode or not os.path.getsize(t.name):
            return None
        return "data:image/jpeg;base64," + base64.b64encode(open(t.name, "rb").read()).decode()


def thumb_for(url):
    m = RAW.search(url or "")
    if not m:
        return None
    repo, ref, path = m.group(1), m.group(2), unquote(m.group(3))
    if repo == "clips" and os.path.exists(os.path.join(ROOT, path)):
        return frame(os.path.join(ROOT, path))
    gitdir = ROOT if repo == "clips" else MG
    with tempfile.NamedTemporaryFile(suffix=os.path.splitext(path)[1]) as t:
        r = subprocess.run(["git", "-C", gitdir, "cat-file", "-p", f"{ref}:{path}"], stdout=t)
        if r.returncode:
            subprocess.run(["git", "-C", gitdir, "fetch", "-q", "origin", ref])
            t.seek(0); t.truncate()
            r = subprocess.run(["git", "-C", gitdir, "cat-file", "-p", f"{ref}:{path}"], stdout=t)
        t.flush()
        return frame(t.name) if r.returncode == 0 else None


def main(out):
    sched = json.load(open(os.path.join(ROOT, "state", "schedule.json")))
    now = datetime.now(timezone.utc)
    synced = sched.get("synced_from_zernio")
    if not synced or now - datetime.strptime(synced[:16], "%Y-%m-%d %H:%M").replace(tzinfo=MT) > timedelta(hours=2):
        sys.exit("state/schedule.json is not freshly synced with Zernio. Pull posts_list_posts and run "
                 "tools/sync_schedule.py first (PLAYBOOK HARD RULE).")
    rows = []
    for s in sched.get("slots", []):
        if s.get("status") != "scheduled" or s.get("platform") == "facebook":
            continue
        local = datetime.strptime(f"{s['date']} {s['scheduled_mt']}", "%Y-%m-%d %H:%M").replace(tzinfo=MT)
        when = local.astimezone(timezone.utc)
        if when < now:
            continue
        media = s.get("live_media") or {}
        tt = media.get("TikTok") or media.get("IG") or media.get("X") or ""
        x = media.get("X")
        plats = [p for p in ("IG", "IG story", "X", "TikTok") if p in media]
        where = " · ".join("IG reel" if p == "IG" else p for p in plats)
        if "TikTok" in media:
            where += " (cover = first frame)"
        pid = next((v for v in (s.get("zernio") or {}).values() if isinstance(v, str)), "")
        rows.append({
            "when": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "when_mt": local.strftime("%a %b %-d · %-I:%M%p").replace("AM", "am").replace("PM", "pm"),
            "slot": "morning" if local.hour < 11 else ("midday" if local.hour < 16 else "evening"),
            "clip": unquote(tt.split("/")[-1]).rsplit(".", 1)[0],
            "caption": s.get("caption", ""),
            "hook": "",
            "where": where,
            "thumb": thumb_for(tt),
            "ig_url": x or tt,
            "full_url": tt,
            "note": "Matches Zernio " + pid,
        })
    rows.sort(key=lambda r: r["when"])
    json.dump(rows, open(out, "w"))
    print(f"{len(rows)} upcoming posts -> {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "upnext.json")
