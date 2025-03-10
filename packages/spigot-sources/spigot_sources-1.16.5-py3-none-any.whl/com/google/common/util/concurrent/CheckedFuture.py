"""
Python module generated from Java source file com.google.common.util.concurrent.CheckedFuture

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import CancellationException
from java.util.concurrent import ExecutionException
from java.util.concurrent import Future
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from typing import Any, Callable, Iterable, Tuple


class CheckedFuture(ListenableFuture):
    """
    A `CheckedFuture` is a ListenableFuture that includes versions of the `get`
    methods that can throw a checked exception. This makes it easier to create a future that executes
    logic which can throw an exception.
    
    **Warning:** We recommend against using `CheckedFuture` in new projects. `CheckedFuture` is difficult to build libraries atop. `CheckedFuture` ports of methods like
    Futures.transformAsync have historically had bugs, and some of these bugs are necessary,
    unavoidable consequences of the `CheckedFuture` API. Additionally, `CheckedFuture`
    encourages users to take exceptions from one thread and rethrow them in another, producing
    confusing stack traces.
    
    A common implementation is Futures.immediateCheckedFuture.
    
    Implementations of this interface must adapt the exceptions thrown by `Future.get()`:
    CancellationException, ExecutionException and InterruptedException into
    the type specified by the `X` type parameter.
    
    This interface also extends the ListenableFuture interface to allow listeners to be added.
    This allows the future to be used as a normal Future or as an asynchronous callback
    mechanism as needed. This allows multiple callbacks to be registered for a particular task, and
    the future will guarantee execution of all listeners when the task completes.
    
    For a simpler alternative to CheckedFuture, consider accessing Future values with Futures.getChecked(Future, Class) Futures.getChecked().

    Author(s)
    - Sven Mawson

    Since
    - 1.0
    """

    def checkedGet(self) -> "V":
        """
        Exception checking version of Future.get() that will translate InterruptedException, CancellationException and ExecutionException into
        application-specific exceptions.

        Returns
        - the result of executing the future.

        Raises
        - X: on interruption, cancellation or execution exceptions.
        """
        ...


    def checkedGet(self, timeout: int, unit: "TimeUnit") -> "V":
        """
        Exception checking version of Future.get(long, TimeUnit) that will translate InterruptedException, CancellationException and ExecutionException into
        application-specific exceptions.  On timeout this method throws a normal TimeoutException.

        Returns
        - the result of executing the future.

        Raises
        - TimeoutException: if retrieving the result timed out.
        - X: on interruption, cancellation or execution exceptions.
        """
        ...
