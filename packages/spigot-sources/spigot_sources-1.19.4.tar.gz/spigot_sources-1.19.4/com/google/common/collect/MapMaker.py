"""
Python module generated from Java source file com.google.common.collect.MapMaker

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
from com.google.common.collect import *
from com.google.common.collect.MapMakerInternalMap import Strength
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.lang.ref import WeakReference
from java.util import ConcurrentModificationException
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MapMaker:
    """
    A builder of ConcurrentMap instances that can have keys or values automatically wrapped
    in WeakReference weak references.
    
    Usage example:
    
    ````ConcurrentMap<Request, Stopwatch> timers = new MapMaker()
        .concurrencyLevel(4)
        .weakKeys()
        .makeMap();````
    
    These features are all optional; `new MapMaker().makeMap()` returns a valid concurrent
    map that behaves similarly to a ConcurrentHashMap.
    
    The returned map is implemented as a hash table with similar performance characteristics to
    ConcurrentHashMap. It supports all optional operations of the `ConcurrentMap`
    interface. It does not permit null keys or values.
    
    **Note:** by default, the returned map uses equality comparisons (the Object.equals
    equals method) to determine equality for keys or values. However, if .weakKeys was
    specified, the map uses identity (`==`) comparisons instead for keys. Likewise, if .weakValues was specified, the map uses identity comparisons for values.
    
    The view collections of the returned map have *weakly consistent iterators*. This means
    that they are safe for concurrent use, but if other threads modify the map after the iterator is
    created, it is undefined which of these changes, if any, are reflected in that iterator. These
    iterators never throw ConcurrentModificationException.
    
    If .weakKeys or .weakValues are requested, it is possible for a key or value
    present in the map to be reclaimed by the garbage collector. Entries with reclaimed keys or
    values may be removed from the map on each map modification or on occasional map accesses; such
    entries may be counted by Map.size, but will never be visible to read or write
    operations. A partially-reclaimed entry is never exposed to the user. Any Map.Entry
    instance retrieved from the map's Map.entrySet entry set is a snapshot of that
    entry's state at the time of retrieval; such entries do, however, support Map.Entry.setValue, which simply calls Map.put on the entry's key.
    
    The maps produced by `MapMaker` are serializable, and the deserialized maps retain all
    the configuration properties of the original map. During deserialization, if the original map had
    used weak references, the entries are reconstructed as they were, but it's not unlikely they'll
    be quickly garbage-collected before they are ever accessed.
    
    `new MapMaker().weakKeys().makeMap()` is a recommended replacement for java.util.WeakHashMap, but note that it compares keys using object identity whereas `WeakHashMap` uses Object.equals.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    def __init__(self):
        """
        Constructs a new `MapMaker` instance with default settings, including strong keys, strong
        values, and no automatic eviction of any kind.
        """
        ...


    def initialCapacity(self, initialCapacity: int) -> "MapMaker":
        """
        Sets the minimum total size for the internal hash tables. For example, if the initial capacity
        is `60`, and the concurrency level is `8`, then eight segments are created, each
        having a hash table of size eight. Providing a large enough estimate at construction time
        avoids the need for expensive resizing operations later, but setting this value unnecessarily
        high wastes memory.

        Raises
        - IllegalArgumentException: if `initialCapacity` is negative
        - IllegalStateException: if an initial capacity was already set
        """
        ...


    def concurrencyLevel(self, concurrencyLevel: int) -> "MapMaker":
        """
        Guides the allowed concurrency among update operations. Used as a hint for internal sizing. The
        table is internally partitioned to try to permit the indicated number of concurrent updates
        without contention. Because assignment of entries to these partitions is not necessarily
        uniform, the actual concurrency observed may vary. Ideally, you should choose a value to
        accommodate as many threads as will ever concurrently modify the table. Using a significantly
        higher value than you need can waste space and time, and a significantly lower value can lead
        to thread contention. But overestimates and underestimates within an order of magnitude do not
        usually have much noticeable impact. A value of one permits only one thread to modify the map
        at a time, but since read operations can proceed concurrently, this still yields higher
        concurrency than full synchronization. Defaults to 4.
        
        **Note:** Prior to Guava release 9.0, the default was 16. It is possible the default will
        change again in the future. If you care about this value, you should always choose it
        explicitly.

        Raises
        - IllegalArgumentException: if `concurrencyLevel` is nonpositive
        - IllegalStateException: if a concurrency level was already set
        """
        ...


    def weakKeys(self) -> "MapMaker":
        """
        Specifies that each key (not value) stored in the map should be wrapped in a WeakReference (by default, strong references are used).
        
        **Warning:** when this method is used, the resulting map will use identity (`==`)
        comparison to determine equality of keys, which is a technical violation of the Map
        specification, and may not be what you expect.

        Raises
        - IllegalStateException: if the key strength was already set

        See
        - WeakReference
        """
        ...


    def weakValues(self) -> "MapMaker":
        """
        Specifies that each value (not key) stored in the map should be wrapped in a WeakReference (by default, strong references are used).
        
        Weak values will be garbage collected once they are weakly reachable. This makes them a poor
        candidate for caching.
        
        **Warning:** when this method is used, the resulting map will use identity (`==`)
        comparison to determine equality of values. This technically violates the specifications of the
        methods Map.containsValue containsValue, ConcurrentMap.remove(Object, Object)
        remove(Object, Object) and ConcurrentMap.replace(Object, Object, Object) replace(K, V,
        V), and may not be what you expect.

        Raises
        - IllegalStateException: if the value strength was already set

        See
        - WeakReference
        """
        ...


    def makeMap(self) -> "ConcurrentMap"["K", "V"]:
        """
        Builds a thread-safe map. This method does not alter the state of this `MapMaker`
        instance, so it can be invoked again to create multiple independent maps.
        
        The bulk operations `putAll`, `equals`, and `clear` are not guaranteed to
        be performed atomically on the returned map. Additionally, `size` and `containsValue` are implemented as bulk read operations, and thus may fail to observe concurrent
        writes.

        Returns
        - a serializable concurrent map having the requested features
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation for this MapMaker instance. The exact form of the returned
        string is not specified.
        """
        ...
