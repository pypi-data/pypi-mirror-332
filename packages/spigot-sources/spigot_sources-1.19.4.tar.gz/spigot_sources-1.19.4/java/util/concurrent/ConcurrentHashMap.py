"""
Python module generated from Java source file java.util.concurrent.ConcurrentHashMap

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import ObjectStreamField
from java.io import Serializable
from java.lang.reflect import ParameterizedType
from java.lang.reflect import Type
from java.util import Arrays
from java.util import Enumeration
from java.util import Hashtable
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Spliterator
from java.util.concurrent import *
from java.util.concurrent.atomic import AtomicReference
from java.util.concurrent.locks import LockSupport
from java.util.concurrent.locks import ReentrantLock
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import Consumer
from java.util.function import DoubleBinaryOperator
from java.util.function import Function
from java.util.function import IntBinaryOperator
from java.util.function import LongBinaryOperator
from java.util.function import Predicate
from java.util.function import ToDoubleBiFunction
from java.util.function import ToDoubleFunction
from java.util.function import ToIntBiFunction
from java.util.function import ToIntFunction
from java.util.function import ToLongBiFunction
from java.util.function import ToLongFunction
from java.util.stream import Stream
from jdk.internal.misc import Unsafe
from typing import Any, Callable, Iterable, Tuple


class ConcurrentHashMap(AbstractMap, ConcurrentMap, Serializable):
    """
    A hash table supporting full concurrency of retrievals and
    high expected concurrency for updates. This class obeys the
    same functional specification as java.util.Hashtable, and
    includes versions of methods corresponding to each method of
    `Hashtable`. However, even though all operations are
    thread-safe, retrieval operations do *not* entail locking,
    and there is *not* any support for locking the entire table
    in a way that prevents all access.  This class is fully
    interoperable with `Hashtable` in programs that rely on its
    thread safety but not on its synchronization details.
    
    Retrieval operations (including `get`) generally do not
    block, so may overlap with update operations (including `put`
    and `remove`). Retrievals reflect the results of the most
    recently *completed* update operations holding upon their
    onset. (More formally, an update operation for a given key bears a
    *happens-before* relation with any (non-null) retrieval for
    that key reporting the updated value.)  For aggregate operations
    such as `putAll` and `clear`, concurrent retrievals may
    reflect insertion or removal of only some entries.  Similarly,
    Iterators, Spliterators and Enumerations return elements reflecting the
    state of the hash table at some point at or since the creation of the
    iterator/enumeration.  They do *not* throw java.util.ConcurrentModificationException ConcurrentModificationException.
    However, iterators are designed to be used by only one thread at a time.
    Bear in mind that the results of aggregate status methods including
    `size`, `isEmpty`, and `containsValue` are typically
    useful only when a map is not undergoing concurrent updates in other threads.
    Otherwise the results of these methods reflect transient states
    that may be adequate for monitoring or estimation purposes, but not
    for program control.
    
    The table is dynamically expanded when there are too many
    collisions (i.e., keys that have distinct hash codes but fall into
    the same slot modulo the table size), with the expected average
    effect of maintaining roughly two bins per mapping (corresponding
    to a 0.75 load factor threshold for resizing). There may be much
    variance around this average as mappings are added and removed, but
    overall, this maintains a commonly accepted time/space tradeoff for
    hash tables.  However, resizing this or any other kind of hash
    table may be a relatively slow operation. When possible, it is a
    good idea to provide a size estimate as an optional `initialCapacity` constructor argument. An additional optional
    `loadFactor` constructor argument provides a further means of
    customizing initial table capacity by specifying the table density
    to be used in calculating the amount of space to allocate for the
    given number of elements.  Also, for compatibility with previous
    versions of this class, constructors may optionally specify an
    expected `concurrencyLevel` as an additional hint for
    internal sizing.  Note that using many keys with exactly the same
    `hashCode()` is a sure way to slow down performance of any
    hash table. To ameliorate impact, when keys are Comparable,
    this class may use comparison order among keys to help break ties.
    
    A Set projection of a ConcurrentHashMap may be created
    (using .newKeySet() or .newKeySet(int)), or viewed
    (using .keySet(Object) when only keys are of interest, and the
    mapped values are (perhaps transiently) not used or all take the
    same mapping value.
    
    A ConcurrentHashMap can be used as a scalable frequency map (a
    form of histogram or multiset) by using java.util.concurrent.atomic.LongAdder values and initializing via
    .computeIfAbsent computeIfAbsent. For example, to add a count
    to a `ConcurrentHashMap<String,LongAdder> freqs`, you can use
    `freqs.computeIfAbsent(key, k -> new LongAdder()).increment();`
    
    This class and its views and iterators implement all of the
    *optional* methods of the Map and Iterator
    interfaces.
    
    Like Hashtable but unlike HashMap, this class
    does *not* allow `null` to be used as a key or value.
    
    ConcurrentHashMaps support a set of sequential and parallel bulk
    operations that, unlike most Stream methods, are designed
    to be safely, and often sensibly, applied even with maps that are
    being concurrently updated by other threads; for example, when
    computing a snapshot summary of the values in a shared registry.
    There are three kinds of operation, each with four forms, accepting
    functions with keys, values, entries, and (key, value) pairs as
    arguments and/or return values. Because the elements of a
    ConcurrentHashMap are not ordered in any particular way, and may be
    processed in different orders in different parallel executions, the
    correctness of supplied functions should not depend on any
    ordering, or on any other objects or values that may transiently
    change while computation is in progress; and except for forEach
    actions, should ideally be side-effect-free. Bulk operations on
    Map.Entry objects do not support method `setValue`.
    
    
    - forEach: Performs a given action on each element.
    A variant form applies a given transformation on each element
    before performing the action.
    
    - search: Returns the first available non-null result of
    applying a given function on each element; skipping further
    search when a result is found.
    
    - reduce: Accumulates each element.  The supplied reduction
    function cannot rely on ordering (more formally, it should be
    both associative and commutative).  There are five variants:
    
    
    
    - Plain reductions. (There is not a form of this method for
    (key, value) function arguments since there is no corresponding
    return type.)
    
    - Mapped reductions that accumulate the results of a given
    function applied to each element.
    
    - Reductions to scalar doubles, longs, and ints, using a
    given basis value.
    
    
    
    
    These bulk operations accept a `parallelismThreshold`
    argument. Methods proceed sequentially if the current map size is
    estimated to be less than the given threshold. Using a value of
    `Long.MAX_VALUE` suppresses all parallelism.  Using a value
    of `1` results in maximal parallelism by partitioning into
    enough subtasks to fully utilize the ForkJoinPool.commonPool() that is used for all parallel
    computations. Normally, you would initially choose one of these
    extreme values, and then measure performance of using in-between
    values that trade off overhead versus throughput.
    
    The concurrency properties of bulk operations follow
    from those of ConcurrentHashMap: Any non-null result returned
    from `get(key)` and related access methods bears a
    happens-before relation with the associated insertion or
    update.  The result of any bulk operation reflects the
    composition of these per-element relations (but is not
    necessarily atomic with respect to the map as a whole unless it
    is somehow known to be quiescent).  Conversely, because keys
    and values in the map are never null, null serves as a reliable
    atomic indicator of the current lack of any result.  To
    maintain this property, null serves as an implicit basis for
    all non-scalar reduction operations. For the double, long, and
    int versions, the basis should be one that, when combined with
    any other value, returns that other value (more formally, it
    should be the identity element for the reduction). Most common
    reductions have these properties; for example, computing a sum
    with basis 0 or a minimum with basis MAX_VALUE.
    
    Search and transformation functions provided as arguments
    should similarly return null to indicate the lack of any result
    (in which case it is not used). In the case of mapped
    reductions, this also enables transformations to serve as
    filters, returning null (or, in the case of primitive
    specializations, the identity basis) if the element should not
    be combined. You can create compound transformations and
    filterings by composing them yourself under this "null means
    there is nothing there now" rule before using them in search or
    reduce operations.
    
    Methods accepting and/or returning Entry arguments maintain
    key-value associations. They may be useful for example when
    finding the key for the greatest value. Note that "plain" Entry
    arguments can be supplied using `new
    AbstractMap.SimpleEntry(k,v)`.
    
    Bulk operations may complete abruptly, throwing an
    exception encountered in the application of a supplied
    function. Bear in mind when handling such exceptions that other
    concurrently executing functions could also have thrown
    exceptions, or would have done so if the first exception had
    not occurred.
    
    Speedups for parallel compared to sequential forms are common
    but not guaranteed.  Parallel operations involving brief functions
    on small maps may execute more slowly than sequential forms if the
    underlying work to parallelize the computation is more expensive
    than the computation itself.  Similarly, parallelization may not
    lead to much actual parallelism if all processors are busy
    performing unrelated tasks.
    
    All arguments to all task methods must be non-null.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<K>`: the type of keys maintained by this map
    
    Type `<V>`: the type of mapped values

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self):
        """
        Creates a new, empty map with the default initial table size (16).
        """
        ...


    def __init__(self, initialCapacity: int):
        """
        Creates a new, empty map with an initial table size
        accommodating the specified number of elements without the need
        to dynamically resize.

        Arguments
        - initialCapacity: The implementation performs internal
        sizing to accommodate this many elements.

        Raises
        - IllegalArgumentException: if the initial capacity of
        elements is negative
        """
        ...


    def __init__(self, m: dict["K", "V"]):
        """
        Creates a new map with the same mappings as the given map.

        Arguments
        - m: the map
        """
        ...


    def __init__(self, initialCapacity: int, loadFactor: float):
        """
        Creates a new, empty map with an initial table size based on
        the given number of elements (`initialCapacity`) and
        initial table density (`loadFactor`).

        Arguments
        - initialCapacity: the initial capacity. The implementation
        performs internal sizing to accommodate this many elements,
        given the specified load factor.
        - loadFactor: the load factor (table density) for
        establishing the initial table size

        Raises
        - IllegalArgumentException: if the initial capacity of
        elements is negative or the load factor is nonpositive

        Since
        - 1.6
        """
        ...


    def __init__(self, initialCapacity: int, loadFactor: float, concurrencyLevel: int):
        """
        Creates a new, empty map with an initial table size based on
        the given number of elements (`initialCapacity`), initial
        table density (`loadFactor`), and number of concurrently
        updating threads (`concurrencyLevel`).

        Arguments
        - initialCapacity: the initial capacity. The implementation
        performs internal sizing to accommodate this many elements,
        given the specified load factor.
        - loadFactor: the load factor (table density) for
        establishing the initial table size
        - concurrencyLevel: the estimated number of concurrently
        updating threads. The implementation may use this value as
        a sizing hint.

        Raises
        - IllegalArgumentException: if the initial capacity is
        negative or the load factor or concurrencyLevel are
        nonpositive
        """
        ...


    def size(self) -> int:
        """

        """
        ...


    def isEmpty(self) -> bool:
        """

        """
        ...


    def get(self, key: "Object") -> "V":
        """
        Returns the value to which the specified key is mapped,
        or `null` if this map contains no mapping for the key.
        
        More formally, if this map contains a mapping from a key
        `k` to a value `v` such that `key.equals(k)`,
        then this method returns `v`; otherwise it returns
        `null`.  (There can be at most one such mapping.)

        Raises
        - NullPointerException: if the specified key is null
        """
        ...


    def containsKey(self, key: "Object") -> bool:
        """
        Tests if the specified object is a key in this table.

        Arguments
        - key: possible key

        Returns
        - `True` if and only if the specified object
                is a key in this table, as determined by the
                `equals` method; `False` otherwise

        Raises
        - NullPointerException: if the specified key is null
        """
        ...


    def containsValue(self, value: "Object") -> bool:
        """
        Returns `True` if this map maps one or more keys to the
        specified value. Note: This method may require a full traversal
        of the map, and is much slower than method `containsKey`.

        Arguments
        - value: value whose presence in this map is to be tested

        Returns
        - `True` if this map maps one or more keys to the
                specified value

        Raises
        - NullPointerException: if the specified value is null
        """
        ...


    def put(self, key: "K", value: "V") -> "V":
        """
        Maps the specified key to the specified value in this table.
        Neither the key nor the value can be null.
        
        The value can be retrieved by calling the `get` method
        with a key that is equal to the original key.

        Arguments
        - key: key with which the specified value is to be associated
        - value: value to be associated with the specified key

        Returns
        - the previous value associated with `key`, or
                `null` if there was no mapping for `key`

        Raises
        - NullPointerException: if the specified key or value is null
        """
        ...


    def putAll(self, m: dict["K", "V"]) -> None:
        """
        Copies all of the mappings from the specified map to this one.
        These mappings replace any mappings that this map had for any of the
        keys currently in the specified map.

        Arguments
        - m: mappings to be stored in this map
        """
        ...


    def remove(self, key: "Object") -> "V":
        """
        Removes the key (and its corresponding value) from this map.
        This method does nothing if the key is not in the map.

        Arguments
        - key: the key that needs to be removed

        Returns
        - the previous value associated with `key`, or
                `null` if there was no mapping for `key`

        Raises
        - NullPointerException: if the specified key is null
        """
        ...


    def clear(self) -> None:
        """
        Removes all of the mappings from this map.
        """
        ...


    def keySet(self) -> "KeySetView"["K", "V"]:
        """
        Returns a Set view of the keys contained in this map.
        The set is backed by the map, so changes to the map are
        reflected in the set, and vice-versa. The set supports element
        removal, which removes the corresponding mapping from this map,
        via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll`, and `clear`
        operations.  It does not support the `add` or
        `addAll` operations.
        
        The view's iterators and spliterators are
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        
        The view's `spliterator` reports Spliterator.CONCURRENT,
        Spliterator.DISTINCT, and Spliterator.NONNULL.

        Returns
        - the set view
        """
        ...


    def values(self) -> Iterable["V"]:
        """
        Returns a Collection view of the values contained in this map.
        The collection is backed by the map, so changes to the map are
        reflected in the collection, and vice-versa.  The collection
        supports element removal, which removes the corresponding
        mapping from this map, via the `Iterator.remove`,
        `Collection.remove`, `removeAll`,
        `retainAll`, and `clear` operations.  It does not
        support the `add` or `addAll` operations.
        
        The view's iterators and spliterators are
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        
        The view's `spliterator` reports Spliterator.CONCURRENT
        and Spliterator.NONNULL.

        Returns
        - the collection view
        """
        ...


    def entrySet(self) -> set["Map.Entry"["K", "V"]]:
        """
        Returns a Set view of the mappings contained in this map.
        The set is backed by the map, so changes to the map are
        reflected in the set, and vice-versa.  The set supports element
        removal, which removes the corresponding mapping from the map,
        via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll`, and `clear`
        operations.
        
        The view's iterators and spliterators are
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        
        The view's `spliterator` reports Spliterator.CONCURRENT,
        Spliterator.DISTINCT, and Spliterator.NONNULL.

        Returns
        - the set view
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this Map, i.e.,
        the sum of, for each key-value pair in the map,
        `key.hashCode() ^ value.hashCode()`.

        Returns
        - the hash code value for this map
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this map.  The string
        representation consists of a list of key-value mappings (in no
        particular order) enclosed in braces ("`{`}").  Adjacent
        mappings are separated by the characters `", "` (comma
        and space).  Each key-value mapping is rendered as the key
        followed by an equals sign ("`=`") followed by the
        associated value.

        Returns
        - a string representation of this map
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Compares the specified object with this map for equality.
        Returns `True` if the given object is a map with the same
        mappings as this map.  This operation may return misleading
        results if either map is concurrently modified during execution
        of this method.

        Arguments
        - o: object to be compared for equality with this map

        Returns
        - `True` if the specified object is equal to this map
        """
        ...


    def putIfAbsent(self, key: "K", value: "V") -> "V":
        """
        Returns
        - the previous value associated with the specified key,
                or `null` if there was no mapping for the key

        Raises
        - NullPointerException: if the specified key or value is null
        """
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        """
        Raises
        - NullPointerException: if the specified key is null
        """
        ...


    def replace(self, key: "K", oldValue: "V", newValue: "V") -> bool:
        """
        Raises
        - NullPointerException: if any of the arguments are null
        """
        ...


    def replace(self, key: "K", value: "V") -> "V":
        """
        Returns
        - the previous value associated with the specified key,
                or `null` if there was no mapping for the key

        Raises
        - NullPointerException: if the specified key or value is null
        """
        ...


    def getOrDefault(self, key: "Object", defaultValue: "V") -> "V":
        """
        Returns the value to which the specified key is mapped, or the
        given default value if this map contains no mapping for the
        key.

        Arguments
        - key: the key whose associated value is to be returned
        - defaultValue: the value to return if this map contains
        no mapping for the given key

        Returns
        - the mapping for the key, if present; else the default value

        Raises
        - NullPointerException: if the specified key is null
        """
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def replaceAll(self, function: "BiFunction"["K", "V", "V"]) -> None:
        ...


    def computeIfAbsent(self, key: "K", mappingFunction: "Function"["K", "V"]) -> "V":
        """
        If the specified key is not already associated with a value,
        attempts to compute its value using the given mapping function
        and enters it into this map unless `null`.  The entire
        method invocation is performed atomically.  The supplied
        function is invoked exactly once per invocation of this method
        if the key is absent, else not at all.  Some attempted update
        operations on this map by other threads may be blocked while
        computation is in progress, so the computation should be short
        and simple.
        
        The mapping function must not modify this map during computation.

        Arguments
        - key: key with which the specified value is to be associated
        - mappingFunction: the function to compute a value

        Returns
        - the current (existing or computed) value associated with
                the specified key, or null if the computed value is null

        Raises
        - NullPointerException: if the specified key or mappingFunction
                is null
        - IllegalStateException: if the computation detectably
                attempts a recursive update to this map that would
                otherwise never complete
        - RuntimeException: or Error if the mappingFunction does so,
                in which case the mapping is left unestablished
        """
        ...


    def computeIfPresent(self, key: "K", remappingFunction: "BiFunction"["K", "V", "V"]) -> "V":
        """
        If the value for the specified key is present, attempts to
        compute a new mapping given the key and its current mapped
        value.  The entire method invocation is performed atomically.
        The supplied function is invoked exactly once per invocation of
        this method if the key is present, else not at all.  Some
        attempted update operations on this map by other threads may be
        blocked while computation is in progress, so the computation
        should be short and simple.
        
        The remapping function must not modify this map during computation.

        Arguments
        - key: key with which a value may be associated
        - remappingFunction: the function to compute a value

        Returns
        - the new value associated with the specified key, or null if none

        Raises
        - NullPointerException: if the specified key or remappingFunction
                is null
        - IllegalStateException: if the computation detectably
                attempts a recursive update to this map that would
                otherwise never complete
        - RuntimeException: or Error if the remappingFunction does so,
                in which case the mapping is unchanged
        """
        ...


    def compute(self, key: "K", remappingFunction: "BiFunction"["K", "V", "V"]) -> "V":
        """
        Attempts to compute a mapping for the specified key and its
        current mapped value (or `null` if there is no current
        mapping). The entire method invocation is performed atomically.
        The supplied function is invoked exactly once per invocation of
        this method.  Some attempted update operations on this map by
        other threads may be blocked while computation is in progress,
        so the computation should be short and simple.
        
        The remapping function must not modify this map during computation.

        Arguments
        - key: key with which the specified value is to be associated
        - remappingFunction: the function to compute a value

        Returns
        - the new value associated with the specified key, or null if none

        Raises
        - NullPointerException: if the specified key or remappingFunction
                is null
        - IllegalStateException: if the computation detectably
                attempts a recursive update to this map that would
                otherwise never complete
        - RuntimeException: or Error if the remappingFunction does so,
                in which case the mapping is unchanged
        """
        ...


    def merge(self, key: "K", value: "V", remappingFunction: "BiFunction"["V", "V", "V"]) -> "V":
        """
        If the specified key is not already associated with a
        (non-null) value, associates it with the given value.
        Otherwise, replaces the value with the results of the given
        remapping function, or removes if `null`. The entire
        method invocation is performed atomically.  Some attempted
        update operations on this map by other threads may be blocked
        while computation is in progress, so the computation should be
        short and simple, and must not attempt to update any other
        mappings of this Map.

        Arguments
        - key: key with which the specified value is to be associated
        - value: the value to use if absent
        - remappingFunction: the function to recompute a value if present

        Returns
        - the new value associated with the specified key, or null if none

        Raises
        - NullPointerException: if the specified key or the
                remappingFunction is null
        - RuntimeException: or Error if the remappingFunction does so,
                in which case the mapping is unchanged
        """
        ...


    def contains(self, value: "Object") -> bool:
        """
        Tests if some key maps into the specified value in this table.
        
        Note that this method is identical in functionality to
        .containsValue(Object), and exists solely to ensure
        full compatibility with class java.util.Hashtable,
        which supported this method prior to introduction of the
        Java Collections Framework.

        Arguments
        - value: a value to search for

        Returns
        - `True` if and only if some key maps to the
                `value` argument in this table as
                determined by the `equals` method;
                `False` otherwise

        Raises
        - NullPointerException: if the specified value is null
        """
        ...


    def keys(self) -> "Enumeration"["K"]:
        """
        Returns an enumeration of the keys in this table.

        Returns
        - an enumeration of the keys in this table

        See
        - .keySet()
        """
        ...


    def elements(self) -> "Enumeration"["V"]:
        """
        Returns an enumeration of the values in this table.

        Returns
        - an enumeration of the values in this table

        See
        - .values()
        """
        ...


    def mappingCount(self) -> int:
        """
        Returns the number of mappings. This method should be used
        instead of .size because a ConcurrentHashMap may
        contain more mappings than can be represented as an int. The
        value returned is an estimate; the actual count may differ if
        there are concurrent insertions or removals.

        Returns
        - the number of mappings

        Since
        - 1.8
        """
        ...


    @staticmethod
    def newKeySet() -> "KeySetView"["K", "Boolean"]:
        """
        Creates a new Set backed by a ConcurrentHashMap
        from the given type to `Boolean.TRUE`.
        
        Type `<K>`: the element type of the returned set

        Returns
        - the new set

        Since
        - 1.8
        """
        ...


    @staticmethod
    def newKeySet(initialCapacity: int) -> "KeySetView"["K", "Boolean"]:
        """
        Creates a new Set backed by a ConcurrentHashMap
        from the given type to `Boolean.TRUE`.
        
        Type `<K>`: the element type of the returned set

        Arguments
        - initialCapacity: The implementation performs internal
        sizing to accommodate this many elements.

        Returns
        - the new set

        Raises
        - IllegalArgumentException: if the initial capacity of
        elements is negative

        Since
        - 1.8
        """
        ...


    def keySet(self, mappedValue: "V") -> "KeySetView"["K", "V"]:
        """
        Returns a Set view of the keys in this map, using the
        given common mapped value for any additions (i.e., Collection.add and Collection.addAll(Collection)).
        This is of course only appropriate if it is acceptable to use
        the same value for all additions from this view.

        Arguments
        - mappedValue: the mapped value to use for any additions

        Returns
        - the set view

        Raises
        - NullPointerException: if the mappedValue is null
        """
        ...


    def forEach(self, parallelismThreshold: int, action: "BiConsumer"["K", "V"]) -> None:
        """
        Performs the given action for each (key, value).

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - action: the action

        Since
        - 1.8
        """
        ...


    def forEach(self, parallelismThreshold: int, transformer: "BiFunction"["K", "V", "U"], action: "Consumer"["U"]) -> None:
        """
        Performs the given action for each non-null transformation
        of each (key, value).
        
        Type `<U>`: the return type of the transformer

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element, or null if there is no transformation (in
        which case the action is not applied)
        - action: the action

        Since
        - 1.8
        """
        ...


    def search(self, parallelismThreshold: int, searchFunction: "BiFunction"["K", "V", "U"]) -> "U":
        """
        Returns a non-null result from applying the given search
        function on each (key, value), or null if none.  Upon
        success, further element processing is suppressed and the
        results of any other parallel invocations of the search
        function are ignored.
        
        Type `<U>`: the return type of the search function

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - searchFunction: a function returning a non-null
        result on success, else null

        Returns
        - a non-null result from applying the given search
        function on each (key, value), or null if none

        Since
        - 1.8
        """
        ...


    def reduce(self, parallelismThreshold: int, transformer: "BiFunction"["K", "V", "U"], reducer: "BiFunction"["U", "U", "U"]) -> "U":
        """
        Returns the result of accumulating the given transformation
        of all (key, value) pairs using the given reducer to
        combine values, or null if none.
        
        Type `<U>`: the return type of the transformer

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element, or null if there is no transformation (in
        which case it is not combined)
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all (key, value) pairs

        Since
        - 1.8
        """
        ...


    def reduceToDouble(self, parallelismThreshold: int, transformer: "ToDoubleBiFunction"["K", "V"], basis: float, reducer: "DoubleBinaryOperator") -> float:
        """
        Returns the result of accumulating the given transformation
        of all (key, value) pairs using the given reducer to
        combine values, and the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all (key, value) pairs

        Since
        - 1.8
        """
        ...


    def reduceToLong(self, parallelismThreshold: int, transformer: "ToLongBiFunction"["K", "V"], basis: int, reducer: "LongBinaryOperator") -> int:
        """
        Returns the result of accumulating the given transformation
        of all (key, value) pairs using the given reducer to
        combine values, and the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all (key, value) pairs

        Since
        - 1.8
        """
        ...


    def reduceToInt(self, parallelismThreshold: int, transformer: "ToIntBiFunction"["K", "V"], basis: int, reducer: "IntBinaryOperator") -> int:
        """
        Returns the result of accumulating the given transformation
        of all (key, value) pairs using the given reducer to
        combine values, and the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all (key, value) pairs

        Since
        - 1.8
        """
        ...


    def forEachKey(self, parallelismThreshold: int, action: "Consumer"["K"]) -> None:
        """
        Performs the given action for each key.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - action: the action

        Since
        - 1.8
        """
        ...


    def forEachKey(self, parallelismThreshold: int, transformer: "Function"["K", "U"], action: "Consumer"["U"]) -> None:
        """
        Performs the given action for each non-null transformation
        of each key.
        
        Type `<U>`: the return type of the transformer

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element, or null if there is no transformation (in
        which case the action is not applied)
        - action: the action

        Since
        - 1.8
        """
        ...


    def searchKeys(self, parallelismThreshold: int, searchFunction: "Function"["K", "U"]) -> "U":
        """
        Returns a non-null result from applying the given search
        function on each key, or null if none. Upon success,
        further element processing is suppressed and the results of
        any other parallel invocations of the search function are
        ignored.
        
        Type `<U>`: the return type of the search function

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - searchFunction: a function returning a non-null
        result on success, else null

        Returns
        - a non-null result from applying the given search
        function on each key, or null if none

        Since
        - 1.8
        """
        ...


    def reduceKeys(self, parallelismThreshold: int, reducer: "BiFunction"["K", "K", "K"]) -> "K":
        """
        Returns the result of accumulating all keys using the given
        reducer to combine values, or null if none.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating all keys using the given
        reducer to combine values, or null if none

        Since
        - 1.8
        """
        ...


    def reduceKeys(self, parallelismThreshold: int, transformer: "Function"["K", "U"], reducer: "BiFunction"["U", "U", "U"]) -> "U":
        """
        Returns the result of accumulating the given transformation
        of all keys using the given reducer to combine values, or
        null if none.
        
        Type `<U>`: the return type of the transformer

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element, or null if there is no transformation (in
        which case it is not combined)
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all keys

        Since
        - 1.8
        """
        ...


    def reduceKeysToDouble(self, parallelismThreshold: int, transformer: "ToDoubleFunction"["K"], basis: float, reducer: "DoubleBinaryOperator") -> float:
        """
        Returns the result of accumulating the given transformation
        of all keys using the given reducer to combine values, and
        the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all keys

        Since
        - 1.8
        """
        ...


    def reduceKeysToLong(self, parallelismThreshold: int, transformer: "ToLongFunction"["K"], basis: int, reducer: "LongBinaryOperator") -> int:
        """
        Returns the result of accumulating the given transformation
        of all keys using the given reducer to combine values, and
        the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all keys

        Since
        - 1.8
        """
        ...


    def reduceKeysToInt(self, parallelismThreshold: int, transformer: "ToIntFunction"["K"], basis: int, reducer: "IntBinaryOperator") -> int:
        """
        Returns the result of accumulating the given transformation
        of all keys using the given reducer to combine values, and
        the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all keys

        Since
        - 1.8
        """
        ...


    def forEachValue(self, parallelismThreshold: int, action: "Consumer"["V"]) -> None:
        """
        Performs the given action for each value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - action: the action

        Since
        - 1.8
        """
        ...


    def forEachValue(self, parallelismThreshold: int, transformer: "Function"["V", "U"], action: "Consumer"["U"]) -> None:
        """
        Performs the given action for each non-null transformation
        of each value.
        
        Type `<U>`: the return type of the transformer

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element, or null if there is no transformation (in
        which case the action is not applied)
        - action: the action

        Since
        - 1.8
        """
        ...


    def searchValues(self, parallelismThreshold: int, searchFunction: "Function"["V", "U"]) -> "U":
        """
        Returns a non-null result from applying the given search
        function on each value, or null if none.  Upon success,
        further element processing is suppressed and the results of
        any other parallel invocations of the search function are
        ignored.
        
        Type `<U>`: the return type of the search function

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - searchFunction: a function returning a non-null
        result on success, else null

        Returns
        - a non-null result from applying the given search
        function on each value, or null if none

        Since
        - 1.8
        """
        ...


    def reduceValues(self, parallelismThreshold: int, reducer: "BiFunction"["V", "V", "V"]) -> "V":
        """
        Returns the result of accumulating all values using the
        given reducer to combine values, or null if none.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating all values

        Since
        - 1.8
        """
        ...


    def reduceValues(self, parallelismThreshold: int, transformer: "Function"["V", "U"], reducer: "BiFunction"["U", "U", "U"]) -> "U":
        """
        Returns the result of accumulating the given transformation
        of all values using the given reducer to combine values, or
        null if none.
        
        Type `<U>`: the return type of the transformer

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element, or null if there is no transformation (in
        which case it is not combined)
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all values

        Since
        - 1.8
        """
        ...


    def reduceValuesToDouble(self, parallelismThreshold: int, transformer: "ToDoubleFunction"["V"], basis: float, reducer: "DoubleBinaryOperator") -> float:
        """
        Returns the result of accumulating the given transformation
        of all values using the given reducer to combine values,
        and the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all values

        Since
        - 1.8
        """
        ...


    def reduceValuesToLong(self, parallelismThreshold: int, transformer: "ToLongFunction"["V"], basis: int, reducer: "LongBinaryOperator") -> int:
        """
        Returns the result of accumulating the given transformation
        of all values using the given reducer to combine values,
        and the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all values

        Since
        - 1.8
        """
        ...


    def reduceValuesToInt(self, parallelismThreshold: int, transformer: "ToIntFunction"["V"], basis: int, reducer: "IntBinaryOperator") -> int:
        """
        Returns the result of accumulating the given transformation
        of all values using the given reducer to combine values,
        and the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all values

        Since
        - 1.8
        """
        ...


    def forEachEntry(self, parallelismThreshold: int, action: "Consumer"["Map.Entry"["K", "V"]]) -> None:
        """
        Performs the given action for each entry.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - action: the action

        Since
        - 1.8
        """
        ...


    def forEachEntry(self, parallelismThreshold: int, transformer: "Function"["Map.Entry"["K", "V"], "U"], action: "Consumer"["U"]) -> None:
        """
        Performs the given action for each non-null transformation
        of each entry.
        
        Type `<U>`: the return type of the transformer

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element, or null if there is no transformation (in
        which case the action is not applied)
        - action: the action

        Since
        - 1.8
        """
        ...


    def searchEntries(self, parallelismThreshold: int, searchFunction: "Function"["Map.Entry"["K", "V"], "U"]) -> "U":
        """
        Returns a non-null result from applying the given search
        function on each entry, or null if none.  Upon success,
        further element processing is suppressed and the results of
        any other parallel invocations of the search function are
        ignored.
        
        Type `<U>`: the return type of the search function

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - searchFunction: a function returning a non-null
        result on success, else null

        Returns
        - a non-null result from applying the given search
        function on each entry, or null if none

        Since
        - 1.8
        """
        ...


    def reduceEntries(self, parallelismThreshold: int, reducer: "BiFunction"["Map.Entry"["K", "V"], "Map.Entry"["K", "V"], "Map.Entry"["K", "V"]]) -> "Map.Entry"["K", "V"]:
        """
        Returns the result of accumulating all entries using the
        given reducer to combine values, or null if none.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating all entries

        Since
        - 1.8
        """
        ...


    def reduceEntries(self, parallelismThreshold: int, transformer: "Function"["Map.Entry"["K", "V"], "U"], reducer: "BiFunction"["U", "U", "U"]) -> "U":
        """
        Returns the result of accumulating the given transformation
        of all entries using the given reducer to combine values,
        or null if none.
        
        Type `<U>`: the return type of the transformer

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element, or null if there is no transformation (in
        which case it is not combined)
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all entries

        Since
        - 1.8
        """
        ...


    def reduceEntriesToDouble(self, parallelismThreshold: int, transformer: "ToDoubleFunction"["Map.Entry"["K", "V"]], basis: float, reducer: "DoubleBinaryOperator") -> float:
        """
        Returns the result of accumulating the given transformation
        of all entries using the given reducer to combine values,
        and the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all entries

        Since
        - 1.8
        """
        ...


    def reduceEntriesToLong(self, parallelismThreshold: int, transformer: "ToLongFunction"["Map.Entry"["K", "V"]], basis: int, reducer: "LongBinaryOperator") -> int:
        """
        Returns the result of accumulating the given transformation
        of all entries using the given reducer to combine values,
        and the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all entries

        Since
        - 1.8
        """
        ...


    def reduceEntriesToInt(self, parallelismThreshold: int, transformer: "ToIntFunction"["Map.Entry"["K", "V"]], basis: int, reducer: "IntBinaryOperator") -> int:
        """
        Returns the result of accumulating the given transformation
        of all entries using the given reducer to combine values,
        and the given basis as an identity value.

        Arguments
        - parallelismThreshold: the (estimated) number of elements
        needed for this operation to be executed in parallel
        - transformer: a function returning the transformation
        for an element
        - basis: the identity (initial default value) for the reduction
        - reducer: a commutative associative combining function

        Returns
        - the result of accumulating the given transformation
        of all entries

        Since
        - 1.8
        """
        ...


    class KeySetView(CollectionView, Set, Serializable):
        """
        A view of a ConcurrentHashMap as a Set of keys, in
        which additions may optionally be enabled by mapping to a
        common value.  This class cannot be directly instantiated.
        See .keySet() keySet(),
        .keySet(Object) keySet(V),
        .newKeySet() newKeySet(),
        .newKeySet(int) newKeySet(int).

        Since
        - 1.8
        """

        def getMappedValue(self) -> "V":
            """
            Returns the default mapped value for additions,
            or `null` if additions are not supported.

            Returns
            - the default mapped value for additions, or `null`
            if not supported
            """
            ...


        def contains(self, o: "Object") -> bool:
            """
            Raises
            - NullPointerException: if the specified key is null
            """
            ...


        def remove(self, o: "Object") -> bool:
            """
            Removes the key from this map view, by removing the key (and its
            corresponding value) from the backing map.  This method does
            nothing if the key is not in the map.

            Arguments
            - o: the key to be removed from the backing map

            Returns
            - `True` if the backing map contained the specified key

            Raises
            - NullPointerException: if the specified key is null
            """
            ...


        def iterator(self) -> Iterator["K"]:
            """
            Returns
            - an iterator over the keys of the backing map
            """
            ...


        def add(self, e: "K") -> bool:
            """
            Adds the specified key to this set view by mapping the key to
            the default mapped value in the backing map, if defined.

            Arguments
            - e: key to be added

            Returns
            - `True` if this set changed as a result of the call

            Raises
            - NullPointerException: if the specified key is null
            - UnsupportedOperationException: if no default mapped value
            for additions was provided
            """
            ...


        def addAll(self, c: Iterable["K"]) -> bool:
            """
            Adds all of the elements in the specified collection to this set,
            as if by calling .add on each one.

            Arguments
            - c: the elements to be inserted into this set

            Returns
            - `True` if this set changed as a result of the call

            Raises
            - NullPointerException: if the collection or any of its
            elements are `null`
            - UnsupportedOperationException: if no default mapped value
            for additions was provided
            """
            ...


        def hashCode(self) -> int:
            ...


        def equals(self, o: "Object") -> bool:
            ...


        def spliterator(self) -> "Spliterator"["K"]:
            ...


        def forEach(self, action: "Consumer"["K"]) -> None:
            ...
