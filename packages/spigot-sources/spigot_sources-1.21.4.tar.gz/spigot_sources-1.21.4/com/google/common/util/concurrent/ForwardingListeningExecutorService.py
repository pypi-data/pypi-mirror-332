"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingListeningExecutorService

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from java.util.concurrent import Callable
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingListeningExecutorService(ForwardingExecutorService, ListeningExecutorService):
    """
    A listening executor service which forwards all its method calls to another listening executor
    service. Subclasses should override one or more methods to modify the behavior of the backing
    executor service as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingListeningExecutorService`.

    Author(s)
    - Isaac Shum

    Since
    - 10.0
    """

    def submit(self, task: "Callable"["T"]) -> "ListenableFuture"["T"]:
        ...


    def submit(self, task: "Runnable") -> "ListenableFuture"[Any]:
        ...


    def submit(self, task: "Runnable", result: "T") -> "ListenableFuture"["T"]:
        ...
