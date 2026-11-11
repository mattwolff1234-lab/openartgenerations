#!/usr/bin/env python3
"""Build reel-style ASS captions (1-3 words, mid-frame) from cN.txt word timestamps.

Usage:
    python3 make_captions.py captions.json
captions.json example:
{
  "font": "Metropolis", "size": 74, "y": 1100,
  "highlight_color": "&H00D4FF&",            # ASS BGR, this one = yellow
  "clips": [
    {"name": "c1", "duration": 15.07},
    {"name": "c2", "duration": 12.06, "replace": {"rents": "Rent's"}},
    {"name": "c4", "duration": 15.07, "y": 1085,
     "merge": [["openart", ".ai", "-slash", "-try", "openart.ai/try"],
               ["click", "explainer", "Click Explainer"]],
     "replace": {"direct": "Direct"}},
    {"name": "c5", "duration": 8.06, "highlight": ["AI"]}
  ]
}
- "replace": case-insensitive whole-word swaps (fix whisper spellings/brand casing).
- "merge": consecutive whisper tokens collapsed into one display token (last item = text).
- "highlight": words drawn in highlight_color and 115% size.
- Step numbers like "2." always start a new caption line.
Burn with: -vf "subtitles=c1.ass:fontsdir=/usr/share/fonts/truetype/higgsfield"
"""
import json, re, sys

cfg = json.load(open(sys.argv[1]))
FONT = cfg.get("font", "Metropolis")
SIZE = cfg.get("size", 74)
HL = cfg.get("highlight_color", "&H00D4FF&")
NUM = re.compile(r"\d\.")


def words(name):
    ws = []
    for line in open(f"{name}.txt"):
        if line.startswith("  W"):
            _, s, e, w = line.split(None, 3)
            ws.append([float(s), float(e), w.strip()])
    return ws


def apply_fixes(ws, clip):
    merges = clip.get("merge", [])
    rep = {k.lower(): v for k, v in clip.get("replace", {}).items()}
    out, k = [], 0
    while k < len(ws):
        done = False
        for m in merges:
            seq, text = [t.lower().rstrip(",.!?") for t in m[:-1]], m[-1]
            if [w[2].lower().rstrip(",.!?") for w in ws[k:k + len(seq)]] == seq:
                out.append([ws[k][0], ws[k + len(seq) - 1][1], text])
                k += len(seq)
                done = True
                break
        if done:
            continue
        s, e, w = ws[k]
        core = w.rstrip(".,!?")
        tail = w[len(core):]
        if core.lower() in rep:
            new = rep[core.lower()]
            # a replacement that brings its own punctuation replaces the old punctuation
            w = new if re.search(r"[.,!?]$", new) else new + tail
        out.append([s, e, w])
        k += 1
    return out


def group(ws):
    gs, cur = [], []
    for x in ws:
        if NUM.fullmatch(x[2]) and cur:
            gs.append(cur)
            cur = []
        cur.append(x)
        end_punct = bool(re.search(r"[.,!?]$", x[2])) and not NUM.fullmatch(x[2])
        if len(cur) >= 3 or end_punct or len(" ".join(c[2] for c in cur)) > 16:
            gs.append(cur)
            cur = []
    if cur:
        gs.append(cur)
    return gs


def ts(t):
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def render_word(w, hl):
    core = w.rstrip(".,!?")
    if core in hl:
        return "{\\c%s\\fscx115\\fscy115}%s{\\c&HFFFFFF&\\fscx100\\fscy100}%s" % (HL, core, w[len(core):])
    return w


HDR = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{FONT},{SIZE},&H00FFFFFF,&H00FFFFFF,&H80000000,&H64000000,-1,0,0,0,100,100,0,0,1,2,3,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

for clip in cfg["clips"]:
    name, dur = clip["name"], clip["duration"]
    y = clip.get("y", cfg.get("y", 1100))
    hl = set(clip.get("highlight", []))
    gs = group(apply_fixes(words(name), clip))
    ev = []
    for n, g in enumerate(gs):
        st = g[0][0]
        en = gs[n + 1][0][0] if n + 1 < len(gs) else min(dur, g[-1][1] + 0.5)
        en = min(en, g[-1][1] + 0.6) if n + 1 < len(gs) else en
        txt = " ".join(render_word(w[2], hl) for w in g)
        ev.append(f"Dialogue: 0,{ts(st)},{ts(en)},Cap,,0,0,0,,{{\\pos(540,{y})}}{txt}")
    open(f"{name}.ass", "w").write(HDR + "\n".join(ev) + "\n")
    print(name, [" ".join(w[2] for w in g) for g in gs])
