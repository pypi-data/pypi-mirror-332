"""
Python module generated from Java source file com.google.common.util.concurrent.WrappingScheduledExecutorService

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import Callable
from java.util.concurrent import ScheduledExecutorService
from java.util.concurrent import ScheduledFuture
from java.util.concurrent import TimeUnit
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class WrappingScheduledExecutorService(WrappingExecutorService, ScheduledExecutorService):
    """
    An abstract `ScheduledExecutorService` that allows subclasses to .wrapTask(Callable) wrap tasks before they are submitted to the underlying executor.
    
    Note that task wrapping may occur even if the task is never executed.

    Author(s)
    - Luke Sandberg
    """

    def schedule(self, command: "Runnable", delay: int, unit: "TimeUnit") -> "ScheduledFuture"[Any]:
        ...


    def schedule(self, task: "Callable"["V"], delay: int, unit: "TimeUnit") -> "ScheduledFuture"["V"]:
        ...


    def scheduleAtFixedRate(self, command: "Runnable", initialDelay: int, period: int, unit: "TimeUnit") -> "ScheduledFuture"[Any]:
        ...


    def scheduleWithFixedDelay(self, command: "Runnable", initialDelay: int, delay: int, unit: "TimeUnit") -> "ScheduledFuture"[Any]:
        ...
