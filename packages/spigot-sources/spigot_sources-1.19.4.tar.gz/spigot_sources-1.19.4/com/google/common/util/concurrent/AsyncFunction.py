"""
Python module generated from Java source file com.google.common.util.concurrent.AsyncFunction

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from java.util.concurrent import Future
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AsyncFunction:
    """
    Transforms a value, possibly asynchronously. For an example usage and more information, see
    Futures.transformAsync(ListenableFuture, AsyncFunction, Executor).

    Author(s)
    - Chris Povirk

    Since
    - 11.0
    """

    def apply(self, input: "I") -> "ListenableFuture"["O"]:
        """
        Returns an output `Future` to use in place of the given `input`. The output `Future` need not be Future.isDone done, making `AsyncFunction` suitable for
        asynchronous derivations.
        
        Throwing an exception from this method is equivalent to returning a failing `Future`.
        """
        ...
