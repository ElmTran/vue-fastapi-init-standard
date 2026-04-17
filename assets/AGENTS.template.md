# Repository Working Rules

This repository uses this `AGENTS.md` file as the authoritative development guide for all future agent work.

In addition, visual design work must follow:

- `./DESIGN.md`

Agents must always read and follow these instructions before proposing, generating, or editing code in this workspace.

## Rule Priority

When working in this repository, apply constraints in this order:

1. Direct user request
2. This `AGENTS.md`
3. `DESIGN.md` for visual design, layout, typography, color, and component styling work
4. Existing repository patterns in the touched files

If guidance conflicts:

- Prefer the more specific section for the area being changed
- Preserve existing repository conventions unless the user asks to change them
- Ask the user before making a choice when two rules have non-obvious tradeoffs

## Always-On Workflow

Before starting any substantial implementation:

- Identify whether the task is backend, frontend, design, or mixed
- Re-read the relevant section(s) in this file and `DESIGN.md` when UI presentation is touched
- State which rule source(s) are being applied in a short progress update

Before any code edit:

- Match the repository stack and architecture from the relevant rule section
- Keep diffs small and scoped
- Avoid unrelated refactors

After implementation:

- Verify the result against the relevant rule section
- Call out any deliberate deviations and why they were necessary

## Backend Rules

For Python, FastAPI, API, config, models, services, tasks, validation, or backend performance work:

- Use Python 3.13+, FastAPI, Pydantic or pydantic-settings, and `uv` workflows when applicable
- Keep code inside an `app/` package layout where relevant
- Use clear separation between routing, validation, persistence, and domain logic
- Prefer one responsibility per module and small files that are easy to scan
- Keep routers thin and move heavier logic into services or helpers
- Use typed public APIs
- Prefer async for I/O
- Never raise bare `Exception`; use a unified app error hierarchy
- Return unified JSON error envelopes
- Keep diffs minimal and avoid creating god modules
- Follow REST conventions with versioned routes such as `/v1/...`
- Preserve `X-Trace-Id` semantics if request flow or logging is touched
- Prefer extending existing patterns instead of inventing parallel structures

## Frontend Rules

For UI, pages, components, routing, API client, composables, or frontend architecture work:

- Use Vue 3 + TypeScript + Vite
- Use `pnpm` for package and script workflows
- Prefer component-first structure and small files
- Put heavy logic into composables instead of views when appropriate
- Keep views orchestration-focused rather than logic-heavy
- Keep stores focused and small
- Prefer reuse over duplicating large template blocks
- Follow existing alias and project structure conventions
- Prefer shadcn-vue and existing UI primitives over ad hoc raw HTML when appropriate
- Add shadcn-vue components with the Vue CLI flow, not the React shadcn CLI
- Do not introduce React, Next.js, or unrelated frontend stacks

## Design Rules

For layouts, styling, components, theming, visual polish, landing pages, dashboards, and any UI presentation work, follow `./DESIGN.md`.

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

- Backend-only request: apply the backend rules in this file
- Frontend-only request: apply the frontend rules in this file and `DESIGN.md`
- Full-stack feature: apply both backend and frontend rules, plus `DESIGN.md` when UI is involved
- Pure product or PRD work: use these files only when discussing implementation, UI, or architecture implications

## Non-Goals

Unless the user explicitly asks otherwise, do not:

- Switch the stack away from Vue + Vite + FastAPI
- Introduce a different design system
- Add large documentation files unrelated to the task
- Perform broad refactors only for personal preference

## Expected Progress Updates

When relevant, use short updates like:

- `Reviewing backend rules before touching the API layer.`
- `Applying frontend rules and DESIGN.md before editing the page.`
- `Cross-checking the implementation against local repository rules.`

These updates should be concise, but the behavior is mandatory.