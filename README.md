# Skit Studio

Everything from the Raghav / OpenArt animated skit project: the pipeline skill, prompts, editing scripts, reference videos, every prompt used, and a downloadable bundle of all generated media. Set up to run from a terminal with Claude Code and no permission prompts.

## Setup (once)

1. Install Claude Code and log in with the same Claude account you used in the app:

```bash
npm install -g @anthropic-ai/claude-code
```

2. Clone this repo and open it:

```bash
git clone https://github.com/mattwolff1234-lab/openartgenerations.git
```

```bash
cd openartgenerations && claude
```

3. In Claude Code, run `/mcp` and check that **Higgsfield** and **Open Art** are listed and connected. Connectors from your claude.ai account usually show up automatically when you're logged in with that account. If one is missing, add it from that service's MCP setup page (`claude mcp add ...`), then restart `claude`.

4. Optional, to get the media on your machine (about 1.4 GB):

```bash
./scripts/fetch_media.sh
```

## No permission prompts

`.claude/settings.json` sets `"defaultMode": "bypassPermissions"` and pre-allows Bash, file edits and the Higgsfield / Open Art tools, so Claude runs on its own in this folder. The first time, Claude Code shows a one-time warning about bypass mode; accept it. Starting it explicitly also works:

```bash
claude --dangerously-skip-permissions
```

Bypass mode means Claude can run any command in this folder without asking. Only use it in this project folder.

If your org has disabled bypass mode, the allow list in the same file still covers the tools this project uses.

## Picking up where we left off

Just say: "read HANDOFF.md and continue." Next step queued there: the "Turn that light OFF" skit (crash-zoom hook #4).

## Layout

| Path | What |
|---|---|
| `HANDOFF.md` | Current state, every finished video link, open items, credits |
| `CLAUDE.md` | Instructions Claude loads automatically |
| `MEDIA.md` | What's in the media bundle and how to restore it |
| `.claude/skills/openart-skit-pipeline/` | The full pipeline skill (SKILL.md, brief template, formats, prompts, caption/mix scripts) |
| `scripts/` | Laptop dashboard animation, green-screen compositor, music extender, media fetcher |
| `assets/` | OpenArt reference IDs and every prompt used (clips, images, music) |
| `reference/` | The original skill specs, reference reels and screen recordings |
| `docs/` | Early barbershop-reel recreation notes |
