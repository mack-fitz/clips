#!/usr/bin/env python3
"""Build state/sources.json (one entry per UNIQUE source video) and state/media_sources.json
(every media file we post -> which source videos it contains) for tools/check_repeats.py.

Run from anywhere; needs both repos side by side:
    /home/claude/clips  and  /home/claude/mackygolfs-mackthegolfer
    python3 tools/build_media_map.py

Sources = ONLY Dropbox /Golf Captions + /golfclips (Mack's rule). Files that are the same video
(byte-identical twins, alt takes of the same hole) share one source id. Fingerprint groupings are
in ALIASES below (checked Oct 19 with tools/match_fp.py over every pair of source fingerprints).

Media -> source comes from, in order:
  1. clips repo clip numbers (processed.json clip_map + CLIP_SRC below), tt_/xt_ exports, stories
  2. mackygolfs-mackthegolfer state/trials.json (each reel's name + every file under it)
  3. compilation bit lists (compilations/comp*_bits.json, newest round wins) -> every bit's source,
     main = first bit (the opening clip)
  4. shorties/<slug>_notes.md (source file named in the notes)
  5. inbox/videos/<original name>
  6. MANUAL below (anything else, e.g. fingerprint-resolved trials)
Anything not resolved is listed as UNKNOWN; check_repeats.py refuses to pass a post with unknown media.
When you make a new edit/comp/shorty, add it (MANUAL or the normal state files) and re-run this.
"""
import json, os, re, glob

CLIPS = "/home/claude/clips"
MG = "/home/claude/mackygolfs-mackthegolfer"

# Source id = Dropbox file name of the canonical copy (Golf Captions name when there is one).
GC = "/Golf Captions/"
GCL = "/golfclips/"
ALIASES = {
    # byte-identical twins (same size + content in both folders)
    "Video Oct 11 2026, 9 02 57 AM (2).mp4": [GCL + "Video Aug 27 2026, 5 43 32 PM.MP4"],
    "Video Oct 11 2026, 9 02 57 AM (3).mp4": [GCL + "Video Aug 27 2026, 5 49 54 PM.MP4"],
    "Video Oct 11 2026, 9 02 57 AM.mp4": [GCL + "Video Aug 27 2026, 5 51 18 PM.MP4"],
    # alt takes of the same hole (fingerprint: 22.7 s audio + 26 s frames / 19.4 s + 14 s)
    "Video Oct 12 2026, 7 33 50 AM.mov": [GC + "Video Oct 12 2026, 7 38 06 AM.mov"],
    "Video Oct 12 2026, 7 35 57 AM.mov": [GC + "Video Oct 12 2026, 7 37 01 AM.mov"],
}
GOLFCLIPS_ONLY = ["IMG_6394.MP4", "copy_A526847D-927A-4E66-BA6A-83EF27833CEC.MOV",
                  "copy_99A28E54-DA4E-4AD6-956C-A4CC7A3C4FC1.MOV", "copy_292850AB-28FF-4896-87F6-BAE3D3750515.MOV",
                  "0cef0458001241e4b2c974c97174e51f.MOV", "copy_2A97DD30-DDC0-49D9-8870-4C269E760E1D.MOV",
                  "17ad39c4cb414ab3a7e6618492d7c7a3.MOV", "copy_4E5F508B-EA57-40DF-AC16-CF253290B923.MOV",
                  "copy_0B6BFBE5-2F81-487A-9544-B2C587E0EE74.MOV", "copy_2CC073A6-0417-450E-A364-BDCE638A2D66.MOV",
                  "copy_6FFD8A7C-C1C6-458D-A2EE-21B81C660A11.MOV", "IMG_6391.MP4"]

