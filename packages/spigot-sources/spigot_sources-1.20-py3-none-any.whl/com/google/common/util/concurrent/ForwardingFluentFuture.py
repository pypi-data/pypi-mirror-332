"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingFluentFuture

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingFluentFuture(FluentFuture):
    """
    FluentFuture that forwards all calls to a delegate.
    
    <h3>Extension</h3>
    
    If you want a class like `FluentFuture` but with extra methods, we recommend declaring your
    own subclass of ListenableFuture, complete with a method like .from to adapt an
    existing `ListenableFuture`, implemented atop a ForwardingListenableFuture that
    forwards to that future and adds the desired methods.
    """

    def addListener(self, listener: "Runnable", executor: "Executor") -> None:
        ...


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


    def toString(self) -> str:
        ...
