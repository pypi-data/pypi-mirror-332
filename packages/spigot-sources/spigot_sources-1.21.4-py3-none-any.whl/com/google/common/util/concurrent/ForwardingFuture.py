"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingFuture

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Preconditions
from com.google.common.collect import ForwardingObject
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import ExecutionException
from java.util.concurrent import Future
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingFuture(ForwardingObject, Future):
    """
    A Future which forwards all its method calls to another future. Subclasses should
    override one or more methods to modify the behavior of the backing future as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    Most subclasses can just use SimpleForwardingFuture.

    Author(s)
    - Sven Mawson

    Since
    - 1.0
    """

    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        ...


    def isCancelled(self) -> bool:
        ...


    def isDone(self) -> bool:
        ...


    def get(self) -> "V":
        ...


    def get(self, timeout: int, unit: "TimeUnit") -> "V":
        ...


    class SimpleForwardingFuture(ForwardingFuture):
        """
        A simplified version of ForwardingFuture where subclasses can pass in an already
        constructed Future as the delegate.

        Since
        - 9.0
        """


