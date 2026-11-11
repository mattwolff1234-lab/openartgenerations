---
name: openart-skit-pipeline
description: End-to-end pipeline that turns a creator's photos, a chosen story format (6 built in, a different one every video, with the supporting cast auto-generated from the creator's own image) and a few OpenArt screen recordings into a finished ~65s vertical Pixar-style skit (5 clips) that teaches the OpenArt Explainer flow, with burned-in captions, screen-recording cards, an original score and a CTA. Character sheets, sets, music and editing run in Higgsfield; the talking clips render on OpenArt Seedance 2.5 at 1080p. Use when a creator wants a "revenge / glow-up" animated skit for the OpenArt campaign, or says "make my skit", "make the Raghav-style video", "animated story with my character".
---

# OpenArt Skit Pipeline

Photos + topic + screen recordings in, a finished 9:16 skit out (~65s, 5 clips), in rounds the creator approves. Proven on a real run; every gotcha below happened at least once.

**Read `BRIEF_TEMPLATE.md` first and get it filled in.** It front-loads every question so the run can go unattended (overnight) after one approval.

## Running it unattended (overnight)

1. The creator fills in `BRIEF_TEMPLATE.md` completely (budget caps included) and attaches photos + screen recordings.
2. Best: run from a terminal in this repo (`claude`), where `.claude/settings.json` turns on bypass mode so nothing waits on prompts. In the Claude app instead, set the permission mode to **Auto**; a cloud session's network must allow `upload.higgsfield.ai`.
3. Claude runs Stage 1, posts the sheets, and waits for the one "approve". Then it writes the locked script and total cost and waits for the second "approve".
4. After the second approval: render, QA, edit, deliver without further questions. Stay inside the brief's budget caps; if a fix would exceed them, finish everything else and list it as open.

## Tools and where each step runs

| Step | Where | Why |
|---|---|---|
| Character sheets, side cast, sets, props | Higgsfield `generate_image` (`nano_banana_pro`) | Best likeness and layout match |
| Reusable characters | Higgsfield `manage_reference_elements` | For Higgsfield video, if used |
| Talking clips (finals) | OpenArt `byte-plus-seedance-2-5`, `element2video`, 1080p, 9:16, audio on | Best lip-synced dialogue with references |
| Finished explainer payoff | OpenArt `byte-plus-seedance-2-5`, `text2video` | Real-looking explainer on the demo topic |
| Music | Higgsfield `generate_audio`, `elevenlabs_music_v2_5`, `force_instrumental: true` | Original score, timed to the story |
| QA + editing | Higgsfield `sandbox_exec` (ffmpeg, ImageMagick, faster-whisper, Pillow, Metropolis font) | Has internet to both CDNs and all tools |

Run every download, transcode, caption burn and mix **inside the Higgsfield sandbox**. A Claude cloud sandbox usually cannot reach `d8j0ntlcm91z4.cloudfront.net` / `d2ol7oe51mr4n9.cloudfront.net` / `cdn.openart.ai`, and Hugging Face (Whisper models) is often blocked there too.

## Ground rules

- **Approval gates:** get one "yes" on (1) the character sheets, (2) the locked script + total cost. After that, run to the finished cut without stopping unless something fails QA twice. Always report what was spent.
- **Credits:** call Higgsfield `balance` and OpenArt `openart_account_get` before the clip batch. OpenArt Seedance 2.5, 1080p, 9:16, audio on (Nov 2026 prices): **15s = 4,810 · 12s = 3,850 · 10s ≈ 3,210 · 8s = 2,565**. Always re-quote with `openart_model_cost`. Higgsfield images are about 2 credits each (`nano_banana_pro`) or 0.25 (`gpt_image_2_5`); music is a few credits.
- **Originality:** new story, names and lines every time. Reuse only the structure below. Never copy another creator's video.
- **PG-13, no real brands or lookalikes in generated footage.** Real platform logos only as edit overlays (see Stage 6).
- **Campaign rules** (OpenArt): see the Compliance section. They override creative requests unless the creator's coach approves in writing.

## Stage 1. Character

