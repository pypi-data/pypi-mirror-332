"""
Python module generated from Java source file com.google.common.util.concurrent.GwtFuturesCatchingSpecialization

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class GwtFuturesCatchingSpecialization:
    """
    Hidden superclass of Futures that provides us a place to declare special GWT versions of
    the Futures.catching(ListenableFuture, Class, com.google.common.base.Function,
    java.util.concurrent.Executor) Futures.catching family of methods. Those versions have slightly
    different signatures.
    """


