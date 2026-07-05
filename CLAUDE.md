# Project: timm.fyi — Personal Academic Website

## Tech Stack
- Pure HTML + CSS, no build tools, no JS frameworks
- Single CSS file: `site.css` (the "150 words of css")
- Font Awesome 6.5.1 via cdnjs `<link>` in each `<head>`
- Dark theme: bg `#1a1a1a`, fg `#e0e0e0`, accent amber `#ffb86c`, muted `#888`

## Pages
- **Personal pages**: `index.html`, `research.html`, `teach.html`, `blog.html`, `news.html`, plus `irl.html` (lab home, formerly separate "Service" page dropped 2026-05).
- **Blog posts**: root-level `<slug>.html` files (e.g. `higher_way.html`, `symbolic_ai.html`, `ezr2.html`, `drr.html`). Listed under `blog.html` Posts section.
- **Nav on personal pages** (uniform): `Home | Research | Teach | Tools | Blog | Lab`. Tools restored to nav 2026-06; everything under `tools/` is GENERATED (see Tools section) — don't hand-edit it.
- **IRL section** (4 pages): `irl.html`, `irl-projects.html`, `irl-people.html`, `irl-collaborators.html`. Linked from main nav as "Lab".
- **Static assets**: PDFs at root (e.g. `26smooth.pdf`, kept at root for stable external links). Images in `assets/img/`. Old/unlinked stuff moved to `old/`.

## Tools (imported from the aiez org)
The tool sources are repos in the GitHub org `aiez` (local checkouts at
`~/gits/aiez/<slug>`, e.g. `~/gits/aiez/luk`; the old `~/gists` tree is
dead). `make tools` runs `~/gits/aiez/gistsite/gistsite.py -g aiez`
(needs network + pandoc), which pulls every org repo's `README.md` via
the GitHub API, strips repo-only lines (shields badges, `**Files:**`
TOC, relative-file links), and renders the catalog to `tools/`:
`tools/index.html` (roster) + `tools/<slug>.html` (one per tool).
Everything in `tools/` is GENERATED — don't hand-edit; regenerate after
README changes. Curate by exclusion: edit `SKIP` (and `DOOT`/`ORG`) in
the `Makefile`. Some tools also ship on package managers (e.g. `luk` on
luarocks as `timm/luk`).

### Tools vs Blog — what goes where (a repo may ship two docs)
- `README.md` — the man-page → **Tools** (auto-imported by `make tools`).
  One per repo.
- `<name>.md` — an optional long-form "tour" / genetic-stanza tutorial →
  a **Blog** post. Render it with pandoc through `etc/blog.html` (the fyi
  chrome template), e.g.
  `pandoc ~/gits/aiez/<g>/<name>.md -s --template=etc/blog.html
  --syntax-highlighting=breezedark --metadata title="..." --metadata
  slug=<name> --metadata description="..." -o <name>.html`, then add a
  row to `blog.html` Posts (and usually `news.html`). **Copy any images
  the tour uses into `assets/img/` and repoint the `src=` — fyi never
  reads from other repos.**
- Never put the long tour in Tools (the strip rules mangle it); never put
  the man-page in Blog (too terse). Cross-link the two.

## Page Structure
All pages share:
- `<nav>`: home icon (left, → `index.html`; on irl pages → `irl.html`) + section links + `papers:` group with arxiv & Scholar icons (right). Flex with `flex-wrap: wrap; gap: 8px;` so it wraps cleanly on narrow screens.
- Photo + h1 + contact lines (icon + text for phone/email).
- `<hr>` separators.
- Footer: NC State logo, copyright, css link, designed.2.last.

## Conventions
- All visible text lowercase via CSS `text-transform: lowercase` on `nav, h1, h2, h3, p`. Override with inline `style="text-transform:none"` when needed (e.g. mission-statement quote).
- Recruit-style call-out boxes: amber border, dark `#2a2218` background, centered, max-width 75%. Used for "wanna work with me?" (index), "join my reading group" (teaching `#reading-group`), "join us?" (irl).
- News table format: 3-column `<table class="news">`. Col 1 = `<b>MMM'YR</b>` (skip on continuation rows). Col 2 = type icon (FA, narrow, muted). Col 3 = title with optional `<a>`.
- **News split (2026-05)**: canonical full news lives in `news.html`. `index.html` shows only top 5 rows + "> more news & older" link to `news.html`. When adding news: prepend to `news.html` first, then mirror new top 5 onto `index.html`.

## New Paper Workflow
When user announces a new accepted paper, update these locations:

1. **News** — prepend row to `news.html` (canonical), then mirror onto `index.html` top 5 (drop oldest). See `ADD-NEWS-HINT` comment.
2. **research.html Recent Work** — insert `<li>` under matching topic h3 (see `ADD-PAPER-HINT` comment).
3. **research.html venues bar** — increment venue count, bar width = `round(100 * count / 36)`. New venue → `Other` count +1.
4. **irl-projects.html** — add `<li>` under existing project, OR new `<h2>` section (`ADD-PROJECT-HINT` comment has template).
5. **irl-people.html** — for each student-coauthor, prepend to their "Recent" `<ul>` (keep ≤3).

**Auto-derive when possible**: title/authors/abstract via `WebFetch` arxiv; student lead from `irl-people.html`; year from arxiv ID + submission date.

**Must ask user**: topic bucket (AI for Less / LLMs / Security / Analytics / Trust / Other); venue (target journal/conf, since arxiv preprint doesn't say); whether to create new IRL project section.

## Style Preferences
- Compact — minimize vertical scrolling.
- Don't add features beyond what's asked.
- Keep pages self-contained (single HTML file).
- Less is more: prefer dropping over adding.

## Handoff Command
When told to "hand off" or running out of context on a complex task:
- Write `HANDOFF.md` with: what the task is, what you tried, what worked, what didn't, and what remains.
- Goal: next agent loads `HANDOFF.md` alone and has full context to finish the job.
- Delete `HANDOFF.md` when task is complete.
