"""This module provides integration wrappers for popular open source eval frameworks.

to be used with LightHousellm.
"""

from lighthousellm.evaluation.integrations._langchain import LangChainStringEvaluator

__all__ = ["LangChainStringEvaluator"]
