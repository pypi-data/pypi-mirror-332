"""
Python module generated from Java source file com.google.common.util.concurrent.AbstractFuture

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Strings
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.internal import InternalFutureFailureAccess
from com.google.common.util.concurrent.internal import InternalFutures
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import ForOverride
from com.google.j2objc.annotations import ReflectionSupport
from java.lang.reflect import Field
from java.security import AccessController
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.util import Locale
from java.util.concurrent import CancellationException
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from java.util.concurrent import Future
from java.util.concurrent import ScheduledFuture
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from java.util.concurrent.atomic import AtomicReferenceFieldUpdater
from java.util.concurrent.locks import LockSupport
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from sun.misc import Unsafe
from typing import Any, Callable, Iterable, Tuple


class AbstractFuture(InternalFutureFailureAccess, ListenableFuture):
    """
    An abstract implementation of ListenableFuture, intended for advanced users only. More
    common ways to create a `ListenableFuture` include instantiating a SettableFuture,
    submitting a task to a ListeningExecutorService, and deriving a `Future` from an
    existing one, typically using methods like Futures.transform(ListenableFuture,
    com.google.common.base.Function, java.util.concurrent.Executor) Futures.transform and Futures.catching(ListenableFuture, Class, com.google.common.base.Function,
    java.util.concurrent.Executor) Futures.catching.
    
    This class implements all methods in `ListenableFuture`. Subclasses should provide a way
    to set the result of the computation through the protected methods .set(Object), .setFuture(ListenableFuture) and .setException(Throwable). Subclasses may also override
    .afterDone(), which will be invoked automatically when the future completes. Subclasses
    should rarely override other methods.

    Author(s)
    - Luke Sandberg

    Since
    - 1.0
    """

    def get(self, timeout: int, unit: "TimeUnit") -> "V":
        """
        
        
        The default AbstractFuture implementation throws `InterruptedException` if the
        current thread is interrupted during the call, even if the value is already available.

        Raises
        - CancellationException: 
        """
        ...


    def get(self) -> "V":
        """
        
        
        The default AbstractFuture implementation throws `InterruptedException` if the
        current thread is interrupted during the call, even if the value is already available.

        Raises
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
        
        Rather than override this method to perform additional cancellation work or cleanup,
        subclasses should override .afterDone, consulting .isCancelled and .wasInterrupted as necessary. This ensures that the work is done even if the future is
        cancelled without a call to `cancel`, such as by calling `setFuture(cancelledFuture)`.
        
        Beware of completing a future while holding a lock. Its listeners may do slow work or
        acquire other locks, risking deadlocks.
        """
        ...


    def addListener(self, listener: "Runnable", executor: "Executor") -> None:
        """
        Since
        - 10.0
        """
        ...


    def toString(self) -> str:
        ...
