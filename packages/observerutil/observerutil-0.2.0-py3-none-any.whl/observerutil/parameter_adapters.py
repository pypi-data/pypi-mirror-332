"""
Module of parameter adapters
"""

from typing import Any, Callable, Dict, Iterable, Tuple

from .interfaces import IParametersAdapter


# pylint: disable=too-few-public-methods
class ParametersAdapters(IParametersAdapter):
    """
    Apply each parameters adapter in order
    """

    def __init__(self, adapters: Iterable[IParametersAdapter]):
        self.adapters = adapters

    def __call__(self, *args, **kwargs) -> Tuple[Iterable[Any], Dict[str, Any]]:
        for adapter in self.adapters:
            args, kwargs = adapter(*args, **kwargs)
        return args, kwargs


# -------------------------------------------------------------------------------------------------

# pylint: disable=too-few-public-methods
class CustomParametersAdapter(IParametersAdapter):
    """
    Customizable adapter by single func to adapt.
    Make adapting simpler
    """
    def __init__(self, func: Callable):
        self.func = func


# pylint: disable=too-few-public-methods
class AdaptArgs(CustomParametersAdapter):
    """
    Adapt args with single func
    """

    def __call__(self, *args, **kwargs) -> Tuple[Iterable[Any], Dict[str, Any]]:
        return self.func(args), kwargs


# pylint: disable=too-few-public-methods
class AdaptKwargs(CustomParametersAdapter):
    """
    Adapt kwargs with single func
    """

    def __call__(self, *args, **kwargs) -> Tuple[Iterable[Any], Dict[str, Any]]:
        return args, self.func(kwargs)


# pylint: disable=too-few-public-methods
class AdaptArgsKwargs(CustomParametersAdapter):
    """
    Adapt args and kwargs with single func
    """

    def __call__(self, *args, **kwargs) -> Tuple[Iterable[Any], Dict[str, Any]]:
        return self.func(args, kwargs)


# pylint: disable=too-few-public-methods
class AdaptEachArg(CustomParametersAdapter):
    """
    Adapt each arg with single func
    """

    def __call__(self, *args, **kwargs) -> Tuple[Iterable[Any], Dict[str, Any]]:
        return [self.func(arg) for arg in args], kwargs
