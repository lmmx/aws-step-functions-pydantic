r"""
:mod:`sfn_val` provides Pydantic models for AWS step functions.

    >>> import sfn_val
"""

# Sphinx automodule relies on modules being exposed through `__all__` here

__all__ = ["generated", "StateMachine"]  # type: ignore

__author__ = "Louis Maddox"
__license__ = "MIT"
__description__ = "Pydantic models for AWS step functions"
__url__ = "https://github.com/lmmx/aws-step-functions-pydantic"
__uri__ = __url__
__email__ = "louismmx@gmail.com"

from .generated.base_state_machine import StateMachine
