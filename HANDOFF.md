# Handoff: where we left off (Nov 11, 2026)

Read this first in any new session. It's the state of the Raghav / OpenArt skit project at the moment it moved out of the Claude app into this repo.

## What this project is

Pixar-style 9:16 animated skits starring **Raghav** (the creator's character, built from 2 photos) that teach the OpenArt Explainer flow (`openart.ai/try`). Every video follows the same skeleton: Hook → Grind → Reveal → Lesson (5 steps, screen-recording cards) → CTA ("Now post and start printing", $123→$999 counter, "Comment **AI** if you want the full setup"). Talking clips render on OpenArt Seedance 2.5 at 1080p; images, music and all editing happen in Higgsfield (images via `generate_image`, editing via `sandbox_exec`).

The full how-to is the project skill at `.claude/skills/openart-skit-pipeline/SKILL.md`. Story formats are in `.claude/skills/openart-skit-pipeline/formats/FORMATS.md`.

## Finished videos (all permanent links)

Base: `https://d2ol7oe51mr4n9.cloudfront.net/user_3Kn2gmXeWEZVSCnsDtwLIgqwM2S/<id>.mp4`

| Video | Format | Music | No music |
|---|---|---|---|
| **Driveway v2 (latest)** | F15 crash-zoom "Get that thing off my driveway" | `f21e3a7c-4b1d-4802-a26b-121b86c7cbdc` | `f40948ff-831b-4d62-8ee3-047325b56b47` |
| Driveway v1 (graph as floating card) | F15 | `32937a63-8676-4bb5-bcd4-9cd6a93f7201` | `c4d94b2f-2396-4c93-9132-e6caa486bfde` |
| Evicted (v3, quieter mix) | F1 | `9f36e3cb-ebd1-4da9-a2c7-7f090ab5e4eb` | `8890252d-d0c3-4056-a5c7-cd4bf6147fc3` |
| Fired (quieter) | F2 | `79c08551-157a-4fe4-8955-d6040d6aca81` | `1db984a8-eff8-4135-96f5-1a3aa1661b38` |
| Family Dinner (quieter) | F3 | `b9d5973f-0eae-4565-a31f-a7a0207ba470` | `85229082-8cdd-4495-b62a-fba39e007d20` |
| Stood Up (quieter) | F5 | `5b080b80-0b81-4fbb-abb9-5a901c545f47` | `315a0c9b-fbd9-4371-9f72-682ccc5ac146` |

Older/loud versions (superseded): Evicted v1 `e5dd1734-854e-4b83-85b6-c294a298fcf7`, v2 `d696265a-2237-465a-8b79-e73fe64372a3`, v3 loud `c17905b8-480b-4193-85f3-75ac303e08ee`, Fired loud `9c957589-43b9-438d-94fe-afe1fb1c67bd`, Family Dinner loud `8f3b1a82-89d2-497f-b390-b646638dbd34`, Stood Up loud `99fc156f-ffb1-456c-86c9-ad1010a3e92d`.

Every working file (raw Seedance clips, captioned clips, the reusable lesson + CTA clips, music, character sheets, sets, logos, QA frames, edit scripts) is in the media bundle: see `MEDIA.md` and run `scripts/fetch_media.sh`.

## Driveway v2 cut (75.6s)

1. `dwa` 15s hook: Hank (huge red-bearded neighbor) storms down the driveway, crash zoom into his face: "Get that thing off my driveway!" Raghav pokes out of the van: "It's... temporary?" Hank: "You've got till sundown, cartoon boy."
2. `dwb` 12s grind in the van: "One idea. One explainer. Post it. Again. Last night in the van."
3. `dwr` 10s laptop reaction: over-the-shoulder on a green-screen laptop with the animated Insights dashboard composited on (1,204 → 1.2M views, $14 → $4,820 earned), then his face: "No way." / "Wait... that's from ONE video?"
4. `dwc` 15s reveal, "6 MONTHS LATER": sports car on Hank's driveway. "Is that the van kid?" / "Relax, it's not on your driveway." / "How did you...?" / "Five steps."
5. `n4` lesson + `n5` CTA (shared by every video).

Music: `music_dw.mp3` (66s) extended to 76s with `scripts/extend_music.sh music_dw.mp3 music_dw3.mp3 42 30`, mixed with `mix_music.sh` levels.

## Open items / next steps

1. **Driveway story order**: the van scene ends on "Last night in the van" before the graph plays, which reads slightly backwards. Option: trim that line from `dwb` (cut at ~9s) so the graph is what gets him out of the van. Not done yet; ask before changing.
2. **Next video, recommended: hook #4 "Turn that light OFF."** A massive landlord pounds on the van window at 3am because the laptop glow keeps him up. Payoff: Raghav rents the guy's best unit, and the light is still on. Reuses Set-Van, the green-screen laptop trick and n4/n5, so it's cheap. Other crash-zoom hooks pitched:
   - "Who parked in MY spot?" (security guard, reserved spot, payoff: spot has his name)
   - "You're sitting at my table." (restaurant owner, payoff: he buys the restaurant's explainer / brings a date)
   - "Is that YOUR laptop on my porch?" (neighbor, payoff: she asks him to make her bakery's video)
   - "Off my lawn. NOW." (terrifying HOA lady with a megaphone, payoff: HOA hires him)
3. **FORMATS.md** has F1–F6 only. The viral formats F7–F15 (F15 = Driveway crash-zoom) were pitched in chat but not written into the file yet.
4. Name pronunciation: some Seedance clips say "Ragge"/"Drag-Av". Captions are always corrected; spell it "Raghav (RAH-guv)" in prompts if it matters.

## Credits (approx., Nov 11)

- OpenArt: ~6,600 left after the Driveway reaction clip. Seedance 2.5 1080p 9:16 with audio: 15s = 4,810 · 12s = 3,850 · 10s ≈ 3,210 · 8s = 2,565. Always re-check with `openart_model_cost`.
- Higgsfield: check with `balance`. Images ~2 credits each, music a few credits.

## Reusable assets

- OpenArt reference images (already on cdn.openart.ai, pass in `visualReferences` with their metadata): `assets/openart_refs.json` (Raghav-Early, Raghav-Later, Hank, Priya, Brandon, Boss-Dana, Tyler, Zara, Mom, Dad, Cousin-Arjun, Prop-Car, 11 sets incl. Set-Van and Set-Driveway).
- Every Seedance prompt used: `assets/clip_prompts_used.json`. Every image prompt: `assets/image_prompts_used.json`. Music prompts: `assets/music_prompts_used.json`. Raw OpenArt clip URLs: `assets/openart_clips.json`.
- Shareable guide (Claude Docs): https://claude.ai/artifact/Ax5G7m44po2zKUQB7AciHK

## Standing preferences from the creator

- Character name is **Raghav** (never "Matt").
- Captions on every clip (white Metropolis Bold, 1-3 words, mid-frame). "AI" in the CTA in yellow.
- Music under everything but quiet (voice -16 LUFS, music -30 LUFS, ducked, extra -4 dB over the CTA). Always export a no-music version too.
- Don't ask for approvals mid-run; finish and report what was spent.
- Crop anything personal (workspace name, history, email, credit balance) out of screen recordings.
