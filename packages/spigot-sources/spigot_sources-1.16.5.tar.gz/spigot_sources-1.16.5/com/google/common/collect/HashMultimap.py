"""
Python module generated from Java source file com.google.common.collect.HashMultimap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Preconditions
from com.google.common.collect import *
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from typing import Any, Callable, Iterable, Tuple


class HashMultimap(AbstractSetMultimap):
    """
    Implementation of Multimap using hash tables.
    
    The multimap does not store duplicate key-value pairs. Adding a new
    key-value pair equal to an existing key-value pair has no effect.
    
    Keys and values may be null. All optional multimap methods are supported,
    and all returned views are modifiable.
    
    This class is not threadsafe when any concurrent operations update the
    multimap. Concurrent read operations will work correctly. To allow concurrent
    update operations, wrap your multimap with a call to Multimaps.synchronizedSetMultimap.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def create() -> "HashMultimap"["K", "V"]:
        """
        Creates a new, empty `HashMultimap` with the default initial capacities.
        
        This method will soon be deprecated in favor of `MultimapBuilder.hashKeys().hashSetValues().build()`.
        """
        ...


    @staticmethod
    def create(expectedKeys: int, expectedValuesPerKey: int) -> "HashMultimap"["K", "V"]:
        """
        Constructs an empty `HashMultimap` with enough capacity to hold the specified numbers of
        keys and values without rehashing.
        
        This method will soon be deprecated in favor of `MultimapBuilder.hashKeys(expectedKeys).hashSetValues(expectedValuesPerKey).build()`.

        Arguments
        - expectedKeys: the expected number of distinct keys
        - expectedValuesPerKey: the expected average number of values per key

        Raises
        - IllegalArgumentException: if `expectedKeys` or `expectedValuesPerKey` is
            negative
        """
        ...


    @staticmethod
    def create(multimap: "Multimap"["K", "V"]) -> "HashMultimap"["K", "V"]:
        """
        Constructs a `HashMultimap` with the same mappings as the specified multimap. If a
        key-value mapping appears multiple times in the input multimap, it only appears once in the
        constructed multimap.
        
        This method will soon be deprecated in favor of `MultimapBuilder.hashKeys().hashSetValues().build(multimap)`.

        Arguments
        - multimap: the multimap whose contents are copied to this multimap
        """
        ...
