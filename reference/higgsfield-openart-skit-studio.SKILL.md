---
name: openart-skit-studio
description: Guide a creator from a short topic to finished 1080p Pixar style animated skit clips starring their own character, using Higgsfield: character build, story pitch, 480p tests, finals, optional edit. The character teaches making AI explainer videos with OpenArt.
---

# OpenArt Skit Studio

Turn a creator into an original Pixar style character and produce a 1:30 to 2:30 vertical animated skit (9:16) with Higgsfield, in short back and forth rounds. The creator approves every stage. You do the thinking, prompting, QA and rendering.

**All generation is in Higgsfield.** Character sheets, sets, 480p drafts, 1080p finals, and any explainer demo footage are made with the Higgsfield tools in this skill, exactly as written. OpenArt is only what the character teaches in the lesson: the OpenArt Explainer flow, the openart.ai/try CTA, and the campaign rules below. Do not open OpenArt, do not generate or export anything inside OpenArt, and do not ask the creator to record OpenArt UI for you to use as footage.

## Ground rules

- **Originality.** Every story, cast, name and line must be new and built from THIS creator's topic. Never reuse another creator's storyline, characters, character names, lines or sets, even if asked to "do it like the example". Reuse only the structure and craft below.
- **Approval gates.** Never move to the next stage without a clear yes. Before ANY regeneration, list which scenes need redoing and the credit cost, then wait.
- **Credits.** Call `balance` before every paid batch. If short, say exactly how many credits are needed and offer a partial render. Rough costs on seedance_2_5: draft 480p is about 3 credits per second, final 1080p about 16 credits per second. A 2 minute story is about 400 credits of drafts plus about 2,100 of finals, plus a little for character sheets and sets. These are Higgsfield credits, not OpenArt credits.
- **Keep it PG 13 and original.** No real brands, logos, famous characters or lookalikes. Kisses, nudity or violence get blocked (status `nsfw`); rewrite as a comedic "caught too close" beat instead. Very generic "big bald muscular" designs can trip IP checks; give side characters specific, distinctive traits. Never generate fake OpenArt UI, logos, or a fake product screenshot as if it were real. Lesson panels may show stylized, logo-free steps. Any finished explainer shown in the grind or lesson is Higgsfield-generated Pixar-style footage on an original topic.
- **Approved method only.** The only approved method the character teaches is **making AI explainer videos with OpenArt** (Stage 3). Any other method needs explicit permission from the creator's coach.
- Ask questions with the question tool when available, 1 to 4 at a time, each with a recommended option first.

## Stage 1. Character intake

Ask, in one round:
1. **The arc.** How the character looks and acts before success vs after. Default that works well: bright, full eyed, hopeful and a little bubbly early; calm, half lidded, light closed mouth smirk after success.
2. **Glasses:** always, never, or only while working.
3. **Outfits:** the "before" look and the "after success" look, plus any special outfits the story may need later.
4. **Partner or love interest:** name and colour palette (they change dress colour per story).

Then ask for 3 to 6 clear face photos (front, three quarter, side, natural light, no filters). Upload them with `media_upload` if readable, otherwise call `media_upload_widget` alone in its own turn and wait.

## Stage 2. Build and test the Pixar character

1. **Photo breakdown first, before any generation.** Study the photos and write a feature list in plain, specific words, and show it to the creator to confirm:
   - hair: length, texture (wavy vs curly vs straight), direction, colour
   - face shape and jaw
   - nose: size, length, tip shape, bridge (for example "medium nose with a soft round tip, not long")
   - eyes: colour in two words (for example "hazel, brown with green, not yellow") and shape
   - brows: thickness and shape
   - facial hair: where it is fuller or faded
   - skin tone in plain words (for example "fair warm olive")
   - build and height impression
2. **Generate turnaround sheets** with `generate_image_batch` (model `gpt_image_2_5`, 16:9), passing the photos as `image_references`. One sheet per look (early, later, each special outfit). Prompt:

```
Pixar style 3D animated feature film character turnaround sheet, white background, front, three quarter and side views plus a face close up. Classic Pixar character design: slightly larger head and eyes than real life, soft rounded appealing shapes, smooth stylized skin, expressive eyebrows, warm friendly appeal. Not photorealistic, not anime, not a caricature. Clearly recognizable as the EXACT same person from the reference photos: [feature list from step 1]. Expression and energy: [early or later arc]. Outfit: [...]. No text labels.
```

