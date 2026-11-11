# Media bundle

Every file from the Higgsfield editing sandbox (393 files, ~1.4 GB), minus frame-by-frame PNG folders that scripts regenerate. Split into 3 tars that unpack into the same tree:

| Part | URL | SHA-256 |
|---|---|---|
| 1 | https://d2ol7oe51mr4n9.cloudfront.net/user_3Kn2gmXeWEZVSCnsDtwLIgqwM2S/eeedaf59-1e80-4d57-8a8f-cdacfabb311e.tar | 60f3923172a14b3d03bdd28cce87ab098342f0dfd3e0a48fca55d09e984c985f |
| 2 | https://d2ol7oe51mr4n9.cloudfront.net/user_3Kn2gmXeWEZVSCnsDtwLIgqwM2S/031b2e1a-5ad4-4654-ba70-469967ce39f0.tar | c6a2acdb0e2882abc8350c00cf848da6f4d801d5f6330fe8b67cc4ebdc9066e5 |
| 3 | https://d2ol7oe51mr4n9.cloudfront.net/user_3Kn2gmXeWEZVSCnsDtwLIgqwM2S/4584566b-2421-46fb-b224-3dc0eb8add84.tar | 3eb32db1f522340b2751dbd9acd529fcbdab332b3bc1cebecb834f6fdb63345a |

On your machine: `./scripts/fetch_media.sh` (puts everything in `media/`, which git ignores).
In the Higgsfield sandbox (to restore `~/cut` for editing): curl the 3 URLs into `~` and `tar -xf` each one there.

`MEDIA_FILES.txt` lists every file and which part it's in.

## What's where

- `cut/final_*.mp4`: finished videos. `final_dw3` = Driveway v2 (latest), `final_dw2` = Driveway v1, `final_f2` Fired, `final_f3` Family Dinner, `final_f5` Stood Up (each with `_nm` no-music). `cut_v1..v3` = Evicted versions; `q_<id>.mp4` = the quieter remixes that were delivered.
- `cut/c1..c5.mp4`: raw Seedance clips for Evicted. `f2a/b/c`, `f3a/b/c`, `f5a/b/c`, `dwa/b/c`, `dwr`: raw clips per format (a = hook, b = grind, c = reveal, dwr = laptop reaction). Matching `.txt` = Whisper word timestamps, `.ass` = captions.
- `cut/n_*.mp4`: captioned clips ready to concat. **`n4.mp4` (lesson with screen-recording cards) and `n5.mp4` (CTA with $ counter and "Comment AI") are shared by every video.**
- `cut/music*.mp3`: scores (`music_dw.mp3` 66s, `music_dw3.mp3` extended to 76s).
- `cut/lap/`: Driveway laptop scene (`react.mp4` raw green-screen clip, `dash.mp4` dashboard, `plate.png` laptop close-up plate, `comp.py`/`dash.py`).
- `cut/*.sh`, `*.py`: the exact build scripts used (`build.sh` per-format build, `builddw.sh`/`buildr.sh` Driveway, `mix2.sh` current mix, `mkcap.py` captions, `tx2.py` transcription, `money.py` $ counter, `graph.py` insights card).
- `cut/tab.mp4`, `try.mp4`, `tile.mp4`, `form.mp4`, `expl.mp4`: cropped screen recordings and the water-cycle explainer payoff.
- `oa/`, `ov/`, `dw/`, `fam/`: character sheets and sets (Raghav early/later, Priya, Brandon, Boss-Dana, Tyler, Zara, Mom, Dad, Cousin, Hank; all sets). `logos/`: platform logos. `qa/`: QA contact sheets.
