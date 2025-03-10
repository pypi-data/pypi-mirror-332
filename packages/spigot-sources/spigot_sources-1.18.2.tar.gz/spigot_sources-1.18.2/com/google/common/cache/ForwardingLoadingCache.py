"""
Python module generated from Java source file com.google.common.cache.ForwardingLoadingCache

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.cache import *
from com.google.common.collect import ImmutableMap
from java.util.concurrent import ExecutionException
from typing import Any, Callable, Iterable, Tuple


class ForwardingLoadingCache(ForwardingCache, LoadingCache):
    """
    A cache which forwards all its method calls to another cache. Subclasses should override one or
    more methods to modify the behavior of the backing cache as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    Note that .get, .getUnchecked, and .apply all expose the same
    underlying functionality, so should probably be overridden as a group.

    Author(s)
    - Charles Fry

    Since
    - 11.0
    """

    def get(self, key: "K") -> "V":
        ...


    def getUnchecked(self, key: "K") -> "V":
        ...


    def getAll(self, keys: Iterable["K"]) -> "ImmutableMap"["K", "V"]:
        ...


    def apply(self, key: "K") -> "V":
        ...


    def refresh(self, key: "K") -> None:
        ...


    class SimpleForwardingLoadingCache(ForwardingLoadingCache):
        """
        A simplified version of ForwardingLoadingCache where subclasses can pass in an already
        constructed LoadingCache as the delegate.

        Since
        - 10.0
        """


