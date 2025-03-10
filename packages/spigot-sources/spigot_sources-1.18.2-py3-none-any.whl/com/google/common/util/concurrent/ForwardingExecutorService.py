"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingExecutorService

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import ForwardingObject
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import Callable
from java.util.concurrent import ExecutionException
from java.util.concurrent import ExecutorService
from java.util.concurrent import Future
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingExecutorService(ForwardingObject, ExecutorService):
    """
    An executor service which forwards all its method calls to another executor service. Subclasses
    should override one or more methods to modify the behavior of the backing executor service as
    desired per the <a href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 10.0
    """

    def awaitTermination(self, timeout: int, unit: "TimeUnit") -> bool:
        ...


    def invokeAll(self, tasks: Iterable["Callable"["T"]]) -> list["Future"["T"]]:
        ...


    def invokeAll(self, tasks: Iterable["Callable"["T"]], timeout: int, unit: "TimeUnit") -> list["Future"["T"]]:
        ...


    def invokeAny(self, tasks: Iterable["Callable"["T"]]) -> "T":
        ...


    def invokeAny(self, tasks: Iterable["Callable"["T"]], timeout: int, unit: "TimeUnit") -> "T":
        ...


    def isShutdown(self) -> bool:
        ...


    def isTerminated(self) -> bool:
        ...


    def shutdown(self) -> None:
        ...


    def shutdownNow(self) -> list["Runnable"]:
        ...


    def execute(self, command: "Runnable") -> None:
        ...


    def submit(self, task: "Callable"["T"]) -> "Future"["T"]:
        ...


    def submit(self, task: "Runnable") -> "Future"[Any]:
        ...


    def submit(self, task: "Runnable", result: "T") -> "Future"["T"]:
        ...
