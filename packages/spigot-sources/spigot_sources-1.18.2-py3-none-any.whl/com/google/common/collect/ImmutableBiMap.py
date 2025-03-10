"""
Python module generated from Java source file com.google.common.collect.ImmutableBiMap

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from java.util import Arrays
from java.util import Comparator
from java.util.function import Function
from java.util.stream import Collector
from java.util.stream import Collectors
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
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
        Returns a Collector that accumulates elements into an `ImmutableBiMap` whose keys
        and values are the result of applying the provided mapping functions to the input elements.
        Entries appear in the result `ImmutableBiMap` in encounter order.
        
        If the mapped keys or values contain duplicates (according to Object.equals(Object),
        an `IllegalArgumentException` is thrown when the collection operation is performed. (This
        differs from the `Collector` returned by Collectors.toMap(Function, Function),
        which throws an `IllegalStateException`.)

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
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are added

        Since
        - 31.0
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are added

        Since
        - 31.0
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V", k8: "K", v8: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are added

        Since
        - 31.0
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V", k8: "K", v8: "V", k9: "K", v9: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are added

        Since
        - 31.0
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V", k8: "K", v8: "V", k9: "K", v9: "V", k10: "K", v10: "V") -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are added

        Since
        - 31.0
        """
        ...


    @staticmethod
    def ofEntries(*entries: Tuple["Entry"["K", "V"], ...]) -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable map containing the given entries, in order.

        Raises
        - IllegalArgumentException: if duplicate keys or values are provided

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
    def copyOf(map: dict["K", "V"]) -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable bimap containing the same entries as `map`. If `map` somehow
        contains entries with duplicate keys (for example, if it is a `SortedMap` whose
        comparator is not *consistent with equals*), the results of this method are undefined.
        
        The returned `BiMap` iterates over entries in the same order as the `entrySet`
        of the original map.
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.

        Raises
        - IllegalArgumentException: if two keys have the same value or two values have the same
            key
        - NullPointerException: if any key or value in `map` is null
        """
        ...


    @staticmethod
    def copyOf(entries: Iterable["Entry"["K", "V"]]) -> "ImmutableBiMap"["K", "V"]:
        """
        Returns an immutable bimap containing the given entries. The returned bimap iterates over
        entries in the same order as the original iterable.

        Raises
        - IllegalArgumentException: if two keys have the same value or two values have the same
            key
        - NullPointerException: if any key, value, or entry is null

        Since
        - 19.0
        """
        ...


    def inverse(self) -> "ImmutableBiMap"["V", "K"]:
        """
        
        
        The inverse of an `ImmutableBiMap` is another `ImmutableBiMap`.
        """
        ...


    def values(self) -> "ImmutableSet"["V"]:
        """
        Returns an immutable set of the values in this map, in the same order they appear in .entrySet.
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
        A builder for creating immutable bimap instances, especially `public static final` bimaps
        ("constant bimaps"). Example:
        
        ````static final ImmutableBiMap<String, Integer> WORD_TO_INT =
            new ImmutableBiMap.Builder<String, Integer>()
                .put("one", 1)
                .put("two", 2)
                .put("three", 3)
                .buildOrThrow();````
        
        For *small* immutable bimaps, the `ImmutableBiMap.of()` methods are even more
        convenient.
        
        By default, a `Builder` will generate bimaps that iterate over entries in the order
        they were inserted into the builder. For example, in the above example, `WORD_TO_INT.entrySet()` is guaranteed to iterate over the entries in the order `"one"=1,
        "two"=2, "three"=3`, and `keySet()` and `values()` respect the same order. If you
        want a different order, consider using .orderEntriesByValue(Comparator), which changes
        this builder to sort entries by value.
        
        Builder instances can be reused - it is safe to call .buildOrThrow multiple times to
        build multiple bimaps in series. Each bimap is a superset of the bimaps created before it.

        Since
        - 2.0
        """

        def __init__(self):
            """
            Creates a new builder. The returned builder is equivalent to the builder generated by ImmutableBiMap.builder.
            """
            ...


        def put(self, key: "K", value: "V") -> "Builder"["K", "V"]:
            """
            Associates `key` with `value` in the built bimap. Duplicate keys or values are
            not allowed, and will cause .build to fail.
            """
            ...


        def put(self, entry: "Entry"["K", "V"]) -> "Builder"["K", "V"]:
            """
            Adds the given `entry` to the bimap. Duplicate keys or values are not allowed, and will
            cause .build to fail.

            Since
            - 19.0
            """
            ...


        def putAll(self, map: dict["K", "V"]) -> "Builder"["K", "V"]:
            """
            Associates all of the given map's keys and values in the built bimap. Duplicate keys or
            values are not allowed, and will cause .build to fail.

            Raises
            - NullPointerException: if any key or value in `map` is null
            """
            ...


        def putAll(self, entries: Iterable["Entry"["K", "V"]]) -> "Builder"["K", "V"]:
            """
            Adds all of the given entries to the built bimap. Duplicate keys or values are not allowed,
            and will cause .build to fail.

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


        def build(self) -> "ImmutableBiMap"["K", "V"]:
            """
            Returns a newly-created immutable bimap. The iteration order of the returned bimap is the
            order in which entries were inserted into the builder, unless .orderEntriesByValue
            was called, in which case entries are sorted by value.
            
            Prefer the equivalent method .buildOrThrow() to make it explicit that the method
            will throw an exception if there are duplicate keys or values. The `build()` method
            will soon be deprecated.

            Raises
            - IllegalArgumentException: if duplicate keys or values were added
            """
            ...


        def buildOrThrow(self) -> "ImmutableBiMap"["K", "V"]:
            """
            Returns a newly-created immutable bimap, or throws an exception if any key or value was added
            more than once. The iteration order of the returned bimap is the order in which entries were
            inserted into the builder, unless .orderEntriesByValue was called, in which case
            entries are sorted by value.

            Raises
            - IllegalArgumentException: if duplicate keys or values were added

            Since
            - 31.0
            """
            ...
