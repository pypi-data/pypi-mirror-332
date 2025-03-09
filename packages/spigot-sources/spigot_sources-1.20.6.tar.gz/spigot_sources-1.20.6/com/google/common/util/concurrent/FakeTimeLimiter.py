"""
Python module generated from Java source file com.google.common.util.concurrent.FakeTimeLimiter

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import Callable
from java.util.concurrent import ExecutionException
from java.util.concurrent import TimeUnit
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class FakeTimeLimiter(TimeLimiter):
    """
    A TimeLimiter implementation which actually does not attempt to limit time at all. This may be
    desirable to use in some unit tests. More importantly, attempting to debug a call which is
    time-limited would be extremely annoying, so this gives you a time-limiter you can easily swap in
    for your real time-limiter while you're debugging.

    Author(s)
    - Jens Nyman

    Since
    - 1.0
    """

    def newProxy(self, target: "T", interfaceType: type["T"], timeoutDuration: int, timeoutUnit: "TimeUnit") -> "T":
        ...


    def callWithTimeout(self, callable: "Callable"["T"], timeoutDuration: int, timeoutUnit: "TimeUnit") -> "T":
        ...


    def callUninterruptiblyWithTimeout(self, callable: "Callable"["T"], timeoutDuration: int, timeoutUnit: "TimeUnit") -> "T":
        ...


    def runWithTimeout(self, runnable: "Runnable", timeoutDuration: int, timeoutUnit: "TimeUnit") -> None:
        ...


    def runUninterruptiblyWithTimeout(self, runnable: "Runnable", timeoutDuration: int, timeoutUnit: "TimeUnit") -> None:
        ...
