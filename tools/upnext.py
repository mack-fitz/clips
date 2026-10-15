#!/usr/bin/env python3
"""Build the dashboard's "Up next" file: every scheduled post that hasn't gone out yet.

Usage: python3 tools/upnext.py out.json
Reads state/schedule.json; uses the slot's "file" (e.g. queue/<clip>_v2.mp4) and its
matching _cover.jpg when present, else queue/<clip>.mp4 and queue/<clip>_cover.jpg. Each row gets a small cover thumbnail
(data URI) so the dashboard can show it without loading anything from another site.
"""
import base64, json, subprocess, sys, tempfile, os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

MT = ZoneInfo("America/Denver")
RAW = "https://raw.githubusercontent.com/mack-fitz/clips/main/"


def thumb(path, width=240):
    if not os.path.exists(path):
        return None
    with tempfile.NamedTemporaryFile(suffix=".jpg") as t:
        subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", path,
                        "-vf", f"scale={width}:-2", "-q:v", "5", t.name], check=True)
        return "data:image/jpeg;base64," + base64.b64encode(open(t.name, "rb").read()).decode()


def main(out):
    sched = json.load(open("state/schedule.json"))
    now = datetime.now(timezone.utc)
    rows = []
    for s in sched.get("slots", []):
        if s.get("status") not in ("scheduled", "fixed"):
            continue
        local = datetime.strptime(f"{s['date']} {s['scheduled_mt']}", "%Y-%m-%d %H:%M").replace(tzinfo=MT)
        when = local.astimezone(timezone.utc)
        if when < now:
            continue
        if s.get("platform") == "facebook" or "clip" not in s:
            continue  # Facebook Page posts live on Facebook Stats / Base Camp, not this list
        clip = s["clip"]
        video = s.get("file") or f"queue/{clip}.mp4"
        cover = video[:-4] + "_cover.jpg"
        if not os.path.exists(cover):
            cover = f"queue/{clip}_cover.jpg"
        rows.append({
            "when": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "when_mt": local.strftime("%a %b %-d · %-I:%M%p").replace("AM", "am").replace("PM", "pm"),
            "slot": s.get("slot", ""),
            "clip": clip,
            "caption": s.get("caption", ""),
            "hook": s.get("hook", ""),
            "where": "IG reel + story · X · TikTok",
            "thumb": thumb(cover),
            "ig_url": RAW + video,
            "full_url": RAW + (s.get("tiktok_file") or f"queue/{clip}_full.mp4"),
            "note": s.get("note", ""),
        })
    rows.sort(key=lambda r: r["when"])
    json.dump(rows, open(out, "w"))
    print(f"{len(rows)} upcoming posts -> {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "upnext.json")
