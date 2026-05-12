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

- Default to a crisp, polished workspace interface rather than a showcase or landing-page layout.
- Keep typography compact, confident, and readable; avoid oversized hero text.
- Use a near-white page, translucent white surfaces, one restrained Burgundy accent, and very light warm-neutral borders.
- Prefer shadcn-vue primitives with tuned CSS tokens over ad hoc component styling.
- Use borders, backdrop blur, and soft shadows sparingly; rely on spacing before adding more card chrome.
- Keep motion subtle: gentle fade, slight translate, restrained hover feedback.

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
