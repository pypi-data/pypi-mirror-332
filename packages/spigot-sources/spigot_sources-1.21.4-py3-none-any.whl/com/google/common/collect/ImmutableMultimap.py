"""
Python module generated from Java source file com.google.common.collect.ImmutableMultimap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from com.google.errorprone.annotations import DoNotMock
from com.google.j2objc.annotations import Weak
from com.google.j2objc.annotations import WeakOuter
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.util import Arrays
from java.util import Comparator
from java.util import Iterator
from java.util import Spliterator
from java.util.function import BiConsumer
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableMultimap(BaseImmutableMultimap, Serializable):
    """
    A Multimap whose contents will never change, with many other important properties
    detailed at ImmutableCollection.
    
    **Warning:** avoid *direct* usage of ImmutableMultimap as a type (as with
    Multimap itself). Prefer subtypes such as ImmutableSetMultimap or ImmutableListMultimap, which have well-defined .equals semantics, thus avoiding a common
    source of bugs and confusion.
    
    **Note:** every ImmutableMultimap offers an .inverse view, so there is no
    need for a distinct `ImmutableBiMultimap` type.
    
    <a id="iteration"></a>
    
    **Key-grouped iteration.** All view collections follow the same iteration order. In all
    current implementations, the iteration order always keeps multiple entries with the same key
    together. Any creation method that would customarily respect insertion order (such as .copyOf(Multimap)) instead preserves key-grouped order by inserting entries for an existing key
    immediately after the last entry having that key.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/ImmutableCollectionsExplained">immutable collections</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def of() -> "ImmutableMultimap"["K", "V"]:
        """
        Returns an empty multimap.
        
        **Performance note:** the instance returned is a singleton.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V") -> "ImmutableMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing a single entry.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V") -> "ImmutableMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the given entries, in order.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V") -> "ImmutableMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the given entries, in the "key-grouped" insertion
        order described in the <a href="#iteration">class documentation</a>.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V") -> "ImmutableMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the given entries, in the "key-grouped" insertion
        order described in the <a href="#iteration">class documentation</a>.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V") -> "ImmutableMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the given entries, in the "key-grouped" insertion
        order described in the <a href="#iteration">class documentation</a>.
        """
        ...


    @staticmethod
    def builder() -> "Builder"["K", "V"]:
        """
        Returns a new builder. The generated builder is equivalent to the builder created by the Builder constructor.
        """
        ...


    @staticmethod
    def builderWithExpectedKeys(expectedKeys: int) -> "Builder"["K", "V"]:
        """
        Returns a new builder with a hint for how many distinct keys are expected to be added. The
        generated builder is equivalent to that returned by .builder, but may perform better if
        `expectedKeys` is a good estimate.

        Raises
        - IllegalArgumentException: if `expectedKeys` is negative

        Since
        - 33.3.0
        """
        ...


    @staticmethod
    def copyOf(multimap: "Multimap"["K", "V"]) -> "ImmutableMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the same mappings as `multimap`, in the
        "key-grouped" iteration order described in the class documentation.
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.

        Raises
        - NullPointerException: if any key or value in `multimap` is null
        """
        ...


    @staticmethod
    def copyOf(entries: Iterable["Entry"["K", "V"]]) -> "ImmutableMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the specified entries. The returned multimap iterates
        over keys in the order they were first encountered in the input, and the values for each key
        are iterated in the order they were encountered.

        Raises
        - NullPointerException: if any key, value, or entry is null

        Since
        - 19.0
        """
        ...


    def removeAll(self, key: "Object") -> "ImmutableCollection"["V"]:
        """
        Guaranteed to throw an exception and leave the multimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> "ImmutableCollection"["V"]:
        """
        Guaranteed to throw an exception and leave the multimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def clear(self) -> None:
        """
        Guaranteed to throw an exception and leave the multimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def get(self, key: "K") -> "ImmutableCollection"["V"]:
        """
        Returns an immutable collection of the values for the given key. If no mappings in the multimap
        have the provided key, an empty immutable collection is returned. The values are in the same
        order as the parameters used to build this multimap.
        """
        ...


    def inverse(self) -> "ImmutableMultimap"["V", "K"]:
        """
        Returns an immutable multimap which is the inverse of this one. For every key-value mapping in
        the original, the result will have a mapping with key and value reversed.

        Since
        - 11.0
        """
        ...


    def put(self, key: "K", value: "V") -> bool:
        """
        Guaranteed to throw an exception and leave the multimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def putAll(self, key: "K", values: Iterable["V"]) -> bool:
        """
        Guaranteed to throw an exception and leave the multimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def putAll(self, multimap: "Multimap"["K", "V"]) -> bool:
        """
        Guaranteed to throw an exception and leave the multimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        """
        Guaranteed to throw an exception and leave the multimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def size(self) -> int:
        ...


    def keySet(self) -> "ImmutableSet"["K"]:
        """
        Returns an immutable set of the distinct keys in this multimap, in the same order as they
        appear in this multimap.
        """
        ...


    def asMap(self) -> "ImmutableMap"["K", Iterable["V"]]:
        """
        Returns an immutable map that associates each key with its corresponding values in the
        multimap. Keys and values appear in the same order as in this multimap.
        """
        ...


    def entries(self) -> "ImmutableCollection"["Entry"["K", "V"]]:
        """
        Returns an immutable collection of all key-value pairs in the multimap.
        """
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def keys(self) -> "ImmutableMultiset"["K"]:
        """
        Returns an immutable multiset containing all the keys in this multimap, in the same order and
        with the same frequencies as they appear in this multimap; to get only a single occurrence of
        each key, use .keySet.
        """
        ...


    def values(self) -> "ImmutableCollection"["V"]:
        """
        Returns an immutable collection of the values in this multimap. Its iterator traverses the
        values for the first key, the values for the second key, and so on.
        """
        ...


    class Builder:
        """
        A builder for creating immutable multimap instances, especially `public static final`
        multimaps ("constant multimaps"). Example:
        
        ````static final Multimap<String, Integer> STRING_TO_INTEGER_MULTIMAP =
            new ImmutableMultimap.Builder<String, Integer>()
                .put("one", 1)
                .putAll("several", 1, 2, 3)
                .putAll("many", 1, 2, 3, 4, 5)
                .build();````
        
        Builder instances can be reused; it is safe to call .build multiple times to build
        multiple multimaps in series. Each multimap contains the key-value mappings in the previously
        created multimaps.

        Since
        - 2.0
        """

        def __init__(self):
            """
            Creates a new builder. The returned builder is equivalent to the builder generated by ImmutableMultimap.builder.
            """
            ...


        def expectedValuesPerKey(self, expectedValuesPerKey: int) -> "Builder"["K", "V"]:
            """
            Provides a hint for how many values will be associated with each key newly added to the
            builder after this call. This does not change semantics, but may improve performance if
            `expectedValuesPerKey` is a good estimate.
            
            This may be called more than once; each newly added key will use the most recent call to
            .expectedValuesPerKey as its hint.

            Raises
            - IllegalArgumentException: if `expectedValuesPerKey` is negative

            Since
            - 33.3.0
            """
            ...


        def put(self, key: "K", value: "V") -> "Builder"["K", "V"]:
            """
            Adds a key-value mapping to the built multimap.
            """
            ...


        def put(self, entry: "Entry"["K", "V"]) -> "Builder"["K", "V"]:
            """
            Adds an entry to the built multimap.

            Since
            - 11.0
            """
            ...


        def putAll(self, entries: Iterable["Entry"["K", "V"]]) -> "Builder"["K", "V"]:
            """
            Adds entries to the built multimap.

            Since
            - 19.0
            """
            ...


        def putAll(self, key: "K", values: Iterable["V"]) -> "Builder"["K", "V"]:
            """
            Stores a collection of values with the same key in the built multimap.

            Raises
            - NullPointerException: if `key`, `values`, or any element in `values`
                is null. The builder is left in an invalid state.
            """
            ...


        def putAll(self, key: "K", *values: Tuple["V", ...]) -> "Builder"["K", "V"]:
            """
            Stores an array of values with the same key in the built multimap.

            Raises
            - NullPointerException: if the key or any value is null. The builder is left in an
                invalid state.
            """
            ...


        def putAll(self, multimap: "Multimap"["K", "V"]) -> "Builder"["K", "V"]:
            """
            Stores another multimap's entries in the built multimap. The generated multimap's key and
            value orderings correspond to the iteration ordering of the `multimap.asMap()` view,
            with new keys and values following any existing keys and values.

            Raises
            - NullPointerException: if any key or value in `multimap` is null. The builder is
                left in an invalid state.
            """
            ...


        def orderKeysBy(self, keyComparator: "Comparator"["K"]) -> "Builder"["K", "V"]:
            """
            Specifies the ordering of the generated multimap's keys.

            Since
            - 8.0
            """
            ...


        def orderValuesBy(self, valueComparator: "Comparator"["V"]) -> "Builder"["K", "V"]:
            """
            Specifies the ordering of the generated multimap's values for each key.

            Since
            - 8.0
            """
            ...


        def build(self) -> "ImmutableMultimap"["K", "V"]:
            """
            Returns a newly-created immutable multimap.
            """
            ...