1. **Photos:** 2-6 clear photos (front, three-quarter, side). Upload with `media_upload` → `curl PUT` → `media_confirm`. If the PUT to `upload.higgsfield.ai` is refused by the network, the session's environment needs that host allowed.
2. **Feature list:** write it in plain words (hair texture + cut + fade, face shape, nose, eye colour/shape, brows, facial hair where fuller or faded, skin tone, build, jewellery/watch). Get it confirmed, or let the first sheet confirm it.
3. **Early sheet:** `generate_image`, `model: nano_banana_pro`, `aspect_ratio: 3:2`, the photos as `image_references`, prompt from `prompts/character_sheet.txt`. That labelled layout (FRONT / THREE-QUARTER / SIDE / BACK + NEUTRAL / HAPPY / SURPRISED / TALKING on cream) beats unlabelled turnarounds for likeness. Generate 2 and let the creator pick. Expect the job to report `nano_banana_2`; that's normal.
4. **Later (glow-up) sheet:** same model, the approved early sheet as the only reference, prompt `prompts/character_sheet_later.txt`. Change only outfit + energy (bubbly → calm half-lidded smirk).
5. **Pick the format** from `formats/FORMATS.md` (the creator's choice, or the one they haven't used yet). The format decides the cast, sets, hook prop and reveal. Every video should be a different format.
6. **Auto-cast from the hero:** follow `prompts/cast_from_hero.txt`. Pass the approved hero sheet as the reference and generate one sheet per role in the format's cast list, in one `generate_image_batch`. CONTRAST roles (exes, rivals, bosses) must look clearly unlike the hero and each other. FAMILY roles (parents, cousins) must visibly share the hero's skin tone, eyes, nose and hair colour. The creator only provides their own image; everyone else is generated from it.
7. **Sets (9:16, no people)** from the format's set list, each with a named key light; the lesson office always has the desk, the laptop at one side, a brass lamp, a city window, and the front of the desk clear for overlays. **Hero props** get their own image (e.g. matte-black badge-free car). For a keyed graphic use a background colour that is NOT in the object (a green bill on green screen gets keyed out; use magenta).
8. QA every image in the sandbox with `image_paths` before showing. The first approval covers the hero sheets, cast and sets together.

## Stage 2. Story (5 clips, ~65s)

Fill the chosen format's card (`formats/FORMATS.md`) with new names, lines and a new demo topic. The skeleton below is shared by every format; the table shows F1 (Evicted) as the worked example. Each clip ends on the beat or prop the next one opens on, so it flows:

| # | Len | Beat | Rule |
|---|---|---|---|
| 1 | 15s | **Jarring hook**: a hard physical prop in the first second (fist slams an eviction notice on the door), then the partner leaves and the rival twists the knife with one line. **Ends** on the hero holding the prop. | Heartbreak + money pressure, no violence |
| 2 | 12s | **Grind**: opens with the same prop taped above the desk; montage of making explainers; **ends** by crumpling the prop ("Rent's paid."). | Edit card "6 MONTHS LATER" |
| 3 | 15s | **Reveal**: status flip in front of the doubters (picks up the tab, badge-free car outside), callback to their insult as a one-word comeback, then "How did you...?" → hero to camera "Five steps." | |
| 4 | 15s | **Lesson** at the office desk, 5 steps that match the REAL UI labels (see below). | Screen recordings overlaid in the edit |
| 5 | 8s | **CTA**: comment keyword (and the optional money beat, coach-approved only). | Keyword coloured in captions; `openart.ai/try` on screen |

