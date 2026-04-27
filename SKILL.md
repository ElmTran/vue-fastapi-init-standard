---
name: vue-fastapi-init-standard
description: Bootstrap and standardize a new Vue 3 + Vite frontend and FastAPI backend project with documented frontend setup steps, generated backend starter structure, a project-level AGENTS.md file with embedded backend and frontend rules, and a calm minimal tool-style design system. Use when Codex or another coding agent needs to create an initial full-stack workspace, scaffold the backend, document the frontend initialization process, generate a project-level AGENTS.md file, preserve a full DESIGN.md reference, or keep future implementation aligned with the same architecture and coding standards.
---

# Vue FastAPI Init Standard

Use this skill to create or normalize a reusable project baseline for a Vue 3 frontend and FastAPI backend.

## Workflow

1. Read `references/development-rules.md` first.
2. Read `references/frontend-setup.md` when the task touches frontend initialization, routing, components, styling, or design setup.
3. Read `references/backend-standard.md` when the task touches backend scaffolding, API modules, config, errors, tracing, or services.
4. Create a project-level `AGENTS.md` from `assets/AGENTS.template.md` when starting a new project.
5. Copy `assets/DESIGN.template.md` into the new project as `DESIGN.md`.
6. Copy the backend starter from `assets/backend-template/` when the user wants a ready backend skeleton.
7. Keep changes small and architectural. Do not invent product features unless the user explicitly asks.

## What This Skill Should Produce

- A documented frontend bootstrap path based on `pnpm create vite`
- A FastAPI backend starter with `app/` package layout
- A project-level `AGENTS.md` file that embeds backend and frontend development rules
- A full `DESIGN.md` file kept as a standalone style reference
- Shared engineering rules that keep coding agents from drifting away from the chosen stack
- Development habits that encourage small files, clear separation, and reusable structure

## AGENTS.md Requirement

When using this skill for a new project:

- Create `AGENTS.md` at the project root by adapting `assets/AGENTS.template.md`.
- Keep backend and frontend coding rules inline in `AGENTS.md` instead of creating separate `backend-py.md` and `frontend-vue.md` files.
- Keep it implementation-facing rather than product-facing.
- Use it as the primary rule file for future agents.
- Keep product requirements, features, and PRD content outside `AGENTS.md`.

## Design File Requirement

When using this skill for a new project:

- Copy `assets/DESIGN.template.md` into the project root as `DESIGN.md`.
- Preserve the design file as a standalone reference.
- Treat it as the visual style guide for later UI work.

## Resources

- `references/frontend-setup.md`: manual frontend bootstrap steps and integration sequence
- `references/backend-standard.md`: backend architecture and implementation expectations
- `references/development-rules.md`: shared standards, design rules, and anti-drift constraints
- `assets/AGENTS.template.md`: root-level AGENTS.md template for new projects
- `assets/DESIGN.template.md`: full standalone design reference for new projects
- `assets/backend-template/`: starter backend files to copy into a new project
