#!/usr/bin/env python3
"""Source inventory + rotation ledger (Mack, Oct 19: rotate through ALL clips, least-recently-used first).

    python3 tools/inventory.py --zernio p1.txt p2.txt --analytics an_*.txt [--md out.md] [--free 2026-10-22T07:40-06:00 ...]

Writes state/inventory.json: for every unique source video in /Golf Captions + /golfclips
  files, trip (shirt/day/place), last appearance in ANY version on ANY account (incl. TikTok and Mack's
  own posts), last appearance per account, next scheduled appearance, posted_ever.
--free T...: for each time T, list the sources that may be the main clip of a post at T on a pool account
  (no pool appearance within the guard window, 30 days, either side), least-recently-used first. Use it to pick footage.
Inputs are the same raw Zernio outputs check_repeats.py takes. Mack's older own posts come from the
mackygolfs-mackthegolfer state/posted_index.json fingerprint matches.
"""
import argparse, json, os, sys, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_repeats as C

CLIPS = C.CLIPS
# shirt / day / place per source (from the compilation spacing notes + review notes; "?" = not confirmed)
TRIP = {
    "Video Oct 12 2026, 7 13 58 AM.mov": "Texas: Amarillo (white shirt, camo hat)",
    "Video Oct 12 2026, 7 16 02 AM.mov": "Texas: Amarillo (white shirt, camo hat)",
    "Video Oct 12 2026, 7 17 58 AM.mov": "Texas: Amarillo (white shirt, camo hat)",
    "Video Oct 12 2026, 7 19 40 AM.mov": "Texas: Amarillo (white shirt, camo hat)",
    "Video Oct 12 2026, 7 26 20 AM.mov": "Texas: Amarillo (white shirt, camo hat)",
    "Video Oct 12 2026, 12 03 20 AM.mov": "Texas: San Angelo (green pinstripe, Bad hat)",
    "Video Oct 12 2026, 12 11 12 AM.mov": "Texas: San Angelo (green)",
    "Video Oct 12 2026, 7 30 44 AM.mov": "Texas: San Angelo (olive, cactus day)",
    "Video Oct 12 2026, 12 05 56 AM.mov": "Texas trip? (green)",
    "Video Oct 12 2026, 12 14 03 AM.mov": "Texas trip? (green)",
    "Video Oct 12 2026, 12 17 30 AM.mov": "green polo day (Texas?)",
    "Video Oct 12 2026, 12 22 39 AM.mov": "green polo day (Texas?)",
    "Video Oct 12 2026, 12 00 30 AM.mov": "rain day (blue striped polo)",
    "Video Oct 12 2026, 7 33 50 AM.mov": "light blue print day",
    "Video Oct 12 2026, 7 34 47 AM.mov": "bandana day",
    "Video Oct 12 2026, 7 35 57 AM.mov": "Colorado (black shirt, sunset par 3)",
    "Video Oct 11 2026, 9 02 57 AM (1).mp4": "Colorado (orange checker)",
    "Video Oct 11 2026, 9 02 57 AM (2).mp4": "Colorado (orange checker)",
    "Video Oct 11 2026, 9 02 57 AM (3).mp4": "Colorado (orange checker)",
    "Video Oct 11 2026, 9 02 57 AM.mp4": "Colorado (orange checker)",
    "Video Sep 21 2026, 7 09 34 PM.mov": "Colorado, Sep 21 (red Hawaiian shirt)",
    "Video Sep 21 2026, 7 12 01 PM.mov": "Colorado, Sep 21 (red Hawaiian shirt)",
    "Video Sep 21 2026, 7 24 34 PM.mov": "Colorado, Sep 21 (red Hawaiian shirt)",
    "Video Sep 21 2026, 7 28 37 PM.mov": "Colorado, Sep 21 (red Hawaiian shirt)",
    "Video Sep 21 2026, 7 31 40 PM.mov": "Colorado, Sep 21 (red Hawaiian shirt)",
    "Video Sep 23 2026, 1 04 53 PM.mov": "Colorado, Sep 23 (red Hawaiian shirt)",
    "Video Sep 23 2026, 1 07 33 PM.mov": "Colorado, Sep 23 (red Hawaiian shirt)",
}
GOLFCLIPS_TRIP = "golfclips batch (Aug-Sep, uploaded Oct 12)"


