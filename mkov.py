#!/usr/bin/env python3
# Overlay graphics for the mulligan promos: top_<y>.png (transparent, 1080x1920) and endcard.png
import sys, os
from PIL import Image, ImageDraw, ImageFont
FONT = "/tmp/claude-0/-home-claude/1d9eeb67-4425-509b-9799-b9746fe458c6/scratchpad/tt/poppins900.ttf"
OUT = os.path.dirname(os.path.abspath(__file__)) + "/ov"
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1920
RED = (227, 30, 36, 255)

def text_c(d, cx, y, s, size, stroke, fill=(255, 255, 255, 255)):
    f = ImageFont.truetype(FONT, size)
    b = d.textbbox((0, 0), s, font=f, stroke_width=stroke)
    w = b[2] - b[0]
    d.text((cx - w / 2 - b[0], y - b[1]), s, font=f, fill=fill, stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
    return b[3] - b[1]

def box_c(d, cx, y, s, size, padx=28, pady=14, stroke=6):
    f = ImageFont.truetype(FONT, size)
    b = d.textbbox((0, 0), s, font=f)
    w, h = b[2] - b[0], b[3] - b[1]
    x0, y0, x1, y1 = cx - w / 2 - padx, y, cx + w / 2 + padx, y + h + 2 * pady
    d.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=RED, outline=(0, 0, 0, 255), width=stroke)
    d.text((cx - w / 2 - b[0], y0 + pady - b[1]), s, font=f, fill=(255, 255, 255, 255))
    return y1 - y0

def top(y0, name):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx = 500  # shifted left of centre: clear of the right-edge buttons (x > ~950)
    h = text_c(d, cx, y0, "MULLIGAN EVERY HOLE", 76, 9)
    bh = box_c(d, cx, y0 + h + 22, "CAN I BREAK 50?", 62)
    im.save(f"{OUT}/{name}.png")
    bb = im.getbbox(); print(name, "ink bbox", bb)

def endcard():
    im = Image.new("RGBA", (W, H), (255, 214, 10, 255)); d = ImageDraw.Draw(im)
    for k in range(-H, W + H, 90):  # diagonal stripes
        d.polygon([(k, 0), (k + 45, 0), (k + 45 - H, H), (k - H, H)], fill=(247, 190, 0, 255))
    cx = W / 2; y = 360
    for line in ["CAN I", "BREAK 50", "WITH A", "MULLIGAN", "ON EVERY", "HOLE?"]:
        y += text_c(d, cx, y, line, 128, 12) + 40
    y += 40
    y += box_c(d, cx, y, "NEW VIDEO", 92, padx=34, pady=18, stroke=8) + 40
    box_c(d, cx, y, "ON YOUTUBE", 92, padx=34, pady=18, stroke=8)
    im.convert("RGB").save(f"{OUT}/endcard.png"); print("endcard ink to", y + 150)

for y in (int(a) for a in sys.argv[1:] or ["230"]):
    top(y, f"top_{y}")
endcard()
