#!/usr/bin/env bash
# Platform icons for the "post everywhere" beat (edit overlay only, never in generated footage).
# Produces transparent PNGs + icons_row.png (920 px wide) in ./logos
set -euo pipefail
mkdir -p logos && cd logos
UA="Mozilla/5.0 (compatible; skit-edit/1.0)"
curl -sSfL -A "$UA" -o tiktok.svg    "https://upload.wikimedia.org/wikipedia/en/a/a9/TikTok_logo.svg"
curl -sSfL -A "$UA" -o youtube.svg   "https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg"
curl -sSfL -A "$UA" -o facebook.svg  "https://upload.wikimedia.org/wikipedia/commons/b/b9/2023_Facebook_icon.svg"
curl -sSfL -A "$UA" -o instagram.svg "https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg"
for f in tiktok youtube facebook instagram; do rsvg-convert -h 400 $f.svg -o $f.png; done
# TikTok file is the wordmark: keep the note icon and make its black core white (readable on dark scenes).
convert tiktok.png -crop 380x400+0+0 +repage -channel RGB -fuzz 25% -fill white -opaque black +channel tiktok.png
for f in tiktok youtube facebook instagram; do convert $f.png -resize x150 -background none -gravity center -extent 170x150 i_$f.png; done
convert i_tiktok.png i_youtube.png i_facebook.png i_instagram.png -background none +append -resize 920x icons_row.png
echo "logos/icons_row.png ready"
