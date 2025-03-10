"""
Python module generated from Java source file com.google.common.util.concurrent.WrappingExecutorService

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import ImmutableList
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import Callable
from java.util.concurrent import ExecutionException
from java.util.concurrent import ExecutorService
from java.util.concurrent import Executors
from java.util.concurrent import Future
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class WrappingExecutorService(ExecutorService):
    """
    An abstract `ExecutorService` that allows subclasses to .wrapTask(Callable)
    wrap tasks before they are submitted to the underlying executor.
    
    Note that task wrapping may occur even if the task is never executed.
    
    For delegation without task-wrapping, see ForwardingExecutorService.

    Author(s)
    - Chris Nokleberg
    """

    def execute(self, command: "Runnable") -> None:
        ...


    def submit(self, task: "Callable"["T"]) -> "Future"["T"]:
        ...


    def submit(self, task: "Runnable") -> "Future"[Any]:
        ...


    def submit(self, task: "Runnable", result: "T") -> "Future"["T"]:
        ...


    def invokeAll(self, tasks: Iterable["Callable"["T"]]) -> list["Future"["T"]]:
        ...


    def invokeAll(self, tasks: Iterable["Callable"["T"]], timeout: int, unit: "TimeUnit") -> list["Future"["T"]]:
        ...


    def invokeAny(self, tasks: Iterable["Callable"["T"]]) -> "T":
        ...


    def invokeAny(self, tasks: Iterable["Callable"["T"]], timeout: int, unit: "TimeUnit") -> "T":
        ...


    def shutdown(self) -> None:
        ...


    def shutdownNow(self) -> list["Runnable"]:
        ...


    def isShutdown(self) -> bool:
        ...


    def isTerminated(self) -> bool:
        ...


    def awaitTermination(self, timeout: int, unit: "TimeUnit") -> bool:
        ...
