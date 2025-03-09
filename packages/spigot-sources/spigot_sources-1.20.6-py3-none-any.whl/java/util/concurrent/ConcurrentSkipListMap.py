"""
Python module generated from Java source file java.util.concurrent.ConcurrentSkipListMap

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import Serializable
from java.lang.invoke import MethodHandles
from java.lang.invoke import VarHandle
from java.util import AbstractCollection
from java.util import AbstractSet
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util import NavigableSet
from java.util import NoSuchElementException
from java.util import SortedMap
from java.util import Spliterator
from java.util.concurrent import *
from java.util.concurrent.atomic import LongAdder
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import Consumer
from java.util.function import Function
from java.util.function import Predicate
from typing import Any, Callable, Iterable, Tuple


class ConcurrentSkipListMap(AbstractMap, ConcurrentNavigableMap, Cloneable, Serializable):
    """
    A scalable concurrent ConcurrentNavigableMap implementation.
    The map is sorted according to the Comparable natural
    ordering of its keys, or by a Comparator provided at map
    creation time, depending on which constructor is used.
    
    This class implements a concurrent variant of <a
    href="http://en.wikipedia.org/wiki/Skip_list" target="_top">SkipLists</a>
    providing expected average *log(n)* time cost for the
    `containsKey`, `get`, `put` and
    `remove` operations and their variants.  Insertion, removal,
    update, and access operations safely execute concurrently by
    multiple threads.
    
    Iterators and spliterators are
    <a href="package-summary.html#Weakly">*weakly consistent*</a>.
    
    Ascending key ordered views and their iterators are faster than
    descending ones.
    
    All `Map.Entry` pairs returned by methods in this class
    and its views represent snapshots of mappings at the time they were
    produced. They do *not* support the `Entry.setValue`
    method. (Note however that it is possible to change mappings in the
    associated map using `put`, `putIfAbsent`, or
    `replace`, depending on exactly which effect you need.)
    
    Beware that bulk operations `putAll`, `equals`,
    `toArray`, `containsValue`, and `clear` are
    *not* guaranteed to be performed atomically. For example, an
    iterator operating concurrently with a `putAll` operation
    might view only some of the added elements.
    
    This class and its views and iterators implement all of the
    *optional* methods of the Map and Iterator
    interfaces. Like most other concurrent collections, this class does
    *not* permit the use of `null` keys or values because some
    null return values cannot be reliably distinguished from the absence of
    elements.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<K>`: the type of keys maintained by this map
    
    Type `<V>`: the type of mapped values

    Author(s)
    - Doug Lea

    Since
    - 1.6
    """

    def __init__(self):
        """
        Constructs a new, empty map, sorted according to the
        Comparable natural ordering of the keys.
        """
        ...


    def __init__(self, comparator: "Comparator"["K"]):
        """
        Constructs a new, empty map, sorted according to the specified
        comparator.

        Arguments
        - comparator: the comparator that will be used to order this map.
               If `null`, the Comparable natural
               ordering of the keys will be used.
        """
        ...


    def __init__(self, m: dict["K", "V"]):
        """
        Constructs a new map containing the same mappings as the given map,
        sorted according to the Comparable natural ordering of
        the keys.

        Arguments
        - m: the map whose mappings are to be placed in this map

        Raises
        - ClassCastException: if the keys in `m` are not
                Comparable, or are not mutually comparable
        - NullPointerException: if the specified map or any of its keys
                or values are null
        """
        ...


    def __init__(self, m: "SortedMap"["K", "V"]):
        """
        Constructs a new map containing the same mappings and using the
        same ordering as the specified sorted map.

        Arguments
        - m: the sorted map whose mappings are to be placed in this
               map, and whose comparator is to be used to sort this map

        Raises
        - NullPointerException: if the specified sorted map or any of
                its keys or values are null
        """
        ...


    def clone(self) -> "ConcurrentSkipListMap"["K", "V"]:
        """
        Returns a shallow copy of this `ConcurrentSkipListMap`
        instance. (The keys and values themselves are not cloned.)

        Returns
        - a shallow copy of this map
        """
        ...


    def containsKey(self, key: "Object") -> bool:
        """
        Returns `True` if this map contains a mapping for the specified
        key.

        Arguments
        - key: key whose presence in this map is to be tested

        Returns
        - `True` if this map contains a mapping for the specified key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
        """
        ...


    def get(self, key: "Object") -> "V":
        """
        Returns the value to which the specified key is mapped,
        or `null` if this map contains no mapping for the key.
        
        More formally, if this map contains a mapping from a key
        `k` to a value `v` such that `key` compares
        equal to `k` according to the map's ordering, then this
        method returns `v`; otherwise it returns `null`.
        (There can be at most one such mapping.)

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
        """
        ...


    def getOrDefault(self, key: "Object", defaultValue: "V") -> "V":
        """
        Returns the value to which the specified key is mapped,
        or the given defaultValue if this map contains no mapping for the key.

        Arguments
        - key: the key
        - defaultValue: the value to return if this map contains
        no mapping for the given key

        Returns
        - the mapping for the key, if present; else the defaultValue

        Raises
        - NullPointerException: if the specified key is null

        Since
        - 1.8
        """
        ...


    def put(self, key: "K", value: "V") -> "V":
        """
        Associates the specified value with the specified key in this map.
        If the map previously contained a mapping for the key, the old
        value is replaced.

        Arguments
        - key: key with which the specified value is to be associated
        - value: value to be associated with the specified key

        Returns
        - the previous value associated with the specified key, or
                `null` if there was no mapping for the key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key or value is null
        """
        ...


    def remove(self, key: "Object") -> "V":
        """
        Removes the mapping for the specified key from this map if present.

        Arguments
        - key: key for which mapping should be removed

        Returns
        - the previous value associated with the specified key, or
                `null` if there was no mapping for the key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
        """
        ...


    def containsValue(self, value: "Object") -> bool:
        """
        Returns `True` if this map maps one or more keys to the
        specified value.  This operation requires time linear in the
        map size. Additionally, it is possible for the map to change
        during execution of this method, in which case the returned
        result may be inaccurate.

        Arguments
        - value: value whose presence in this map is to be tested

        Returns
        - `True` if a mapping to `value` exists;
                `False` otherwise

        Raises
        - NullPointerException: if the specified value is null
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


    def clear(self) -> None:
        """
        Removes all of the mappings from this map.
        """
        ...


    def computeIfAbsent(self, key: "K", mappingFunction: "Function"["K", "V"]) -> "V":
        """
        If the specified key is not already associated with a value,
        attempts to compute its value using the given mapping function
        and enters it into this map unless `null`.  The function
        is *NOT* guaranteed to be applied once atomically only
        if the value is not present.

        Arguments
        - key: key with which the specified value is to be associated
        - mappingFunction: the function to compute a value

        Returns
        - the current (existing or computed) value associated with
                the specified key, or null if the computed value is null

        Raises
        - NullPointerException: if the specified key is null
                or the mappingFunction is null

        Since
        - 1.8
        """
        ...


    def computeIfPresent(self, key: "K", remappingFunction: "BiFunction"["K", "V", "V"]) -> "V":
        """
        If the value for the specified key is present, attempts to
        compute a new mapping given the key and its current mapped
        value. The function is *NOT* guaranteed to be applied
        once atomically.

        Arguments
        - key: key with which a value may be associated
        - remappingFunction: the function to compute a value

        Returns
        - the new value associated with the specified key, or null if none

        Raises
        - NullPointerException: if the specified key is null
                or the remappingFunction is null

        Since
        - 1.8
        """
        ...


    def compute(self, key: "K", remappingFunction: "BiFunction"["K", "V", "V"]) -> "V":
        """
        Attempts to compute a mapping for the specified key and its
        current mapped value (or `null` if there is no current
        mapping). The function is *NOT* guaranteed to be applied
        once atomically.

        Arguments
        - key: key with which the specified value is to be associated
        - remappingFunction: the function to compute a value

        Returns
        - the new value associated with the specified key, or null if none

        Raises
        - NullPointerException: if the specified key is null
                or the remappingFunction is null

        Since
        - 1.8
        """
        ...


    def merge(self, key: "K", value: "V", remappingFunction: "BiFunction"["V", "V", "V"]) -> "V":
        """
        If the specified key is not already associated with a value,
        associates it with the given value.  Otherwise, replaces the
        value with the results of the given remapping function, or
        removes if `null`. The function is *NOT*
        guaranteed to be applied once atomically.

        Arguments
        - key: key with which the specified value is to be associated
        - value: the value to use if absent
        - remappingFunction: the function to recompute a value if present

        Returns
        - the new value associated with the specified key, or null if none

        Raises
        - NullPointerException: if the specified key or value is null
                or the remappingFunction is null

        Since
        - 1.8
        """
        ...


    def keySet(self) -> "NavigableSet"["K"]:
        """
        Returns a NavigableSet view of the keys contained in this map.
        
        The set's iterator returns the keys in ascending order.
        The set's spliterator additionally reports Spliterator.CONCURRENT,
        Spliterator.NONNULL, Spliterator.SORTED and
        Spliterator.ORDERED, with an encounter order that is ascending
        key order.
        
        The Spliterator.getComparator() spliterator's comparator
        is `null` if the .comparator() map's comparator
        is `null`.
        Otherwise, the spliterator's comparator is the same as or imposes the
        same total ordering as the map's comparator.
        
        The set is backed by the map, so changes to the map are
        reflected in the set, and vice-versa.  The set supports element
        removal, which removes the corresponding mapping from the map,
        via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll`, and `clear`
        operations.  It does not support the `add` or `addAll`
        operations.
        
        The view's iterators and spliterators are
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        
        This method is equivalent to method `navigableKeySet`.

        Returns
        - a navigable set view of the keys in this map
        """
        ...


    def navigableKeySet(self) -> "NavigableSet"["K"]:
        ...


    def values(self) -> Iterable["V"]:
        """
        Returns a Collection view of the values contained in this map.
        The collection's iterator returns the values in ascending order
        of the corresponding keys. The collections's spliterator additionally
        reports Spliterator.CONCURRENT, Spliterator.NONNULL and
        Spliterator.ORDERED, with an encounter order that is ascending
        order of the corresponding keys.
        
        The collection is backed by the map, so changes to the map are
        reflected in the collection, and vice-versa.  The collection
        supports element removal, which removes the corresponding
        mapping from the map, via the `Iterator.remove`,
        `Collection.remove`, `removeAll`,
        `retainAll` and `clear` operations.  It does not
        support the `add` or `addAll` operations.
        
        The view's iterators and spliterators are
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        """
        ...


    def entrySet(self) -> set["Map.Entry"["K", "V"]]:
        """
        Returns a Set view of the mappings contained in this map.
        
        The set's iterator returns the entries in ascending key order.  The
        set's spliterator additionally reports Spliterator.CONCURRENT,
        Spliterator.NONNULL, Spliterator.SORTED and
        Spliterator.ORDERED, with an encounter order that is ascending
        key order.
        
        The set is backed by the map, so changes to the map are
        reflected in the set, and vice-versa.  The set supports element
        removal, which removes the corresponding mapping from the map,
        via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll` and `clear`
        operations.  It does not support the `add` or
        `addAll` operations.
        
        The view's iterators and spliterators are
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        
        The `Map.Entry` elements traversed by the `iterator`
        or `spliterator` do *not* support the `setValue`
        operation.

        Returns
        - a set view of the mappings contained in this map,
                sorted in ascending key order
        """
        ...


    def descendingMap(self) -> "ConcurrentNavigableMap"["K", "V"]:
        ...


    def descendingKeySet(self) -> "NavigableSet"["K"]:
        ...


    def equals(self, o: "Object") -> bool:
        """
        Compares the specified object with this map for equality.
        Returns `True` if the given object is also a map and the
        two maps represent the same mappings.  More formally, two maps
        `m1` and `m2` represent the same mappings if
        `m1.entrySet().equals(m2.entrySet())`.  This
        operation may return misleading results if either map is
        concurrently modified during execution of this method.

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
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key or value is null
        """
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        """
        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key is null
        """
        ...


    def replace(self, key: "K", oldValue: "V", newValue: "V") -> bool:
        """
        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if any of the arguments are null
        """
        ...


    def replace(self, key: "K", value: "V") -> "V":
        """
        Returns
        - the previous value associated with the specified key,
                or `null` if there was no mapping for the key

        Raises
        - ClassCastException: if the specified key cannot be compared
                with the keys currently in the map
        - NullPointerException: if the specified key or value is null
        """
        ...


    def comparator(self) -> "Comparator"["K"]:
        ...


    def firstKey(self) -> "K":
        """
        Raises
        - NoSuchElementException: 
        """
        ...


    def lastKey(self) -> "K":
        """
        Raises
        - NoSuchElementException: 
        """
        ...


    def subMap(self, fromKey: "K", fromInclusive: bool, toKey: "K", toInclusive: bool) -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: if `fromKey` or `toKey` is null
        - IllegalArgumentException: 
        """
        ...


    def headMap(self, toKey: "K", inclusive: bool) -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: if `toKey` is null
        - IllegalArgumentException: 
        """
        ...


    def tailMap(self, fromKey: "K", inclusive: bool) -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: if `fromKey` is null
        - IllegalArgumentException: 
        """
        ...


    def subMap(self, fromKey: "K", toKey: "K") -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: if `fromKey` or `toKey` is null
        - IllegalArgumentException: 
        """
        ...


    def headMap(self, toKey: "K") -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: if `toKey` is null
        - IllegalArgumentException: 
        """
        ...


    def tailMap(self, fromKey: "K") -> "ConcurrentNavigableMap"["K", "V"]:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: if `fromKey` is null
        - IllegalArgumentException: 
        """
        ...


    def lowerEntry(self, key: "K") -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the greatest key
        strictly less than the given key, or `null` if there is
        no such key. The returned entry does *not* support the
        `Entry.setValue` method.

        Raises
        - ClassCastException: 
        - NullPointerException: if the specified key is null
        """
        ...


    def lowerKey(self, key: "K") -> "K":
        """
        Raises
        - ClassCastException: 
        - NullPointerException: if the specified key is null
        """
        ...


    def floorEntry(self, key: "K") -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the greatest key
        less than or equal to the given key, or `null` if there
        is no such key. The returned entry does *not* support
        the `Entry.setValue` method.

        Arguments
        - key: the key

        Raises
        - ClassCastException: 
        - NullPointerException: if the specified key is null
        """
        ...


    def floorKey(self, key: "K") -> "K":
        """
        Arguments
        - key: the key

        Raises
        - ClassCastException: 
        - NullPointerException: if the specified key is null
        """
        ...


    def ceilingEntry(self, key: "K") -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the least key
        greater than or equal to the given key, or `null` if
        there is no such entry. The returned entry does *not*
        support the `Entry.setValue` method.

        Raises
        - ClassCastException: 
        - NullPointerException: if the specified key is null
        """
        ...


    def ceilingKey(self, key: "K") -> "K":
        """
        Raises
        - ClassCastException: 
        - NullPointerException: if the specified key is null
        """
        ...


    def higherEntry(self, key: "K") -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the least key
        strictly greater than the given key, or `null` if there
        is no such key. The returned entry does *not* support
        the `Entry.setValue` method.

        Arguments
        - key: the key

        Raises
        - ClassCastException: 
        - NullPointerException: if the specified key is null
        """
        ...


    def higherKey(self, key: "K") -> "K":
        """
        Arguments
        - key: the key

        Raises
        - ClassCastException: 
        - NullPointerException: if the specified key is null
        """
        ...


    def firstEntry(self) -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the least
        key in this map, or `null` if the map is empty.
        The returned entry does *not* support
        the `Entry.setValue` method.
        """
        ...


    def lastEntry(self) -> "Map.Entry"["K", "V"]:
        """
        Returns a key-value mapping associated with the greatest
        key in this map, or `null` if the map is empty.
        The returned entry does *not* support
        the `Entry.setValue` method.
        """
        ...


    def pollFirstEntry(self) -> "Map.Entry"["K", "V"]:
        """
        Removes and returns a key-value mapping associated with
        the least key in this map, or `null` if the map is empty.
        The returned entry does *not* support
        the `Entry.setValue` method.
        """
        ...


    def pollLastEntry(self) -> "Map.Entry"["K", "V"]:
        """
        Removes and returns a key-value mapping associated with
        the greatest key in this map, or `null` if the map is empty.
        The returned entry does *not* support
        the `Entry.setValue` method.
        """
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def replaceAll(self, function: "BiFunction"["K", "V", "V"]) -> None:
        ...
