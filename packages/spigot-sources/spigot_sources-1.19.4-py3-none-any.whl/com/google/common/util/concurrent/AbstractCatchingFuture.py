"""
Python module generated from Java source file com.google.common.util.concurrent.AbstractCatchingFuture

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Function
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.internal import InternalFutureFailureAccess
from com.google.common.util.concurrent.internal import InternalFutures
from com.google.errorprone.annotations import ForOverride
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractCatchingFuture(TrustedFuture, Runnable):
    """
    Implementations of `Futures.catching*`.
    """

    def run(self) -> None:
        ...