Steps for clip 4 (confirmed against the live UI, Nov 2026; re-check labels in the creator's recordings):
1. "Go to openart dot A I slash try."
2. "Click Explainer and type what you want to explain." (form field: *What do you want to explain?*)
3. "Add your audience and pick a visual style." (fields: *Who's your audience?*, *Visual style*: Cinematic / Whiteboard / Minimal / Illustrated)
4. "Hit Direct my explainer." (button label: **Direct my explainer**)
5. "Now post."

Write the locked script as a table: clip, set, characters + wardrobe, beat, exact lines spelled as spoken ("openart dot A I slash try", "comment A I"). Spoken lines per 15s clip: about 35 words max.

## Stage 3. Get references into OpenArt

OpenArt video only accepts images hosted on `cdn.openart.ai` with metadata. Per image:
1. `openart_upload_sign` (`mediaType: image`, exact byte `size`, `purpose: create-video`, a `label` such as `Raghav-Early`).
2. From the **Higgsfield sandbox**: download the image, convert it to JPG ≤2000px, then `curl -X PUT -H "Content-Type: image/jpeg" -H "Content-Length: <size>" --data-binary @file "<signURL>"`.
3. `openart_upload_metadata_get` with the `accessURL` + `uploadId` + `label`. Pass the returned `visualReference` **including its `metadata`** into `params.visualReferences` (without it: "Image metadata is required").

## Stage 4. Render the clips

`openart_generate_video_batch`, one item per clip, `model: byte-plus-seedance-2-5`, `mode: element2video`, `duration`, `aspectRatio: 9:16`, `resolution: 1080p`, `generateAudio: true`, `autoEnhancePrompt: false`, references = the character sheet(s) in that clip + the set (+ prop). Put the hero's sheet first. Use the prompt template in `prompts/clip_template.txt`. Key lines that matter:
- "Language: English only." Spell tricky words as spoken.
- "absolutely no background music" (music is added in the edit).
- A STAGING line whenever 3+ people share a space.
- Name a real light source on faces.
- "No subtitles, no on screen text", and any sign or paper: "no readable text" (it will still garble; patch it in the edit).
- Laptop/phone screens: "soft abstract glowing shapes, no interface, no logos".
- For the lesson and CTA clips, copy the exact STAGING from the previous clip (same chair, laptop side, framing) to keep continuity. Even then the laptop can jump sides, so check.

Higgsfield `seedance_2_5` draft mode may be unavailable on the account; when it is, finals cannot inherit a draft. Go straight to 1080p and redo single clips if needed.

## Stage 5. QA (in the Higgsfield sandbox)

```bash
curl -sSf -o c1.mp4 "<openart url>"   # per clip
python3 scripts/transcribe.py c1.mp4 c2.mp4 ...            # word timestamps -> cN.txt
ffmpeg -i c1.mp4 -vf "fps=1,scale=150:-1,tile=8x2" -frames:v 1 g1.jpg   # view with image_paths
```
Check the transcript word for word against the script; check faces, outfits, set, extra people, garbled signs, screen content, continuity between clips. Fix in the edit when possible (free); re-render only what the edit can't fix, and say the cost.

## Stage 6. Edit (Higgsfield sandbox; see `scripts/`)

Copy `scripts/` into the sandbox with a heredoc. The `.filter.example` files contain `#` comment lines, which ffmpeg does not accept, so strip them first: `grep -v '^#' lesson_cards.filter.example > lesson.filter`, then `ffmpeg ... -filter_complex_script lesson.filter`.

1. **Captions on every clip.** `scripts/make_captions.py` (config: `scripts/captions.example.json`) turns whisper word timestamps into ASS: Metropolis (ExtraBold, family name `Metropolis`, `Bold=-1`), size 74, white, thin dark outline + soft shadow, 1-3 words per line, centred at y=1085-1110 of 1920, step numbers start a new line, per-clip word fixes, and a coloured keyword (`{\c&H00D4FF&}AI{\c&HFFFFFF&}` = yellow). Burn with `subtitles=cN.ass:fontsdir=/usr/share/fonts/truetype/higgsfield`.
2. **Garbled prop text:** `drawbox` (fill with the prop's own dark colour) + `drawtext` the correct word, enabled only while the prop is still (find the window from 0.3s frame crops).
3. **Time card:** `drawbox` band + "6 MONTHS LATER" over the first 1.5s of clip 3.
4. **Screen-recording cards in the lesson clip** (rounded, drop shadow, below the captions): see `scripts/lesson_cards.filter.example`. Crop recipes:
   - URL typing: crop only the address-bar row, so no history dropdown or tabs show.
   - Quick Starts → Explainer tile: crop out the browser chrome, the workspace name / top bar and the left sidebar **before the file leaves the creator's machine**.
   - Explainer form: crop the right-hand form panel only; drop the macOS "Record Entire Screen" pill and capture toolbar.
   - Speed each segment so it lands on its spoken step (`setpts=(PTS-STARTPTS)*target/source`).
5. **Finished explainer payoff:** a 10s `text2video` explainer on the same topic the creator typed in the recording (prompt in `prompts/explainer_payoff.txt`), shown as a 9:16 card under step 5, sped up and muted.
6. **Platform icons** (TikTok, YouTube, Facebook, Instagram) from Wikimedia Commons SVGs → `rsvg-convert`, TikTok black recoloured to white. See `scripts/get_logos.sh`. Show them on "post".
7. **CTA:** coloured keyword caption; hold `openart.ai/try` on screen (small pill at the bottom); optional coach-approved money beat (counter filter in `scripts/counter.filter.example`).
8. **Music:** `elevenlabs_music_v2_5`, `force_instrumental: true`, `duration` = cut length + 1s, prompt with one timed section per clip (`prompts/music.txt`). Mix with `scripts/mix_music.sh`: it levels the dialogue first, sets the music about 14 dB under it with hard ducking, and drops it another 4 dB over the CTA so the finale never drowns the last lines. Keep the music quiet: an earlier mix at the same level as the voices was too loud, especially the ending. Always also export a **NoMusic** version.
9. Concat (`-f concat -c copy`; all clips are 1080x1920, 24fps, AAC 48k), `loudnorm I=-14 TP=-1.5`, re-transcribe the final cut to confirm every line is intelligible, check frames at each overlay.

## Stage 7. Deliver

Upload the finals from the sandbox with `media_upload` → `curl PUT --upload-file` → `media_confirm`, and give the creator the links: `Name_Skit_vN.mp4`, `Name_Skit_vN_NoMusic.mp4`, the logo zip. Report credits spent per tool, what was fixed in the edit, and anything still open.

## Compliance (OpenArt campaign)

- Every video sends viewers to **openart.ai/try** only: on screen during the CTA, in the caption and the bio. Say "OpenArt" out loud somewhere (the URL line counts as weak; prefer a clear "Open Art" mention).
- **No fabricated income, no virality or earnings promises.** "Start printing", dollar counters and "viral" are implied income claims. They need the creator's coach to approve in writing; otherwise use a status flip without numbers (car, picking up the tab, "Rent's paid").
- "Comment KEYWORD" only if the creator can actually send that guide.
- Paid-partnership / ad disclosure in the post caption, with wording confirmed with the campaign.
- No fake OpenArt UI in generated footage; real UI appears only via the creator's own screen recordings, cropped for privacy (no workspace names, emails, history, credits).

## Batch mode (several formats for the same creator)

Clips 4 (lesson) and 5 (CTA) are identical in every format, because every reveal ends with the hero saying "Five steps." to camera. Render and edit them once, keep the finished `n4.mp4` / `n5.mp4`, and for each extra format render only clips 1-3 (≈13,500 OpenArt credits instead of ≈20,000). Proven on the overnight Raghav batch (F2, F3, F5).
- OpenArt runs at most **8 videos at once** per plan (`PARALLEL_LIMIT_EXCEEDED`). Submit 8, then submit the rest as slots free up.
- Generate one score per format (the hook mood differs), timed to the same 15/12/15/15/8 boundaries.
- Pre-create the final upload slots (`media_upload` with all final filenames) early. The presigned URLs last 24h, and this also gets every tool approved once while the creator is still awake.
- Names in reveal lines sometimes come out mispronounced ("Raghav" → "Ragge"). If the name matters, avoid putting it in the reveal clip, or spell it phonetically in the prompt (e.g. "Raa-guv").

## Known gotchas

- Instagram/TikTok links can't be downloaded from Claude's sandbox; ask for the .mp4.
- An all-black screen recording means the capture area missed the window. Use Cmd+Shift+5 → Record Selected Portion; if it's still black, turn off Chrome's graphics acceleration.
- Seedance renders signs as near-words ("EVICTION RAGTICE"); plan the patch.
- OpenArt element2video records may list only 2 `inputImages` even when you sent 4; QA the side characters anyway (in the proven run they still came out right).
- Re-quote every OpenArt price; prices are per job and change with duration and resolution.
