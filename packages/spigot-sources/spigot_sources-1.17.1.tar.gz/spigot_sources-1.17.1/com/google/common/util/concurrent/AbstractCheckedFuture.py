"""
Python module generated from Java source file com.google.common.util.concurrent.AbstractCheckedFuture

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import CancellationException
from java.util.concurrent import ExecutionException
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from typing import Any, Callable, Iterable, Tuple


class AbstractCheckedFuture(SimpleForwardingListenableFuture, CheckedFuture):
    """
    A delegating wrapper around a ListenableFuture that adds support for the .checkedGet() and .checkedGet(long, TimeUnit) methods.

    Author(s)
    - Sven Mawson

    Since
    - 1.0
    """

    def checkedGet(self) -> "V":
        """
        
        
        This implementation calls .get() and maps that method's standard exceptions to
        instances of type `X` using .mapException.
        
        In addition, if `get` throws an InterruptedException, this implementation will
        set the current thread's interrupt status before calling `mapException`.

        Raises
        - X: if .get() throws an InterruptedException, CancellationException, or ExecutionException
        """
        ...


    def checkedGet(self, timeout: int, unit: "TimeUnit") -> "V":
        """
        
        
        This implementation calls .get(long, TimeUnit) and maps that method's standard
        exceptions (excluding TimeoutException, which is propagated) to instances of type
        `X` using .mapException.
        
        In addition, if `get` throws an InterruptedException, this implementation will
        set the current thread's interrupt status before calling `mapException`.

        Raises
        - X: if .get() throws an InterruptedException, CancellationException, or ExecutionException
        """
        ...
