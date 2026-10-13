#!/bin/bash
# usage: render.sh src segs.json "" "" out.mp4
# segs.json = [[start,end,zoom],...]; zoom=1 punches in 15%.
# Single high-quality pass (Quality rules, PLAYBOOK): segments are cut with trim/atrim inside ONE
# ffmpeg run straight from the source -> no pre-encoded intermediates, no double encode.
# libx264 -crf 17 -preset slow, source frame rate kept, 1080x1920 (or the source size if bigger),
# AAC 192k. The hook arguments are ignored: NO text is ever drawn on the video (Mack, Oct 12).
set -e
SRC="$1"; SEGS="$2"; OUT="$5"
if [ -n "$3$4" ]; then echo "render.sh: hook text ignored (no added text on videos)" >&2; fi
FC=$(python3 -I - "$SEGS" "$SRC" <<'PY'
import json,sys,subprocess
s=json.load(open(sys.argv[1]))
p=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height:stream_side_data=rotation','-of','json',sys.argv[2]],capture_output=True,text=True)
st=json.loads(p.stdout)['streams'][0]; w,h=st['width'],st['height']
rot=0
for sd in st.get('side_data_list',[]) or []:
    rot=abs(int(sd.get('rotation',0)))
if rot in (90,270): w,h=h,w
# target: 1080x1920, or the source's size if it is bigger (keep 9:16 portrait)
if h>1920: TW,TH=(w//2)*2,(h//2)*2
else: TW,TH=1080,1920
parts=[];n=len(s)
for i,(a,b,z) in enumerate(s):
    fin = i>0 and abs(s[i-1][1]-a)>0.01
    fout = i<n-1 and abs(s[i+1][0]-b)>0.01
    crop="crop=trunc(iw/1.15/2)*2:trunc(ih/1.15/2)*2," if z==1 else ""
    parts.append(f"[0:v]trim=start={a}:end={b},setpts=PTS-STARTPTS,{crop}scale={TW}:{TH}:flags=lanczos,setsar=1[v{i}]")
    af=[f"atrim=start={a}:end={b}","asetpts=PTS-STARTPTS"]
    if fin: af.append("afade=t=in:d=0.03")
    if fout: af.append(f"afade=t=out:st={round(b-a-0.03,3)}:d=0.03")
    parts.append(f"[0:a]{','.join(af)},aresample=48000[a{i}]")
parts.append("".join(f"[v{i}][a{i}]" for i in range(n))+f"concat=n={n}:v=1:a=1[v][a]")
print(";".join(parts))
PY
)
ffmpeg -nostdin -v error -y -i "$SRC" -filter_complex "$FC" -map "[v]" -map "[a]" \
  -c:v libx264 -crf 17 -preset slow -profile:v high -pix_fmt yuv420p -fps_mode passthrough \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$OUT"
