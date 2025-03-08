# ruff: noqa: SLF001
from __future__ import annotations

import builtins
import importlib._bootstrap
import logging
import site
import sys
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from collections.abc import Mapping
    from types import CodeType
    from typing import Any

    from _typeshed import ReadableBuffer

__version__ = "0.0.1"

KNOWN_EXEC_CALLERS = {
    site.addpackage.__code__,
    importlib._bootstrap._call_with_frames_removed.__code__,  # type: ignore[reportAttributeAccessIssue]
}
KNOWN_EVAL_CALLERS = set()

logger = logging.getLogger(__name__)

original_exec = builtins.exec
original_eval = builtins.eval


class ExecBlockedError(RuntimeError):
    def __init__(
        self,
        caller: CodeType,
        source: str | ReadableBuffer | CodeType,
        globals: dict[str, Any] | None = None,
        locals: Mapping[str, object] | None = None,
        *args: object,
    ) -> None:
        super().__init__(f"blocked execution of {source!r}", *args)
        self.caller = caller
        self.source = source
        self.globals = globals
        self.locals = locals


class EvalBlockedError(ExecBlockedError):
    pass


def wrap_builtin(builtin: Callable, /) -> Callable[[Callable], Callable]:
    def decorator(func: Callable, /) -> Callable:
        builtins.__dict__[builtin.__name__] = func
        return func

    return decorator


@wrap_builtin(exec)
def safe_exec(
    source: str | ReadableBuffer | CodeType,
    globals: dict[str, Any] | None = None,
    locals: Mapping[str, object] | None = None,
) -> None:
    caller = sys._getframe(1).f_code
    if caller in KNOWN_EXEC_CALLERS:
        logging.info(
            "allowed exec call by %r from %r:%i",
            caller.co_name,
            caller.co_filename,
            caller.co_firstlineno,
        )
        return original_exec(source, globals, locals)
    raise ExecBlockedError(caller=caller, source=source, globals=globals, locals=locals)


@wrap_builtin(eval)
def save_eval(
    source: str | ReadableBuffer | CodeType,
    globals: dict[str, Any] | None = None,
    locals: Mapping[str, object] | None = None,
) -> Any:  # noqa: ANN401
    caller = sys._getframe(1).f_code
    if caller in KNOWN_EVAL_CALLERS:
        logging.info(
            "allowed eval call by %r from %r:%i",
            caller.co_name,
            caller.co_filename,
            caller.co_firstlineno,
        )
        return original_eval(source, globals, locals)
    raise EvalBlockedError(caller=caller, source=source, globals=globals, locals=locals)
