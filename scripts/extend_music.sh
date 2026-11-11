#!/usr/bin/env bash
# Lengthen a score when the cut grows, without changing tempo: keep the start and the ending,
# repeat a middle section with a 2s crossfade.
# Usage: extend_music.sh in.mp3 out.mp3 KEEP_HEAD_SEC RESUME_FROM_SEC
# Example (66s score -> 76s): extend_music.sh music_dw.mp3 music_dw3.mp3 42 30
set -euo pipefail
ffmpeg -nostdin -v error -y -i "$1" -filter_complex \
 "[0:a]atrim=0:$3,asetpts=PTS-STARTPTS[a];[0:a]atrim=$4,asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d=2[m]" \
 -map "[m]" "$2"
