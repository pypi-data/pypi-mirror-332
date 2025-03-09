"""
Python module generated from Java source file com.google.common.collect.ImmutableMap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from com.google.errorprone.annotations import DoNotMock
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import RetainedWith
from com.google.j2objc.annotations import WeakOuter
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.util import Arrays
from java.util import BitSet
from java.util import Collections
from java.util import Comparator
from java.util import EnumMap
from java.util import Iterator
from java.util import SortedMap
from java.util import Spliterator
from java.util.function import BiFunction
from java.util.function import BinaryOperator
from java.util.function import Function
from java.util.stream import Collector
from java.util.stream import Collectors
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableMap(Map, Serializable):
    """
    A Map whose contents will never change, with many other important properties detailed at
    ImmutableCollection.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/ImmutableCollectionsExplained">immutable collections</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    @staticmethod
    def toImmutableMap(keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"]) -> "Collector"["T", Any, "ImmutableMap"["K", "V"]]:
        """
        Returns a Collector that accumulates elements into an `ImmutableMap` whose keys
        and values are the result of applying the provided mapping functions to the input elements.
        Entries appear in the result `ImmutableMap` in encounter order.
        
        If the mapped keys contain duplicates (according to Object.equals(Object), an `IllegalArgumentException` is thrown when the collection operation is performed. (This differs
        from the `Collector` returned by Collectors.toMap(Function, Function), which
        throws an `IllegalStateException`.)

        Since
        - 21.0
        """
        ...


    @staticmethod
    def toImmutableMap(keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"], mergeFunction: "BinaryOperator"["V"]) -> "Collector"["T", Any, "ImmutableMap"["K", "V"]]:
        """
        Returns a Collector that accumulates elements into an `ImmutableMap` whose keys
        and values are the result of applying the provided mapping functions to the input elements.
        
        If the mapped keys contain duplicates (according to Object.equals(Object)), the
        values are merged using the specified merging function. Entries will appear in the encounter
        order of the first occurrence of the key.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableMap"["K", "V"]:
        """
        Returns the empty map. This map behaves and performs comparably to Collections.emptyMap, and is preferable mainly for consistency and maintainability of your
        code.
        
        **Performance note:** the instance returned is a singleton.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing a single entry. This map behaves and performs comparably to
        Collections.singletonMap but will not accept a null key or value. It is preferable
        mainly for consistency and maintainability of your code.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided

        Since
        - 31.0
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided

        Since
        - 31.0
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V", k8: "K", v8: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided

        Since
        - 31.0
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V", k8: "K", v8: "V", k9: "K", v9: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided

        Since
        - 31.0
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V", k8: "K", v8: "V", k9: "K", v9: "V", k10: "K", v10: "V") -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided

        Since
        - 31.0
        """
        ...


    @staticmethod
    def ofEntries(*entries: Tuple["Entry"["K", "V"], ...]) -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys are provided

        Since
        - 31.0
        """
        ...


    @staticmethod
    def builder() -> "Builder"["K", "V"]:
        """
        Returns a new builder. The generated builder is equivalent to the builder created by the Builder constructor.
        """
        ...


    @staticmethod
    def builderWithExpectedSize(expectedSize: int) -> "Builder"["K", "V"]:
        """
        Returns a new builder, expecting the specified number of entries to be added.
        
        If `expectedSize` is exactly the number of entries added to the builder before Builder.build is called, the builder is likely to perform better than an unsized .builder() would have.
        
        It is not specified if any performance benefits apply if `expectedSize` is close to,
        but not exactly, the number of entries added to the builder.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def copyOf(map: dict["K", "V"]) -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the same entries as `map`. The returned map iterates
        over entries in the same order as the `entrySet` of the original map. If `map`
        somehow contains entries with duplicate keys (for example, if it is a `SortedMap` whose
        comparator is not *consistent with equals*), the results of this method are undefined.
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.

        Raises
        - NullPointerException: if any key or value in `map` is null
        """
        ...


    @staticmethod
    def copyOf(entries: Iterable["Entry"["K", "V"]]) -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map containing the specified entries. The returned map iterates over
        entries in the same order as the original iterable.

        Raises
        - NullPointerException: if any key, value, or entry is null
        - IllegalArgumentException: if two entries have the same key

        Since
        - 19.0
        """
        ...


    def put(self, k: "K", v: "V") -> "V":
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def putIfAbsent(self, key: "K", value: "V") -> "V":
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def replace(self, key: "K", oldValue: "V", newValue: "V") -> bool:
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def replace(self, key: "K", value: "V") -> "V":
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def computeIfAbsent(self, key: "K", mappingFunction: "Function"["K", "V"]) -> "V":
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def computeIfPresent(self, key: "K", remappingFunction: "BiFunction"["K", "V", "V"]) -> "V":
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def compute(self, key: "K", remappingFunction: "BiFunction"["K", "V", "V"]) -> "V":
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def merge(self, key: "K", value: "V", function: "BiFunction"["V", "V", "V"]) -> "V":
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def putAll(self, map: dict["K", "V"]) -> None:
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def replaceAll(self, function: "BiFunction"["K", "V", "V"]) -> None:
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def remove(self, o: "Object") -> "V":
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def clear(self) -> None:
        """
        Guaranteed to throw an exception and leave the map unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def isEmpty(self) -> bool:
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def get(self, key: "Object") -> "V":
        ...


    def getOrDefault(self, key: "Object", defaultValue: "V") -> "V":
        """
        Since
        - 21.0 (but only since 23.5 in the Android <a
            href="https://github.com/google/guava#guava-google-core-libraries-for-java">flavor</a>).
            Note, however, that Java 8 users can call this method with any version and flavor of Guava.
        """
        ...


    def entrySet(self) -> "ImmutableSet"["Entry"["K", "V"]]:
        """
        Returns an immutable set of the mappings in this map. The iteration order is specified by the
        method used to create this map. Typically, this is insertion order.
        """
        ...


    def keySet(self) -> "ImmutableSet"["K"]:
        """
        Returns an immutable set of the keys in this map, in the same order that they appear in .entrySet.
        """
        ...


    def values(self) -> "ImmutableCollection"["V"]:
        """
        Returns an immutable collection of the values in this map, in the same order that they appear
        in .entrySet.
        """
        ...


    def asMultimap(self) -> "ImmutableSetMultimap"["K", "V"]:
        """
        Returns a multimap view of the map.

        Since
        - 14.0
        """
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    class Builder:
        """
        A builder for creating immutable map instances, especially `public static final` maps
        ("constant maps"). Example:
        
        ````static final ImmutableMap<String, Integer> WORD_TO_INT =
            new ImmutableMap.Builder<String, Integer>()
                .put("one", 1)
                .put("two", 2)
                .put("three", 3)
                .buildOrThrow();````
        
        For *small* immutable maps, the `ImmutableMap.of()` methods are even more
        convenient.
        
        By default, a `Builder` will generate maps that iterate over entries in the order they
        were inserted into the builder, equivalently to `LinkedHashMap`. For example, in the
        above example, `WORD_TO_INT.entrySet()` is guaranteed to iterate over the entries in the
        order `"one"=1, "two"=2, "three"=3`, and `keySet()` and `values()` respect
        the same order. If you want a different order, consider using ImmutableSortedMap to
        sort by keys, or call .orderEntriesByValue(Comparator), which changes this builder to
        sort entries by value.
        
        Builder instances can be reused - it is safe to call .buildOrThrow multiple times to
        build multiple maps in series. Each map is a superset of the maps created before it.

        Since
        - 2.0
        """

        def __init__(self):
            """
            Creates a new builder. The returned builder is equivalent to the builder generated by ImmutableMap.builder.
            """
            ...


        def put(self, key: "K", value: "V") -> "Builder"["K", "V"]:
            """
            Associates `key` with `value` in the built map. If the same key is put more than
            once, .buildOrThrow will fail, while .buildKeepingLast will keep the last
            value put for that key.
            """
            ...


        def put(self, entry: "Entry"["K", "V"]) -> "Builder"["K", "V"]:
            """
            Adds the given `entry` to the map, making it immutable if necessary. If the same key is
            put more than once, .buildOrThrow will fail, while .buildKeepingLast will
            keep the last value put for that key.

            Since
            - 11.0
            """
            ...


        def putAll(self, map: dict["K", "V"]) -> "Builder"["K", "V"]:
            """
            Associates all of the given map's keys and values in the built map. If the same key is put
            more than once, .buildOrThrow will fail, while .buildKeepingLast will keep
            the last value put for that key.

            Raises
            - NullPointerException: if any key or value in `map` is null
            """
            ...


        def putAll(self, entries: Iterable["Entry"["K", "V"]]) -> "Builder"["K", "V"]:
            """
            Adds all of the given entries to the built map. If the same key is put more than once, .buildOrThrow will fail, while .buildKeepingLast will keep the last value put for
            that key.

            Raises
            - NullPointerException: if any key, value, or entry is null

            Since
            - 19.0
            """
            ...


        def orderEntriesByValue(self, valueComparator: "Comparator"["V"]) -> "Builder"["K", "V"]:
            """
            Configures this `Builder` to order entries by value according to the specified
            comparator.
            
            The sort order is stable, that is, if two entries have values that compare as equivalent,
            the entry that was inserted first will be first in the built map's iteration order.

            Raises
            - IllegalStateException: if this method was already called

            Since
            - 19.0
            """
            ...


        def build(self) -> "ImmutableMap"["K", "V"]:
            """
            Returns a newly-created immutable map. The iteration order of the returned map is the order
            in which entries were inserted into the builder, unless .orderEntriesByValue was
            called, in which case entries are sorted by value.
            
            Prefer the equivalent method .buildOrThrow() to make it explicit that the method
            will throw an exception if there are duplicate keys. The `build()` method will soon be
            deprecated.

            Raises
            - IllegalArgumentException: if duplicate keys were added
            """
            ...


        def buildOrThrow(self) -> "ImmutableMap"["K", "V"]:
            """
            Returns a newly-created immutable map, or throws an exception if any key was added more than
            once. The iteration order of the returned map is the order in which entries were inserted
            into the builder, unless .orderEntriesByValue was called, in which case entries are
            sorted by value.

            Raises
            - IllegalArgumentException: if duplicate keys were added

            Since
            - 31.0
            """
            ...


        def buildKeepingLast(self) -> "ImmutableMap"["K", "V"]:
            """
            Returns a newly-created immutable map, using the last value for any key that was added more
            than once. The iteration order of the returned map is the order in which entries were
            inserted into the builder, unless .orderEntriesByValue was called, in which case
            entries are sorted by value. If a key was added more than once, it appears in iteration order
            based on the first time it was added, again unless .orderEntriesByValue was called.
            
            In the current implementation, all values associated with a given key are stored in the
            `Builder` object, even though only one of them will be used in the built map. If there
            can be many repeated keys, it may be more space-efficient to use a java.util.LinkedHashMap LinkedHashMap and ImmutableMap.copyOf(Map) rather than
            `ImmutableMap.Builder`.

            Since
            - 31.1
            """
            ...
