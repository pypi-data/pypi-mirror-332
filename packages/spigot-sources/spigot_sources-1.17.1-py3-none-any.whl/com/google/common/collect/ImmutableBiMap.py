"""
Python module generated from Java source file com.google.common.collect.ImmutableBiMap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Arrays
from java.util import Comparator
from java.util.function import Function
from java.util.stream import Collector
from java.util.stream import Collectors
from typing import Any, Callable, Iterable, Tuple


class ImmutableBiMap(ImmutableBiMapFauxverideShim, BiMap):
    """
    A BiMap whose contents will never change, with many other important properties detailed
    at ImmutableCollection.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def toImmutableBiMap(keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"]) -> "Collector"["T", Any, "ImmutableBiMap"["K", "V"]]:
        """
        Returns a Collector that accumulates elements into an `ImmutableBiMap` whose
        keys and values are the result of applying the provided mapping functions to the input
        elements. Entries appear in the result `ImmutableBiMap` in encounter order.
        
        If the mapped keys or values contain duplicates
        (according to Object.equals(Object), an `IllegalArgumentException` is thrown
        when the collection operation is performed. (This differs from the `Collector` returned
        by Collectors.toMap(Function, Function), which throws an
        `IllegalStateException`.)

        Since
        - 21.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableBiMap"["K", "V"]:
        ...


    @staticmethod
    def of(k1: "K", v1: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable bimap containing a single entry.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are added
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are added
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are added
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are added
        """
        ...


    @staticmethod
    def builder() -> "Builder"["K", "V"]:
        """
        Returns a new builder. The generated builder is equivalent to the builder
        created by the Builder constructor.
        """
        ...


    @staticmethod
    def copyOf(map: dict["K", "V"]) -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable bimap containing the same entries as `map`. If
        `map` somehow contains entries with duplicate keys (for example, if
        it is a `SortedMap` whose comparator is not *consistent with
        equals*), the results of this method are undefined.
        
        Despite the method name, this method attempts to avoid actually copying
        the data when it is safe to do so. The exact circumstances under which a
        copy will or will not be performed are undocumented and subject to change.

        Raises
        - IllegalArgumentException: if two keys have the same value
        - NullPointerException: if any key or value in `map` is null
        """
        ...


    @staticmethod
    def copyOf(entries: Iterable["Entry"["K", "V"]]) -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable bimap containing the given entries.

        Raises
        - IllegalArgumentException: if two keys have the same value or two
                values have the same key
        - NullPointerException: if any key, value, or entry is null

        Since
        - 19.0
        """
        ...


    def inverse(self) -> "ImmutableBiMap"["V", "K"]:
        """
        
        
        The inverse of an `ImmutableBiMap` is another
        `ImmutableBiMap`.
        """
        ...


    def values(self) -> "ImmutableSet"["V"]:
        """
        Returns an immutable set of the values in this map. The values are in the
        same order as the parameters used to build this map.
        """
        ...


    def forcePut(self, key: "K", value: "V") -> "V":
        """
        Guaranteed to throw an exception and leave the bimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    class Builder(Builder):
        """
        A builder for creating immutable bimap instances, especially `public
        static final` bimaps ("constant bimaps"). Example: ```   `static final ImmutableBiMap<String, Integer> WORD_TO_INT =
              new ImmutableBiMap.Builder<String, Integer>()
                  .put("one", 1)
                  .put("two", 2)
                  .put("three", 3)
                  .build();````
        
        For *small* immutable bimaps, the `ImmutableBiMap.of()` methods
        are even more convenient.
        
        Builder instances can be reused - it is safe to call .build
        multiple times to build multiple bimaps in series. Each bimap is a superset
        of the bimaps created before it.

        Since
        - 2.0
        """

        def __init__(self):
            """
            Creates a new builder. The returned builder is equivalent to the builder
            generated by ImmutableBiMap.builder.
            """
            ...


        def put(self, key: "K", value: "V") -> "Builder"["K", "V"]:
            """
            Associates `key` with `value` in the built bimap. Duplicate
            keys or values are not allowed, and will cause .build to fail.
            """
            ...


        def put(self, entry: "Entry"["K", "V"]) -> "Builder"["K", "V"]:
            """
            Adds the given `entry` to the bimap.  Duplicate keys or values
            are not allowed, and will cause .build to fail.

            Since
            - 19.0
            """
            ...


        def putAll(self, map: dict["K", "V"]) -> "Builder"["K", "V"]:
            """
            Associates all of the given map's keys and values in the built bimap.
            Duplicate keys or values are not allowed, and will cause .build
            to fail.

            Raises
            - NullPointerException: if any key or value in `map` is null
            """
            ...


        def putAll(self, entries: Iterable["Entry"["K", "V"]]) -> "Builder"["K", "V"]:
            """
            Adds all of the given entries to the built bimap.  Duplicate keys or
            values are not allowed, and will cause .build to fail.

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
            
            The sort order is stable, that is, if two entries have values that compare
            as equivalent, the entry that was inserted first will be first in the built map's
            iteration order.

            Raises
            - IllegalStateException: if this method was already called

            Since
            - 19.0
            """
            ...


        def build(self) -> "ImmutableBiMap"["K", "V"]:
            """
            Returns a newly-created immutable bimap.

            Raises
            - IllegalArgumentException: if duplicate keys or values were added
            """
            ...
