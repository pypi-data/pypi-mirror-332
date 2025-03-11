"""
Python module generated from Java source file com.google.common.util.concurrent.AbstractService

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.Monitor import Guard
from com.google.common.util.concurrent.Service import State
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import ForOverride
from com.google.errorprone.annotations.concurrent import GuardedBy
from com.google.j2objc.annotations import WeakOuter
from java.time import Duration
from java.util.concurrent import Executor
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AbstractService(Service):
    """
    Base class for implementing services that can handle .doStart and .doStop
    requests, responding to them with .notifyStarted() and .notifyStopped()
    callbacks. Its subclasses must manage threads manually; consider AbstractExecutionThreadService if you need only a single execution thread.

    Author(s)
    - Luke Sandberg

    Since
    - 1.0
    """

    def startAsync(self) -> "Service":
        ...


    def stopAsync(self) -> "Service":
        ...


    def awaitRunning(self) -> None:
        ...


    def awaitRunning(self, timeout: "Duration") -> None:
        """
        Since
        - 28.0
        """
        ...


    def awaitRunning(self, timeout: int, unit: "TimeUnit") -> None:
        ...


    def awaitTerminated(self) -> None:
        ...


    def awaitTerminated(self, timeout: "Duration") -> None:
        """
        Since
        - 28.0
        """
        ...


    def awaitTerminated(self, timeout: int, unit: "TimeUnit") -> None:
        ...


    def isRunning(self) -> bool:
        ...


    def state(self) -> "State":
        ...


    def failureCause(self) -> "Throwable":
        """
        Since
        - 14.0
        """
        ...


    def addListener(self, listener: "Listener", executor: "Executor") -> None:
        """
        Since
        - 13.0
        """
        ...


    def toString(self) -> str:
        ...
