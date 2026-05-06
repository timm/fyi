# Handoff: irl.html + project setup

## What was done (all committed & pushed unless noted)
- Widened irl.html layout from 600px to 820px, bumped font from 88% to 100% (inline `<style>` override, not shared style.css)
- Added irl.png banner image to repo
- Changed home link (top-left house icon) from `index.html` to `https://timm.fyi`
- Added handoff protocol to CLAUDE.md (**uncommitted** — stage & push)
- Configured status line (`~/.claude/statusline-command.sh` + `~/.claude/settings.json`) showing model, context %, cost, git branch
- Upgraded claude-code 2.1.104 → 2.1.108

## What remains
- **Banner image readability**: User noted middle of irl.png (researchers around glowing table) is indistinct/hard to read. Baked into raster — can't fix with CSS alone. Options discussed:
  1. CSS contrast/brightness boost on `.banner` (blunt, affects whole image)
  2. Regenerate image with better mid-tone contrast (needs external image gen)
  3. CSS gradient overlay to selectively lighten/darken center
  - User hasn't picked approach yet. Ask which they prefer.
- **CLAUDE.md** has uncommitted change (handoff protocol section). Commit & push it.

## What didn't work / notes
- Can't selectively edit regions of PNG via code — need image editing tool or regeneration
- All irl.html style overrides in inline `<style>` block to avoid affecting other pages sharing style.css

## Files touched this session
- `irl.html` — layout override + home link (pushed)
- `irl.png` — banner image (pushed)
- `CLAUDE.md` — added handoff protocol (uncommitted)
- `HANDOFF.md` — this file
