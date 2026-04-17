# Frontend Setup

Use this reference when preparing the frontend part of the starter project.

## Goal

Document the initialization path for a Vue 3 + TypeScript + Vite frontend without forcing execution unless the user asks for it.

## Initialization Steps

1. Run `pnpm create vite` and choose Vue + TypeScript.
2. Install dependencies with `pnpm install`.
3. Integrate Tailwind by following the Vite guide at `https://tailwindcss.com/docs/installation/using-vite`.
4. Integrate Iconify for Vue by following `https://iconify.design/docs/icon-components/vue/`.
5. Integrate shadcn-vue for an existing Vite project by following the Vite existing-project flow at `https://ui.shadcn.com/docs/installation/vite`.

## Expected Frontend Stack

- Vue 3
- TypeScript
- Vite
- Vue Router
- Pinia
- Tailwind CSS
- Iconify via `@iconify/vue`
- shadcn-vue
- pnpm

## Project Shape

Prefer a small, component-first structure:

```text
src/
  components/
    ui/
    shared/
  composables/
  router/
  stores/
  views/
  api/
  types/
  styles/
```

## Development Habits

- Build UI from small, reusable components.
- Keep one concern per file whenever possible.
- Split files when logic, template, or styling starts dominating the component.
- Keep views orchestration-focused rather than logic-heavy.
- Move reusable stateful logic into composables.
- Keep stores small and domain-focused.
- Prefer shared behavior and shared types over duplication.
- Match surrounding naming and composition API patterns.

## Tooling Habits

- Use `pnpm` for installs and scripts.
- Prefer `pnpm run dev`, `pnpm run build`, and related scripts over npm or yarn.
- Keep aliases consistent with `@ -> ./src` in root `tsconfig.json`.
- Add shadcn-vue components with the Vue CLI flow, not the React shadcn CLI.
- Prefer shadcn-vue and existing UI primitives over ad hoc raw HTML when appropriate.

## Design Direction

Apply these defaults unless the user requests another direction:

- Base background: `#f7f4ed`
- Primary text and dark CTA: `#1c1c1c`
- Passive border: `#eceae4`
- Interactive border: `rgba(28,28,28,0.4)`
- Avoid heavy card shadows.
- Prefer restrained, warm, editorial styling.

## What Not To Do

- Do not introduce React, Next.js, Nuxt, or unrelated frontend stacks.
- Do not replace pnpm with npm or yarn.
- Do not default to white backgrounds or generic template styling.
- Do not add business-specific routes or screens during initialization unless requested.
- Do not let a starter view become a large catch-all file.