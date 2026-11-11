#!/usr/bin/env python3
"""Word-timestamp transcripts for each clip: c1.mp4 -> c1.txt.

Usage (Higgsfield sandbox, faster-whisper preinstalled):
    python3 transcribe.py c1.mp4 c2.mp4 c3.mp4 ...
Output lines:
    [start-end] segment text
      W start end word
"""
import sys
from pathlib import Path
from faster_whisper import WhisperModel

model = WhisperModel("small", compute_type="int8")
for clip in sys.argv[1:]:
    segs, _ = model.transcribe(clip, word_timestamps=True, language="en")
    out = Path(clip).with_suffix(".txt")
    with open(out, "w") as f:
        for s in segs:
            f.write(f"[{s.start:5.2f}-{s.end:5.2f}] {s.text}\n")
            for w in s.words:
                f.write(f"  W {w.start:.2f} {w.end:.2f} {w.word.strip()}\n")
    print(out, "written")
