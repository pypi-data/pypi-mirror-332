"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingListenableFuture

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Preconditions
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import Executor
from typing import Any, Callable, Iterable, Tuple


class ForwardingListenableFuture(ForwardingFuture, ListenableFuture):
    """
    A ListenableFuture which forwards all its method calls to another future. Subclasses
    should override one or more methods to modify the behavior of the backing future as desired per
    the <a href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    Most subclasses can just use SimpleForwardingListenableFuture.

    Author(s)
    - Shardul Deo

    Since
    - 4.0
    """

    def addListener(self, listener: "Runnable", exec: "Executor") -> None:
        ...


    class SimpleForwardingListenableFuture(ForwardingListenableFuture):
        """
        A simplified version of ForwardingListenableFuture where subclasses can pass in an
        already constructed ListenableFuture as the delegate.

        Since
        - 9.0
        """


