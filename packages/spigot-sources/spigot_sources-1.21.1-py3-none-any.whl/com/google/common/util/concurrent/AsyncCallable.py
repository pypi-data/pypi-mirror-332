"""
Python module generated from Java source file com.google.common.util.concurrent.AsyncCallable

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from java.util.concurrent import Future
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AsyncCallable:
    """
    Computes a value, possibly asynchronously. For an example usage and more information, see Futures.FutureCombiner.callAsync(AsyncCallable, java.util.concurrent.Executor).
    
    Much like java.util.concurrent.Callable, but returning a ListenableFuture
    result.

    Since
    - 20.0
    """

    def call(self) -> "ListenableFuture"["V"]:
        """
        Computes a result `Future`. The output `Future` need not be Future.isDone done, making `AsyncCallable` suitable for asynchronous derivations.
        
        Throwing an exception from this method is equivalent to returning a failing ListenableFuture.
        """
        ...
