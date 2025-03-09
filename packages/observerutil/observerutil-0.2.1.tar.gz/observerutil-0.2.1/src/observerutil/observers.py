# coding=utf-8
"""
Observers
"""

from typing import Any, Callable, Optional, Iterable

from .interfaces import (
    IObserver,
    IParametersAdapter,
    IErrorHandler,
)


# pylint: disable=too-few-public-methods
class Observer(IObserver):
    """
    Observer that can get message and do some work and handle errors.
    """
    def __init__(
        self,
        func: Callable,
        error_handler: Optional[IErrorHandler] = None,
    ):
        self.func = func
        self.error_handler = error_handler

    def __call__(self, *args, **kwargs):
        """
        Listen message.
        Catch errors by error_handler (if provided)
        """
        try:
            self.func(*args, **kwargs)
        except Exception as exc:  # pylint: disable=broad-exception-caught
            if callable(self.error_handler):
                self.error_handler(exc)


class Observers:
    """
    Registry of observers.
    It is not possible to subscribe each observer more than once.
    Provide parameters_adapter if you would like to adapt parameters for all registered observers.
    Any exceptions of observers will be excepted while sending message.
    """

    def __init__(
        self,
        observers: Optional[Iterable[IObserver | Callable]] = None,
        *,
        parameters_adapter: Optional[IParametersAdapter] = None,
    ):
        self.registry = {id(x): x for x in observers or []}
        self.parameters_adapter = parameters_adapter

    def __bool__(self):
        return bool(self.registry)

    def __iter__(self):
        return iter(self.registry.values())

    def __len__(self):
        return len(self.registry)

    def __call__(self, *args, **kwargs):
        self.notify(*args, **kwargs)

    def add(self, observer: Any):
        """
        Subscribe observer
        """
        self.registry[id(observer)] = observer

    def remove(self, observer: Any):
        """
        Unsubscribe observer
        """
        self.registry.pop(id(observer), None)

    def notify(self, *args, **kwargs):
        """
        Notify observers
        """
        if self.parameters_adapter:
            args, kwargs = self.parameters_adapter(*args, **kwargs)

        for observer in self:
            try:
                observer(*args, **kwargs)
            except Exception:  # pylint: disable=broad-exception-caught
                continue
