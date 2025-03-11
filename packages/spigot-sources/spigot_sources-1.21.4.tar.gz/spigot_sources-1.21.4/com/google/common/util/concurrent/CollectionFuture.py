"""
Python module generated from Java source file com.google.common.util.concurrent.CollectionFuture

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import ImmutableCollection
from com.google.common.collect import Lists
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations.concurrent import LazyInit
from java.util import Collections
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CollectionFuture(AggregateFuture):
    """
    Aggregate future that collects (stores) results of each future.
    """


