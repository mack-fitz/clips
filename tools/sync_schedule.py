#!/usr/bin/env python3
"""Make state/schedule.json match Zernio exactly (HARD RULE: run before ANY dashboard rebuild).

    python3 tools/sync_schedule.py --zernio p1.txt p2.txt [--from 2026-10-05]

Inputs: raw saved outputs of Zernio posts_list_posts (from_date..to_date covering every page, sort scheduled-asc),
the same files tools/check_repeats.py takes. Scope: the accounts this repo runs - @moremackygolfs IG,
@mackygolfs X + TikTok, macky.golfs Facebook. (@mackygolfs / @mackthegolfer IG live in the
mackygolfs-mackthegolfer repo and are not in this file.)

For every slot dated on/after --from that names a Zernio post:
  - Zernio published  -> status "published" (+ posted_mt)
  - Zernio scheduled  -> status "scheduled", date/scheduled_mt/caption/live platforms/media taken from Zernio
  - Zernio draft      -> status "draft"
  - not in Zernio     -> status "removed" (keeps an older removed_* status if it had one)
Zernio posts in scope that no slot names are added as new slots (added_by_sync).
"""
import argparse, json, os, sys, datetime as dt
from zoneinfo import ZoneInfo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_repeats as C

MT = ZoneInfo("America/Denver")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCOPE = {("instagram", "moremackygolfs"), ("twitter", "mackygolfs"), ("tiktok", "mackygolfs"), ("facebook", "macky.golfs")}
NAME = {"instagram": "IG", "twitter": "X", "tiktok": "TikTok", "facebook": "Facebook"}


def load_posts(paths):
    posts = {}
    for p in paths:
        for post in C.load_tool(p)["posts"]:
            plats = []
            for pl in post["platforms"]:
                a = pl["accountId"]
                un = a.get("username") if isinstance(a, dict) else a
                if (pl["platform"], un) not in SCOPE:
                    continue
                st = pl.get("status") or post["status"]
                if post.get("isDraft") or post["status"] == "draft":
                    st = "draft"
                if st in ("failed", "cancelled"):
                    continue
                psd = pl.get("platformSpecificData") or {}
                t = C.parse_t(pl.get("publishedAt") or pl.get("scheduledFor") or post["scheduledFor"]).astimezone(MT)
                media = (pl.get("customMedia") or post.get("mediaItems") or [{}])[0].get("url")
                plats.append({"platform": pl["platform"], "story": psd.get("contentType") == "story",
                              "status": "published" if st == "published" else st, "t": t, "media": media,
                              "url": pl.get("platformPostUrl")})
            if plats:
                posts[post["_id"]] = {"caption": post.get("content", ""), "plats": plats}
    return posts


def live_platform(plats):
    kinds = sorted({p["platform"] for p in plats if not p["story"]})
    if kinds == ["facebook"]:
        return "facebook"
    if kinds == ["instagram"]:
        return "instagram"
    return "x_tiktok" if "instagram" not in kinds else "ig_x_tiktok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zernio", nargs="+", required=True)
    ap.add_argument("--from", dest="since", default="2026-10-05")
    a = ap.parse_args()
    posts = load_posts(a.zernio)
    path = os.path.join(ROOT, "state", "schedule.json")
    d = json.load(open(path))
    named, changes = set(), []
    stamp = dt.datetime.now(MT).strftime("%Y-%m-%d %H:%M MT")
    for s in d["slots"]:
        ids = [v for v in (s.get("zernio") or {}).values() if isinstance(v, str)]
        named.update(ids)
        if s.get("date", "") < a.since or not ids:
            continue
        found = [posts[i] for i in ids if i in posts]
        old = (s.get("status"), s.get("date"), s.get("scheduled_mt"))
        if not found:
            if not str(s.get("status", "")).startswith("removed") and s.get("status") not in ("pulled",):
                s["status"] = "removed"
        else:
            plats = [p for f in found for p in f["plats"]]
            sts = {p["status"] for p in plats}
            t = min(p["t"] for p in plats)
            s["status"] = "draft" if sts == {"draft"} else ("published" if sts == {"published"} else "scheduled")
            s["date"], s["scheduled_mt"] = t.strftime("%Y-%m-%d"), t.strftime("%H:%M")
            s["caption"] = found[0]["caption"]
            s["live_platforms"] = sorted({NAME[p["platform"]] + (" story" if p["story"] else "") for p in plats})
            s["live_media"] = {NAME[p["platform"]] + (" story" if p["story"] else ""): p["media"] for p in plats}
            if s["status"] == "published":
                s["posted_mt"] = t.strftime("%Y-%m-%d %H:%M")
        if (s.get("status"), s.get("date"), s.get("scheduled_mt")) != old:
            s["synced"] = stamp
            changes.append(f"{old} -> {(s.get('status'), s.get('date'), s.get('scheduled_mt'))} {s.get('caption', '')[:40]!r}")
    for pid, post in posts.items():
        if pid in named:
            continue
        plats = post["plats"]
        t = min(p["t"] for p in plats)
        if t.strftime("%Y-%m-%d") < a.since:
            continue
        sts = {p["status"] for p in plats}
        s = {"date": t.strftime("%Y-%m-%d"), "scheduled_mt": t.strftime("%H:%M"),
             "slot": "morning" if t.hour < 11 else ("midday" if t.hour < 16 else "evening"),
             "platform": live_platform(plats), "caption": post["caption"], "zernio": {"post": pid},
             "status": "draft" if sts == {"draft"} else ("published" if sts == {"published"} else "scheduled"),
             "live_platforms": sorted({NAME[p["platform"]] + (" story" if p["story"] else "") for p in plats}),
             "live_media": {NAME[p["platform"]] + (" story" if p["story"] else ""): p["media"] for p in plats},
             "added_by_sync": stamp}
        d["slots"].append(s)
        changes.append(f"added {s['date']} {s['scheduled_mt']} {s['status']} {s['caption'][:40]!r}")
    d["slots"].sort(key=lambda s: (s.get("date", ""), s.get("scheduled_mt", "")))
    d["synced_from_zernio"] = stamp
    json.dump(d, open(path, "w"), indent=1, ensure_ascii=False)
    print("\n".join(changes) or "already in sync")
    print(f"{len(changes)} change(s); schedule.json synced {stamp}")


if __name__ == "__main__":
    main()
