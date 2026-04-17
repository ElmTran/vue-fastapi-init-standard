# Repository Working Rules

This repository uses the following local rule files as the authoritative development guides for all future agent work:

- `./backend-py.md`
- `./frontend-vue.md`
- `./DESIGN.md`

Agents must always read and follow these files before proposing, generating, or editing code in this workspace.

## Rule Priority

When working in this repository, apply constraints in this order:

1. Direct user request
2. This `AGENTS.md`
3. `backend-py.md` for backend and API work
4. `frontend-vue.md` for frontend and UI implementation work
5. `DESIGN.md` for visual design, layout, typography, color, and component styling work
6. Existing repository patterns in the touched files

If guidance conflicts:

- Prefer the more specific file for the area being changed
- Preserve existing repository conventions unless the user asks to change them
- Ask the user before making a choice when two rules have non-obvious tradeoffs

## Always-On Workflow

Before starting any substantial implementation:

- Identify whether the task is backend, frontend, design, or mixed
- Re-read the relevant rule file(s) before editing
- State which rule file(s) are being applied in a short progress update

Before any code edit:

- Match the repository stack and architecture from the relevant rule file
- Keep diffs small and scoped
- Avoid unrelated refactors

After implementation:

- Verify the result against the relevant rule file checklist
- Call out any deliberate deviations and why they were necessary

## Backend Rules

For Python, FastAPI, API, config, models, services, tasks, validation, or backend performance work, agents must follow `./backend-py.md`.

Required defaults:

- Use Python 3.13+, FastAPI, Pydantic or pydantic-settings, and `uv` workflows when applicable
- Keep code inside an `app/` package layout where relevant
- Use clear separation between routing, validation, persistence, and domain logic
- Use typed public APIs
- Prefer async for I/O
- Never raise bare `Exception`; use a unified app error hierarchy
- Return unified JSON error envelopes
- Keep diffs minimal and avoid creating god modules
- Follow REST conventions with versioned routes such as `/v1/...`
- Preserve `X-Trace-Id` semantics if request flow or logging is touched

## Frontend Rules

For UI, pages, components, routing, API client, composables, or frontend architecture work, agents must follow `./frontend-vue.md`.

Required defaults:

- Use Vue 3 + TypeScript + Vite
- Use `pnpm` for package and script workflows
- Prefer component-first structure and small files
- Put heavy logic into composables instead of views when appropriate
- Follow existing alias and project structure conventions
- Prefer shadcn-vue and existing UI primitives over ad hoc raw HTML when appropriate
- Keep stores focused and small
- Do not introduce React, Next.js, or unrelated frontend stacks

## Design Rules

For layouts, styling, components, theming, visual polish, landing pages, dashboards, and any UI presentation work, agents must follow `./DESIGN.md`.

Required defaults:

- Use cream `#f7f4ed` as the base page background instead of plain white
- Use charcoal `#1c1c1c` as the primary text and dark action color
- Use `#eceae4` or opacity-derived charcoal borders instead of heavy shadows
- Keep the warm, restrained Lovable-inspired visual language
- Respect typography rules, spacing scale, border radius scale, and button treatment
- Use inset-shadow dark primary buttons where the design calls for a main CTA
- Preserve responsive behavior and avoid generic default styling

## Task Routing

Use this quick routing guide:

- Backend-only request: read `backend-py.md`
- Frontend-only request: read `frontend-vue.md` and `DESIGN.md`
- Full-stack feature: read all three files
- Pure product or PRD work: use these files only when discussing implementation, UI, or architecture implications

## Non-Goals

Unless the user explicitly asks otherwise, do not:

- Switch the stack away from Vue + Vite + FastAPI
- Introduce a different design system
- Add large documentation files unrelated to the task
- Perform broad refactors only for personal preference

## Expected Progress Updates

When relevant, use short updates like:

- `Reviewing backend-py.md before touching the API layer.`
- `Applying frontend-vue.md and DESIGN.md before editing the results page.`
- `Cross-checking the implementation against local repository rules.`

These updates should be concise, but the behavior is mandatory.