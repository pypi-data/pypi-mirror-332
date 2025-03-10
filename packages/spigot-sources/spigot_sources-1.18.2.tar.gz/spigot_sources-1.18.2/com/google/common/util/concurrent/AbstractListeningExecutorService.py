"""
Python module generated from Java source file com.google.common.util.concurrent.AbstractListeningExecutorService

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import AbstractExecutorService
from java.util.concurrent import Callable
from java.util.concurrent import RunnableFuture
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractListeningExecutorService(AbstractExecutorService, ListeningExecutorService):
    """
    Abstract ListeningExecutorService implementation that creates ListenableFuture
    instances for each Runnable and Callable submitted to it. These tasks are run
    with the abstract .execute execute(Runnable) method.
    
    In addition to .execute, subclasses must implement all methods related to shutdown and
    termination.

    Author(s)
    - Chris Povirk

    Since
    - 14.0
    """

    def submit(self, task: "Runnable") -> "ListenableFuture"[Any]:
        ...


    def submit(self, task: "Runnable", result: "T") -> "ListenableFuture"["T"]:
        ...


    def submit(self, task: "Callable"["T"]) -> "ListenableFuture"["T"]:
        ...
