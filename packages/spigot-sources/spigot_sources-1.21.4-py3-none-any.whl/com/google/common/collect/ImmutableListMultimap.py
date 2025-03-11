"""
Python module generated from Java source file com.google.common.collect.ImmutableListMultimap

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
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import RetainedWith
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.util import Comparator
from java.util.function import Function
from java.util.stream import Collector
from java.util.stream import Stream
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableListMultimap(ImmutableMultimap, ListMultimap):
    """
    A ListMultimap whose contents will never change, with many other important properties
    detailed at ImmutableCollection.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/ImmutableCollectionsExplained">immutable collections</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def toImmutableListMultimap(keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"]) -> "Collector"["T", Any, "ImmutableListMultimap"["K", "V"]]:
        """
        Returns a Collector that accumulates elements into an `ImmutableListMultimap`
        whose keys and values are the result of applying the provided mapping functions to the input
        elements.
        
        For streams with defined encounter order (as defined in the Ordering section of the java.util.stream Javadoc), that order is preserved, but entries are <a
        href="ImmutableMultimap.html#iteration">grouped by key</a>.
        
        Example:
        
        ````static final Multimap<Character, String> FIRST_LETTER_MULTIMAP =
            Stream.of("banana", "apple", "carrot", "asparagus", "cherry")
                .collect(toImmutableListMultimap(str -> str.charAt(0), str -> str.substring(1)));
        
        // is equivalent to
        
        static final Multimap<Character, String> FIRST_LETTER_MULTIMAP =
            new ImmutableListMultimap.Builder<Character, String>()
                .put('b', "anana")
                .putAll('a', "pple", "sparagus")
                .putAll('c', "arrot", "herry")
                .build();````

        Since
        - 21.0
        """
        ...


    @staticmethod
    def flatteningToImmutableListMultimap(keyFunction: "Function"["T", "K"], valuesFunction: "Function"["T", "Stream"["V"]]) -> "Collector"["T", Any, "ImmutableListMultimap"["K", "V"]]:
        """
        Returns a `Collector` accumulating entries into an `ImmutableListMultimap`. Each
        input element is mapped to a key and a stream of values, each of which are put into the
        resulting `Multimap`, in the encounter order of the stream and the encounter order of the
        streams of values.
        
        Example:
        
        ````static final ImmutableListMultimap<Character, Character> FIRST_LETTER_MULTIMAP =
            Stream.of("banana", "apple", "carrot", "asparagus", "cherry")
                .collect(
                    flatteningToImmutableListMultimap(
                         str -> str.charAt(0),
                         str -> str.substring(1).chars().mapToObj(c -> (char) c));
        
        // is equivalent to
        
        static final ImmutableListMultimap<Character, Character> FIRST_LETTER_MULTIMAP =
            ImmutableListMultimap.<Character, Character>builder()
                .putAll('b', Arrays.asList('a', 'n', 'a', 'n', 'a'))
                .putAll('a', Arrays.asList('p', 'p', 'l', 'e'))
                .putAll('c', Arrays.asList('a', 'r', 'r', 'o', 't'))
                .putAll('a', Arrays.asList('s', 'p', 'a', 'r', 'a', 'g', 'u', 's'))
                .putAll('c', Arrays.asList('h', 'e', 'r', 'r', 'y'))
                .build();`
        }```

        Since
        - 21.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableListMultimap"["K", "V"]:
        ...


    @staticmethod
    def of(k1: "K", v1: "V") -> "ImmutableListMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing a single entry.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V") -> "ImmutableListMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the given entries, in order.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V") -> "ImmutableListMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the given entries, in order.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V") -> "ImmutableListMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the given entries, in order.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V") -> "ImmutableListMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the given entries, in order.
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
    def copyOf(multimap: "Multimap"["K", "V"]) -> "ImmutableListMultimap"["K", "V"]:
        """
        Returns an immutable multimap containing the same mappings as `multimap`. The generated
        multimap's key and value orderings correspond to the iteration ordering of the `multimap.asMap()` view.
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.

        Raises
        - NullPointerException: if any key or value in `multimap` is null
        """
        ...


    @staticmethod
    def copyOf(entries: Iterable["Entry"["K", "V"]]) -> "ImmutableListMultimap"["K", "V"]:
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


    def get(self, key: "K") -> "ImmutableList"["V"]:
        """
        Returns an immutable list of the values for the given key. If no mappings in the multimap have
        the provided key, an empty immutable list is returned. The values are in the same order as the
        parameters used to build this multimap.
        """
        ...


    def inverse(self) -> "ImmutableListMultimap"["V", "K"]:
        """
        
        
        Because an inverse of a list multimap can contain multiple pairs with the same key and
        value, this method returns an `ImmutableListMultimap` rather than the `ImmutableMultimap` specified in the `ImmutableMultimap` class.

        Since
        - 11.0
        """
        ...


    def removeAll(self, key: "Object") -> "ImmutableList"["V"]:
        """
        Guaranteed to throw an exception and leave the multimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> "ImmutableList"["V"]:
        """
        Guaranteed to throw an exception and leave the multimap unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    class Builder(Builder):
        """
        A builder for creating immutable `ListMultimap` instances, especially `public
        static final` multimaps ("constant multimaps"). Example:
        
        ````static final Multimap<String, Integer> STRING_TO_INTEGER_MULTIMAP =
            new ImmutableListMultimap.Builder<String, Integer>()
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
            Creates a new builder. The returned builder is equivalent to the builder generated by ImmutableListMultimap.builder.
            """
            ...


        def expectedValuesPerKey(self, expectedValuesPerKey: int) -> "Builder"["K", "V"]:
            """
            Since
            - 33.3.0
            """
            ...


        def put(self, key: "K", value: "V") -> "Builder"["K", "V"]:
            ...


        def put(self, entry: "Entry"["K", "V"]) -> "Builder"["K", "V"]:
            """
            Since
            - 11.0
            """
            ...


        def putAll(self, entries: Iterable["Entry"["K", "V"]]) -> "Builder"["K", "V"]:
            """
            Since
            - 19.0
            """
            ...


        def putAll(self, key: "K", values: Iterable["V"]) -> "Builder"["K", "V"]:
            ...


        def putAll(self, key: "K", *values: Tuple["V", ...]) -> "Builder"["K", "V"]:
            ...


        def putAll(self, multimap: "Multimap"["K", "V"]) -> "Builder"["K", "V"]:
            ...


        def orderKeysBy(self, keyComparator: "Comparator"["K"]) -> "Builder"["K", "V"]:
            """
            Since
            - 8.0
            """
            ...


        def orderValuesBy(self, valueComparator: "Comparator"["V"]) -> "Builder"["K", "V"]:
            """
            Since
            - 8.0
            """
            ...


        def build(self) -> "ImmutableListMultimap"["K", "V"]:
            """
            Returns a newly-created immutable list multimap.
            """
            ...
