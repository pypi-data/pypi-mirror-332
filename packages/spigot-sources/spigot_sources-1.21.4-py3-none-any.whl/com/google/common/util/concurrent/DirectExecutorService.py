"""
Python module generated from Java source file com.google.common.util.concurrent.DirectExecutorService

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations.concurrent import GuardedBy
from java.util import Collections
from java.util.concurrent import RejectedExecutionException
from java.util.concurrent import TimeUnit
from typing import Any, Callable, Iterable, Tuple


class DirectExecutorService(AbstractListeningExecutorService):
    """
    See newDirectExecutorService javadoc for behavioral notes.
    """

    def execute(self, command: "Runnable") -> None:
        ...


    def isShutdown(self) -> bool:
        ...


    def shutdown(self) -> None:
        ...


    def shutdownNow(self) -> list["Runnable"]:
        ...


    def isTerminated(self) -> bool:
        ...


    def awaitTermination(self, timeout: int, unit: "TimeUnit") -> bool:
        ...