# clips repo clip number -> source id
CLIP_SRC = {
    "001": "Video Oct 11 2026, 9 02 57 AM (1).mp4",   # chat upload Video_Aug_27_5_44_55 = this file
    "002": "copy_2CC073A6-0417-450E-A364-BDCE638A2D66.MOV",
    "003": "copy_0B6BFBE5-2F81-487A-9544-B2C587E0EE74.MOV",
    "004": "17ad39c4cb414ab3a7e6618492d7c7a3.MOV",
    "005": "0cef0458001241e4b2c974c97174e51f.MOV",
    "006": "copy_2A97DD30-DDC0-49D9-8870-4C269E760E1D.MOV",
    "007": "IMG_6391.MP4",
    "008": "IMG_6394.MP4",
    "009": "Video Oct 11 2026, 9 02 57 AM (2).mp4",
    "010": "Video Oct 11 2026, 9 02 57 AM (3).mp4",
    "011": "Video Oct 11 2026, 9 02 57 AM.mp4",
    "012": "copy_292850AB-28FF-4896-87F6-BAE3D3750515.MOV",
    "013": "copy_4E5F508B-EA57-40DF-AC16-CF253290B923.MOV",
    "014": "copy_6FFD8A7C-C1C6-458D-A2EE-21B81C660A11.MOV",
    "015": "copy_99A28E54-DA4E-4AD6-956C-A4CC7A3C4FC1.MOV",
    "016": "copy_A526847D-927A-4E66-BA6A-83EF27833CEC.MOV",
    "017": "Video Oct 12 2026, 7 19 40 AM.mov",
    "018": "Video Oct 12 2026, 7 13 58 AM.mov",
    "019": "Video Oct 12 2026, 7 16 02 AM.mov",
    "020": "Video Oct 12 2026, 12 17 30 AM.mov",
    "021": "Video Oct 12 2026, 12 22 39 AM.mov",
}
TT_SRC = {  # clips/queue/tt_* and xt_* (uncut originals for X/TikTok)
    "cactus": "Video Oct 12 2026, 7 30 44 AM.mov",
    "hole-in-one-loading": "Video Oct 12 2026, 12 14 03 AM.mov",
    "hot-dog": "Video Sep 21 2026, 7 28 37 PM.mov",
    "lock-it-in": "Video Oct 12 2026, 7 17 58 AM.mov",
    "pond-par-3": "Video Sep 21 2026, 7 12 01 PM.mov",
    "six-months": "Video Oct 12 2026, 7 26 20 AM.mov",
    "pent-bogey": "Video Sep 21 2026, 7 24 34 PM.mov",
}
# Resolved by fingerprint (tools/match_fp.py vs state/fp/repo, Oct 19) / review notes (repo:path -> source id or list; first = main)
MANUAL = {
    "mackygolfs-mackthegolfer:trials/036_san-angelo-wipe-open_a.mp4": "Video Oct 12 2026, 12 03 20 AM.mov",  # fp 125.5 s
    "mackygolfs-mackthegolfer:trials/037_guess-my-score-wipe_a.mp4": "Video Oct 12 2026, 12 05 56 AM.mov",
    "mackygolfs-mackthegolfer:trials/038_handicap-par-5-wipe_a.mp4": "Video Oct 12 2026, 7 33 50 AM.mov",
    "mackygolfs-mackthegolfer:trials/041_cart-path-wipe_a.mp4": "Video Oct 12 2026, 7 16 02 AM.mov",
    "mackygolfs-mackthegolfer:trials/019_beach-day-par-4_b.mp4": "copy_2CC073A6-0417-450E-A364-BDCE638A2D66.MOV",
    "mackygolfs-mackthegolfer:trials/043_king-of-the-world-wipe_a.mp4": "Video Oct 11 2026, 9 02 57 AM.mp4",  # review card: orange-checker king-of-the-world par 4
    "mackygolfs-mackthegolfer:trials/044_san-angelo-lesson-wipe_a.mp4": "Video Oct 12 2026, 12 03 20 AM.mov",
    "mackygolfs-mackthegolfer:trials/045_hole-in-one-attempt-wipe_a.mp4": "copy_99A28E54-DA4E-4AD6-956C-A4CC7A3C4FC1.MOV",
    "mackygolfs-mackthegolfer:trials/046_one-swing-pond-par-3_b.mp4": "copy_2A97DD30-DDC0-49D9-8870-4C269E760E1D.MOV",
    "mackygolfs-mackthegolfer:trials/047_reverse-round-driver-putter_b.mp4": "Video Oct 11 2026, 9 02 57 AM (3).mp4",
    "mackygolfs-mackthegolfer:trials/048_guess-my-score-par-3-wipe_a.mp4": "copy_0B6BFBE5-2F81-487A-9544-B2C587E0EE74.MOV",
    "mackygolfs-mackthegolfer:trials/049_kids-par-4-talk-first_b.mp4": "copy_2CC073A6-0417-450E-A364-BDCE638A2D66.MOV",
    "mackygolfs-mackthegolfer:trials/050_help-my-swing-talk-first_b.mp4": "copy_A526847D-927A-4E66-BA6A-83EF27833CEC.MOV",
    "mackygolfs-mackthegolfer:trials/051_cliff-par-5-talk-first_b.mp4": "copy_4E5F508B-EA57-40DF-AC16-CF253290B923.MOV",
}
OVERRIDES_FILE = os.path.join(CLIPS, "state", "media_manual.json")  # optional extra MANUAL entries


