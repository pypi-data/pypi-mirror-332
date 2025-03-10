"""
Python module generated from Java source file com.google.common.util.concurrent.ListeningScheduledExecutorService

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import Callable
from java.util.concurrent import ScheduledExecutorService
from java.util.concurrent import TimeUnit
from typing import Any, Callable, Iterable, Tuple


class ListeningScheduledExecutorService(ScheduledExecutorService, ListeningExecutorService):
    """
    A ScheduledExecutorService that returns ListenableFuture instances from its
    `ExecutorService` methods. To create an instance from an existing ScheduledExecutorService, call MoreExecutors.listeningDecorator(ScheduledExecutorService).

    Author(s)
    - Chris Povirk

    Since
    - 10.0
    """

    def schedule(self, command: "Runnable", delay: int, unit: "TimeUnit") -> "ListenableScheduledFuture"[Any]:
        """
        Since
        - 15.0 (previously returned ScheduledFuture)
        """
        ...


    def schedule(self, callable: "Callable"["V"], delay: int, unit: "TimeUnit") -> "ListenableScheduledFuture"["V"]:
        """
        Since
        - 15.0 (previously returned ScheduledFuture)
        """
        ...


    def scheduleAtFixedRate(self, command: "Runnable", initialDelay: int, period: int, unit: "TimeUnit") -> "ListenableScheduledFuture"[Any]:
        """
        Since
        - 15.0 (previously returned ScheduledFuture)
        """
        ...


    def scheduleWithFixedDelay(self, command: "Runnable", initialDelay: int, delay: int, unit: "TimeUnit") -> "ListenableScheduledFuture"[Any]:
        """
        Since
        - 15.0 (previously returned ScheduledFuture)
        """
        ...
