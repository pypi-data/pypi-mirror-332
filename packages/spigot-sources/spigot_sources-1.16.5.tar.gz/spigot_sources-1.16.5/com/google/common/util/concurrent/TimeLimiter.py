"""
Python module generated from Java source file com.google.common.util.concurrent.TimeLimiter

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
from java.util.concurrent import TimeUnit
from typing import Any, Callable, Iterable, Tuple


class TimeLimiter:
    """
    Produces proxies that impose a time limit on method calls to the proxied object. For example, to
    return the value of `target.someMethod()`, but substitute `DEFAULT_VALUE` if this
    method call takes over 50 ms, you can use this code:
    
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
    
    Please see `SimpleTimeLimiterTest` for more usage examples.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    def newProxy(self, target: "T", interfaceType: type["T"], timeoutDuration: int, timeoutUnit: "TimeUnit") -> "T":
        """
        Returns an instance of `interfaceType` that delegates all method calls to the
        `target` object, enforcing the specified time limit on each call. This time-limited
        delegation is also performed for calls to Object.equals, Object.hashCode, and
        Object.toString.
        
        If the target method call finishes before the limit is reached, the return value or
        exception is propagated to the caller exactly as-is. If, on the other hand, the time limit is
        reached, the proxy will attempt to abort the call to the target, and will throw an
        UncheckedTimeoutException to the caller.
        
        It is important to note that the primary purpose of the proxy object is to return control to
        the caller when the timeout elapses; aborting the target method call is of secondary concern.
        The particular nature and strength of the guarantees made by the proxy is
        implementation-dependent. However, it is important that each of the methods on the target
        object behaves appropriately when its thread is interrupted.

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


    def callWithTimeout(self, callable: "Callable"["T"], timeoutDuration: int, timeoutUnit: "TimeUnit", interruptible: bool) -> "T":
        """
        Invokes a specified Callable, timing out after the specified time limit. If the target method
        call finished before the limit is reached, the return value or exception is propagated to the
        caller exactly as-is. If, on the other hand, the time limit is reached, we attempt to abort the
        call to the target, and throw an UncheckedTimeoutException to the caller.

        Arguments
        - callable: the Callable to execute
        - timeoutDuration: with timeoutUnit, the maximum length of time to wait
        - timeoutUnit: with timeoutDuration, the maximum length of time to wait
        - interruptible: whether to respond to thread interruption by aborting the operation and
            throwing InterruptedException; if False, the operation is allowed to complete or time out,
            and the current thread's interrupt status is re-asserted.

        Returns
        - the result returned by the Callable

        Raises
        - InterruptedException: if `interruptible` is True and our thread is interrupted
            during execution
        - UncheckedTimeoutException: if the time limit is reached
        """
        ...
