"""
Python module generated from Java source file com.google.common.util.concurrent.SimpleTimeLimiter

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import ObjectArrays
from com.google.common.collect import Sets
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.lang.reflect import InvocationHandler
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from java.lang.reflect import Proxy
from java.util.concurrent import Callable
from java.util.concurrent import ExecutionException
from java.util.concurrent import ExecutorService
from java.util.concurrent import Executors
from java.util.concurrent import Future
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from typing import Any, Callable, Iterable, Tuple


class SimpleTimeLimiter(TimeLimiter):
    """
    A TimeLimiter that runs method calls in the background using an ExecutorService. If the
    time limit expires for a given method call, the thread running the call will be interrupted.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    def __init__(self, executor: "ExecutorService"):
        """
        Constructs a TimeLimiter instance using the given executor service to execute proxied method
        calls.
        
        **Warning:** using a bounded executor may be counterproductive! If the thread pool fills
        up, any time callers spend waiting for a thread may count toward their time limit, and in this
        case the call may even time out before the target method is ever invoked.

        Arguments
        - executor: the ExecutorService that will execute the method calls on the target objects;
            for example, a Executors.newCachedThreadPool().
        """
        ...


    def __init__(self):
        """
        Constructs a TimeLimiter instance using a Executors.newCachedThreadPool() to execute
        proxied method calls.
        
        **Warning:** using a bounded executor may be counterproductive! If the thread pool fills
        up, any time callers spend waiting for a thread may count toward their time limit, and in this
        case the call may even time out before the target method is ever invoked.
        """
        ...


    def newProxy(self, target: "T", interfaceType: type["T"], timeoutDuration: int, timeoutUnit: "TimeUnit") -> "T":
        ...


    def callWithTimeout(self, callable: "Callable"["T"], timeoutDuration: int, timeoutUnit: "TimeUnit", amInterruptible: bool) -> "T":
        ...
