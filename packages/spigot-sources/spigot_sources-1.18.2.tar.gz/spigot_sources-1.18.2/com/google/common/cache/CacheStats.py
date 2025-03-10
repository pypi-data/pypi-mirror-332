"""
Python module generated from Java source file com.google.common.cache.CacheStats

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import MoreObjects
from com.google.common.base import Objects
from com.google.common.cache import *
from java.util.concurrent import Callable
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class CacheStats:
    """
    Statistics about the performance of a Cache. Instances of this class are immutable.
    
    Cache statistics are incremented according to the following rules:
    
    
      - When a cache lookup encounters an existing cache entry `hitCount` is incremented.
      - When a cache lookup first encounters a missing cache entry, a new entry is loaded.
          
            - After successfully loading an entry `missCount` and `loadSuccessCount`
                are incremented, and the total loading time, in nanoseconds, is added to `totalLoadTime`.
            - When an exception is thrown while loading an entry, `missCount` and `loadExceptionCount` are incremented, and the total loading time, in nanoseconds, is
                added to `totalLoadTime`.
            - Cache lookups that encounter a missing cache entry that is still loading will wait
                for loading to complete (whether successful or not) and then increment `missCount`.
          
      - When an entry is evicted from the cache, `evictionCount` is incremented.
      - No stats are modified when a cache entry is invalidated or manually removed.
      - No stats are modified by operations invoked on the Cache.asMap asMap view of
          the cache.
    
    
    A lookup is specifically defined as an invocation of one of the methods LoadingCache.get(Object), LoadingCache.getUnchecked(Object), Cache.get(Object,
    Callable), or LoadingCache.getAll(Iterable).

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    def __init__(self, hitCount: int, missCount: int, loadSuccessCount: int, loadExceptionCount: int, totalLoadTime: int, evictionCount: int):
        """
        Constructs a new `CacheStats` instance.
        
        Five parameters of the same type in a row is a bad thing, but this class is not constructed
        by end users and is too fine-grained for a builder.
        """
        ...


    def requestCount(self) -> int:
        """
        Returns the number of times Cache lookup methods have returned either a cached or
        uncached value. This is defined as `hitCount + missCount`.
        
        **Note:** the values of the metrics are undefined in case of overflow (though it is
        guaranteed not to throw an exception). If you require specific handling, we recommend
        implementing your own stats collector.
        """
        ...


    def hitCount(self) -> int:
        """
        Returns the number of times Cache lookup methods have returned a cached value.
        """
        ...


    def hitRate(self) -> float:
        """
        Returns the ratio of cache requests which were hits. This is defined as `hitCount /
        requestCount`, or `1.0` when `requestCount == 0`. Note that `hitRate +
        missRate =~ 1.0`.
        """
        ...


    def missCount(self) -> int:
        """
        Returns the number of times Cache lookup methods have returned an uncached (newly
        loaded) value, or null. Multiple concurrent calls to Cache lookup methods on an absent
        value can result in multiple misses, all returning the results of a single cache load
        operation.
        """
        ...


    def missRate(self) -> float:
        """
        Returns the ratio of cache requests which were misses. This is defined as `missCount /
        requestCount`, or `0.0` when `requestCount == 0`. Note that `hitRate +
        missRate =~ 1.0`. Cache misses include all requests which weren't cache hits, including
        requests which resulted in either successful or failed loading attempts, and requests which
        waited for other threads to finish loading. It is thus the case that `missCount &gt;=
        loadSuccessCount + loadExceptionCount`. Multiple concurrent misses for the same key will result
        in a single load operation.
        """
        ...


    def loadCount(self) -> int:
        """
        Returns the total number of times that Cache lookup methods attempted to load new
        values. This includes both successful load operations, as well as those that threw exceptions.
        This is defined as `loadSuccessCount + loadExceptionCount`.
        
        **Note:** the values of the metrics are undefined in case of overflow (though it is
        guaranteed not to throw an exception). If you require specific handling, we recommend
        implementing your own stats collector.
        """
        ...


    def loadSuccessCount(self) -> int:
        """
        Returns the number of times Cache lookup methods have successfully loaded a new value.
        This is usually incremented in conjunction with .missCount, though `missCount` is
        also incremented when an exception is encountered during cache loading (see .loadExceptionCount). Multiple concurrent misses for the same key will result in a single load
        operation. This may be incremented not in conjunction with `missCount` if the load occurs
        as a result of a refresh or if the cache loader returned more items than was requested. `missCount` may also be incremented not in conjunction with this (nor .loadExceptionCount) on calls to `getIfPresent`.
        """
        ...


    def loadExceptionCount(self) -> int:
        """
        Returns the number of times Cache lookup methods threw an exception while loading a new
        value. This is usually incremented in conjunction with `missCount`, though `missCount` is also incremented when cache loading completes successfully (see .loadSuccessCount). Multiple concurrent misses for the same key will result in a single load
        operation. This may be incremented not in conjunction with `missCount` if the load occurs
        as a result of a refresh or if the cache loader returned more items than was requested. `missCount` may also be incremented not in conjunction with this (nor .loadSuccessCount)
        on calls to `getIfPresent`.
        """
        ...


    def loadExceptionRate(self) -> float:
        """
        Returns the ratio of cache loading attempts which threw exceptions. This is defined as `loadExceptionCount / (loadSuccessCount + loadExceptionCount)`, or `0.0` when `loadSuccessCount + loadExceptionCount == 0`.
        
        **Note:** the values of the metrics are undefined in case of overflow (though it is
        guaranteed not to throw an exception). If you require specific handling, we recommend
        implementing your own stats collector.
        """
        ...


    def totalLoadTime(self) -> int:
        """
        Returns the total number of nanoseconds the cache has spent loading new values. This can be
        used to calculate the miss penalty. This value is increased every time `loadSuccessCount`
        or `loadExceptionCount` is incremented.
        """
        ...


    def averageLoadPenalty(self) -> float:
        """
        Returns the average time spent loading new values. This is defined as `totalLoadTime /
        (loadSuccessCount + loadExceptionCount)`.
        
        **Note:** the values of the metrics are undefined in case of overflow (though it is
        guaranteed not to throw an exception). If you require specific handling, we recommend
        implementing your own stats collector.
        """
        ...


    def evictionCount(self) -> int:
        """
        Returns the number of times an entry has been evicted. This count does not include manual
        Cache.invalidate invalidations.
        """
        ...


    def minus(self, other: "CacheStats") -> "CacheStats":
        """
        Returns a new `CacheStats` representing the difference between this `CacheStats`
        and `other`. Negative values, which aren't supported by `CacheStats` will be
        rounded up to zero.
        """
        ...


    def plus(self, other: "CacheStats") -> "CacheStats":
        """
        Returns a new `CacheStats` representing the sum of this `CacheStats` and `other`.
        
        **Note:** the values of the metrics are undefined in case of overflow (though it is
        guaranteed not to throw an exception). If you require specific handling, we recommend
        implementing your own stats collector.

        Since
        - 11.0
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...
