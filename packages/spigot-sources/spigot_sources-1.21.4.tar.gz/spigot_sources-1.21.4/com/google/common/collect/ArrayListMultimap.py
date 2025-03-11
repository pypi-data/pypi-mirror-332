"""
Python module generated from Java source file com.google.common.collect.ArrayListMultimap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ArrayListMultimap(ArrayListMultimapGwtSerializationDependencies):
    """
    Implementation of `Multimap` that uses an `ArrayList` to store the values for a given
    key. A HashMap associates each key with an ArrayList of values.
    
    When iterating through the collections supplied by this class, the ordering of values for a
    given key agrees with the order in which the values were added.
    
    This multimap allows duplicate key-value pairs. After adding a new key-value pair equal to an
    existing key-value pair, the `ArrayListMultimap` will contain entries for both the new
    value and the old value.
    
    Keys and values may be null. All optional multimap methods are supported, and all returned
    views are modifiable.
    
    The lists returned by .get, .removeAll, and .replaceValues all
    implement java.util.RandomAccess.
    
    This class is not threadsafe when any concurrent operations update the multimap. Concurrent
    read operations will work correctly. To allow concurrent update operations, wrap your multimap
    with a call to Multimaps.synchronizedListMultimap.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multimap">`Multimap`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def create() -> "ArrayListMultimap"["K", "V"]:
        """
        Creates a new, empty `ArrayListMultimap` with the default initial capacities.
        
        You may also consider the equivalent `MultimapBuilder.hashKeys().arrayListValues().build()`, which provides more control over the
        underlying data structure.
        """
        ...


    @staticmethod
    def create(expectedKeys: int, expectedValuesPerKey: int) -> "ArrayListMultimap"["K", "V"]:
        """
        Constructs an empty `ArrayListMultimap` with enough capacity to hold the specified
        numbers of keys and values without resizing.
        
        You may also consider the equivalent `MultimapBuilder.hashKeys(expectedKeys).arrayListValues(expectedValuesPerKey).build()`, which
        provides more control over the underlying data structure.

        Arguments
        - expectedKeys: the expected number of distinct keys
        - expectedValuesPerKey: the expected average number of values per key

        Raises
        - IllegalArgumentException: if `expectedKeys` or `expectedValuesPerKey` is
            negative
        """
        ...


    @staticmethod
    def create(multimap: "Multimap"["K", "V"]) -> "ArrayListMultimap"["K", "V"]:
        """
        Constructs an `ArrayListMultimap` with the same mappings as the specified multimap.
        
        You may also consider the equivalent `MultimapBuilder.hashKeys().arrayListValues().build(multimap)`, which provides more control over
        the underlying data structure.

        Arguments
        - multimap: the multimap whose contents are copied to this multimap
        """
        ...


    def trimToSize(self) -> None:
        """
        Reduces the memory used by this `ArrayListMultimap`, if feasible.

        Deprecated
        - For a ListMultimap that automatically trims to size, use ImmutableListMultimap. If you need a mutable collection, remove the `trimToSize`
            call, or switch to a `HashMap<K, ArrayList<V>>`.
        """
        ...
