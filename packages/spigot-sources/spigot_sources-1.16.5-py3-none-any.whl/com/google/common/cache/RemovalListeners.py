"""
Python module generated from Java source file com.google.common.cache.RemovalListeners

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.cache import *
from java.util.concurrent import Executor
from typing import Any, Callable, Iterable, Tuple


class RemovalListeners:
    """
    A collection of common removal listeners.

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    @staticmethod
    def asynchronous(listener: "RemovalListener"["K", "V"], executor: "Executor") -> "RemovalListener"["K", "V"]:
        """
        Returns a `RemovalListener` which processes all eviction notifications using
        `executor`.

        Arguments
        - listener: the backing listener
        - executor: the executor with which removal notifications are asynchronously executed
        """
        ...
