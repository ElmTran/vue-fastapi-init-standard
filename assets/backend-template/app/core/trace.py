from contextvars import ContextVar
from uuid import uuid4


_trace_id_ctx: ContextVar[str] = ContextVar("trace_id", default="")


def new_trace_id() -> str:
    return uuid4().hex


def set_trace_id(trace_id: str) -> None:
    _trace_id_ctx.set(trace_id)


def get_trace_id() -> str:
    trace_id = _trace_id_ctx.get()
    return trace_id or ""