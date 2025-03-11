"""
Python module generated from Java source file com.google.common.util.concurrent.AggregateFuture

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import ImmutableCollection
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import ForOverride
from com.google.errorprone.annotations import OverridingMethodsMustInvokeSuper
from java.util.concurrent import ExecutionException
from java.util.concurrent import Future
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AggregateFuture(AggregateFutureState):
    """
    A future whose value is derived from a collection of input futures.

    Arguments
    - <InputT>: the type of the individual inputs
    - <OutputT>: the type of the output (i.e. this) future
    """


