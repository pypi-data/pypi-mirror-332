"""
Python module generated from Java source file com.google.common.cache.CacheBuilder

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Ascii
from com.google.common.base import Equivalence
from com.google.common.base import MoreObjects
from com.google.common.base import Supplier
from com.google.common.base import Suppliers
from com.google.common.base import Ticker
from com.google.common.cache import *
from com.google.common.cache.AbstractCache import SimpleStatsCounter
from com.google.common.cache.AbstractCache import StatsCounter
from com.google.common.cache.LocalCache import Strength
from com.google.errorprone.annotations import CheckReturnValue
from com.google.j2objc.annotations import J2ObjCIncompatible
from java.util import ConcurrentModificationException
from java.util import IdentityHashMap
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import TimeUnit
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CacheBuilder:
    """
    A builder of LoadingCache and Cache instances.
    
    <h2>Prefer <a href="https://github.com/ben-manes/caffeine/wiki">Caffeine</a> over Guava's caching
    API</h2>
    
    The successor to Guava's caching API is <a
    href="https://github.com/ben-manes/caffeine/wiki">Caffeine</a>. Its API is designed to make it a
    nearly drop-in replacement -- though it requires Java 8 APIs, is not available for Android or
    GWT/j2cl, and may have <a href="https://github.com/ben-manes/caffeine/wiki/Guava">different
    (usually better) behavior</a> when multiple threads attempt concurrent mutations. Its equivalent
    to `CacheBuilder` is its <a
    href="https://www.javadoc.io/doc/com.github.ben-manes.caffeine/caffeine/latest/com.github.benmanes.caffeine/com/github/benmanes/caffeine/cache/Caffeine.html">`Caffeine`</a> class. Caffeine offers better performance, more features (including asynchronous
    loading), and fewer <a
    href="https://github.com/google/guava/issues?q=is%3Aopen+is%3Aissue+label%3Apackage%3Dcache+label%3Atype%3Ddefect">bugs</a>.
    
    Caffeine defines its own interfaces (<a
    href="https://www.javadoc.io/doc/com.github.ben-manes.caffeine/caffeine/latest/com.github.benmanes.caffeine/com/github/benmanes/caffeine/cache/Cache.html">`Cache`</a>, <a
    href="https://www.javadoc.io/doc/com.github.ben-manes.caffeine/caffeine/latest/com.github.benmanes.caffeine/com/github/benmanes/caffeine/cache/LoadingCache.html">`LoadingCache`</a>, <a
    href="https://www.javadoc.io/doc/com.github.ben-manes.caffeine/caffeine/latest/com.github.benmanes.caffeine/com/github/benmanes/caffeine/cache/CacheLoader.html">`CacheLoader`</a>, etc.), so you can use Caffeine without needing to use any Guava types.
    Caffeine's types are better than Guava's, especially for <a
    href="https://www.javadoc.io/doc/com.github.ben-manes.caffeine/caffeine/latest/com.github.benmanes.caffeine/com/github/benmanes/caffeine/cache/AsyncLoadingCache.html">their
    deep support for asynchronous operations</a>. But if you want to migrate to Caffeine with minimal
    code changes, you can use <a
    href="https://www.javadoc.io/doc/com.github.ben-manes.caffeine/guava/latest/com.github.benmanes.caffeine.guava/com/github/benmanes/caffeine/guava/CaffeinatedGuava.html">its
    `CaffeinatedGuava` adapter class</a>, which lets you build a Guava `Cache` or a Guava
    `LoadingCache` backed by a Guava `CacheLoader`.
    
    Caffeine's API for asynchronous operations uses `CompletableFuture`: <a
    href="https://www.javadoc.io/doc/com.github.ben-manes.caffeine/caffeine/latest/com.github.benmanes.caffeine/com/github/benmanes/caffeine/cache/AsyncLoadingCache.html#get(K)">`AsyncLoadingCache.get`</a> returns a `CompletableFuture`, and implementations of <a
    href="https://www.javadoc.io/doc/com.github.ben-manes.caffeine/caffeine/latest/com.github.benmanes.caffeine/com/github/benmanes/caffeine/cache/AsyncCacheLoader.html#asyncLoad(K,java.util.concurrent.Executor)">`AsyncCacheLoader.asyncLoad`</a> must return a `CompletableFuture`. Users of Guava's com.google.common.util.concurrent.ListenableFuture can adapt between the two `Future`
    types by using <a href="https://github.com/lukas-krecan/future-converter#java8-guava">`net.javacrumbs.futureconverter.java8guava.FutureConverter`</a>.
    
    <h2>More on `CacheBuilder`</h2>
    
    `CacheBuilder` builds caches with any combination of the following features:
    
    
      - automatic loading of entries into the cache
      - least-recently-used eviction when a maximum size is exceeded (note that the cache is
          divided into segments, each of which does LRU internally)
      - time-based expiration of entries, measured since last access or last write
      - keys automatically wrapped in `WeakReference`
      - values automatically wrapped in `WeakReference` or `SoftReference`
      - notification of evicted (or otherwise removed) entries
      - accumulation of cache access statistics
    
    
    These features are all optional; caches can be created using all or none of them. By default
    cache instances created by `CacheBuilder` will not perform any type of eviction.
    
    Usage example:
    
    ````LoadingCache<Key, Graph> graphs = CacheBuilder.newBuilder()
        .maximumSize(10000)
        .expireAfterWrite(Duration.ofMinutes(10))
        .removalListener(MY_LISTENER)
        .build(
            new CacheLoader<Key, Graph>() {
              public Graph load(Key key) throws AnyException {
                return createExpensiveGraph(key);`
            });
    }```
    
    Or equivalently,
    
    ````// In real life this would come from a command-line flag or config file
    String spec = "maximumSize=10000,expireAfterWrite=10m";
    
    LoadingCache<Key, Graph> graphs = CacheBuilder.from(spec)
        .removalListener(MY_LISTENER)
        .build(
            new CacheLoader<Key, Graph>() {
              public Graph load(Key key) throws AnyException {
                return createExpensiveGraph(key);`
            });
    }```
    
    The returned cache is implemented as a hash table with similar performance characteristics to
    ConcurrentHashMap. It implements all optional operations of the LoadingCache and
    Cache interfaces. The `asMap` view (and its collection views) have *weakly
    consistent iterators*. This means that they are safe for concurrent use, but if other threads
    modify the cache after the iterator is created, it is undefined which of these changes, if any,
    are reflected in that iterator. These iterators never throw ConcurrentModificationException.
    
    **Note:** by default, the returned cache uses equality comparisons (the Object.equals equals method) to determine equality for keys or values. However, if .weakKeys was specified, the cache uses identity (`==`) comparisons instead for keys.
    Likewise, if .weakValues or .softValues was specified, the cache uses identity
    comparisons for values.
    
    Entries are automatically evicted from the cache when any of .maximumSize(long)
    maximumSize, .maximumWeight(long) maximumWeight, .expireAfterWrite
    expireAfterWrite, .expireAfterAccess expireAfterAccess, .weakKeys
    weakKeys, .weakValues weakValues, or .softValues softValues are
    requested.
    
    If .maximumSize(long) maximumSize or .maximumWeight(long)
    maximumWeight is requested entries may be evicted on each cache modification.
    
    If .expireAfterWrite expireAfterWrite or .expireAfterAccess
    expireAfterAccess is requested entries may be evicted on each cache modification, on occasional
    cache accesses, or on calls to Cache.cleanUp. Expired entries may be counted by Cache.size, but will never be visible to read or write operations.
    
    If .weakKeys weakKeys, .weakValues weakValues, or .softValues softValues are requested, it is possible for a key or value present in the cache to
    be reclaimed by the garbage collector. Entries with reclaimed keys or values may be removed from
    the cache on each cache modification, on occasional cache accesses, or on calls to Cache.cleanUp; such entries may be counted in Cache.size, but will never be visible to
    read or write operations.
    
    Certain cache configurations will result in the accrual of periodic maintenance tasks which
    will be performed during write operations, or during occasional read operations in the absence of
    writes. The Cache.cleanUp method of the returned cache will also perform maintenance, but
    calling it should not be necessary with a high throughput cache. Only caches built with
    .removalListener removalListener, .expireAfterWrite expireAfterWrite,
    .expireAfterAccess expireAfterAccess, .weakKeys weakKeys, .weakValues weakValues, or .softValues softValues perform periodic maintenance.
    
    The caches produced by `CacheBuilder` are serializable, and the deserialized caches
    retain all the configuration properties of the original cache. Note that the serialized form does
    *not* include cache contents, but only configuration.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/CachesExplained">caching</a> for a higher-level
    explanation.
    
    Type `<K>`: the most general key type this builder will be able to create caches for. This is
        normally `Object` unless it is constrained by using a method like `.removalListener`. Cache keys may not be null.
    
    Type `<V>`: the most general value type this builder will be able to create caches for. This is
        normally `Object` unless it is constrained by using a method like `.removalListener`. Cache values may not be null.

    Author(s)
    - Kevin Bourrillion

    Since
    - 10.0
    """

    @staticmethod
    def newBuilder() -> "CacheBuilder"["Object", "Object"]:
        """
        Constructs a new `CacheBuilder` instance with default settings, including strong keys,
        strong values, and no automatic eviction of any kind.
        
        Note that while this return type is `CacheBuilder<Object, Object>`, type parameters on
        the .build methods allow you to create a cache of any key and value type desired.
        """
        ...


    @staticmethod
    def from(spec: "CacheBuilderSpec") -> "CacheBuilder"["Object", "Object"]:
        """
        Constructs a new `CacheBuilder` instance with the settings specified in `spec`.

        Since
        - 12.0
        """
        ...


    @staticmethod
    def from(spec: str) -> "CacheBuilder"["Object", "Object"]:
        """
        Constructs a new `CacheBuilder` instance with the settings specified in `spec`.
        This is especially useful for command-line configuration of a `CacheBuilder`.

        Arguments
        - spec: a String in the format specified by CacheBuilderSpec

        Since
        - 12.0
        """
        ...


    def initialCapacity(self, initialCapacity: int) -> "CacheBuilder"["K", "V"]:
        """
        Sets the minimum total size for the internal hash tables. For example, if the initial capacity
        is `60`, and the concurrency level is `8`, then eight segments are created, each
        having a hash table of size eight. Providing a large enough estimate at construction time
        avoids the need for expensive resizing operations later, but setting this value unnecessarily
        high wastes memory.

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `initialCapacity` is negative
        - IllegalStateException: if an initial capacity was already set
        """
        ...


    def concurrencyLevel(self, concurrencyLevel: int) -> "CacheBuilder"["K", "V"]:
        """
        Guides the allowed concurrency among update operations. Used as a hint for internal sizing. The
        table is internally partitioned to try to permit the indicated number of concurrent updates
        without contention. Because assignment of entries to these partitions is not necessarily
        uniform, the actual concurrency observed may vary. Ideally, you should choose a value to
        accommodate as many threads as will ever concurrently modify the table. Using a significantly
        higher value than you need can waste space and time, and a significantly lower value can lead
        to thread contention. But overestimates and underestimates within an order of magnitude do not
        usually have much noticeable impact. A value of one permits only one thread to modify the cache
        at a time, but since read operations and cache loading computations can proceed concurrently,
        this still yields higher concurrency than full synchronization.
        
        Defaults to 4. **Note:**The default may change in the future. If you care about this
        value, you should always choose it explicitly.
        
        The current implementation uses the concurrency level to create a fixed number of hashtable
        segments, each governed by its own write lock. The segment lock is taken once for each explicit
        write, and twice for each cache loading computation (once prior to loading the new value, and
        once after loading completes). Much internal cache management is performed at the segment
        granularity. For example, access queues and write queues are kept per segment when they are
        required by the selected eviction algorithm. As such, when writing unit tests it is not
        uncommon to specify `concurrencyLevel(1)` in order to achieve more deterministic eviction
        behavior.
        
        Note that future implementations may abandon segment locking in favor of more advanced
        concurrency controls.

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `concurrencyLevel` is nonpositive
        - IllegalStateException: if a concurrency level was already set
        """
        ...


    def maximumSize(self, maximumSize: int) -> "CacheBuilder"["K", "V"]:
        """
        Specifies the maximum number of entries the cache may contain.
        
        Note that the cache **may evict an entry before this limit is exceeded**. For example, in
        the current implementation, when `concurrencyLevel` is greater than `1`, each
        resulting segment inside the cache *independently* limits its own size to approximately
        `maximumSize / concurrencyLevel`.
        
        When eviction is necessary, the cache evicts entries that are less likely to be used again.
        For example, the cache may evict an entry because it hasn't been used recently or very often.
        
        If `maximumSize` is zero, elements will be evicted immediately after being loaded into
        cache. This can be useful in testing, or to disable caching temporarily.
        
        This feature cannot be used in conjunction with .maximumWeight.

        Arguments
        - maximumSize: the maximum size of the cache

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `maximumSize` is negative
        - IllegalStateException: if a maximum size or weight was already set
        """
        ...


    def maximumWeight(self, maximumWeight: int) -> "CacheBuilder"["K", "V"]:
        """
        Specifies the maximum weight of entries the cache may contain. Weight is determined using the
        Weigher specified with .weigher, and use of this method requires a
        corresponding call to .weigher prior to calling .build.
        
        Note that the cache **may evict an entry before this limit is exceeded**. For example, in
        the current implementation, when `concurrencyLevel` is greater than `1`, each
        resulting segment inside the cache *independently* limits its own weight to approximately
        `maximumWeight / concurrencyLevel`.
        
        When eviction is necessary, the cache evicts entries that are less likely to be used again.
        For example, the cache may evict an entry because it hasn't been used recently or very often.
        
        If `maximumWeight` is zero, elements will be evicted immediately after being loaded
        into cache. This can be useful in testing, or to disable caching temporarily.
        
        Note that weight is only used to determine whether the cache is over capacity; it has no
        effect on selecting which entry should be evicted next.
        
        This feature cannot be used in conjunction with .maximumSize.

        Arguments
        - maximumWeight: the maximum total weight of entries the cache may contain

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `maximumWeight` is negative
        - IllegalStateException: if a maximum weight or size was already set

        Since
        - 11.0
        """
        ...


    def weigher(self, weigher: "Weigher"["K1", "V1"]) -> "CacheBuilder"["K1", "V1"]:
        """
        Specifies the weigher to use in determining the weight of entries. Entry weight is taken into
        consideration by .maximumWeight(long) when determining which entries to evict, and use
        of this method requires a corresponding call to .maximumWeight(long) prior to calling
        .build. Weights are measured and recorded when entries are inserted into the cache, and
        are thus effectively static during the lifetime of a cache entry.
        
        When the weight of an entry is zero it will not be considered for size-based eviction
        (though it still may be evicted by other means).
        
        **Important note:** Instead of returning *this* as a `CacheBuilder`
        instance, this method returns `CacheBuilder<K1, V1>`. From this point on, either the
        original reference or the returned reference may be used to complete configuration and build
        the cache, but only the "generic" one is type-safe. That is, it will properly prevent you from
        building caches whose key or value types are incompatible with the types accepted by the
        weigher already provided; the `CacheBuilder` type cannot do this. For best results,
        simply use the standard method-chaining idiom, as illustrated in the documentation at top,
        configuring a `CacheBuilder` and building your Cache all in a single statement.
        
        **Warning:** if you ignore the above advice, and use this `CacheBuilder` to build a
        cache whose key or value type is incompatible with the weigher, you will likely experience a
        ClassCastException at some *undefined* point in the future.

        Arguments
        - weigher: the weigher to use in calculating the weight of cache entries

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `size` is negative
        - IllegalStateException: if a maximum size was already set

        Since
        - 11.0
        """
        ...


    def weakKeys(self) -> "CacheBuilder"["K", "V"]:
        """
        Specifies that each key (not value) stored in the cache should be wrapped in a WeakReference (by default, strong references are used).
        
        **Warning:** when this method is used, the resulting cache will use identity (`==`)
        comparison to determine equality of keys. Its Cache.asMap view will therefore
        technically violate the Map specification (in the same way that IdentityHashMap
        does).
        
        Entries with keys that have been garbage collected may be counted in Cache.size, but
        will never be visible to read or write operations; such entries are cleaned up as part of the
        routine maintenance described in the class javadoc.

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalStateException: if the key strength was already set
        """
        ...


    def weakValues(self) -> "CacheBuilder"["K", "V"]:
        """
        Specifies that each value (not key) stored in the cache should be wrapped in a WeakReference (by default, strong references are used).
        
        Weak values will be garbage collected once they are weakly reachable. This makes them a poor
        candidate for caching; consider .softValues instead.
        
        **Note:** when this method is used, the resulting cache will use identity (`==`)
        comparison to determine equality of values.
        
        Entries with values that have been garbage collected may be counted in Cache.size,
        but will never be visible to read or write operations; such entries are cleaned up as part of
        the routine maintenance described in the class javadoc.

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalStateException: if the value strength was already set
        """
        ...


    def softValues(self) -> "CacheBuilder"["K", "V"]:
        """
        Specifies that each value (not key) stored in the cache should be wrapped in a SoftReference (by default, strong references are used). Softly-referenced objects will be
        garbage-collected in a *globally* least-recently-used manner, in response to memory
        demand.
        
        **Warning:** in most circumstances it is better to set a per-cache .maximumSize(long) maximum size instead of using soft references. You should only use this
        method if you are well familiar with the practical consequences of soft references.
        
        **Note:** when this method is used, the resulting cache will use identity (`==`)
        comparison to determine equality of values.
        
        Entries with values that have been garbage collected may be counted in Cache.size,
        but will never be visible to read or write operations; such entries are cleaned up as part of
        the routine maintenance described in the class javadoc.

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalStateException: if the value strength was already set
        """
        ...


    def expireAfterWrite(self, duration: "java.time.Duration") -> "CacheBuilder"["K", "V"]:
        """
        Specifies that each entry should be automatically removed from the cache once a fixed duration
        has elapsed after the entry's creation, or the most recent replacement of its value.
        
        When `duration` is zero, this method hands off to .maximumSize(long)
        maximumSize`(0)`, ignoring any otherwise-specified maximum size or weight. This can be
        useful in testing, or to disable caching temporarily without a code change.
        
        Expired entries may be counted in Cache.size, but will never be visible to read or
        write operations. Expired entries are cleaned up as part of the routine maintenance described
        in the class javadoc.

        Arguments
        - duration: the length of time after an entry is created that it should be automatically
            removed

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `duration` is negative
        - IllegalStateException: if .expireAfterWrite was already set
        - ArithmeticException: for durations greater than +/- approximately 292 years

        Since
        - 25.0
        """
        ...


    def expireAfterWrite(self, duration: int, unit: "TimeUnit") -> "CacheBuilder"["K", "V"]:
        """
        Specifies that each entry should be automatically removed from the cache once a fixed duration
        has elapsed after the entry's creation, or the most recent replacement of its value.
        
        When `duration` is zero, this method hands off to .maximumSize(long)
        maximumSize`(0)`, ignoring any otherwise-specified maximum size or weight. This can be
        useful in testing, or to disable caching temporarily without a code change.
        
        Expired entries may be counted in Cache.size, but will never be visible to read or
        write operations. Expired entries are cleaned up as part of the routine maintenance described
        in the class javadoc.
        
        If you can represent the duration as a java.time.Duration (which should be preferred
        when feasible), use .expireAfterWrite(Duration) instead.

        Arguments
        - duration: the length of time after an entry is created that it should be automatically
            removed
        - unit: the unit that `duration` is expressed in

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `duration` is negative
        - IllegalStateException: if .expireAfterWrite was already set
        """
        ...


    def expireAfterAccess(self, duration: "java.time.Duration") -> "CacheBuilder"["K", "V"]:
        """
        Specifies that each entry should be automatically removed from the cache once a fixed duration
        has elapsed after the entry's creation, the most recent replacement of its value, or its last
        access. Access time is reset by all cache read and write operations (including `Cache.asMap().get(Object)` and `Cache.asMap().put(K, V)`), but not by `containsKey(Object)`, nor by operations on the collection-views of Cache.asMap}. So,
        for example, iterating through `Cache.asMap().entrySet()` does not reset access time for
        the entries you retrieve.
        
        When `duration` is zero, this method hands off to .maximumSize(long)
        maximumSize`(0)`, ignoring any otherwise-specified maximum size or weight. This can be
        useful in testing, or to disable caching temporarily without a code change.
        
        Expired entries may be counted in Cache.size, but will never be visible to read or
        write operations. Expired entries are cleaned up as part of the routine maintenance described
        in the class javadoc.

        Arguments
        - duration: the length of time after an entry is last accessed that it should be
            automatically removed

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `duration` is negative
        - IllegalStateException: if .expireAfterAccess was already set
        - ArithmeticException: for durations greater than +/- approximately 292 years

        Since
        - 25.0
        """
        ...


    def expireAfterAccess(self, duration: int, unit: "TimeUnit") -> "CacheBuilder"["K", "V"]:
        """
        Specifies that each entry should be automatically removed from the cache once a fixed duration
        has elapsed after the entry's creation, the most recent replacement of its value, or its last
        access. Access time is reset by all cache read and write operations (including `Cache.asMap().get(Object)` and `Cache.asMap().put(K, V)`), but not by `containsKey(Object)`, nor by operations on the collection-views of Cache.asMap. So, for
        example, iterating through `Cache.asMap().entrySet()` does not reset access time for the
        entries you retrieve.
        
        When `duration` is zero, this method hands off to .maximumSize(long)
        maximumSize`(0)`, ignoring any otherwise-specified maximum size or weight. This can be
        useful in testing, or to disable caching temporarily without a code change.
        
        Expired entries may be counted in Cache.size, but will never be visible to read or
        write operations. Expired entries are cleaned up as part of the routine maintenance described
        in the class javadoc.
        
        If you can represent the duration as a java.time.Duration (which should be preferred
        when feasible), use .expireAfterAccess(Duration) instead.

        Arguments
        - duration: the length of time after an entry is last accessed that it should be
            automatically removed
        - unit: the unit that `duration` is expressed in

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `duration` is negative
        - IllegalStateException: if .expireAfterAccess was already set
        """
        ...


    def refreshAfterWrite(self, duration: "java.time.Duration") -> "CacheBuilder"["K", "V"]:
        """
        Specifies that active entries are eligible for automatic refresh once a fixed duration has
        elapsed after the entry's creation, or the most recent replacement of its value. The semantics
        of refreshes are specified in LoadingCache.refresh, and are performed by calling CacheLoader.reload.
        
        As the default implementation of CacheLoader.reload is synchronous, it is
        recommended that users of this method override CacheLoader.reload with an asynchronous
        implementation; otherwise refreshes will be performed during unrelated cache read and write
        operations.
        
        Currently automatic refreshes are performed when the first stale request for an entry
        occurs. The request triggering refresh will make a synchronous call to CacheLoader.reload
        to obtain a future of the new value. If the returned future is already complete, it is returned
        immediately. Otherwise, the old value is returned.
        
        **Note:** *all exceptions thrown during refresh will be logged and then swallowed*.

        Arguments
        - duration: the length of time after an entry is created that it should be considered
            stale, and thus eligible for refresh

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `duration` is negative
        - IllegalStateException: if .refreshAfterWrite was already set
        - ArithmeticException: for durations greater than +/- approximately 292 years

        Since
        - 25.0
        """
        ...


    def refreshAfterWrite(self, duration: int, unit: "TimeUnit") -> "CacheBuilder"["K", "V"]:
        """
        Specifies that active entries are eligible for automatic refresh once a fixed duration has
        elapsed after the entry's creation, or the most recent replacement of its value. The semantics
        of refreshes are specified in LoadingCache.refresh, and are performed by calling CacheLoader.reload.
        
        As the default implementation of CacheLoader.reload is synchronous, it is
        recommended that users of this method override CacheLoader.reload with an asynchronous
        implementation; otherwise refreshes will be performed during unrelated cache read and write
        operations.
        
        Currently automatic refreshes are performed when the first stale request for an entry
        occurs. The request triggering refresh will make a synchronous call to CacheLoader.reload
        and immediately return the new value if the returned future is complete, and the old value
        otherwise.
        
        **Note:** *all exceptions thrown during refresh will be logged and then swallowed*.
        
        If you can represent the duration as a java.time.Duration (which should be preferred
        when feasible), use .refreshAfterWrite(Duration) instead.

        Arguments
        - duration: the length of time after an entry is created that it should be considered
            stale, and thus eligible for refresh
        - unit: the unit that `duration` is expressed in

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalArgumentException: if `duration` is negative
        - IllegalStateException: if .refreshAfterWrite was already set

        Since
        - 11.0
        """
        ...


    def ticker(self, ticker: "Ticker") -> "CacheBuilder"["K", "V"]:
        """
        Specifies a nanosecond-precision time source for this cache. By default, System.nanoTime is used.
        
        The primary intent of this method is to facilitate testing of caches with a fake or mock
        time source.

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalStateException: if a ticker was already set
        """
        ...


    def removalListener(self, listener: "RemovalListener"["K1", "V1"]) -> "CacheBuilder"["K1", "V1"]:
        """
        Specifies a listener instance that caches should notify each time an entry is removed for any
        RemovalCause reason. Each cache created by this builder will invoke this listener
        as part of the routine maintenance described in the class documentation above.
        
        **Warning:** after invoking this method, do not continue to use *this* cache builder
        reference; instead use the reference this method *returns*. At runtime, these point to the
        same instance, but only the returned reference has the correct generic type information so as
        to ensure type safety. For best results, use the standard method-chaining idiom illustrated in
        the class documentation above, configuring a builder and building your cache in a single
        statement. Failure to heed this advice can result in a ClassCastException being thrown
        by a cache operation at some *undefined* point in the future.
        
        **Warning:** any exception thrown by `listener` will *not* be propagated to
        the `Cache` user, only logged via a Logger.

        Returns
        - this `CacheBuilder` instance (for chaining)

        Raises
        - IllegalStateException: if a removal listener was already set
        """
        ...


    def recordStats(self) -> "CacheBuilder"["K", "V"]:
        """
        Enable the accumulation of CacheStats during the operation of the cache. Without this
        Cache.stats will return zero for all statistics. Note that recording stats requires
        bookkeeping to be performed with each operation, and thus imposes a performance penalty on
        cache operation.

        Returns
        - this `CacheBuilder` instance (for chaining)

        Since
        - 12.0 (previously, stats collection was automatic)
        """
        ...


    def build(self, loader: "CacheLoader"["K1", "V1"]) -> "LoadingCache"["K1", "V1"]:
        """
        Builds a cache, which either returns an already-loaded value for a given key or atomically
        computes or retrieves it using the supplied `CacheLoader`. If another thread is currently
        loading the value for this key, simply waits for that thread to finish and returns its loaded
        value. Note that multiple threads can concurrently load values for distinct keys.
        
        This method does not alter the state of this `CacheBuilder` instance, so it can be
        invoked again to create multiple independent caches.

        Arguments
        - loader: the cache loader used to obtain new values

        Returns
        - a cache having the requested features
        """
        ...


    def build(self) -> "Cache"["K1", "V1"]:
        """
        Builds a cache which does not automatically load values when keys are requested.
        
        Consider .build(CacheLoader) instead, if it is feasible to implement a `CacheLoader`.
        
        This method does not alter the state of this `CacheBuilder` instance, so it can be
        invoked again to create multiple independent caches.

        Returns
        - a cache having the requested features

        Since
        - 11.0
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation for this CacheBuilder instance. The exact form of the returned
        string is not specified.
        """
        ...
