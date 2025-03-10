"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingLock

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.util.concurrent import *
from java.util.concurrent import TimeUnit
from java.util.concurrent.locks import Condition
from java.util.concurrent.locks import Lock
from typing import Any, Callable, Iterable, Tuple


class ForwardingLock(Lock):
    """
    Forwarding wrapper around a `Lock`.
    """

    def lock(self) -> None:
        ...


    def lockInterruptibly(self) -> None:
        ...


    def tryLock(self) -> bool:
        ...


    def tryLock(self, time: int, unit: "TimeUnit") -> bool:
        ...


    def unlock(self) -> None:
        ...


    def newCondition(self) -> "Condition":
        ...