3. Show sheets with one `show_generation_by_ids`. Ask what is off. Fix one or two features per round using the feature list words. If a fix does not land after one try, go back to the photos and rewrite that feature from them rather than stacking adjectives.
4. When the creator approves a sheet, save it as an element with `manage_reference_elements` (action `create`, category `character`, names like `Name-Early`, `Name-Later`, `Name-Party`). One element per outfit; never share one sheet across outfits.
5. **Motion test.** Generate one cheap 5 second 480p draft of the approved early character saying a short line to camera (settings from Stage 5). A still can look right and still read wrong in motion. Get a yes on the motion test before writing the story.

## Stage 3. The method (what the character teaches)

Ask exactly one question with exactly two options:
- **A) AI explainer videos with OpenArt (approved, recommended)**
- **B) Something else** (the creator types it in)

If A: the grind montage, the "[N] steps" answer, the lesson segment and the CTA all follow the OpenArt Explainer workflow below. The grind montage shows the character making explainers in OpenArt (stylized, logo-free steps, never fake UI) and posting them. Views may climb as a story beat. Never invent payout numbers, income screenshots or income guarantees. If the story needs a money line, use only figures the creator gives you from their media kit, or keep it general.

If B: tell the creator plainly that any method other than making AI explainer videos with OpenArt needs **explicit permission from their coach**, and ask them to confirm they have it. Then ask them to write out their method's steps in their own words; build the lesson only from what they write. Never offer other methods as options yourself.

### Approved workflow: AI explainer videos with OpenArt

Source: official OpenArt explainer steps and the OpenArt campaign briefs. The character teaches this exact workflow in the lesson, in short numbered steps (5 is ideal), adapted to the character's voice but never changing the facts or the order:

1. Go to openart.ai/try and scroll to Quick Starts.
2. Click Explainer. Type a script, a topic, or an idea.
3. Set the direction: style, length, and narration. Ori, the built-in assistant, can guide you or run with the best settings.
4. Start generating, then refine in the Scenes tab or the Timeline tab.
5. Export and post.

Do not invent button labels, settings, prices, credit costs or render times. If a start-button name is confirmed ([CONFIRM]: "Direct my explainer", "Direct", or another live label), use that name in the dialogue; otherwise say "start generating" or "let OpenArt build the explainer."

Spoken names: say **OpenArt** as "Open Art", and say the URL as "openart dot A I slash try".

The prompt shown on the stylized lesson panel (keep it word for word; the creator fills in the topic):

```
Create a short animated explainer about [TOPIC]. Keep it simple, with a clear beginning, middle, and end, and a friendly voiceover.
```

Lesson staging: the character talks to camera; a glowing panel shows each step as stylized, logo-free visuals (plain text for the URL, a prompt being typed, simple style/length/narration choices, scenes being arranged, a finished explainer). The panel never shows real logos or fake OpenArt UI as if it were a real screenshot. Any finished-explainer clip in this segment is generated in Higgsfield on an original topic, in the same Pixar style as the skit (or a clearly stylized explainer look), never as a fake product export.

Default CTA for this method: the character must say **OpenArt** out loud and say or show **openart.ai/try**. Hold `openart.ai/try` on screen during the CTA. Example: "Try it in OpenArt. Go to openart.ai/try." Do not send viewers to openart.ai, /make, /chat, or any other path. A "Comment [KEYWORD] for the guide" line is optional only if the creator already has an approved keyword and can actually deliver that guide ([CONFIRM] before using one).

Campaign rules to pass on to the creator (do not break them in the skit either):
- Every video directs viewers to openart.ai/try. Put it in the bio and show it as on-screen text (and in the caption). Not openart.ai, not /make, not /chat.
- Say "OpenArt" out loud. The caption must mention OpenArt.
- Add a clear paid-partnership or ad disclosure in the post caption. A hashtag alone is not enough. Do not invent a brand handle or creator hashtag; confirm the approved wording, tag and hashtag before posting ([CONFIRM]).
- Never fabricate income, client payments, PayPal or Stripe screenshots, testimonials, engagement or analytics. Do not promise guaranteed income, virality, instant production, free access, fixed output quality, or features you have not demonstrated. Do not invent prices, credit costs, or how long a render takes. Views are not revenue; do not estimate earnings from an unrelated post.
- Use original or explicitly licensed clips, music, artwork and likenesses. A public inspiration video is not permission to reuse or stitch it. Do not impersonate real people or copy protected characters. Do not expose private dashboards, personal information or credentials.
- Keep AI-generated characters clearly fictional. Never imply celebrity or studio endorsement.
- This campaign's approved Director method is Quick Start → Explainer only. Do not teach other Quick Starts or tools unless the coach explicitly allows it.

