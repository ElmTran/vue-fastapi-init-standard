# vue-fastapi-init-standard

A reusable Codex skill for bootstrapping a Vue 3 + Vite frontend and a FastAPI backend with strong architectural guardrails.

## What It Includes

- Frontend setup guidance for `pnpm create vite`
- Tailwind integration notes for Vite
- Iconify integration notes for Vue
- shadcn-vue installation guidance for an existing Vite project
- A generated FastAPI backend starter under `assets/backend-template`
- Shared development rules to keep coding agents aligned with the chosen stack and design system

## Skill Structure

```text
vue-fastapi-init-standard/
  SKILL.md
  agents/
    openai.yaml
  references/
    frontend-setup.md
    backend-standard.md
    development-rules.md
  assets/
    backend-template/
```

## Intended Use

Use this skill when you want Codex or another coding agent to:

- scaffold a standard full-stack starter
- document the frontend initialization path without executing it
- generate a backend starter structure immediately
- keep future work aligned with Vue 3, Vite, FastAPI, and the same design rules

Example prompt:

```text
Use $vue-fastapi-init-standard to scaffold a Vue 3 + FastAPI starter with documented frontend setup and a generated backend baseline.
```

## Design Direction

The skill carries a warm, restrained design language:

- Cream page background `#f7f4ed`
- Charcoal text and CTA `#1c1c1c`
- Light borders `#eceae4`
- Minimal shadow use
- Editorial spacing and typography guidance

## License

MIT