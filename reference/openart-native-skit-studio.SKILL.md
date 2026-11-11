---
name: openart-native-skit-studio
description: Guide a creator from a short topic to finished 1080p Pixar style animated skit clips starring their own character, using OpenArt for all generation: Characters, turnaround sheets, sets, lip-synced video drafts and finals, then Director Mode or a local edit.
---

# OpenArt Native Skit Studio

Turn a creator into an original Pixar style character and produce a 1:30 to 2:30 vertical animated skit (9:16) in OpenArt, in short back and forth rounds. The creator approves every stage. You do the thinking, prompting, QA and rendering.

**All generation is in OpenArt.** Character creation, turnaround sheets, sets, 480p drafts, 1080p finals, any explainer demo footage, and assembly happen in OpenArt (or a free local edit of OpenArt exports). Do not use Higgsfield or any other generator for these assets.

## How to drive OpenArt

Use the first path that is available. Do not invent tool names, button labels, prices or credit costs.

**A) OpenArt MCP (preferred if connected).** Official server: `https://mcp.openart.ai/mcp` (docs: https://openart.ai/mcp/). The creator signs in with their OpenArt account via OAuth. There is no public API key, and OpenArt does not currently offer a public API. Official docs do not publish stable MCP function names, and "the tool list updates automatically as new tools ship." Read the live tool list from the connector and use those names. Documented capabilities: generate images and video, plan multi-shot videos with Smart Shot (preview the Shot Plan first, or plan and render), discover available models, track results, upload reference files (Claude has an upload widget), check account and credits, switch workspaces, organize projects, and reuse items from the OpenArt library. There is no Characters or Brand Kit tool in MCP (Character is on the roadmap). MCP does not edit video.

**B) OpenArt CLI,** if MCP is not connected but the CLI is signed in (`openart login`). Documented commands (https://github.com/OpenArt-AI/cli): `openart account`, `openart model list`, `openart model cost --model <id> --mode <mode>`, `openart upload add <file>`, `openart generate image "..." --model ...`, `openart generate video "..." --model ... [--duration] [--aspect-ratio] [--resolution]`, `openart creation get <id>` / `openart creation wait <id>`. Duration, aspect ratio and resolution are model-specific; omit them only when you want the model's defaults, and confirm 9:16 was actually used.

**C) openart.ai in the browser,** with you driving it or guiding the creator click-by-click. Use the real feature names in this skill. If a button label is unclear, mark it [CONFIRM] and follow whatever is on the live screen.

Before every paid batch: check remaining credits, read the credit cost OpenArt shows for that model, resolution and length, tell the creator the cost, and wait for a yes. If credits are short, say so and offer a partial render. Never invent a per-second or per-clip price. Credits vary by model and resolution, and MCP spends the same credits as the OpenArt site.

Default models, unless a live model list shows a better current option:
- Still images (sheets, sets, props): GPT Image 2.5.
- Talking clips: Seedance 2.5, which official docs describe as synced audio with dialogue and lip sync, clips up to 30 seconds at up to 1080p, with start/end frame and a large reference budget. Drafts: Seedance 2.5 Draft, which official docs say renders at 480p and can be upgraded to 1080p on the same video.
- Skit clips are 9:16, 6 to 15 seconds, within the chosen model's limit. Veo 3.1 also has native audio but only 4, 6 or 8 second clips, so it is a poor fit for longer lines. Other published options with synced audio include Kling 3.0 / Kling 3 Omni, Gemini Omni Flash and Wan 3.0. Ask for today's model list if the catalog has changed.

Work in one OpenArt project so characters, stills and clips stay together. Every generation also lands in the OpenArt library.

## Ground rules

