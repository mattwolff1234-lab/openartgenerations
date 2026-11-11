# Skit Studio

Animated OpenArt skits starring Raghav. Start every session by reading `HANDOFF.md` (current state, links, next steps), then follow the project skill at `.claude/skills/openart-skit-pipeline/SKILL.md`.

## How work runs here

- Generation and editing happen through two MCP connectors: **Higgsfield** (images, music, and `sandbox_exec`, a cloud Linux box with ffmpeg, ImageMagick, Pillow, faster-whisper and the Metropolis font) and **Open Art** (Seedance 2.5 video). Do all media downloads, transcodes, captions and mixes inside the Higgsfield sandbox; its files in `/home/user` persist ~24h after last use only.
- The sandbox working folder is `~/cut`. If it's gone (new sandbox), restore it: download the three bundle tars listed in `MEDIA.md` with curl inside the sandbox and `tar -xf` them in `~`.
- Scripts in `scripts/` and `.claude/skills/openart-skit-pipeline/scripts/` are meant to run inside the sandbox. Copy them in with a heredoc when needed.
- Deliver finished videos by `media_upload` → curl PUT from the sandbox → `media_confirm`, then share the cloudfront link. Add every new final to the table in `HANDOFF.md`.

## Rules

- Run unattended. Don't stop to ask for approval between steps; stay inside the budget in the brief and report credits spent at the end.
- OpenArt allows max 8 parallel video jobs. Reference images must be on cdn.openart.ai (upload with `openart_upload_sign` + PUT) and passed with their metadata.
- Never put the creator's email or private info into prompts or external requests.
- Keep `HANDOFF.md` current: when a video ships or a decision changes, update it before ending the session.
