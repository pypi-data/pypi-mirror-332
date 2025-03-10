"""
Python module generated from Java source file com.google.common.util.concurrent.ImmediateFuture

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.AbstractFuture import TrustedFuture
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from java.util.concurrent import TimeUnit
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmediateFuture(ListenableFuture):
    """
    Implementation of Futures.immediateFuture.
    """

    def addListener(self, listener: "Runnable", executor: "Executor") -> None:
        ...


    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        ...


    def get(self) -> "V":
        ...


    def get(self, timeout: int, unit: "TimeUnit") -> "V":
        ...


    def isCancelled(self) -> bool:
        ...


    def isDone(self) -> bool:
        ...


    def toString(self) -> str:
        ...