def canon_map():
    """every known file name -> source id"""
    m = {}
    meta = json.load(open(os.path.join(MG, "state/fp/sources_meta.json")))["files"]
    gc_names = [n for n in meta if not n.startswith(("Golf", "Final", "golfclips/"))]
    for n in gc_names:
        m[n] = n
    for n in GOLFCLIPS_ONLY:
        m[n] = n
    for sid, others in ALIASES.items():
        for o in others:
            m[os.path.basename(o)] = sid
    return m


def sources_catalog(cmap):
    cat = {}
    for name, sid in cmap.items():
        e = cat.setdefault(sid, {"files": []})
        folder = GCL if (name in GOLFCLIPS_ONLY or name.startswith("Video Aug 27")) else GC
        e["files"].append(folder + name)
    for e in cat.values():
        e["files"] = sorted(set(e["files"]))
    return cat


def add(media, key, srcs, kind, note=""):
    srcs = [s for s in srcs if s]
    if not srcs:
        return
    seen = []
    for s in srcs:
        if s not in seen:
            seen.append(s)
    media[key] = {"sources": seen, "main": seen[0], "kind": kind}
    if note:
        media[key]["note"] = note


def build():
    cmap = canon_map()
    canon = lambda n: cmap.get(os.path.basename(n.replace(".partNN", "")), None)
    media = {}
    # 1. clips repo
    import subprocess
    hist = subprocess.run(["git", "-C", CLIPS, "log", "--all", "--name-only", "--format=", "--", "queue", "stories"],
                          capture_output=True, text=True).stdout.split()
    qfiles = sorted({h.split("/", 1)[1] for h in hist if h.startswith("queue/")} | set(os.listdir(os.path.join(CLIPS, "queue"))))
    sfiles = sorted({h.split("/", 1)[1] for h in hist if h.startswith("stories/")} | set(os.listdir(os.path.join(CLIPS, "stories"))))
    for f in qfiles:
        m = re.match(r"(\d{3})_", f)
        if m and m.group(1) in CLIP_SRC:
            add(media, "clips:queue/" + f, [CLIP_SRC[m.group(1)]], "original" if re.search(r"_(full|orig|x|xshort)\.", f) else "edit")
        m = re.match(r"(?:tt|xt)_(.+?)_(x|xshort)\.mp4$", f)
        if m and m.group(1) in TT_SRC:
            add(media, "clips:queue/" + f, [TT_SRC[m.group(1)]], "original")
    for f in sfiles:
        m = re.match(r"story_(\d{3})", f)
        if m and m.group(1) in CLIP_SRC:
            add(media, "clips:stories/" + f, [CLIP_SRC[m.group(1)]], "story")
    # 2. trials.json
    t = json.load(open(os.path.join(MG, "state/trials.json")))["reels"]
    for k, v in t.items():
        sid = canon(v.get("name") or "")
        if not sid:
            m = re.search(r"(Video [A-Z][a-z]{2} \d+ 2026, [\d ]+[AP]M(?: \(\d\))?\.(?:mov|mp4|MOV|MP4))", json.dumps(v))
            sid = canon(m.group(1)) if m else None
        if not sid:
            continue
        for f in set(re.findall(r"trials/[A-Za-z0-9_.-]+\.mp4", json.dumps(v))):
            add(media, "mackygolfs-mackthegolfer:" + f, [sid], "edit")
    # 3. compilations
    comp_dir = os.path.join(MG, "compilations")
    bits = {}
    for bf in glob.glob(os.path.join(comp_dir, "comp*_bits.json")):
        b = os.path.basename(bf)[:-len("_bits.json")]  # comp7_r5 / comp13
        m = re.match(r"(comp[^_]+)(?:_(r\d+))?$", b)
        if not m:
            continue
        try:
            d = json.load(open(bf))
        except Exception:
            continue
        lst = d if isinstance(d, list) else d.get("bits") or []
        srcs = [canon(x.get("src") or x.get("source") or "") for x in lst if isinstance(x, dict)]
        bits[(m.group(1), m.group(2) or "r1")] = [s for s in srcs if s]
    for f in sorted(os.listdir(comp_dir)):
        if not f.endswith(".mp4"):
            continue
        m = re.match(r"(comp[^_]+)_[a-z0-9-]+?(?:_(r\d+))?\.mp4$", f)
        if not m:
            continue
        comp, rnd = m.group(1), m.group(2) or "r1"
        cands = sorted([k for k in bits if k[0] == comp], key=lambda k: int(k[1][1:]))
        pick = [k for k in cands if k[1] == rnd] or [k for k in cands if int(k[1][1:]) <= int(rnd[1:])][-1:] or cands[-1:]
        if pick:
            add(media, "mackygolfs-mackthegolfer:compilations/" + f, bits[pick[0]], "comp")
    # comps without bit lists: parse the notes table (source column)
    for nf in glob.glob(os.path.join(comp_dir, "comp*_notes.md")):
        comp = os.path.basename(nf)[:-len("_notes.md")]
        txt = open(nf).read()
        srcs = []
        for line in txt.splitlines():
            if line.startswith("|") and ("Video" in line or "queue/" in line):
                m = re.search(r"(Video [A-Z][a-z]{2} \d+ 2026, [\d ]+[AP]M(?: \(\d\))?\.(?:mov|mp4|MOV|MP4))", line)
                q = re.search(r"queue/(\d{3})_", line)
                srcs.append(canon(m.group(1)) if m else (CLIP_SRC.get(q.group(1)) if q else None))
        srcs = [s for s in srcs if s]
        if srcs:
            for f in os.listdir(comp_dir):
                if f.startswith(comp + "_") and f.endswith(".mp4") and "mackygolfs-mackthegolfer:compilations/" + f not in media:
                    add(media, "mackygolfs-mackthegolfer:compilations/" + f, srcs, "comp", "from notes table")
    # 4. shorties
    sh = os.path.join(MG, "shorties")
    for nf in glob.glob(os.path.join(sh, "*_notes.md")):
        slug = os.path.basename(nf)[:-len("_notes.md")]
        txt = open(nf).read()
        m = re.search(r"(Video [A-Z][a-z]{2} \d+ 2026, [\d ]+[AP]M(?: \(\d\))?\.(?:mov|mp4|MOV|MP4))", txt)
        q = re.search(r"queue/(\d{3})_", txt)
        sid = canon(m.group(1)) if m else (CLIP_SRC.get(q.group(1)) if q else None)
        for f in os.listdir(sh):
            if f.startswith(slug) and f.endswith(".mp4") and (f == slug + ".mp4" or f[len(slug)] == "_"):
                add(media, "mackygolfs-mackthegolfer:shorties/" + f, [sid], "shorty")
    # 5. originals in inbox/videos (and parts)
    for name, sid in cmap.items():
        add(media, "mackygolfs-mackthegolfer:inbox/videos/" + name, [sid], "original")
    # 6. manual
    manual = dict(MANUAL)
    if os.path.exists(OVERRIDES_FILE):
        manual.update(json.load(open(OVERRIDES_FILE)))
    for k, v in manual.items():
        srcs = v if isinstance(v, list) else [v]
        kind = media.get(k, {}).get("kind") or ("comp" if "compilations/" in k else "shorty" if "shorties/" in k else "edit")
        add(media, k, srcs, kind, "manual")
    return sources_catalog(cmap), media


if __name__ == "__main__":
    cat, media = build()
    json.dump({"note": "Unique source videos (Dropbox /Golf Captions + /golfclips). Built by tools/build_media_map.py.",
               "count": len(cat), "sources": cat}, open(os.path.join(CLIPS, "state/sources.json"), "w"), indent=1)
    json.dump({"note": "media file (repo:path) -> source videos in it; main = opening clip. Built by tools/build_media_map.py.",
               "media": media}, open(os.path.join(CLIPS, "state/media_sources.json"), "w"), indent=1)
    print(f"sources: {len(cat)}  media files mapped: {len(media)}")
