# coding=utf-8
"""
Interfaces
"""

from abc import abstractmethod
from typing import Any, Dict, Iterable, Tuple


# pylint: disable=too-few-public-methods
class IObserver:
    """
    Observer interface.
    Get message and do some work with it.
    """
    @abstractmethod
    def __call__(self, *args, **kwags):
        """
        Listen message
        """
        raise NotImplementedError()


class ISubject:
    """
    Subject iterface.
    """


# pylint: disable=too-few-public-methods
class IParametersAdapter:
    """
    Parameters adapter interface.
    """

    def __call__(self, *args, **kwargs) -> Tuple[Iterable[Any], Dict[str, Any]]:
        """
        Adapt parameters for observer
        """
        return args, kwargs


# pylint: disable=too-few-public-methods
class IErrorHandler:
    """
    Error handler interface.
    Get exception and do some work with it.
    """

    @abstractmethod
    def __call__(self, exc: Exception):
        """
        Handle exception
        """
        raise NotImplementedError()
