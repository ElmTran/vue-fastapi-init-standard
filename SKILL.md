---
name: vue-fastapi-init-standard
description: Bootstrap and standardize a new Vue 3 + Vite frontend and FastAPI backend project with documented frontend setup steps, generated backend starter structure, Lovable-inspired design rules, and strict agent development guardrails. Use when Codex or another coding agent needs to create an initial full-stack workspace, scaffold the backend, document the frontend initialization process, or keep future implementation aligned with the same architecture and coding standards.
---

# Vue FastAPI Init Standard

Use this skill to create or normalize a reusable project baseline for a Vue 3 frontend and FastAPI backend.

## Workflow

1. Read `references/development-rules.md` first.
2. Read `references/frontend-setup.md` when the task touches frontend initialization, routing, components, styling, or design setup.
3. Read `references/backend-standard.md` when the task touches backend scaffolding, API modules, config, errors, tracing, or services.
4. Copy the backend starter from `assets/backend-template/` when the user wants a ready backend skeleton.
5. Keep changes small and architectural. Do not invent product features unless the user explicitly asks.

## What This Skill Should Produce

- A documented frontend bootstrap path based on `pnpm create vite`
- A FastAPI backend starter with `app/` package layout
- Shared engineering rules that keep coding agents from drifting away from the chosen stack
- Design guidance for warm cream, charcoal, low-shadow UI work
- Development habits that encourage small files, clear separation, and reusable structure

## Frontend Rules

For a new frontend app:

- Do not silently switch stacks away from Vue 3 + TypeScript + Vite.
- Treat frontend initialization as a documented sequence unless the user explicitly asks you to run the commands.
- Prefer `pnpm` for all package and script workflows.
- Add Tailwind, Iconify, and shadcn-vue in the order documented in `references/frontend-setup.md`.
- Keep heavy view logic in composables and keep stores focused.
- Prefer small, component-first files over monolithic route components.
- Use design tokens and follow the cream-and-charcoal design language from `references/development-rules.md`.

## Backend Rules

For backend setup:

- Use Python 3.13+, `uv`, FastAPI, and `pydantic-settings`.
- Keep code under `app/` with clean separation across API, schemas, services, repositories, and core modules.
- Preserve unified JSON error envelopes and `X-Trace-Id` semantics.
- Use async for I/O paths and typed public APIs.
- Prefer small modules with one responsibility each.
- Never raise bare `Exception` in application code; define domain errors beneath `AppError`.

## Agent Guardrails

When Codex, Claude Code, or another agent uses this skill:

- Start by naming which references are being applied.
- Keep the project template generic. Product requirements belong in PRD files, not in the starter architecture.
- Avoid broad refactors, extra stacks, or alternate design systems.
- Preserve the selected baseline even when adding future features, unless the user explicitly approves a change in direction.
- If two valid architectural options have non-obvious tradeoffs, pause and ask once before committing.

## Resources

- `references/frontend-setup.md`: manual frontend bootstrap steps and integration sequence
- `references/backend-standard.md`: backend architecture and implementation expectations
- `references/development-rules.md`: shared standards, design rules, and anti-drift constraints
- `assets/backend-template/`: starter backend files to copy into a new project