"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingCondition

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.util.concurrent import *
from java.util import Date
from java.util.concurrent import TimeUnit
from java.util.concurrent.locks import Condition
from typing import Any, Callable, Iterable, Tuple


class ForwardingCondition(Condition):
    """
    Forwarding wrapper around a `Condition`.
    """

    def await(self) -> None:
        ...


    def await(self, time: int, unit: "TimeUnit") -> bool:
        ...


    def awaitUninterruptibly(self) -> None:
        ...


    def awaitNanos(self, nanosTimeout: int) -> int:
        ...


    def awaitUntil(self, deadline: "Date") -> bool:
        ...


    def signal(self) -> None:
        ...


    def signalAll(self) -> None:
        ...