- **Originality.** Every story, cast, name and line must be new and built from THIS creator's topic. Never reuse another creator's storyline, characters, character names, lines or sets, even if asked to "do it like the example". Reuse only the structure and craft below.
- **Approval gates.** Never move to the next stage without a clear yes. Before ANY regeneration, list which scenes need redoing and the credit cost OpenArt shows, then wait.
- **Credits.** Check the remaining balance and the cost shown before every paid batch, as above.
- **Keep it PG 13 and original.** No real brands, logos, famous characters or lookalikes. Kisses, nudity or violence should be rewritten as a comedic "caught too close" beat instead. Give side characters specific, distinctive traits. Never generate fake OpenArt UI, logos, or a fake product screenshot as if it were real. Lesson panels may show stylized, logo-free steps. A finished explainer in the grind or lesson may be a real OpenArt Explainer export on an original topic, or a stylized Pixar-style explainer; never composite fake product chrome around it.
- **Approved method only.** The only approved method the character teaches is **making AI explainer videos with OpenArt** (Stage 3). Any other method needs explicit permission from the creator's coach. Producing this skit uses Characters, Create Image, video models and Director assembly; that is production, not the method being taught.
- Ask questions with the question tool when available, 1 to 4 at a time, each with a recommended option first.

## Stage 1. Character intake

Ask, in one round:
1. **The arc.** How the character looks and acts before success vs after. Default that works well: bright, full eyed, hopeful and a little bubbly early; calm, half lidded, light closed mouth smirk after success.
2. **Glasses:** always, never, or only while working.
3. **Outfits:** the "before" look and the "after success" look, plus any special outfits the story may need later.
4. **Partner or love interest:** name and colour palette (they change dress colour per story).

Then ask for 3 to 6 clear face photos (front, three quarter, side, natural light, no filters). Upload them with the OpenArt MCP upload widget if it is available; otherwise have the creator upload them in OpenArt Characters / Character Builder, or add them with `openart upload add`.

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
2. **Save the character in OpenArt Characters (Character Builder).** This step is in the OpenArt app, because MCP has no Characters tool yet. Start from the reference photos (highest control over the face). Prompt the look as Pixar style 3D animated feature film character design: slightly larger head and eyes than real life, soft rounded appealing shapes, smooth stylized skin, expressive eyebrows, warm friendly appeal. Not photorealistic, not anime, not a caricature. Clearly recognizable as the exact same person from the photos, using the feature list. Save one character (or clearly named variant) per outfit, for example `Name-Early`, `Name-Later`, `Name-Party`. Never share one saved character across outfits that must look different.
3. **Generate turnaround sheets** in Create Image (GPT Image 2.5 or the current best image model), 16:9, with the photos and/or the saved character tagged as references. One sheet per look. Prompt:

```
Pixar style 3D animated feature film character turnaround sheet, white background, front, three quarter and side views plus a face close up. Classic Pixar character design: slightly larger head and eyes than real life, soft rounded appealing shapes, smooth stylized skin, expressive eyebrows, warm friendly appeal. Not photorealistic, not anime, not a caricature. Clearly recognizable as the EXACT same person from the reference photos: [feature list from step 1]. Expression and energy: [early or later arc]. Outfit: [...]. No text labels.
```

After one approved hero still, official docs also support Multi-View: it makes 9 angles of that picture, first as a grid and then as separate images, which you can reuse as references. Prefer Multi-View as a supplement, not a replacement, for a readable turnaround sheet.
4. Show the sheets (and Multi-View angles if you made them). Ask what is off. Fix one or two features per round using the feature list words. If a fix does not land after one try, go back to the photos and rewrite that feature from them rather than stacking adjectives. In the app, Edit Image or Face Swap can repair one still in place if needed.
5. **Motion test.** After approval, generate one cheap short 9:16 draft of the approved early character saying a short line to camera, using Seedance 2.5 Draft (480p, upgrade path in Stage 6) and the settings from Stage 5. Check the credit cost and get a yes first. A still can look right and still read wrong in motion. Get a yes on the motion test before writing the story.

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

