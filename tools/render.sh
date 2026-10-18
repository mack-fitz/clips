#!/bin/bash
# usage: render.sh src segs.json "" "" out.mp4
# segs.json = [[start,end,zoom],...]; zoom=1 punches in 15%.
# Single high-quality pass (Quality rules, PLAYBOOK): every segment is its own input of the SAME source
# (-ss/-t accurate seek), cut and concatenated inside ONE ffmpeg run straight from the source ->
# no pre-encoded intermediates, no double encode, and no frame buffering when segments are out of order
# (the old one-input version ran out of memory on restructured edits of long sources, Oct 15).
# libx264 -crf 17 -preset slow, source frame rate kept, 1080x1920 (or the source size if bigger),
# AAC 192k. The hook arguments are ignored: NO text is ever drawn on the video (Mack, Oct 12).
set -e
SRC="$1"; SEGS="$2"; OUT="$5"
if [ -n "$3$4" ]; then echo "render.sh: hook text ignored (no added text on videos)" >&2; fi
mapfile -t ARGS < <(python3 -I - "$SEGS" "$SRC" <<'PY'
import json,sys,subprocess
s=json.load(open(sys.argv[1])); src=sys.argv[2]
p=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height:stream_side_data=rotation','-of','json',src],capture_output=True,text=True)
st=json.loads(p.stdout)['streams'][0]; w,h=st['width'],st['height']
rot=0
for sd in st.get('side_data_list',[]) or []:
    rot=abs(int(sd.get('rotation',0)))
if rot in (90,270): w,h=h,w
if h>1920: TW,TH=(w//2)*2,(h//2)*2
else: TW,TH=1080,1920
parts=[];n=len(s);args=[]
for i,(a,b,z) in enumerate(s):
    args += ['-ss',f'{a:.3f}','-t',f'{b-a:.3f}','-i',src]
    fin = i>0 and abs(s[i-1][1]-a)>0.01
    fout = i<n-1 and abs(s[i+1][0]-b)>0.01
    crop="crop=trunc(iw/1.15/2)*2:trunc(ih/1.15/2)*2," if z==1 else ""
    parts.append(f"[{i}:v]setpts=PTS-STARTPTS,{crop}scale={TW}:{TH}:flags=lanczos,setsar=1[v{i}]")
    af=["asetpts=PTS-STARTPTS"]
    if fin: af.append("afade=t=in:d=0.03")
    if fout: af.append(f"afade=t=out:st={round(b-a-0.03,3)}:d=0.03")
    parts.append(f"[{i}:a]{','.join(af)},aresample=48000[a{i}]")
parts.append("".join(f"[v{i}][a{i}]" for i in range(n))+f"concat=n={n}:v=1:a=1[v][a]")
for x in args: print(x)
print("-filter_complex"); print(";".join(parts))
PY
)
# VMAXRATE (optional, e.g. 8M): cap the crf-17 video so the file stays under GitHub raw's 100 MiB
# limit (media is served from raw.githubusercontent.com). Still one pass from the source.
CAP=(); if [ -n "$VMAXRATE" ]; then CAP=(-maxrate "$VMAXRATE" -bufsize "${VBUFSIZE:-$VMAXRATE}"); fi
# LEVEL (optional, e.g. 4.1): IG reels must be H.264 High@4.1 <=5 Mbps (Oct 17 transcoding failure) ->
# render IG edits with VMAXRATE=4.8M VBUFSIZE=9.6M LEVEL=4.1 so the single export is already IG-safe.
if [ -n "$LEVEL" ]; then CAP+=(-level:v "$LEVEL"); fi
ffmpeg -nostdin -v error -y "${ARGS[@]}" -map "[v]" -map "[a]" \
  -c:v libx264 -crf 17 "${CAP[@]}" -preset slow -profile:v high -pix_fmt yuv420p -fps_mode passthrough \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$OUT"
