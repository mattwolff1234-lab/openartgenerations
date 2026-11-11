#!/usr/bin/env python3
"""Render an animated "Insights" dashboard (views + $ earned climbing, green growth line)
as PNG frames sized for a laptop screen, plus a notification-ping audio bed.

Usage:
  python3 laptop_dashboard.py --out dframes --views 1248000 --money 4820 --dur 4.0
Then:  ffmpeg -framerate 24 -i dframes/%04d.png -c:v libx264 -crf 14 -pix_fmt yuv420p dash.mp4
Composite it onto a green screen with greenscreen_composite.py.
Font: Metropolis ExtraBold (in the Higgsfield sandbox at /usr/share/fonts/truetype/higgsfield).
"""
import argparse, math, os, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("--out", default="dframes")
ap.add_argument("--views", type=int, default=1248000)
ap.add_argument("--money", type=int, default=4820)
ap.add_argument("--dur", type=float, default=4.0)
ap.add_argument("--w", type=int, default=840)
ap.add_argument("--h", type=int, default=532)
ap.add_argument("--font", default="/usr/share/fonts/truetype/higgsfield/Metropolis-ExtraBold.ttf")
ap.add_argument("--pings", default="pings.wav")
a = ap.parse_args()
W, H, FPS, DUR = a.w, a.h, 24, a.dur
ft = ImageFont.truetype(a.font, 34); fbig = ImageFont.truetype(a.font, 96)
fmid = ImageFont.truetype(a.font, 50); fsm = ImageFont.truetype(a.font, 26)
os.makedirs(a.out, exist_ok=True)
ease = lambda x: (lambda y: y * y * (3 - 2 * y))(max(0, min(1, x)))
pts = [(i / 79, (i / 79) ** 2.4 * 0.9 + 0.04 + 0.02 * math.sin(i * 1.9) * (i / 79)) for i in range(80)]
for f in range(int(FPS * DUR)):
    t = f / FPS; p = ease((t - 0.15) / (DUR - 0.7))
    im = Image.new("RGB", (W, H), (14, 17, 23)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 58], fill=(22, 26, 34)); d.text((40, 14), "Insights", font=ft, fill=(235, 238, 245))
    for i, c in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]):
        d.ellipse([W - 120 + i * 30, 22, W - 104 + i * 30, 38], fill=c)
    views = int(1204 + (a.views - 1204) * p); money = int(14 + (a.money - 14) * p)
    vs = f"{views/1e6:.1f}M" if views >= 1e6 else (f"{views/1000:.0f}K" if views >= 10000 else f"{views:,}")
    d.text((40, 82), vs, font=fbig, fill=(255, 255, 255)); d.text((44, 186), "views", font=fsm, fill=(150, 160, 175))
    d.text((470, 104), f"${money:,}", font=fmid, fill=(61, 220, 132)); d.text((472, 166), "earned", font=fsm, fill=(150, 160, 175))
    x0, y0, x1, y1 = 40, 236, W - 40, H - 28
    for g in range(4):
        yy = y0 + (y1 - y0) * g / 3; d.line([(x0, yy), (x1, yy)], fill=(40, 47, 58), width=2)
    n = max(2, int(len(pts) * p)); poly = [(x0 + (x1 - x0) * px, y1 - (y1 - y0) * py) for px, py in pts[:n]]
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).polygon(poly + [(poly[-1][0], y1), (poly[0][0], y1)], fill=(61, 220, 132, 55))
    im = Image.alpha_composite(im.convert("RGBA"), lay); d = ImageDraw.Draw(im)
    d.line(poly, fill=(61, 220, 132), width=7, joint="curve"); ex, ey = poly[-1]
    d.ellipse([ex - 10, ey - 10, ex + 10, ey + 10], fill=(61, 220, 132))
    im.convert("RGB").save(f"{a.out}/{f:04d}.png")

# accelerating notification pings + soft rain bed
sr = 48000; N = int(sr * DUR); s = np.zeros(N); tt, gap, times = 0.25, 0.5, []
while tt < DUR - 0.15:
    times.append(tt); tt += gap; gap = max(0.07, gap * 0.8)
k = np.arange(int(sr * 0.18)); env = np.exp(-k / sr * 28)
ping = (np.sin(2 * np.pi * 1568 * k / sr) + 0.5 * np.sin(2 * np.pi * 2349 * k / sr)) * env * 0.22
for x in times:
    i = int(x * sr); L = min(len(ping), N - i); s[i:i + L] += ping[:L]
r = np.cumsum(np.random.default_rng(1).standard_normal(N)); r -= np.convolve(r, np.ones(400) / 400, "same")
s = np.clip(s + r / np.abs(r).max() * 0.03, -1, 1); st = (np.stack([s, s], 1) * 32767).astype(np.int16)
w = wave.open(a.pings, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(st.tobytes()); w.close()
print("wrote", a.out, a.pings)
