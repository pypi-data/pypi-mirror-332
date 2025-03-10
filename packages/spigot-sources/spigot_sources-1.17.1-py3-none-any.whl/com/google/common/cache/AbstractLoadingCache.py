"""
Python module generated from Java source file com.google.common.cache.AbstractLoadingCache

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.cache import *
from com.google.common.collect import ImmutableMap
from com.google.common.collect import Maps
from com.google.common.util.concurrent import UncheckedExecutionException
from java.util.concurrent import Callable
from java.util.concurrent import ExecutionException
from typing import Any, Callable, Iterable, Tuple


class AbstractLoadingCache(AbstractCache, LoadingCache):
    """
    This class provides a skeletal implementation of the `Cache` interface to minimize the
    effort required to implement this interface.
    
    To implement a cache, the programmer needs only to extend this class and provide an
    implementation for the .get(Object) and .getIfPresent methods.
    .getUnchecked, .get(Object, Callable), and .getAll are implemented in
    terms of `get`; .getAllPresent is implemented in terms of `getIfPresent`;
    .putAll is implemented in terms of .put, .invalidateAll(Iterable) is
    implemented in terms of .invalidate. The method .cleanUp is a no-op. All other
    methods throw an UnsupportedOperationException.

    Author(s)
    - Charles Fry

    Since
    - 11.0
    """

    def getUnchecked(self, key: "K") -> "V":
        ...


    def getAll(self, keys: Iterable["K"]) -> "ImmutableMap"["K", "V"]:
        ...


    def apply(self, key: "K") -> "V":
        ...


    def refresh(self, key: "K") -> None:
        ...
