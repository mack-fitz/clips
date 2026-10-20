#!/usr/bin/env python3
"""Edit planner for @moremackygolfs re-edits (PLAYBOOK: never cut shots or swearing; cut only dead air / walking /
waiting / pauses between sentences; never mid-word).

    python3 tools/autoplan.py <source video> <transcript.json> [--pre 2.2] [--post 5.0] [--pad 0.15] [--gap 0.6]

Prints:
  strikes  : ball-contact transients (sharp high-frequency onsets) -> each one is kept from `pre` s before
             (address + backswing) to `post` s after (flight / tracer to landing; widen per shot after looking).
  keep     : union of every spoken word (+pad) and every strike window; gaps shorter than `gap` are kept too.
  cut %    : how much dead air the keep list removes (target 25-40 % for @moremackygolfs).
Writes <source>.plan.json {strikes, keep, words} next to the transcript for the segment file.
Always check the strikes on a contact sheet: putts are quiet (add them by hand), claps/cart bumps can fire.
"""
import argparse, json, subprocess, sys
import numpy as np


def audio(src, sr=16000):
    raw = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", src, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                         capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0, sr


def strikes(x, sr):
    hop = sr // 100  # 10 ms
    # high-pass by first difference (emphasises clicks / ball contact over voice and wind)
    d = np.diff(x, prepend=0)
    n = len(d) // hop
    e = np.sqrt((d[:n * hop].reshape(n, hop) ** 2).mean(axis=1)) + 1e-6
    out = []
    for i in range(5, n - 5):
        lo = max(0, i - 100)
        med = np.median(e[lo:i + 100])
        if e[i] > 9 * med and e[i] >= e[i - 3:i + 4].max() and e[i] > 0.01 and e[i] > 2.5 * e[i - 4]:
            t = i / 100
            if not out or t - out[-1][0] > 1.5:
                out.append([round(t, 2), round(float(e[i] / med), 1)])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("transcript")
    ap.add_argument("--pre", type=float, default=2.2); ap.add_argument("--post", type=float, default=5.0)
    ap.add_argument("--pad", type=float, default=0.15); ap.add_argument("--gap", type=float, default=0.6)
    a = ap.parse_args()
    x, sr = audio(a.src)
    dur = len(x) / sr
    st = strikes(x, sr)
    tr = json.load(open(a.transcript))
    ws = [[w[0], w[1], w[2]] for s in tr["segments"] for w in (s.get("words") or [])]
    iv = [[max(0, w[0] - a.pad), min(dur, w[1] + a.pad)] for w in ws]
    iv += [[max(0, t - a.pre), min(dur, t + a.post)] for t, _ in st]
    iv.sort()
    keep = []
    for s, e in iv:
        if keep and s - keep[-1][1] < a.gap:
            keep[-1][1] = max(keep[-1][1], e)
        else:
            keep.append([s, e])
    kept = sum(e - s for s, e in keep)
    print(f"duration {dur:.1f}s  words {len(ws)}  strikes {len(st)}: {st}")
    print(f"keep {kept:.1f}s ({100 * kept / dur:.0f} %), cut {100 - 100 * kept / dur:.0f} %")
    for s, e in keep:
        txt = " ".join(w[2].strip() for w in ws if w[0] >= s - 0.01 and w[1] <= e + 0.01)
        print(f"  {s:6.2f}-{e:6.2f} ({e - s:4.1f}s) {txt[:110]}")
    json.dump({"duration": dur, "strikes": st, "keep": [[round(s, 2), round(e, 2)] for s, e in keep]},
              open(a.transcript.replace(".json", "") + ".plan.json", "w"), indent=1)


if __name__ == "__main__":
    main()
