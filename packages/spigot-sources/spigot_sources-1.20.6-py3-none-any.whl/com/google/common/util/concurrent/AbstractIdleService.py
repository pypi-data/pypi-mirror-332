"""
Python module generated from Java source file com.google.common.util.concurrent.AbstractIdleService

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import Supplier
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import WeakOuter
from java.time import Duration
from java.util.concurrent import Executor
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from typing import Any, Callable, Iterable, Tuple


class AbstractIdleService(Service):
    """
    Base class for services that do not need a thread while "running" but may need one during startup
    and shutdown. Subclasses can implement .startUp and .shutDown methods, each which
    run in an executor which by default uses a separate thread for each method.

    Author(s)
    - Chris Nokleberg

    Since
    - 1.0
    """

    def toString(self) -> str:
        ...


    def isRunning(self) -> bool:
        ...


    def state(self) -> "State":
        ...


    def addListener(self, listener: "Listener", executor: "Executor") -> None:
        """
        Since
        - 13.0
        """
        ...


    def failureCause(self) -> "Throwable":
        """
        Since
        - 14.0
        """
        ...


    def startAsync(self) -> "Service":
        """
        Since
        - 15.0
        """
        ...


    def stopAsync(self) -> "Service":
        """
        Since
        - 15.0
        """
        ...


    def awaitRunning(self) -> None:
        """
        Since
        - 15.0
        """
        ...


    def awaitRunning(self, timeout: "Duration") -> None:
        """
        Since
        - 28.0
        """
        ...


    def awaitRunning(self, timeout: int, unit: "TimeUnit") -> None:
        """
        Since
        - 15.0
        """
        ...


    def awaitTerminated(self) -> None:
        """
        Since
        - 15.0
        """
        ...


    def awaitTerminated(self, timeout: "Duration") -> None:
        """
        Since
        - 28.0
        """
        ...


    def awaitTerminated(self, timeout: int, unit: "TimeUnit") -> None:
        """
        Since
        - 15.0
        """
        ...
