"""
Python module generated from Java source file com.google.common.cache.ForwardingCache

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.cache import *
from com.google.common.collect import ForwardingObject
from com.google.common.collect import ImmutableMap
from java.util.concurrent import Callable
from java.util.concurrent import ConcurrentMap
from java.util.concurrent import ExecutionException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ForwardingCache(ForwardingObject, Cache):
    """
    A cache which forwards all its method calls to another cache. Subclasses should override one or
    more methods to modify the behavior of the backing cache as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    def getIfPresent(self, key: "Object") -> "V":
        """
        Since
        - 11.0
        """
        ...


    def get(self, key: "K", valueLoader: "Callable"["V"]) -> "V":
        """
        Since
        - 11.0
        """
        ...


    def getAllPresent(self, keys: Iterable["Object"]) -> "ImmutableMap"["K", "V"]:
        """
        Since
        - 11.0
        """
        ...


    def put(self, key: "K", value: "V") -> None:
        """
        Since
        - 11.0
        """
        ...


    def putAll(self, m: dict["K", "V"]) -> None:
        """
        Since
        - 12.0
        """
        ...


    def invalidate(self, key: "Object") -> None:
        ...


    def invalidateAll(self, keys: Iterable["Object"]) -> None:
        """
        Since
        - 11.0
        """
        ...


    def invalidateAll(self) -> None:
        ...


    def size(self) -> int:
        ...


    def stats(self) -> "CacheStats":
        ...


    def asMap(self) -> "ConcurrentMap"["K", "V"]:
        ...


    def cleanUp(self) -> None:
        ...


    class SimpleForwardingCache(ForwardingCache):
        """
        A simplified version of ForwardingCache where subclasses can pass in an already
        constructed Cache as the delegate.

        Since
        - 10.0
        """


