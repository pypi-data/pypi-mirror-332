"""LightHousellm Client."""

from importlib import metadata
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from lighthousellm._expect import expect
    from lighthousellm.async_client import AsyncClient
    from lighthousellm.client import Client
    from lighthousellm.evaluation import aevaluate, evaluate
    from lighthousellm.evaluation.evaluator import EvaluationResult, RunEvaluator
    from lighthousellm.run_helpers import (
        get_current_run_tree,
        get_tracing_context,
        trace,
        traceable,
        tracing_context,
    )
    from lighthousellm.run_trees import RunTree
    from lighthousellm.testing._internal import test, unit
    from lighthousellm.utils import (
        ContextThreadPoolExecutor,
    )

# Avoid calling into importlib on every call to __version__
version = ""
try:
    version = metadata.version(__package__)
except metadata.PackageNotFoundError:
    pass


def __getattr__(name: str) -> Any:
    if name == "__version__":
        return version
    elif name == "Client":
        from lighthousellm.client import Client

        return Client
    elif name == "AsyncClient":
        from lighthousellm.async_client import AsyncClient

        return AsyncClient
    elif name == "RunTree":
        from lighthousellm.run_trees import RunTree

        return RunTree
    elif name == "EvaluationResult":
        from lighthousellm.evaluation.evaluator import EvaluationResult

        return EvaluationResult
    elif name == "RunEvaluator":
        from lighthousellm.evaluation.evaluator import RunEvaluator

        return RunEvaluator
    elif name == "trace":
        from lighthousellm.run_helpers import trace

        return trace
    elif name == "traceable":
        from lighthousellm.run_helpers import traceable

        return traceable

    elif name == "test":
        from lighthousellm.testing._internal import test

        return test

    elif name == "expect":
        from lighthousellm._expect import expect

        return expect
    elif name == "evaluate":
        from lighthousellm.evaluation import evaluate

        return evaluate

    elif name == "evaluate_existing":
        from lighthousellm.evaluation import evaluate_existing

        return evaluate_existing
    elif name == "aevaluate":
        from lighthousellm.evaluation import aevaluate

        return aevaluate
    elif name == "aevaluate_existing":
        from lighthousellm.evaluation import aevaluate_existing

        return aevaluate_existing
    elif name == "tracing_context":
        from lighthousellm.run_helpers import tracing_context

        return tracing_context

    elif name == "get_tracing_context":
        from lighthousellm.run_helpers import get_tracing_context

        return get_tracing_context

    elif name == "get_current_run_tree":
        from lighthousellm.run_helpers import get_current_run_tree

        return get_current_run_tree

    elif name == "unit":
        from lighthousellm.testing._internal import unit

        return unit
    elif name == "ContextThreadPoolExecutor":
        from lighthousellm.utils import (
            ContextThreadPoolExecutor,
        )

        return ContextThreadPoolExecutor

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "Client",
    "RunTree",
    "__version__",
    "EvaluationResult",
    "RunEvaluator",
    "anonymizer",
    "traceable",
    "trace",
    "unit",
    "test",
    "expect",
    "evaluate",
    "aevaluate",
    "tracing_context",
    "get_tracing_context",
    "get_current_run_tree",
    "ContextThreadPoolExecutor",
    "AsyncClient",
]
