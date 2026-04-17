# Backend Standard

Use this reference when generating or reviewing the backend starter.

## Stack

- Python 3.13+
- FastAPI
- Pydantic / pydantic-settings
- uv

## Starter Layout

```text
app/
  api/
    router.py
    v1/
      router.py
      endpoints/
        health.py
  core/
    app.py
    config.py
    logging.py
    trace.py
    middleware/
      trace.py
    errors/
      base.py
      handlers.py
  models/
  repositories/
  schemas/
    common.py
    health.py
  services/
  tasks/
  main.py
main.py
pyproject.toml
.env.example
```

## Architecture Rules

- Keep `app/` as the installable package root.
- Prefer small files and one responsibility per module.
- Separate routing, validation, persistence, and domain logic.
- Keep routers thin and push non-trivial logic into services.
- Use typed response models. Do not return ORM rows directly over HTTP.
- Keep route prefixes versioned, such as `/v1`.
- Extend existing patterns instead of inventing alternate structures.
- Ensure `AGENTS.md` references backend rules so later agents keep using this structure.

## Error and Trace Rules

- Use a unified `AppError` hierarchy.
- Return a unified JSON error envelope with `success: false` and `error: { code, message, request_id, details }`.
- Preserve `X-Trace-Id` request and response semantics.
- Sanitize unexpected errors in HTTP responses.
- Log real failures with the trace id for easier correlation.

## Implementation Defaults

- Prefer async for I/O.
- Use f-strings and typed public APIs.
- Use `pydantic-settings` for configuration.
- Keep docs endpoints configurable through settings.
- Provide a simple `/v1/health` endpoint in the starter.
- Use clear abstractions only when multiple implementations actually need them.

## Performance Habits

- Avoid N+1 query patterns.
- Batch writes where possible instead of looping one row at a time.
- Avoid `SELECT *` style data access in hot paths.
- Use caching and queues for expensive or non-critical work when needed.
- Measure before optimizing.

## Development Commands

```bash
uv venv
uv sync
uv run fastapi dev app/main.py
uv run pytest
```

## What Not To Do

- Do not raise bare `Exception` in application code.
- Do not collapse everything into a single file.
- Do not add business endpoints during initialization unless requested.
- Do not remove unified error handling or tracing just to simplify the starter.
- Do not let services, routers, or config modules become god modules.