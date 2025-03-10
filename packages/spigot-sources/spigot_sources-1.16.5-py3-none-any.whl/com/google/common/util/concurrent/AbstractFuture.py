"""
Python module generated from Java source file com.google.common.util.concurrent.AbstractFuture

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import ReflectionSupport
from java.security import AccessController
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.util.concurrent import CancellationException
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from java.util.concurrent import Future
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from java.util.concurrent.atomic import AtomicReferenceFieldUpdater
from java.util.concurrent.locks import LockSupport
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractFuture(ListenableFuture):
    """
    An abstract implementation of ListenableFuture, intended for advanced users only. More
    common ways to create a `ListenableFuture` include instantiating a SettableFuture,
    submitting a task to a ListeningExecutorService, and deriving a `Future` from an
    existing one, typically using methods like Futures.transform(ListenableFuture, Function)
    Futures.transform and Futures.catching(ListenableFuture, Class, Function)
    Futures.catching.
    
    This class implements all methods in `ListenableFuture`. Subclasses should provide a way
    to set the result of the computation through the protected methods .set(Object), .setFuture(ListenableFuture) and .setException(Throwable). Subclasses may also override
    .interruptTask(), which will be invoked automatically if a call to .cancel(boolean) cancel(True) succeeds in canceling the future. Subclasses should rarely
    override other methods.

    Author(s)
    - Luke Sandberg

    Since
    - 1.0
    """

    def get(self, timeout: int, unit: "TimeUnit") -> "V":
        """
        
        
        The default AbstractFuture implementation throws `InterruptedException` if the
        current thread is interrupted before or during the call, even if the value is already
        available.

        Raises
        - InterruptedException: if the current thread was interrupted before or during the call
            (optional but recommended).
        - CancellationException: 
        """
        ...


    def get(self) -> "V":
        """
        
        
        The default AbstractFuture implementation throws `InterruptedException` if the
        current thread is interrupted before or during the call, even if the value is already
        available.

        Raises
        - InterruptedException: if the current thread was interrupted before or during the call
            (optional but recommended).
        - CancellationException: 
        """
        ...


    def isDone(self) -> bool:
        ...


    def isCancelled(self) -> bool:
        ...


    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """
        
        
        If a cancellation attempt succeeds on a `Future` that had previously been .setFuture set asynchronously, then the cancellation will also be propagated to the delegate
        `Future` that was supplied in the `setFuture` call.
        """
        ...


    def addListener(self, listener: "Runnable", executor: "Executor") -> None:
        """
        Since
        - 10.0
        """
        ...
