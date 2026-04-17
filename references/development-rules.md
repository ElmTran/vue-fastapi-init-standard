# Development Rules

Read this file before making architectural or implementation changes.

## Priority

1. Direct user request
2. Existing repository rules in the target project
3. This skill's backend, frontend, and design rules
4. Existing file-local conventions in touched files

## Shared Guardrails

- Keep the starter generic; do not mix product features into the baseline.
- State which rule set you are applying before substantial work.
- Keep diffs small and scoped.
- Avoid unrelated refactors.
- Ask before taking a path with meaningful architectural tradeoffs.
- Prefer extending an existing pattern over introducing a parallel pattern.
- Create `AGENTS.md` early in a new project so future agents inherit the same constraints.

## Frontend Guardrails

- Use Vue 3 + TypeScript + Vite.
- Use pnpm.
- Prefer component-first structure.
- Prefer small files that are easy to scan at a glance.
- Use composables for reusable logic.
- Keep views orchestration-focused.
- Keep stores small and domain-focused.
- Prefer shadcn-vue primitives over ad hoc markup when appropriate.

## Backend Guardrails

- Use FastAPI + uv + pydantic-settings.
- Keep the `app/` package layout.
- Prefer one responsibility per module.
- Separate API, schemas, repositories, services, and core concerns.
- Keep unified error envelopes and `X-Trace-Id` support.
- Prefer thin routers and explicit domain/service boundaries.

## Design Guardrails

- Use cream `#f7f4ed` as the default page background.
- Use charcoal `#1c1c1c` for main text and dark CTA surfaces.
- Use `#eceae4` or opacity-derived charcoal borders in place of heavy shadows.
- Preserve the warm, restrained Lovable-inspired style.
- Keep typography editorial and spacing generous.
- Prefer depth from borders, tone, and inset treatment instead of dramatic elevation.
- Use full-pill radius only for pill-style controls, not every rectangular button.

## Agent Anti-Drift Rules

When an agent is implementing from this starter:

- Do not swap stacks because of personal preference.
- Do not introduce a second design system.
- Do not let generated examples become product requirements.
- Do not overfit initialization code to a single future feature.
- Keep PRD and feature logic separate from architecture files and starter code.
- Do not allow starter files to grow into large catch-all modules without first extracting structure.
- Treat `AGENTS.md` as the root instruction file for future repository work.

## Good Progress Updates

- `Applying frontend setup and design references before touching the UI bootstrap.`
- `Applying backend standard before scaffolding the API package.`
- `Creating AGENTS.md so future implementation follows the same rules.`
- `Cross-checking the implementation against the starter rules.`