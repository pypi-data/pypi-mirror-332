"""
Python module generated from Java source file com.google.common.collect.ImmutableSortedMap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import WeakOuter
from java.util import Arrays
from java.util import Comparator
from java.util import NavigableMap
from java.util import SortedMap
from java.util import Spliterator
from java.util.function import BiConsumer
from java.util.function import BinaryOperator
from java.util.function import Consumer
from java.util.function import Function
from java.util.stream import Collector
from java.util.stream import Collectors
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableSortedMap(ImmutableSortedMapFauxverideShim, NavigableMap):
    """
    A NavigableMap whose contents will never change, with many other important properties
    detailed at ImmutableCollection.
    
    **Warning:** as with any sorted collection, you are strongly advised not to use a Comparator or Comparable type whose comparison behavior is *inconsistent with
    equals*. That is, `a.compareTo(b)` or `comparator.compare(a, b)` should equal zero
    *if and only if* `a.equals(b)`. If this advice is not followed, the resulting map will
    not correctly obey its specification.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/ImmutableCollectionsExplained">
    immutable collections</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0 (implements `NavigableMap` since 12.0)
    """

    @staticmethod
    def toImmutableSortedMap(comparator: "Comparator"["K"], keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"]) -> "Collector"["T", Any, "ImmutableSortedMap"["K", "V"]]:
        """
        Returns a Collector that accumulates elements into an `ImmutableSortedMap`
        whose keys and values are the result of applying the provided mapping functions to the input
        elements.  The generated map is sorted by the specified comparator.
        
        If the mapped keys contain duplicates (according to the specified comparator), an
        `IllegalArgumentException` is thrown when the collection operation is performed.
        (This differs from the `Collector` returned by
        Collectors.toMap(Function, Function), which throws an `IllegalStateException`.)

        Since
        - 21.0
        """
        ...


    @staticmethod
    def toImmutableSortedMap(comparator: "Comparator"["K"], keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"], mergeFunction: "BinaryOperator"["V"]) -> "Collector"["T", Any, "ImmutableSortedMap"["K", "V"]]:
        """
        Returns a Collector that accumulates elements into an `ImmutableSortedMap` whose
        keys and values are the result of applying the provided mapping functions to the input
        elements.
        
        If the mapped keys contain duplicates (according to the comparator), the the values are
        merged using the specified merging function. Entries will appear in the encounter order of the
        first occurrence of the key.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns the empty sorted map.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable map containing a single entry.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable sorted map containing the given entries, sorted by the
        natural ordering of their keys.

        Raises
        - IllegalArgumentException: if the two keys are equal according to
            their natural ordering
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable sorted map containing the given entries, sorted by the
        natural ordering of their keys.

        Raises
        - IllegalArgumentException: if any two keys are equal according to
            their natural ordering
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable sorted map containing the given entries, sorted by the
        natural ordering of their keys.

        Raises
        - IllegalArgumentException: if any two keys are equal according to
            their natural ordering
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable sorted map containing the given entries, sorted by the
        natural ordering of their keys.

        Raises
        - IllegalArgumentException: if any two keys are equal according to
            their natural ordering
        """
        ...


    @staticmethod
    def copyOf(map: dict["K", "V"]) -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable map containing the same entries as `map`, sorted
        by the natural ordering of the keys.
        
        Despite the method name, this method attempts to avoid actually copying
        the data when it is safe to do so. The exact circumstances under which a
        copy will or will not be performed are undocumented and subject to change.
        
        This method is not type-safe, as it may be called on a map with keys
        that are not mutually comparable.

        Raises
        - ClassCastException: if the keys in `map` are not mutually
                comparable
        - NullPointerException: if any key or value in `map` is null
        - IllegalArgumentException: if any two keys are equal according to
                their natural ordering
        """
        ...


    @staticmethod
    def copyOf(map: dict["K", "V"], comparator: "Comparator"["K"]) -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable map containing the same entries as `map`, with
        keys sorted by the provided comparator.
        
        Despite the method name, this method attempts to avoid actually copying
        the data when it is safe to do so. The exact circumstances under which a
        copy will or will not be performed are undocumented and subject to change.

        Raises
        - NullPointerException: if any key or value in `map` is null
        - IllegalArgumentException: if any two keys are equal according to the
                comparator
        """
        ...


    @staticmethod
    def copyOf(entries: Iterable["Entry"["K", "V"]]) -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, with keys sorted
        by the provided comparator.
        
        This method is not type-safe, as it may be called on a map with keys
        that are not mutually comparable.

        Raises
        - NullPointerException: if any key or value in `map` is null
        - IllegalArgumentException: if any two keys are equal according to the
                comparator

        Since
        - 19.0
        """
        ...


    @staticmethod
    def copyOf(entries: Iterable["Entry"["K", "V"]], comparator: "Comparator"["K"]) -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, with keys sorted
        by the provided comparator.

        Raises
        - NullPointerException: if any key or value in `map` is null
        - IllegalArgumentException: if any two keys are equal according to the
                comparator

        Since
        - 19.0
        """
        ...


    @staticmethod
    def copyOfSorted(map: "SortedMap"["K", "V"]) -> "ImmutableSortedMap"["K", "V"]:
        """
        Returns an immutable map containing the same entries as the provided sorted
        map, with the same ordering.
        
        Despite the method name, this method attempts to avoid actually copying
        the data when it is safe to do so. The exact circumstances under which a
        copy will or will not be performed are undocumented and subject to change.

        Raises
        - NullPointerException: if any key or value in `map` is null
        """
        ...


    @staticmethod
    def naturalOrder() -> "Builder"["K", "V"]:
        """
        Returns a builder that creates immutable sorted maps whose keys are
        ordered by their natural ordering. The sorted maps use Ordering.natural() as the comparator.
        """
        ...


    @staticmethod
    def orderedBy(comparator: "Comparator"["K"]) -> "Builder"["K", "V"]:
        """
        Returns a builder that creates immutable sorted maps with an explicit
        comparator. If the comparator has a more general type than the map's keys,
        such as creating a `SortedMap<Integer, String>` with a `Comparator<Number>`, use the Builder constructor instead.

        Raises
        - NullPointerException: if `comparator` is null
        """
        ...


    @staticmethod
    def reverseOrder() -> "Builder"["K", "V"]:
        """
        Returns a builder that creates immutable sorted maps whose keys are
        ordered by the reverse of their natural ordering.
        """
        ...


    def size(self) -> int:
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def get(self, key: "Object") -> "V":
        ...


    def entrySet(self) -> "ImmutableSet"["Entry"["K", "V"]]:
        """
        Returns an immutable set of the mappings in this map, sorted by the key
        ordering.
        """
        ...


    def keySet(self) -> "ImmutableSortedSet"["K"]:
        """
        Returns an immutable sorted set of the keys in this map.
        """
        ...


    def values(self) -> "ImmutableCollection"["V"]:
        """
        Returns an immutable collection of the values in this map, sorted by the
        ordering of the corresponding keys.
        """
        ...


    def comparator(self) -> "Comparator"["K"]:
        """
        Returns the comparator that orders the keys, which is
        Ordering.natural() when the natural ordering of the keys is used.
        Note that its behavior is not consistent with TreeMap.comparator(),
        which returns `null` to indicate natural ordering.
        """
        ...


    def firstKey(self) -> "K":
        ...


    def lastKey(self) -> "K":
        ...


    def headMap(self, toKey: "K") -> "ImmutableSortedMap"["K", "V"]:
        """
        This method returns a `ImmutableSortedMap`, consisting of the entries
        whose keys are less than `toKey`.
        
        The SortedMap.headMap documentation states that a submap of a
        submap throws an IllegalArgumentException if passed a `toKey`
        greater than an earlier `toKey`. However, this method doesn't throw
        an exception in that situation, but instead keeps the original `toKey`.
        """
        ...


    def headMap(self, toKey: "K", inclusive: bool) -> "ImmutableSortedMap"["K", "V"]:
        """
        This method returns a `ImmutableSortedMap`, consisting of the entries
        whose keys are less than (or equal to, if `inclusive`) `toKey`.
        
        The SortedMap.headMap documentation states that a submap of a
        submap throws an IllegalArgumentException if passed a `toKey`
        greater than an earlier `toKey`. However, this method doesn't throw
        an exception in that situation, but instead keeps the original `toKey`.

        Since
        - 12.0
        """
        ...


    def subMap(self, fromKey: "K", toKey: "K") -> "ImmutableSortedMap"["K", "V"]:
        """
        This method returns a `ImmutableSortedMap`, consisting of the entries
        whose keys ranges from `fromKey`, inclusive, to `toKey`,
        exclusive.
        
        The SortedMap.subMap documentation states that a submap of a
        submap throws an IllegalArgumentException if passed a `fromKey` less than an earlier `fromKey`. However, this method doesn't
        throw an exception in that situation, but instead keeps the original `fromKey`. Similarly, this method keeps the original `toKey`, instead
        of throwing an exception, if passed a `toKey` greater than an earlier
        `toKey`.
        """
        ...


    def subMap(self, fromKey: "K", fromInclusive: bool, toKey: "K", toInclusive: bool) -> "ImmutableSortedMap"["K", "V"]:
        """
        This method returns a `ImmutableSortedMap`, consisting of the entries
        whose keys ranges from `fromKey` to `toKey`, inclusive or
        exclusive as indicated by the boolean flags.
        
        The SortedMap.subMap documentation states that a submap of a
        submap throws an IllegalArgumentException if passed a `fromKey` less than an earlier `fromKey`. However, this method doesn't
        throw an exception in that situation, but instead keeps the original `fromKey`. Similarly, this method keeps the original `toKey`, instead
        of throwing an exception, if passed a `toKey` greater than an earlier
        `toKey`.

        Since
        - 12.0
        """
        ...


    def tailMap(self, fromKey: "K") -> "ImmutableSortedMap"["K", "V"]:
        """
        This method returns a `ImmutableSortedMap`, consisting of the entries
        whose keys are greater than or equals to `fromKey`.
        
        The SortedMap.tailMap documentation states that a submap of a
        submap throws an IllegalArgumentException if passed a `fromKey` less than an earlier `fromKey`. However, this method doesn't
        throw an exception in that situation, but instead keeps the original `fromKey`.
        """
        ...


    def tailMap(self, fromKey: "K", inclusive: bool) -> "ImmutableSortedMap"["K", "V"]:
        """
        This method returns a `ImmutableSortedMap`, consisting of the entries
        whose keys are greater than (or equal to, if `inclusive`)
        `fromKey`.
        
        The SortedMap.tailMap documentation states that a submap of a
        submap throws an IllegalArgumentException if passed a `fromKey` less than an earlier `fromKey`. However, this method doesn't
        throw an exception in that situation, but instead keeps the original `fromKey`.

        Since
        - 12.0
        """
        ...


    def lowerEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def lowerKey(self, key: "K") -> "K":
        ...


    def floorEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def floorKey(self, key: "K") -> "K":
        ...


    def ceilingEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def ceilingKey(self, key: "K") -> "K":
        ...


    def higherEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def higherKey(self, key: "K") -> "K":
        ...


    def firstEntry(self) -> "Entry"["K", "V"]:
        ...


    def lastEntry(self) -> "Entry"["K", "V"]:
        ...


    def pollFirstEntry(self) -> "Entry"["K", "V"]:
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def pollLastEntry(self) -> "Entry"["K", "V"]:
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def descendingMap(self) -> "ImmutableSortedMap"["K", "V"]:
        ...


    def navigableKeySet(self) -> "ImmutableSortedSet"["K"]:
        ...


    def descendingKeySet(self) -> "ImmutableSortedSet"["K"]:
        ...


    class Builder(Builder):
        """
        A builder for creating immutable sorted map instances, especially `public static final` maps ("constant maps"). Example: ```   `static final ImmutableSortedMap<Integer, String> INT_TO_WORD =
              new ImmutableSortedMap.Builder<Integer, String>(Ordering.natural())
                  .put(1, "one")
                  .put(2, "two")
                  .put(3, "three")
                  .build();````
        
        For *small* immutable sorted maps, the `ImmutableSortedMap.of()`
        methods are even more convenient.
        
        Builder instances can be reused - it is safe to call .build
        multiple times to build multiple maps in series. Each map is a superset of
        the maps created before it.

        Since
        - 2.0
        """

        def __init__(self, comparator: "Comparator"["K"]):
            """
            Creates a new builder. The returned builder is equivalent to the builder
            generated by ImmutableSortedMap.orderedBy.
            """
            ...


        def put(self, key: "K", value: "V") -> "Builder"["K", "V"]:
            """
            Associates `key` with `value` in the built map. Duplicate
            keys, according to the comparator (which might be the keys' natural
            order), are not allowed, and will cause .build to fail.
            """
            ...


        def put(self, entry: "Entry"["K", "V"]) -> "Builder"["K", "V"]:
            """
            Adds the given `entry` to the map, making it immutable if
            necessary. Duplicate keys, according to the comparator (which might be
            the keys' natural order), are not allowed, and will cause .build
            to fail.

            Since
            - 11.0
            """
            ...


        def putAll(self, map: dict["K", "V"]) -> "Builder"["K", "V"]:
            """
            Associates all of the given map's keys and values in the built map.
            Duplicate keys, according to the comparator (which might be the keys'
            natural order), are not allowed, and will cause .build to fail.

            Raises
            - NullPointerException: if any key or value in `map` is null
            """
            ...


        def putAll(self, entries: Iterable["Entry"["K", "V"]]) -> "Builder"["K", "V"]:
            """
            Adds all the given entries to the built map.  Duplicate keys, according
            to the comparator (which might be the keys' natural order), are not
            allowed, and will cause .build to fail.

            Raises
            - NullPointerException: if any key, value, or entry is null

            Since
            - 19.0
            """
            ...


        def orderEntriesByValue(self, valueComparator: "Comparator"["V"]) -> "Builder"["K", "V"]:
            """
            Throws an `UnsupportedOperationException`.

            Since
            - 19.0

            Deprecated
            - Unsupported by ImmutableSortedMap.Builder.
            """
            ...


        def build(self) -> "ImmutableSortedMap"["K", "V"]:
            """
            Returns a newly-created immutable sorted map.

            Raises
            - IllegalArgumentException: if any two keys are equal according to
                the comparator (which might be the keys' natural order)
            """
            ...
