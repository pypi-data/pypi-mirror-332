"""
Python module generated from Java source file com.google.common.util.concurrent.FuturesGetChecked

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Function
from com.google.common.collect import Ordering
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import J2ObjCIncompatible
from java.lang.ref import WeakReference
from java.lang.reflect import Constructor
from java.lang.reflect import InvocationTargetException
from java.util import Arrays
from java.util.concurrent import CopyOnWriteArraySet
from java.util.concurrent import ExecutionException
from java.util.concurrent import Future
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class FuturesGetChecked:
    """
    Static methods used to implement Futures.getChecked(Future, Class).
    """