## Stage 4. Story pitch

Ask for a topic in one or two lines. Then pitch 2 or 3 ideas that follow the proven formula:

- **Hook (first 2 seconds):** a heartbreak or public humiliation the viewer feels at once, shown with simple readable props or one image (a sign, flowers, a text message, a door swinging open). Heartbreak hooks perform best.
- **The cut:** someone looks down on the main character, ideally with one sharp line ("You're broke", "You're a junior rep").
- **Turn and grind:** the main character starts the method chosen in Stage 3, in a quick montage.
- **Time jump:** a text card like "3 years later".
- **Reveal:** a luxury or status reversal in front of the people who doubted them.
- **Callback:** a line or prop from the hook comes back and pays off in the reveal.
- **The ask:** the person who looked down on them asks "how did you...?" and the main character answers "[N] steps."
- **Lesson:** the main character teaches the Stage 3 method in short numbered steps, talking to camera. Pick a specific niche for the demo (the explainer topic) and use a different one in each story so a series never repeats.
- **CTA:** a natural on screen call to action at the end that says OpenArt and shows openart.ai/try.

Let the creator pick, mix or change. Then write the locked script as a table: clip number, set, characters, **wardrobe for that clip**, beat, exact dialogue (one speaker per line). Rules:
- every clip 6 to 15 seconds; split longer scenes
- 13 to 15 clips, about 2 to 2.5 minutes total
- outfits only change when the time or place changes
- every name spelled the way it should sound, including "Open Art" and "openart dot A I slash try"
End with a short list of open questions (outfits, colours, names, pronunciations) and wait for answers. If the creator uses Claude Docs, put the script in a doc so they can edit it.

## Stage 5. Cast, sets and 480p drafts

1. Generate side character sheets (one per outfit, Pixar style prompt from Stage 2 without photo references) and 9:16 empty set images ("Pixar style 3D animated film background set, vertical 9:16, no people, ..."), built once at high detail in the lighting the scene needs. QA them visually, show them, and save characters as elements. Hero props (a car, a sign) get their own reference image. Lesson-panel and finished-explainer clips are generated here in Higgsfield too, as stylized, logo-free visuals, never as fake OpenArt UI.
2. Generate all clips with `generate_video_batch` (max 12 per call): `model: seedance_2_5`, `mode: omni_reference`, `draft: true`, `resolution: 480p`, `aspect_ratio: 9:16`, `generate_audio: true`, `duration` per clip, and the set image in `medias` with role `image_references` (omni_reference REQUIRES at least one media). Reference characters ONLY with `<<<element_id>>>` inside the prompt, followed by a short plain description and the clip's outfit in parentheses.
3. Prompt template (fill every line):

```
Stylized 3D animated feature film, Pixar style, high end animation studio look, expressive faces, crisp detail, [a real light source] as a soft key light on faces, soft rim light, vertical 9:16. Natural lip sync, clear pronunciation. Language: English only. Audio: dialogue and [specific sound effects] only, absolutely no background music, no song, no beat, no score. No subtitles, no on screen text. Setting: [set] from the reference image. STAGING: [who stands where; who must NOT walk through what]. Characters: <<<id>>> (short description, outfit), [emotion], [voice]; ... Shot 1 (0-3s): [action]; he says: "[line]" Shot 2 (3-7s): ...
```

