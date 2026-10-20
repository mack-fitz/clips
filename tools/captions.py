#!/usr/bin/env python3
"""Burned-in captions in Mack's /Golf Captions style (PLAYBOOK "CAPTION STYLE (Oct 20)").

    python3 tools/captions.py transcript.json segs.json out.ass [--skip a-b ...] [--fix fixes.json] [--y 1532] [--print]

transcript.json : word-timestamped transcript of the SOURCE (state/ingest/transcripts/<name>.json or the
                  mackygolfs-mackthegolfer transcribe workflow format: segments[].words = [start, end, word]).
segs.json       : the edit's segments [[start, end, zoom], ...] in output order (same file render.sh takes).
                  Use [[0, duration, 0]] for an uncut original.
--skip a-b      : SOURCE time spans with no captions (shirt wipe: never text over her chest / bra).
--fix           : JSON {"wrong phrase": "right phrase", ...} applied to the joined caption text (golf terms etc.).

Style (measured from Mack's own captioned videos, Oct 20): white Inter SemiBold 46 px on a 1080x1920 frame, black
outline 3 px, no box, no shadow, centred, bottom of the block at y 1532 (single line ink ~1478-1530 = 77-80 % down,
low in the frame), max 2 lines of <= 26 characters, shown only while she talks, phrase by phrase, snapped to word
timestamps. Lower-case like hers except "I"/"I'm"/"I've" and names; numbers as digits; no full stops/commas; swears
kept, spelled the way she spells them in her own captions (f*ck, f*cking, sh*t, b*tch, p*ssy).
"""
import argparse, json, re

NAMES = {"mack": "Mack", "macky": "Macky", "texas": "Texas", "amarillo": "Amarillo", "san": "San", "angelo": "Angelo",
         "colorado": "Colorado", "lucy": "Lucy", "goosey": "Goosey", "lpga": "LPGA", "pga": "PGA", "tiktok": "TikTok",
         "instagram": "Instagram", "youtube": "YouTube", "titleist": "Titleist", "callaway": "Callaway"}
SWEARS = [(r"\bfuck", "f*ck"), (r"\bshit", "sh*t"), (r"\bbitch", "b*tch"), (r"\bpussy", "p*ssy")]
GOLF_FIX = {  # common faster-whisper misses on golf talk
    r"\bpar three\b": "par 3", r"\bpar four\b": "par 4", r"\bpar five\b": "par 5", r"\bpar for\b": "par 4",
    r"\bbirdy\b": "birdie", r"\bbogie\b": "bogey", r"\bbogies\b": "bogeys", r"\bdouble bogie\b": "double bogey",
    r"\bfare way\b": "fairway", r"\bfairways\b": "fairways", r"\bpin seeker\b": "pin seeker", r"\bt box\b": "tee box",
    r"\btee shirt\b": "tee shot", r"\bbreak a hundred\b": "break 100", r"\bbreak one hundred\b": "break 100",
    r"\bhole in one\b": "hole in one", r"\bchip in\b": "chip in", r"\bshank\b": "shank", r"\bmulligan\b": "mulligan",
}
MAXL, GAP = 26, 0.45


def words(tr):
    out = []
    for s in tr["segments"]:
        for w in s.get("words") or []:
            t = w[2].strip()
            if t:
                out.append([float(w[0]), float(w[1]), t])
    return out


def clean(text, fixes):
    t = " " + text.lower() + " "
    t = re.sub(r"[.,!;:\"“”]", "", t)
    t = t.replace("…", "")
    for k, v in GOLF_FIX.items():
        t = re.sub(k, v, t)
    for k, v in (fixes or {}).items():
        t = re.sub(r"\b" + re.escape(k.lower()) + r"\b", v, t)
    for k, v in SWEARS:
        t = re.sub(k, v, t)
    t = re.sub(r"\bi\b", "I", t)
    t = re.sub(r"\bi'(m|ve|ll|d)\b", lambda m: "I'" + m.group(1), t)
    t = " ".join(NAMES.get(w, w) for w in t.split())
    return t.strip()


def wrap(t):
    ws, lines, cur = t.split(), [], ""
    for w in ws:
        if cur and len(cur) + 1 + len(w) > MAXL:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    if len(lines) == 2 and len(lines[1]) <= 6 and len(lines[0]) + len(lines[1]) + 1 <= MAXL + 6:
        return [lines[0] + " " + lines[1]] if len(lines[0]) + len(lines[1]) + 1 <= MAXL + 4 else lines
    return lines


def chunks(ws):
    """phrases: break on pauses, sentence ends, or when 2 lines would overflow."""
    out, cur = [], []
    for w in ws:
        if cur:
            gap = w[0] - cur[-1][1]
            txt = " ".join(x[2] for x in cur + [w])
            end = re.search(r"[.?!]$", cur[-1][2])
            if gap > GAP or end or len(txt) > 2 * MAXL - 4 or (w[1] - cur[0][0]) > 3.2:
                out.append(cur); cur = []
        cur.append(w)
    if cur:
        out.append(cur)
    return out


def to_out(t, segs):
    """source time -> list of output times (a source moment can appear once per segment containing it)."""
    res, off = [], 0.0
    for a, b, _ in segs:
        if a - 1e-3 <= t <= b + 1e-3:
            res.append(off + (t - a))
        off += b - a
    return res


def ts(x):
    x = max(0, x)
    return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"


def build(tr, segs, skip, fixes, y):
    events = []
    off = 0.0
    for a, b, _ in segs:
        ws = [w for w in words(tr) if w[0] >= a - 0.05 and w[1] <= b + 0.15 and not any(s0 <= (w[0] + w[1]) / 2 <= s1 for s0, s1 in skip)]
        for c in chunks(ws):
            st = off + max(c[0][0], a) - a
            en = off + min(c[-1][1] + 0.15, b) - a
            txt = clean(" ".join(x[2] for x in c), fixes)
            if txt and en - st > 0.12:
                events.append([st, en, txt])
        off += b - a
    # no flicker: extend each caption to the next one when the gap is short; minimum 0.6 s on screen
    events.sort()
    for i, e in enumerate(events):
        nxt = events[i + 1][0] if i + 1 < len(events) else e[1] + 0.6
        if nxt - e[1] < 0.3:
            e[1] = nxt
        if e[1] - e[0] < 0.6:
            e[1] = min(e[0] + 0.6, nxt)
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Mack,Inter SemiBold,46,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,3,0,2,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [f"Dialogue: 0,{ts(s)},{ts(e)},Mack,,0,0,0,,{{\\an2\\pos(540,{y})}}" + "\\N".join(wrap(t)) for s, e, t in events]
    return head + "\n".join(lines) + "\n", events


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript"); ap.add_argument("segs"); ap.add_argument("out")
    ap.add_argument("--skip", nargs="*", default=[])
    ap.add_argument("--fix")
    ap.add_argument("--y", type=int, default=1532)
    ap.add_argument("--print", action="store_true")
    a = ap.parse_args()
    tr = json.load(open(a.transcript))
    segs = json.load(open(a.segs))
    skip = [tuple(float(x) for x in s.split("-")) for s in a.skip]
    fixes = json.load(open(a.fix)) if a.fix else {}
    ass, ev = build(tr, segs, skip, fixes, a.y)
    open(a.out, "w").write(ass)
    if a.print:
        for s, e, t in ev:
            print(f"{s:6.2f}-{e:6.2f}  {' / '.join(wrap(t))}")
    print(f"{len(ev)} captions -> {a.out}")


if __name__ == "__main__":
    main()