Lesson staging: the character talks to camera; a glowing panel shows each step as stylized, logo-free visuals (plain text for the URL, a prompt being typed, simple style/length/narration choices, scenes being arranged, a finished explainer). The panel never shows real logos or fake OpenArt UI as if it were a real screenshot. For the finished-explainer payoff, prefer a real OpenArt Explainer export on an original topic (Quick Start → Explainer, cost shown and approved first). If you skip that, generate a stylized Pixar-style explainer with the same video tools. Never fake the product interface around the result.

Default CTA for this method: the character must say **OpenArt** out loud and say or show **openart.ai/try**. Hold `openart.ai/try` on screen during the CTA. Example: "Try it in OpenArt. Go to openart.ai/try." Do not send viewers to openart.ai, /make, /chat, or any other path. A "Comment [KEYWORD] for the guide" line is optional only if the creator already has an approved keyword and can actually deliver that guide ([CONFIRM] before using one).

Campaign rules to pass on to the creator (do not break them in the skit either):
- Every video directs viewers to openart.ai/try. Put it in the bio and show it as on-screen text (and in the caption). Not openart.ai, not /make, not /chat.
- Say "OpenArt" out loud. The caption must mention OpenArt.
- Add a clear paid-partnership or ad disclosure in the post caption. A hashtag alone is not enough. Do not invent a brand handle or creator hashtag; confirm the approved wording, tag and hashtag before posting ([CONFIRM]).
- Never fabricate income, client payments, PayPal or Stripe screenshots, testimonials, engagement or analytics. Do not promise guaranteed income, virality, instant production, free access, fixed output quality, or features you have not demonstrated. Do not invent prices, credit costs, or how long a render takes. Views are not revenue; do not estimate earnings from an unrelated post.
- Use original or explicitly licensed clips, music, artwork and likenesses. A public inspiration video is not permission to reuse or stitch it. Do not impersonate real people or copy protected characters. Do not expose private dashboards, personal information or credentials.
- Keep AI-generated characters clearly fictional. Never imply celebrity or studio endorsement.
- This campaign's approved Director method to *teach* is Quick Start → Explainer only. Do not teach other Quick Starts or tools unless the coach explicitly allows it.

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

## Stage 5. Cast, sets and draft clips

