"""
Python module generated from Java source file com.google.common.util.concurrent.CombinedFuture

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import ImmutableCollection
from com.google.common.util.concurrent import *
from com.google.j2objc.annotations import WeakOuter
from java.util.concurrent import Callable
from java.util.concurrent import CancellationException
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from java.util.concurrent import RejectedExecutionException
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CombinedFuture(AggregateFuture):
    """
    Aggregate future that computes its value by calling a callable.
    """


