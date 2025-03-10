"""
Python module generated from Java source file com.google.common.util.concurrent.AbstractExecutionThreadService

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Supplier
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.time import Duration
from java.util.concurrent import Executor
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from typing import Any, Callable, Iterable, Tuple


class AbstractExecutionThreadService(Service):
    """
    Base class for services that can implement .startUp, .run and .shutDown
    methods. This class uses a single thread to execute the service; consider AbstractService
    if you would like to manage any threading manually.

    Author(s)
    - Jesse Wilson

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