def history_from_index():
    """Mack's own older posts (fingerprint matches in posted_index.json) -> list of (source, account, time, caption)."""
    out = []
    p = os.path.join(C.MG, "state", "posted_index.json")
    if not os.path.exists(p):
        return out
    d = json.load(open(p))
    for s in d.get("sources", []):
        for m in s.get("matches", []):
            try:
                t = dt.datetime.strptime(m["date_mt"][:16].replace("~", ""), "%Y-%m-%d %H:%M") + dt.timedelta(hours=6)
            except ValueError:
                t = dt.datetime.strptime(m["date_mt"][:10], "%Y-%m-%d") + dt.timedelta(hours=18)
            out.append((s["name"], "ig:" + m["account"], t.replace(tzinfo=dt.timezone.utc), m.get("caption"), m.get("platformPostUrl")))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zernio", nargs="+", required=True)
    ap.add_argument("--analytics", nargs="*", default=[])
    ap.add_argument("--md")
    ap.add_argument("--free", nargs="*", default=[])
    a = ap.parse_args()
    now = dt.datetime.now(dt.timezone.utc)
    mmap = json.load(open(os.path.join(CLIPS, "state", "media_sources.json")))["media"]
    cat = json.load(open(os.path.join(CLIPS, "state", "sources.json")))["sources"]
    from build_media_map import canon_map
    cmap = canon_map()
    uses, _ = C.zernio_uses(a.zernio, mmap)
    ext, _ = C.external_uses(a.analytics, now - dt.timedelta(days=60)) if a.analytics else ([], [])
    uses += ext
    ev = []  # (source, account, t, status, caption, ref, main?)
    for u in uses:
        if u.status == "draft":
            continue
        for s in u.sources:
            ev.append((s, u.account, u.t, u.status, u.caption, u.post_id, s == u.main, u.kind))
    for name, acc, t, cap, url in history_from_index():
        sid = cmap.get(name)
        if sid:
            ev.append((sid, acc, t, "published", cap, url, True, "original"))
    inv = {}
    for sid, e in cat.items():
        mine = [x for x in ev if x[0] == sid]
        past = sorted([x for x in mine if x[2] <= now and (x[7] != "comp" or x[6]) and x[7] != "shorty"], key=lambda x: x[2])
        bits = sorted([x for x in mine if x[2] <= now and x[7] in ("comp", "shorty") and not (x[7] == "comp" and x[6])], key=lambda x: x[2])
        fut = sorted([x for x in mine if x[2] > now and (x[7] != "comp" or x[6]) and x[7] != "shorty"], key=lambda x: x[2])
        per = {}
        for x in past:
            per[x[1]] = C.mt(x[2])
        last = past[-1] if past else None
        lead = [x for x in past if x[6] and x[7] not in ("shorty",)]  # appearances as the main clip
        inv[sid] = {
            "files": e["files"],
            "trip": TRIP.get(sid, GOLFCLIPS_TRIP if any(f.startswith("/golfclips/") for f in e["files"]) else "?"),
            "posted_ever": bool(past),
            "last_any": {"when": C.mt(last[2]), "account": last[1], "caption": (last[4] or "")[:60], "kind": last[7]} if last else None,
            "last_any_iso": last[2].isoformat() if last else None,
            "last_as_main_iso": lead[-1][2].isoformat() if lead else None,
            "last_per_account": per,
            "next_scheduled": [{"when": C.mt(x[2]), "account": x[1], "caption": (x[4] or "")[:50]} for x in fut],
            "last_bit_or_shorty": {"when": C.mt(bits[-1][2]), "account": bits[-1][1], "kind": bits[-1][7]} if bits else None,
            "clip_pages_only": bool(e.get("clip_pages_only")),
            "times_used_14d": len([x for x in past if now - x[2] < dt.timedelta(days=14) and x[1] in C.POOL]),
        }
    json.dump({"updated": now.isoformat(), "note": "Built by tools/inventory.py. last_any = any version on any account (originals, re-edits, comp LEADS; TikTok + Mack's own posts included). Comp bits and shorties are listed separately (last_bit_or_shorty).",
               "sources": inv}, open(os.path.join(CLIPS, "state", "inventory.json"), "w"), indent=1)
    order = sorted(inv, key=lambda s: inv[s]["last_any_iso"] or "")
    if a.md:
        L = ["| # | clip (folder/file) | trip / shirt | last posted (any version, any account) | where | next scheduled |", "|---|---|---|---|---|---|"]
        for i, s in enumerate(order, 1):
            v = inv[s]
            la = v["last_any"]
            L.append(f"| {i} | {' = '.join(v['files'])} | {v['trip']} | {la['when'] if la else 'never'} | "
                     f"{(la['account'] + ' ' + repr(la['caption'])) if la else ''} | "
                     f"{'; '.join(x['when'] + ' ' + x['account'] for x in v['next_scheduled'][:2])} |")
        # Main-account rotation: /Golf Captions ONLY (HARD RULE 12). Least recently on @mackygolfs/@mackthegolfer first.
        gc = [s for s in inv if any(f.startswith("/Golf Captions/") for f in inv[s]["files"])]
        def last_pool(s):
            hits = [x for x in ev if x[0] == s and x[1] in C.POOL and x[2] <= now and x[6] and x[7] not in ("shorty", "story")]
            return max(hits, key=lambda x: x[2]) if hits else None
        def next_pool(s):
            hits = [x for x in ev if x[0] == s and x[1] in C.POOL and x[2] > now and x[6] and x[7] not in ("shorty", "story")]
            return min(hits, key=lambda x: x[2]) if hits else None
        rot = sorted(gc, key=lambda s: (last_pool(s)[2].isoformat() if last_pool(s) else ""))
        R = ["", f"## Main-account rotation (@mackygolfs / @mackthegolfer): /Golf Captions only, {len(rot)} videos",
             "Least recently used on either main account first. /golfclips-only footage is never listed here (HARD RULE 12);",
             "a twin that also exists in /Golf Captions is listed by its /Golf Captions file. Drafts don't count as scheduled.", "",
             "| # | /Golf Captions file | trip / shirt | last on @mackygolfs/@mackthegolfer | next scheduled there | eligible again (30-day rule) |", "|---|---|---|---|---|---|"]
        for i, s in enumerate(rot, 1):
            lp, np_ = last_pool(s), next_pool(s)
            R.append(f"| {i} | {' = '.join(f for f in inv[s]['files'] if f.startswith('/Golf Captions/'))} | {inv[s]['trip']} | "
                     f"{(C.mt(lp[2]) + ' ' + lp[1] + ' ' + repr((lp[4] or '')[:40])) if lp else 'never'} | "
                     f"{(C.mt(np_[2]) + ' ' + np_[1]) if np_ else ''} | "
                     f"{C.mt((np_ or lp)[2] + C.WINDOW) if (np_ or lp) else 'now'} |")
        open(a.md, "w").write("\n".join(L + R) + "\n")
    for T in a.free:
        t = C.parse_t(T)
        ok = []
        for s in order:
            if cat.get(s, {}).get("clip_pages_only"):
                continue  # HARD RULE 12: /golfclips-only footage is never offered to the main accounts
            near = [x for x in ev if x[0] == s and x[1] in C.POOL and abs(x[2] - t) < C.WEEK and x[7] not in ("shorty", "story")
                    and x[7] != "comp"]  # comps + shorties exempt (Mack, Oct 19 final)
            if not near:
                ok.append(s)
        print(f"FREE at {C.mt(t)} ({len(ok)}): " + " | ".join(f"{s} [{(inv[s]['last_any'] or {}).get('when', 'never')}]" for s in ok))
    print(f"{len(inv)} sources; never posted: {sum(1 for v in inv.values() if not v['posted_ever'])}")


if __name__ == "__main__":
    main()
