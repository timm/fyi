# Project: timm.fyi — Personal Academic Website

## Tech Stack
- Single-file HTML pages with inline `<style>` in `<head>`
- No build tools, no JS frameworks — pure HTML + CSS
- CSS-only tabs via radio buttons (no JavaScript)
- Font Awesome icons, IBM Plex Sans / IBM Plex Mono fonts
- All pages (main + blog/sub) use `site.css` (the "99 words of css" — was `min.css` until 2026-05; old `style.css` moved to `old/`)

## Dark Theme
- CSS variables defined in `:root` — always use them, never hardcode colors
- Key vars: `--bg`, `--fg`, `--heading`, `--accent` (#ffb86c amber), `--card`, `--card-2`, `--muted`, `--border`
- Dark logos need `filter: invert(1) brightness(1.05)` (Meta, LexisNexis, NSA)
- Dashed separators use `--muted` color (not `--border` — too dark to see)

## Layout — Home Page (a.html)
- **Link bar** at top (email, phone, scholar, pre-prints)
- **Header**: photo (`assets/img/timm.png`, ~105px) + name + 3 subtitle lines
- **Recruit box** ("Join My Lab?") with rocket icon, full-width above tabs in left column
- **Two columns**: tabbed content (left), news+service (right, 260px)
- **Responsive**: stacks at 680px — news goes to BOTTOM (order:1), not top
- **Gap** between columns: 24px

## Tabs
- Top-level: About (default/landing), Research, Teaching
- Research has 6 sub-tabs: AI for Less, LLMs, Security, Analytics, Trust, Other
- Pill-style labels, amber background when active
- Tab content has fade-in animation

## Right Column
- "News" pill header (styled like always-on tab)
- Month subheadings in monospace amber uppercase
- News = papers, talks, blogs, keynotes, milestones
- Dashed separator (60% width, centered, `--muted` color)
- "Service" pill header below
- Service = PC memberships, area chairing, editorial, review committees
- 2025 items grouped under single "2025" subheading (not per-month)

## Paper Lists
- Venue in monospace pill: `<b>FSE'26</b>` — styled with `--accent` color, border, rounded
- Short title + [pdf] link
- Funder logos in About tab: two centered rows (MS+Meta top, LN+NSF+NASA+NSA bottom)

## Sub-Pages (e.g., higher_way.html, irl.html)
- Same header as home page (photo + name + 3 lines), same `site.css`
- No news column on sub-pages
- Blinking cursor span: `<span class="cursor">&#9612;</span>`

## Style Preferences
- Compact — minimize vertical scrolling
- No unnecessary headings — use pill headers or sub-tabs instead
- Don't add features beyond what's asked
- Keep pages self-contained (single HTML file)
- When adding news items, separate papers/talks (News) from committee work (Service)

## New Paper Workflow
When user announces a new accepted paper, update these locations:

1. **index.html → News table** — prepend row at top (look for `ADD-NEWS-HINT` comment).
2. **research.html → Recent Work `<h3>` matching topic** — insert `<li>` at top (look for `ADD-PAPER-HINT` comment near each topic).
3. **research.html → venues bar** — increment venue count, recompute bar width = `round(100 * count / 36)` (look for `ADD-PAPER-HINT` in DBLP DATA SOURCE comment block).
4. **irl-projects.html** — if it fits an existing project, add `<li>` under that section. If it opens a new thread, add a new `<h2>` section (template in `ADD-PROJECT-HINT` comment).
5. **irl-people.html** — for each student-coauthor, prepend the new paper to their "Recent" line (keep ≤3). Look for `ADD-PAPER-HINT` comment.

**Auto-derive when possible**:
- Title, authors, abstract — fetch from arxiv URL (`WebFetch`).
- Student lead — current students listed in `irl-who.html`.
- Year — from arxiv ID (e.g. `2512.xxxxx` → 2025/2026 boundary; check arxiv submission date).

**Must ask user**:
- Topic bucket (Analytics / Trust / LLMs / Security / AI for Less / Trust / Other).
- Venue (arxiv preprint doesn't say target journal/conf).
- Whether to create new IRL project section.

## Handoff Command
When told to "hand off" or running out of context on a complex task:
- Write `HANDOFF.md` with: what the task is, what you tried, what worked, what didn't, and what remains
- Goal: next agent loads `HANDOFF.md` alone and has full context to finish the job
- Delete `HANDOFF.md` when task is complete
