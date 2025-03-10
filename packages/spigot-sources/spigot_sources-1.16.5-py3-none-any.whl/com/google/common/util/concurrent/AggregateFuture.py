"""
Python module generated from Java source file com.google.common.util.concurrent.AggregateFuture

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import ImmutableCollection
from com.google.common.util.concurrent import *
from java.util.concurrent import ExecutionException
from java.util.concurrent import Future
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class AggregateFuture(TrustedFuture):
    """
    A future made up of a collection of sub-futures.

    Arguments
    - <InputT>: the type of the individual inputs
    - <OutputT>: the type of the output (i.e. this) future
    """


