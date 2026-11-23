#!/usr/bin/env python3
# compose.py <cut.mp4> <out.mp4> <pos list e.g. "low,top,top,..."> <seg durations json list>
# Burns the top-line text per segment (top = y 230, low = y 1250 for close-ups), appends the 2.5 s end card
# with room tone from the quietest gap of the LAST segment (+ crossfade from the last line's tail), one CRF-17 encode.
import sys, json, subprocess, numpy as np, os
src, out, pos, durs = sys.argv[1], sys.argv[2], sys.argv[3].split(","), json.loads(sys.argv[4])
D = os.path.dirname(os.path.abspath(__file__)); OV = D + "/ov"
tmp = out + ".tmp"; os.makedirs(tmp, exist_ok=True)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src], capture_output=True, text=True).stdout)
# segment windows on the clip timeline
edges = [0.0]
for d in durs: edges.append(edges[-1] + d)
edges[-1] = dur
def en(kind):
    w = [f"between(t,{edges[i]:.3f},{edges[i+1]:.3f})" for i, p in enumerate(pos) if p == kind]
    return "+".join(w) if w else "0"
# room tone: quietest 0.4 s inside the last segment (clip audio), tiled with 60 ms crossfades to 2.7 s
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", src, "-vn", "-ac", "2", "-ar", "48000", "-f", "f32le", f"{tmp}/a.raw"], check=True)
a = np.fromfile(f"{tmp}/a.raw", dtype=np.float32).reshape(-1, 2)
sr = 48000; L = int(0.4 * sr); s0 = int(edges[-2] * sr); s1 = len(a) - L
best, bi = None, s0
for k in range(s0, max(s0 + 1, s1), 480):
    v = float(np.sqrt((a[k:k + L] ** 2).mean() + 1e-12))
    if best is None or v < best: best, bi = v, k
piece = a[bi:bi + L].copy(); xf = int(0.06 * sr); ramp = np.linspace(0, 1, xf)[:, None]
tone = piece.copy()
while len(tone) < int(2.7 * sr):
    t2 = piece.copy(); tone[-xf:] = tone[-xf:] * (1 - ramp) + t2[:xf] * ramp; tone = np.concatenate([tone, t2[xf:]])
tone = tone[:int(2.6 * sr)]
fo = int(1.0 * sr); tone[-fo:] *= np.linspace(1, 0, fo)[:, None]
tone.astype(np.float32).tofile(f"{tmp}/tone.raw")
if len(sys.argv) > 5 and sys.argv[5] == "pct":  # pick a typical-ambience window (30th percentile), not near-silence
    ks = list(range(s0, max(s0 + 1, s1), 480)); vs = [float(np.sqrt((a[k:k + L] ** 2).mean() + 1e-12)) for k in ks]
    tgt = np.percentile(vs, 30); j = int(np.argmin([abs(v - tgt) for v in vs])); bi, best = ks[j], vs[j]
    piece = a[bi:bi + L].copy(); tone = piece.copy()
    while len(tone) < int(2.7 * sr):
        t2 = piece.copy(); tone[-xf:] = tone[-xf:] * (1 - ramp) + t2[:xf] * ramp; tone = np.concatenate([tone, t2[xf:]])
    tone = tone[:int(2.6 * sr)]; tone[-fo:] *= np.linspace(1, 0, fo)[:, None]; tone.astype(np.float32).tofile(f"{tmp}/tone.raw")
if len(sys.argv) > 5 and sys.argv[5].startswith("at="):  # explicit clean gap: at=<clip seconds>:<gain dB>
    t0, gdb = map(float, sys.argv[5][3:].split(":")); bi = int(t0 * sr); piece = a[bi:bi + L].copy() * (10 ** (gdb / 20))
    best = float(np.sqrt((piece ** 2).mean() + 1e-12)); tone = piece.copy()
    while len(tone) < int(2.7 * sr):
        t2 = piece.copy(); tone[-xf:] = tone[-xf:] * (1 - ramp) + t2[:xf] * ramp; tone = np.concatenate([tone, t2[xf:]])
    tone = tone[:int(2.6 * sr)]; tone[-fo:] *= np.linspace(1, 0, fo)[:, None]; tone.astype(np.float32).tofile(f"{tmp}/tone.raw")
print(f"room tone from clip t={bi/sr:.2f}s rms={20*np.log10(best):.1f} dB")
fc = (f"[0:v][1:v]overlay=0:0:enable='{en('top')}'[v1];[v1][2:v]overlay=0:0:enable='{en('low')}',fps=30,format=yuv420p,setsar=1[a];"
      f"[3:v]fps=30,format=yuv420p,setsar=1[e];[a][e]concat=n=2:v=1:a=0[v];"
      f"[0:a]aresample=48000,aformat=channel_layouts=stereo[aa];[4:a]aformat=channel_layouts=stereo[tt];"
      f"[aa][tt]acrossfade=d=0.10:c1=tri:c2=tri,atrim=0:{dur+2.5:.3f}[au]")
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", src, "-i", f"{OV}/top_230.png", "-i", f"{OV}/top_1250.png",
                "-loop", "1", "-framerate", "30", "-t", "2.5", "-i", f"{OV}/endcard.png",
                "-f", "f32le", "-ar", "48000", "-ac", "2", "-i", f"{tmp}/tone.raw",
                "-filter_complex", fc, "-map", "[v]", "-map", "[au]",
                "-c:v", "libx264", "-profile:v", "high", "-level", "4.2", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
                "-maxrate", "25M", "-bufsize", "50M",
                "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
                "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-movflags", "+faststart", out], check=True)
print(out, subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip())