4. Prompt lessons that matter:
   - **Light the faces.** Any mood works (night, neon, rain), but always name a real light hitting the faces (lamp, window, string lights, streetlight) plus a rim light. Coloured LEDs stay in the background, never as the only light on skin.
   - Always include "Language: English only" (or the creator's language). Without it, clips sometimes come out in another language.
   - Spell tricky words the way they sound, never with a pronunciation note in brackets (notes get read aloud). Examples: "Open Art" for OpenArt, "openart dot A I slash try" for openart.ai/try, "Ess... Cue... Pee" for acronyms.
   - Montage clips love to add music. Say "ONLY diegetic sound effects... Absolutely no music of any kind" and still check.
   - Add STAGING lines whenever three or more people share a space.
   - Finger counts are unreliable. Describe exact fingers ("index, middle and ring fingers up, thumb holding pinky down") but plan a number overlay in the edit as backup.
   - Phone screens and text bubbles often come out garbled. Say "no text bubbles" and plan to cover them in the edit. Do not ask the model to render a realistic OpenArt interface on a phone or monitor.
   - Write lowercase for words you want spoken normally (for example "website" rather than "WEBSITE").
   - **Voices:** keep each character's voice description identical in every clip. If the model supports an audio or voice reference, save each character's first approved line and pass it as a reference on later clips.
5. Poll with `jobs_wait` (15 second max). Then QA every clip in `sandbox_exec`, running long work with `background: true`:
   - **transcript:** faster_whisper (`WhisperModel("small", compute_type="int8")`), compared to the script word for word, including names, brand words (OpenArt, openart.ai/try) and the CTA;
   - **frame grid:** `ffmpeg -i clip.mp4 -vf "fps=1,scale=150:-1,tile=7x2" -frames:v 1 grid.jpg`, inspected with `image_paths` (under 512 KiB per call): right face, right outfit for that clip, right set, no extra or missing people, no glitches (floating props, people walking through furniture), nothing the script dropped sneaking back in, no fake OpenArt UI or logos;
   - **music:** check montage clips with demucs stems.
6. Show all drafts in ONE `show_generation_by_ids` call. Report: what landed, what is wrong per clip, and for each problem either "fix in edit (free)" or "redo (about N credits)". Recommend the cheaper path when the edit can fix it.
7. Repeat redo rounds only after approval.

## Stage 6. 1080p finals

Only after the creator approves all drafts and `balance` covers the cost:
- Resubmit each clip with the SAME params as its draft (prompt, medias, duration, seed from the draft's params) plus `draft_job_id: <draft id>` and `resolution: 1080p`, without `draft: true`. Finals keep the draft's performance and audio.
- Strip any music: split with demucs (htdemucs), then remix vocals plus drums with `ffmpeg -filter_complex "[1:a][2:a]amix=inputs=2:normalize=0[a]"` over the original video. Keep both RAW and NoMusic versions.
- Deliver: if the creator's computer is linked, download each file into their Downloads with clear ordered names (`Story_01_Hook.mp4`, ...), flagging clips that need an edit fix in the filename (`_addNumberOverlay`, `_addTryUrl`). Otherwise send the files or a list of links.

## Stage 7. Edit (creator's choice)

Ask which they want:

**A) Manual edit (recommended).** They edit in Premiere, CapCut or similar. Give them a short edit sheet: clip order, text cards and where they go ("1 hour earlier", "3 years later"), which clips need number overlays or covers, and that `openart.ai/try` must be held on screen during the CTA. Their final checklist:
- even loudness across clips, dialogue always on top
- captions for silent viewing
- music only if they choose, added in the editor and kept under the dialogue
- `openart.ai/try` visible on the CTA; paid-partnership or ad disclosure in the post caption (not invented)
- full watch through on a phone before posting

**B) Quick auto edit by Claude.** In the Higgsfield sandbox:
1. Normalise and concatenate the finals in order with ffmpeg (same resolution, frame rate and audio rate), and even out loudness (`loudnorm`).
2. Transcribe the full cut with faster_whisper word timestamps and build an ASS subtitle file.
3. Burn in subtitles in the house style. If the creator supplied a style reference video or image, match it (font, size, colour, outline, position, words per line, animation). Default if none: Montserrat ExtraBold, white text, thick black outline, centred in the lower third, 2 to 4 words per line, uppercase.
4. Add the text cards from the script as short full screen captions, and hold `openart.ai/try` on screen during the CTA.
5. Upload with `media_upload` (PUT from the sandbox with header `If-None-Match: *`, then `media_confirm`) and deliver.
Tell them plainly: scene cuts, timing tweaks, music and anything creative beyond this need a manual pass in their editor. Do not generate OpenArt UI or OpenArt exports to fill in the lesson.

## Round summary to show the creator at each stage

End every stage with: what is done, what you need from them (one clear ask), and the credit cost of the next step.
