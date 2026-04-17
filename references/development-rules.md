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

## Frontend Guardrails

- Use Vue 3 + TypeScript + Vite.
- Use pnpm.
- Prefer component-first structure.
- Use composables for reusable logic.
- Prefer shadcn-vue primitives over ad hoc markup when appropriate.

## Backend Guardrails

- Use FastAPI + uv + pydantic-settings.
- Keep the `app/` package layout.
- Separate API, schemas, repositories, services, and core concerns.
- Keep unified error envelopes and `X-Trace-Id` support.

## Design Guardrails

- Use cream `#f7f4ed` as the default page background.
- Use charcoal `#1c1c1c` for main text and dark CTA surfaces.
- Use `#eceae4` or opacity-derived charcoal borders in place of heavy shadows.
- Preserve the warm, restrained Lovable-inspired style.
- Keep typography editorial and spacing generous.

## Agent Anti-Drift Rules

When an agent is implementing from this starter:

- Do not swap stacks because of personal preference.
- Do not introduce a second design system.
- Do not let generated examples become product requirements.
- Do not overfit initialization code to a single future feature.
- Keep PRD and feature logic separate from architecture files and starter code.

## Good Progress Updates

- `Applying frontend setup and design references before touching the UI bootstrap.`
- `Applying backend standard before scaffolding the API package.`
- `Cross-checking the implementation against the starter rules.`