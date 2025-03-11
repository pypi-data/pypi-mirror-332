"""
Python module generated from Java source file com.google.common.util.concurrent.TimeLimiter

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotMock
from java.time import Duration
from java.util.concurrent import Callable
from java.util.concurrent import ExecutionException
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class TimeLimiter:
    """
    Imposes a time limit on method calls.

    Author(s)
    - Jens Nyman

    Since
    - 1.0
    """

    def newProxy(self, target: "T", interfaceType: type["T"], timeoutDuration: int, timeoutUnit: "TimeUnit") -> "T":
        """
        Returns an instance of `interfaceType` that delegates all method calls to the `target` object, enforcing the specified time limit on each call. This time-limited delegation
        is also performed for calls to Object.equals, Object.hashCode, and Object.toString.
        
        If the target method call finishes before the limit is reached, the return value or
        exception is propagated to the caller exactly as-is. If, on the other hand, the time limit is
        reached, the proxy will attempt to abort the call to the target, and will throw an UncheckedTimeoutException to the caller.
        
        It is important to note that the primary purpose of the proxy object is to return control to
        the caller when the timeout elapses; aborting the target method call is of secondary concern.
        The particular nature and strength of the guarantees made by the proxy is
        implementation-dependent. However, it is important that each of the methods on the target
        object behaves appropriately when its thread is interrupted.
        
        For example, to return the value of `target.someMethod()`, but substitute `DEFAULT_VALUE` if this method call takes over 50 ms, you can use this code:
        
        ```
          TimeLimiter limiter = . . .;
          TargetType proxy = limiter.newProxy(
              target, TargetType.class, 50, TimeUnit.MILLISECONDS);
          try {
            return proxy.someMethod();
          } catch (UncheckedTimeoutException e) {
            return DEFAULT_VALUE;
          }
        ```

        Arguments
        - target: the object to proxy
        - interfaceType: the interface you wish the returned proxy to implement
        - timeoutDuration: with timeoutUnit, the maximum length of time that callers are willing to
            wait on each method call to the proxy
        - timeoutUnit: with timeoutDuration, the maximum length of time that callers are willing to
            wait on each method call to the proxy

        Returns
        - a time-limiting proxy

        Raises
        - IllegalArgumentException: if `interfaceType` is a regular class, enum, or
            annotation type, rather than an interface
        """
        ...


    def newProxy(self, target: "T", interfaceType: type["T"], timeout: "Duration") -> "T":
        """
        Returns an instance of `interfaceType` that delegates all method calls to the `target` object, enforcing the specified time limit on each call. This time-limited delegation
        is also performed for calls to Object.equals, Object.hashCode, and Object.toString.
        
        If the target method call finishes before the limit is reached, the return value or
        exception is propagated to the caller exactly as-is. If, on the other hand, the time limit is
        reached, the proxy will attempt to abort the call to the target, and will throw an UncheckedTimeoutException to the caller.
        
        It is important to note that the primary purpose of the proxy object is to return control to
        the caller when the timeout elapses; aborting the target method call is of secondary concern.
        The particular nature and strength of the guarantees made by the proxy is
        implementation-dependent. However, it is important that each of the methods on the target
        object behaves appropriately when its thread is interrupted.
        
        For example, to return the value of `target.someMethod()`, but substitute `DEFAULT_VALUE` if this method call takes over 50 ms, you can use this code:
        
        ```
          TimeLimiter limiter = . . .;
          TargetType proxy = limiter.newProxy(target, TargetType.class, Duration.ofMillis(50));
          try {
            return proxy.someMethod();
          } catch (UncheckedTimeoutException e) {
            return DEFAULT_VALUE;
          }
        ```

        Arguments
        - target: the object to proxy
        - interfaceType: the interface you wish the returned proxy to implement
        - timeout: the maximum length of time that callers are willing to wait on each method call
            to the proxy

        Returns
        - a time-limiting proxy

        Raises
        - IllegalArgumentException: if `interfaceType` is a regular class, enum, or
            annotation type, rather than an interface

        Since
        - 28.0
        """
        ...


    def callWithTimeout(self, callable: "Callable"["T"], timeoutDuration: int, timeoutUnit: "TimeUnit") -> "T":
        """
        Invokes a specified Callable, timing out after the specified time limit. If the target method
        call finishes before the limit is reached, the return value or a wrapped exception is
        propagated. If, on the other hand, the time limit is reached, we attempt to abort the call to
        the target, and throw a TimeoutException to the caller.

        Arguments
        - callable: the Callable to execute
        - timeoutDuration: with timeoutUnit, the maximum length of time to wait
        - timeoutUnit: with timeoutDuration, the maximum length of time to wait

        Returns
        - the result returned by the Callable

        Raises
        - TimeoutException: if the time limit is reached
        - InterruptedException: if the current thread was interrupted during execution
        - ExecutionException: if `callable` throws a checked exception
        - UncheckedExecutionException: if `callable` throws a `RuntimeException`
        - ExecutionError: if `callable` throws an `Error`

        Since
        - 22.0
        """
        ...


    def callWithTimeout(self, callable: "Callable"["T"], timeout: "Duration") -> "T":
        """
        Invokes a specified Callable, timing out after the specified time limit. If the target method
        call finishes before the limit is reached, the return value or a wrapped exception is
        propagated. If, on the other hand, the time limit is reached, we attempt to abort the call to
        the target, and throw a TimeoutException to the caller.

        Arguments
        - callable: the Callable to execute
        - timeout: the maximum length of time to wait

        Returns
        - the result returned by the Callable

        Raises
        - TimeoutException: if the time limit is reached
        - InterruptedException: if the current thread was interrupted during execution
        - ExecutionException: if `callable` throws a checked exception
        - UncheckedExecutionException: if `callable` throws a `RuntimeException`
        - ExecutionError: if `callable` throws an `Error`

        Since
        - 28.0
        """
        ...


    def callUninterruptiblyWithTimeout(self, callable: "Callable"["T"], timeoutDuration: int, timeoutUnit: "TimeUnit") -> "T":
        """
        Invokes a specified Callable, timing out after the specified time limit. If the target method
        call finishes before the limit is reached, the return value or a wrapped exception is
        propagated. If, on the other hand, the time limit is reached, we attempt to abort the call to
        the target, and throw a TimeoutException to the caller.
        
        The difference with .callWithTimeout(Callable, long, TimeUnit) is that this method
        will ignore interrupts on the current thread.

        Arguments
        - callable: the Callable to execute
        - timeoutDuration: with timeoutUnit, the maximum length of time to wait
        - timeoutUnit: with timeoutDuration, the maximum length of time to wait

        Returns
        - the result returned by the Callable

        Raises
        - TimeoutException: if the time limit is reached
        - ExecutionException: if `callable` throws a checked exception
        - UncheckedExecutionException: if `callable` throws a `RuntimeException`
        - ExecutionError: if `callable` throws an `Error`

        Since
        - 22.0
        """
        ...


    def callUninterruptiblyWithTimeout(self, callable: "Callable"["T"], timeout: "Duration") -> "T":
        """
        Invokes a specified Callable, timing out after the specified time limit. If the target method
        call finishes before the limit is reached, the return value or a wrapped exception is
        propagated. If, on the other hand, the time limit is reached, we attempt to abort the call to
        the target, and throw a TimeoutException to the caller.
        
        The difference with .callWithTimeout(Callable, Duration) is that this method will
        ignore interrupts on the current thread.

        Arguments
        - callable: the Callable to execute
        - timeout: the maximum length of time to wait

        Returns
        - the result returned by the Callable

        Raises
        - TimeoutException: if the time limit is reached
        - ExecutionException: if `callable` throws a checked exception
        - UncheckedExecutionException: if `callable` throws a `RuntimeException`
        - ExecutionError: if `callable` throws an `Error`

        Since
        - 28.0
        """
        ...


    def runWithTimeout(self, runnable: "Runnable", timeoutDuration: int, timeoutUnit: "TimeUnit") -> None:
        """
        Invokes a specified Runnable, timing out after the specified time limit. If the target method
        run finishes before the limit is reached, this method returns or a wrapped exception is
        propagated. If, on the other hand, the time limit is reached, we attempt to abort the run, and
        throw a TimeoutException to the caller.

        Arguments
        - runnable: the Runnable to execute
        - timeoutDuration: with timeoutUnit, the maximum length of time to wait
        - timeoutUnit: with timeoutDuration, the maximum length of time to wait

        Raises
        - TimeoutException: if the time limit is reached
        - InterruptedException: if the current thread was interrupted during execution
        - UncheckedExecutionException: if `runnable` throws a `RuntimeException`
        - ExecutionError: if `runnable` throws an `Error`

        Since
        - 22.0
        """
        ...


    def runWithTimeout(self, runnable: "Runnable", timeout: "Duration") -> None:
        """
        Invokes a specified Runnable, timing out after the specified time limit. If the target method
        run finishes before the limit is reached, this method returns or a wrapped exception is
        propagated. If, on the other hand, the time limit is reached, we attempt to abort the run, and
        throw a TimeoutException to the caller.

        Arguments
        - runnable: the Runnable to execute
        - timeout: the maximum length of time to wait

        Raises
        - TimeoutException: if the time limit is reached
        - InterruptedException: if the current thread was interrupted during execution
        - UncheckedExecutionException: if `runnable` throws a `RuntimeException`
        - ExecutionError: if `runnable` throws an `Error`

        Since
        - 28.0
        """
        ...


    def runUninterruptiblyWithTimeout(self, runnable: "Runnable", timeoutDuration: int, timeoutUnit: "TimeUnit") -> None:
        """
        Invokes a specified Runnable, timing out after the specified time limit. If the target method
        run finishes before the limit is reached, this method returns or a wrapped exception is
        propagated. If, on the other hand, the time limit is reached, we attempt to abort the run, and
        throw a TimeoutException to the caller.
        
        The difference with .runWithTimeout(Runnable, long, TimeUnit) is that this method
        will ignore interrupts on the current thread.

        Arguments
        - runnable: the Runnable to execute
        - timeoutDuration: with timeoutUnit, the maximum length of time to wait
        - timeoutUnit: with timeoutDuration, the maximum length of time to wait

        Raises
        - TimeoutException: if the time limit is reached
        - UncheckedExecutionException: if `runnable` throws a `RuntimeException`
        - ExecutionError: if `runnable` throws an `Error`

        Since
        - 22.0
        """
        ...


    def runUninterruptiblyWithTimeout(self, runnable: "Runnable", timeout: "Duration") -> None:
        """
        Invokes a specified Runnable, timing out after the specified time limit. If the target method
        run finishes before the limit is reached, this method returns or a wrapped exception is
        propagated. If, on the other hand, the time limit is reached, we attempt to abort the run, and
        throw a TimeoutException to the caller.
        
        The difference with .runWithTimeout(Runnable, Duration) is that this method will
        ignore interrupts on the current thread.

        Arguments
        - runnable: the Runnable to execute
        - timeout: the maximum length of time to wait

        Raises
        - TimeoutException: if the time limit is reached
        - UncheckedExecutionException: if `runnable` throws a `RuntimeException`
        - ExecutionError: if `runnable` throws an `Error`

        Since
        - 28.0
        """
        ...
