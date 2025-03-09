"""
Python module generated from Java source file com.google.common.cache.AbstractCache

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.cache import *
from com.google.common.collect import ImmutableMap
from com.google.common.collect import Maps
from java.util.concurrent import Callable
from java.util.concurrent import ConcurrentMap
from java.util.concurrent import ExecutionException
from typing import Any, Callable, Iterable, Tuple


class AbstractCache(Cache):
    """
    This class provides a skeletal implementation of the `Cache` interface to minimize the
    effort required to implement this interface.
    
    To implement a cache, the programmer needs only to extend this class and provide an
    implementation for the .put and .getIfPresent methods. .getAllPresent is
    implemented in terms of .getIfPresent; .putAll is implemented in terms of .put, .invalidateAll(Iterable) is implemented in terms of .invalidate. The
    method .cleanUp is a no-op. All other methods throw an UnsupportedOperationException.

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    def get(self, key: "K", valueLoader: "Callable"["V"]) -> "V":
        """
        Since
        - 11.0
        """
        ...


    def getAllPresent(self, keys: Iterable["Object"]) -> "ImmutableMap"["K", "V"]:
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


    def cleanUp(self) -> None:
        ...


    def size(self) -> int:
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


    def stats(self) -> "CacheStats":
        ...


    def asMap(self) -> "ConcurrentMap"["K", "V"]:
        ...


    class StatsCounter:
        """
        Accumulates statistics during the operation of a Cache for presentation by Cache.stats. This is solely intended for consumption by `Cache` implementors.

        Since
        - 10.0
        """

        def recordHits(self, count: int) -> None:
            """
            Records cache hits. This should be called when a cache request returns a cached value.

            Arguments
            - count: the number of hits to record

            Since
            - 11.0
            """
            ...


        def recordMisses(self, count: int) -> None:
            """
            Records cache misses. This should be called when a cache request returns a value that was not
            found in the cache. This method should be called by the loading thread, as well as by threads
            blocking on the load. Multiple concurrent calls to Cache lookup methods with the same
            key on an absent value should result in a single call to either `recordLoadSuccess` or
            `recordLoadException` and multiple calls to this method, despite all being served by
            the results of a single load operation.

            Arguments
            - count: the number of misses to record

            Since
            - 11.0
            """
            ...


        def recordLoadSuccess(self, loadTime: int) -> None:
            """
            Records the successful load of a new entry. This should be called when a cache request causes
            an entry to be loaded, and the loading completes successfully. In contrast to .recordMisses, this method should only be called by the loading thread.

            Arguments
            - loadTime: the number of nanoseconds the cache spent computing or retrieving the new
                value
            """
            ...


        def recordLoadException(self, loadTime: int) -> None:
            """
            Records the failed load of a new entry. This should be called when a cache request causes an
            entry to be loaded, but an exception is thrown while loading the entry. In contrast to .recordMisses, this method should only be called by the loading thread.

            Arguments
            - loadTime: the number of nanoseconds the cache spent computing or retrieving the new
                value prior to an exception being thrown
            """
            ...


        def recordEviction(self) -> None:
            """
            Records the eviction of an entry from the cache. This should only been called when an entry
            is evicted due to the cache's eviction strategy, and not as a result of manual Cache.invalidate invalidations.
            """
            ...


        def snapshot(self) -> "CacheStats":
            """
            Returns a snapshot of this counter's values. Note that this may be an inconsistent view, as
            it may be interleaved with update operations.
            """
            ...


    class SimpleStatsCounter(StatsCounter):
        """
        A thread-safe StatsCounter implementation for use by Cache implementors.

        Since
        - 10.0
        """

        def __init__(self):
            """
            Constructs an instance with all counts initialized to zero.
            """
            ...


        def recordHits(self, count: int) -> None:
            """
            Since
            - 11.0
            """
            ...


        def recordMisses(self, count: int) -> None:
            """
            Since
            - 11.0
            """
            ...


        def recordLoadSuccess(self, loadTime: int) -> None:
            ...


        def recordLoadException(self, loadTime: int) -> None:
            ...


        def recordEviction(self) -> None:
            ...


        def snapshot(self) -> "CacheStats":
            ...


        def incrementBy(self, other: "StatsCounter") -> None:
            """
            Increments all counters by the values in `other`.
            """
            ...