1. Build side characters the same way as Stage 2, from a Pixar style prompt (no photo references) in Character Builder or Create Image, one saved character per outfit. Generate 9:16 empty set images in Create Image ("Pixar style 3D animated film background set, vertical 9:16, no people, ..."), built once at high detail in the lighting the scene needs. QA them visually, show them, and save them to the project library. Hero props (a car, a sign) get their own reference image. Lesson-panel stills are stylized and logo-free; never fake OpenArt UI.
2. Generate draft clips with Seedance 2.5 Draft, 9:16, 480p if that is what the model shows, duration per clip (within the model's limit), with audio / lip sync on, and the approved character plus set (and any hero prop) passed as references. In the OpenArt app, tag the saved Characters and start from an approved still when you want a locked framing (Image to Video, or a still as the first frame vs a subject reference for a new scene). Check the credit cost for the whole batch and get approval before generating. Work in modest batches so a failed clip is cheap to isolate.
3. Prompt template (fill every line):

```
Stylized 3D animated feature film, Pixar style, high end animation studio look, expressive faces, crisp detail, [a real light source] as a soft key light on faces, soft rim light, vertical 9:16. Natural lip sync, clear pronunciation. Language: English only. Audio: dialogue and [specific sound effects] only, absolutely no background music, no song, no beat, no score. No subtitles, no on screen text. Setting: [set] from the reference image. STAGING: [who stands where; who must NOT walk through what]. Characters: [saved character name] (short description, outfit), [emotion], [voice]; ... Shot 1 (0-3s): [action]; he says: "[line]" Shot 2 (3-7s): ...
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
   - **Voices:** keep each character's voice description identical in every clip. If you later need a lip-sync repair, the OpenArt app also has a Lip Sync tool ([CONFIRM] whether it is the right fix for that clip, and check the cost). Only clone a real person's voice with their permission.
5. When each draft is ready, QA it. If you have local tools, transcribe with a speech-to-text model and build a frame grid with `ffmpeg -i clip.mp4 -vf "fps=1,scale=150:-1,tile=7x2" -frames:v 1 grid.jpg`. If you do not, watch and listen carefully and write down issues. Check:
   - **transcript:** spoken lines against the script, word for word, including names, brand words (OpenArt, openart.ai/try) and the CTA;
   - **frames:** right face, right outfit for that clip, right set, no extra or missing people, no glitches (floating props, people walking through furniture), nothing the script dropped sneaking back in, no fake OpenArt UI or logos;
   - **music:** listen for unwanted score, especially on montage clips (split stems only if you have a local separator such as demucs).
6. Show all drafts together (library links or downloaded files). Report: what landed, what is wrong per clip, and for each problem either "fix in edit (free)" or "redo (check cost first)". Recommend the cheaper path when the edit can fix it.
7. Repeat redo rounds only after approval.

## Stage 6. 1080p finals

Only after the creator approves all drafts and the shown credit cost is approved:
- Official docs say a Seedance 2.5 Draft can be upgraded to 1080p on the same video. Use that upgrade when the live UI offers it ([CONFIRM] the exact control label). If a clip has no upgrade path, regenerate it at 1080p with the same prompt, references, duration, aspect ratio and audio settings. Do not invent a Higgsfield-style `draft_job_id`.
- If a final picked up music, strip it locally if you can (for example demucs plus ffmpeg), or flag it for the edit, or regenerate with a stronger no-music prompt after approval. Keep both RAW and NoMusic versions when you strip audio.
- Deliver from the OpenArt library (and any local folder you saved to) with clear ordered names (`Story_01_Hook.mp4`, ...), flagging clips that need an edit fix in the filename (`_addNumberOverlay`, `_addTryUrl`).

## Stage 7. Edit (creator's choice)

Ask which they want:

**A) Manual edit (recommended).** They edit in Premiere, CapCut or similar. Give them a short edit sheet: clip order, text cards and where they go ("1 hour earlier", "3 years later"), which clips need number overlays or covers, and that `openart.ai/try` must be held on screen during the CTA. Their final checklist:
- even loudness across clips, dialogue always on top
- captions for silent viewing
- music only if they choose, added in the editor and kept under the dialogue
- `openart.ai/try` visible on the CTA; paid-partnership or ad disclosure in the post caption (not invented)
- full watch through on a phone before posting

**B) Assemble in OpenArt Director Mode.** In the OpenArt app (MCP does not edit video), open Director Mode, place or refine the approved clips as scenes, review them in the Scenes tab or the Timeline tab, give notes on any shot that needs a change, then export. [CONFIRM] the exact control for importing already-made clips, and whether a "Story" view is present; official docs confirm Scenes, Timeline and export. Director projects can run up to 5 minutes, which covers this skit length. A note about one scene should change only that scene. Check export cost if one is shown, and export 9:16.

**C) Quick auto edit by Claude.** MCP cannot do this. If you have local tools (or a folder of the exported finals):
1. Normalise and concatenate the finals in order with ffmpeg (same resolution, frame rate and audio rate), and even out loudness (`loudnorm`).
2. Transcribe the full cut with word timestamps and build an ASS subtitle file.
3. Burn in subtitles in the house style. If the creator supplied a style reference video or image, match it (font, size, colour, outline, position, words per line, animation). Default if none: Montserrat ExtraBold, white text, thick black outline, centred in the lower third, 2 to 4 words per line, uppercase.
4. Add the text cards from the script as short full screen captions, and hold `openart.ai/try` on screen during the CTA.
5. Deliver the file and, if useful, also keep a copy in the OpenArt library.
Tell them plainly: scene cuts, timing tweaks, music and anything creative beyond this need a manual pass in their editor, or a Director Mode refine.

## Round summary to show the creator at each stage

End every stage with: what is done, what you need from them (one clear ask), and the credit cost of the next step.
