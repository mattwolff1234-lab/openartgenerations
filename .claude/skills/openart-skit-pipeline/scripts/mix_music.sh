#!/usr/bin/env bash
# Mix an instrumental score UNDER the dialogue, plus a no-music version.
# Usage: mix_music.sh raw_cut.mp4 music.mp3 Name_Skit
#
# Levels (tuned after "music too loud at the end" feedback):
# - dialogue leveled to -16 LUFS first (Seedance renders voices quiet and uneven)
# - music bed leveled to -30 LUFS, i.e. ~14 dB under the voice
# - hard sidechain ducking whenever someone speaks
# - an extra -4 dB over the last 8.5s, so the finale fanfare never drowns the CTA
# - whole mix to -14 LUFS for Reels/TikTok
set -euo pipefail
CUT=$1; MUSIC=$2; OUT=$3
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$CUT")
FO=$(python3 -c "print(round($D-1.5,2))")
CTA=$(python3 -c "print(round($D-8.5,2))")
ffmpeg -v error -y -i "$CUT" -i "$MUSIC" -filter_complex \
 "[0:a]loudnorm=I=-16:TP=-2:LRA=11,aresample=48000[v];[v]asplit=2[v1][v2];\
  [1:a]atrim=0:$D,asetpts=PTS-STARTPTS,aresample=48000,loudnorm=I=-30:TP=-9:LRA=11,volume='if(gte(t,$CTA),0.63,1)':eval=frame,afade=t=out:st=$FO:d=1.5[m];\
  [m][v1]sidechaincompress=threshold=0.015:ratio=12:attack=10:release=400[md];\
  [v2][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 "${OUT}.mp4"
ffmpeg -v error -y -i "$CUT" -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 192k -ar 48000 "${OUT}_NoMusic.mp4"
echo "wrote ${OUT}.mp4 and ${OUT}_NoMusic.mp4"
