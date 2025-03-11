"""
Python module generated from Java source file com.google.common.cache.Cache

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.cache import *
from com.google.common.collect import ImmutableMap
from com.google.common.util.concurrent import ExecutionError
from com.google.common.util.concurrent import UncheckedExecutionException
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import CompatibleWith
from com.google.errorprone.annotations import DoNotMock
from java.util.concurrent import Callable
from java.util.concurrent import ConcurrentMap
from java.util.concurrent import ExecutionException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Cache:
    """
    A semi-persistent mapping from keys to values. Cache entries are manually added using .get(Object, Callable) or .put(Object, Object), and are stored in the cache until either
    evicted or manually invalidated. The common way to build instances is using CacheBuilder.
    
    Implementations of this interface are expected to be thread-safe, and can be safely accessed
    by multiple concurrent threads.
    
    Type `<K>`: the type of the cache's keys, which are not permitted to be null
    
    Type `<V>`: the type of the cache's values, which are not permitted to be null

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    def getIfPresent(self, key: "Object") -> "V":
        """
        Returns the value associated with `key` in this cache, or `null` if there is no
        cached value for `key`.

        Since
        - 11.0
        """
        ...


    def get(self, key: "K", loader: "Callable"["V"]) -> "V":
        """
        Returns the value associated with `key` in this cache, obtaining that value from `loader` if necessary. The method improves upon the conventional "if cached, return; otherwise
        create, cache and return" pattern. For further improvements, use LoadingCache and its
        LoadingCache.get(Object) get(K) method instead of this one.
        
        Among the improvements that this method and `LoadingCache.get(K)` both provide are:
        
        
          - LoadingCache.get(Object) awaiting the result of a pending load rather than
              starting a redundant one
          - eliminating the error-prone caching boilerplate
          - tracking load .stats statistics
        
        
        Among the further improvements that `LoadingCache` can provide but this method cannot:
        
        
          - consolidation of the loader logic to CacheBuilder.build(CacheLoader) a single
              authoritative location
          - LoadingCache.refresh refreshing of entries, including CacheBuilder.refreshAfterWrite automated refreshing
          - LoadingCache.getAll bulk loading requests, including CacheLoader.loadAll bulk loading implementations
        
        
        **Warning:** For any given key, every `loader` used with it should compute the same
        value. Otherwise, a call that passes one `loader` may return the result of another call
        with a differently behaving `loader`. For example, a call that requests a short timeout
        for an RPC may wait for a similar call that requests a long timeout, or a call by an
        unprivileged user may return a resource accessible only to a privileged user making a similar
        call. To prevent this problem, create a key object that includes all values that affect the
        result of the query. Or use `LoadingCache.get(K)`, which lacks the ability to refer to
        state other than that in the key.
        
        **Warning:** as with CacheLoader.load, `loader` **must not** return
        `null`; it may either return a non-null value or throw an exception.
        
        No observable state associated with this cache is modified until loading completes.

        Raises
        - ExecutionException: if a checked exception was thrown while loading the value
        - UncheckedExecutionException: if an unchecked exception was thrown while loading the
            value
        - ExecutionError: if an error was thrown while loading the value

        Since
        - 11.0
        """
        ...


    def getAllPresent(self, keys: Iterable["Object"]) -> "ImmutableMap"["K", "V"]:
        ...


    def put(self, key: "K", value: "V") -> None:
        """
        Associates `value` with `key` in this cache. If the cache previously contained a
        value associated with `key`, the old value is replaced by `value`.
        
        Prefer .get(Object, Callable) when using the conventional "if cached, return;
        otherwise create, cache and return" pattern.

        Since
        - 11.0
        """
        ...


    def putAll(self, m: dict["K", "V"]) -> None:
        """
        Copies all of the mappings from the specified map to the cache. The effect of this call is
        equivalent to that of calling `put(k, v)` on this map once for each mapping from key
        `k` to value `v` in the specified map. The behavior of this operation is undefined
        if the specified map is modified while the operation is in progress.

        Since
        - 12.0
        """
        ...


    def invalidate(self, key: "Object") -> None:
        """
        Discards any cached value for key `key`.
        """
        ...


    def invalidateAll(self, keys: Iterable["Object"]) -> None:
        ...


    def invalidateAll(self) -> None:
        """
        Discards all entries in the cache.
        """
        ...


    def size(self) -> int:
        """
        Returns the approximate number of entries in this cache.
        """
        ...


    def stats(self) -> "CacheStats":
        """
        Returns a current snapshot of this cache's cumulative statistics, or a set of default values if
        the cache is not recording statistics. All statistics begin at zero and never decrease over the
        lifetime of the cache.
        
        **Warning:** this cache may not be recording statistical data. For example, a cache
        created using CacheBuilder only does so if the CacheBuilder.recordStats method
        was called. If statistics are not being recorded, a `CacheStats` instance with zero for
        all values is returned.
        """
        ...


    def asMap(self) -> "ConcurrentMap"["K", "V"]:
        """
        Returns a view of the entries stored in this cache as a thread-safe map. Modifications made to
        the map directly affect the cache.
        
        Iterators from the returned map are at least *weakly consistent*: they are safe for
        concurrent use, but if the cache is modified (including by eviction) after the iterator is
        created, it is undefined which of the changes (if any) will be reflected in that iterator.
        """
        ...


    def cleanUp(self) -> None:
        """
        Performs any pending maintenance operations needed by the cache. Exactly which activities are
        performed -- if any -- is implementation-dependent.
        """
        ...
