"""
Python module generated from Java source file com.google.common.util.concurrent.TrustedListenableFutureTask

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from com.google.j2objc.annotations import WeakOuter
from java.util.concurrent import Callable
from java.util.concurrent import Executors
from java.util.concurrent import RunnableFuture
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class TrustedListenableFutureTask(TrustedFuture, RunnableFuture):
    """
    A RunnableFuture that also implements the ListenableFuture interface.
    
    This should be used in preference to ListenableFutureTask when possible for
    performance reasons.
    """

    def run(self) -> None:
        ...
