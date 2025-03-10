"""
Python module generated from Java source file com.google.common.util.concurrent.TimeoutFuture

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.util.concurrent import *
from java.util.concurrent import ExecutionException
from java.util.concurrent import Future
from java.util.concurrent import ScheduledExecutorService
from java.util.concurrent import ScheduledFuture
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class TimeoutFuture(TrustedFuture):
    """
    Implementation of `Futures.withTimeout`.
    
    Future that delegates to another but will finish early (via a TimeoutException wrapped
    in an ExecutionException) if the specified duration expires. The delegate future is
    interrupted and cancelled if it times out.
    """


