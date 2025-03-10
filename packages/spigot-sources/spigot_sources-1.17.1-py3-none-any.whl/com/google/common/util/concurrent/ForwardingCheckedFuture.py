"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingCheckedFuture

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from typing import Any, Callable, Iterable, Tuple


class ForwardingCheckedFuture(ForwardingListenableFuture, CheckedFuture):
    """
    A future which forwards all its method calls to another future. Subclasses should override one or
    more methods to modify the behavior of the backing future as desired per the <a href=
    "http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    Most subclasses can simply extend SimpleForwardingCheckedFuture.
    
    Type `<V>`: The result type returned by this Future's `get` method
    
    Type `<X>`: The type of the Exception thrown by the Future's `checkedGet` method

    Author(s)
    - Anthony Zana

    Since
    - 9.0
    """

    def checkedGet(self) -> "V":
        ...


    def checkedGet(self, timeout: int, unit: "TimeUnit") -> "V":
        ...


    class SimpleForwardingCheckedFuture(ForwardingCheckedFuture):
        """
        A simplified version of ForwardingCheckedFuture where subclasses can pass in an already
        constructed CheckedFuture as the delegate.

        Since
        - 9.0
        """


