"""
Python module generated from Java source file com.google.common.util.concurrent.FutureCallback

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from java.util.concurrent import ExecutionException
from java.util.concurrent import Future
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class FutureCallback:
    """
    A callback for accepting the results of a java.util.concurrent.Future computation
    asynchronously.
    
    To attach to a ListenableFuture use Futures.addCallback.

    Author(s)
    - Anthony Zana

    Since
    - 10.0
    """

    def onSuccess(self, result: "V") -> None:
        """
        Invoked with the result of the `Future` computation when it is successful.
        """
        ...


    def onFailure(self, t: "Throwable") -> None:
        """
        Invoked when a `Future` computation fails or is canceled.
        
        If the future's Future.get() get method throws an ExecutionException, then
        the cause is passed to this method. Any other thrown object is passed unaltered.
        """
        ...
