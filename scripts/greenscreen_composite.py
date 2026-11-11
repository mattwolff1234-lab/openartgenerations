#!/usr/bin/env python3
"""Put an animation (e.g. the laptop dashboard) onto a green laptop screen in a Seedance clip.

How it was done for the Driveway skit: prompt Seedance for an over-the-shoulder shot with a
locked-off camera and "the laptop screen is a perfectly flat, evenly lit, solid chroma-key green
rectangle (pure green #00FF00)... never blocked by his hands or head". Then:

  mkdir rf && ffmpeg -i react.mp4 -vf fps=24 rf/%04d.png
  python3 greenscreen_composite.py --clip-frames rf --anim-frames df --out cf
  # cf/ holds composited frames for the green shot only; splice back with ffmpeg concat:
  ffmpeg -framerate 24 -i cf/%04d.png -i react.mp4 -filter_complex \
    "[0:v]fps=24,format=yuv420p,setsar=1[a];[1:v]trim=start_frame=N,setpts=PTS-STARTPTS,fps=24,format=yuv420p,setsar=1[b];[a][b]concat=n=2:v=1:a=0[v]" \
    -map "[v]" -map 1:a out.mp4        (N = number of composited frames)

Corners are auto-detected from the first frame (pass --corners to override, TL TR BR BL).
Only frames up to the first frame with no green are processed (the shot cut).
"""
import argparse, glob, os
import numpy as np
from PIL import Image, ImageFilter

ap = argparse.ArgumentParser()
ap.add_argument("--clip-frames", required=True)
ap.add_argument("--anim-frames", required=True)
ap.add_argument("--out", default="cf")
ap.add_argument("--corners", help="x,y x,y x,y x,y  (TL TR BR BL)")
ap.add_argument("--pad", type=int, default=4)
a = ap.parse_args()

def green_alpha(arr):
    g = arr[:, :, 1] - np.maximum(arr[:, :, 0], arr[:, :, 2])
    return np.clip((g - 25) / 50, 0, 1)

def detect(arr, pad):
    m = (arr[:, :, 1] > 140) & (arr[:, :, 1] - arr[:, :, 0] > 60) & (arr[:, :, 1] - arr[:, :, 2] > 60)
    ys, xs = np.nonzero(m)
    s, d = xs + ys, xs - ys
    tl = (xs[s.argmin()], ys[s.argmin()]); br = (xs[s.argmax()], ys[s.argmax()])
    tr = (xs[d.argmax()], ys[d.argmax()]); bl = (xs[d.argmin()], ys[d.argmin()])
    return [(tl[0] - pad, tl[1] - pad), (tr[0] + pad, tr[1] - pad), (br[0] + pad, br[1] + pad), (bl[0] - pad, bl[1] + pad)]

def coeffs(dst, src):
    A, B = [], []
    for (x, y), (X, Y) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -X * x, -X * y], [0, 0, 0, x, y, 1, -Y * x, -Y * y]]; B += [X, Y]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()

clip = sorted(glob.glob(os.path.join(a.clip_frames, "*.png")))
anim = sorted(glob.glob(os.path.join(a.anim_frames, "*.png")))
first = np.asarray(Image.open(clip[0]).convert("RGB")).astype(float)
FW, FH = Image.open(clip[0]).size
dst = [tuple(map(float, c.split(","))) for c in a.corners.split()] if a.corners else detect(first, a.pad)
AW, AH = Image.open(anim[0]).size
c = coeffs(dst, [(0, 0), (AW, 0), (AW, AH), (0, AH)])
dm = np.asarray(Image.new("L", (AW, AH), 255).transform((FW, FH), Image.PERSPECTIVE, c, Image.BICUBIC)) / 255.0
os.makedirs(a.out, exist_ok=True)
n = 0
for i, f in enumerate(clip):
    arr = np.asarray(Image.open(f).convert("RGB")).astype(float)
    alpha = green_alpha(arr)
    if (alpha > 0.5).sum() < 2000: break  # shot changed: stop
    d = Image.open(anim[min(i, len(anim) - 1)]).convert("RGB").transform((FW, FH), Image.PERSPECTIVE, c, Image.BICUBIC)
    al = np.asarray(Image.fromarray((alpha * dm * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))) / 255.0
    b = arr.copy(); mx = np.maximum(arr[:, :, 0], arr[:, :, 2])
    b[:, :, 1] = np.where(alpha > 0, np.minimum(arr[:, :, 1], mx + 10), arr[:, :, 1])  # despill
    out = b * (1 - al[..., None]) + np.asarray(d).astype(float) * al[..., None]
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(os.path.join(a.out, f"{i+1:04d}.png")); n += 1
print(f"corners={dst} composited_frames={n}")
