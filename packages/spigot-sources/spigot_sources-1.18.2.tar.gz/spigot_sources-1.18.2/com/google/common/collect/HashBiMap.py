"""
Python module generated from Java source file com.google.common.collect.HashBiMap

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Objects
from com.google.common.collect import *
from com.google.common.collect.Maps import IteratorBasedAbstractMap
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import RetainedWith
from com.google.j2objc.annotations import Weak
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util import Arrays
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util import NoSuchElementException
from java.util.function import BiConsumer
from java.util.function import BiFunction
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class HashBiMap(IteratorBasedAbstractMap, BiMap, Serializable):
    """
    A BiMap backed by two hash tables. This implementation allows null keys and values. A
    `HashBiMap` and its inverse are both serializable.
    
    This implementation guarantees insertion-based iteration order of its keys.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#bimap"> `BiMap` </a>.

    Author(s)
    - Mike Bostock

    Since
    - 2.0
    """

    @staticmethod
    def create() -> "HashBiMap"["K", "V"]:
        """
        Returns a new, empty `HashBiMap` with the default initial capacity (16).
        """
        ...


    @staticmethod
    def create(expectedSize: int) -> "HashBiMap"["K", "V"]:
        """
        Constructs a new, empty bimap with the specified expected size.

        Arguments
        - expectedSize: the expected number of entries

        Raises
        - IllegalArgumentException: if the specified expected size is negative
        """
        ...


    @staticmethod
    def create(map: dict["K", "V"]) -> "HashBiMap"["K", "V"]:
        """
        Constructs a new bimap containing initial values from `map`. The bimap is created with an
        initial capacity sufficient to hold the mappings in the specified map.
        """
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        """
        Returns `True` if this BiMap contains an entry whose value is equal to `value` (or,
        equivalently, if this inverse view contains a key that is equal to `value`).
        
        Due to the property that values in a BiMap are unique, this will tend to execute in
        faster-than-linear time.

        Arguments
        - value: the object to search for in the values of this BiMap

        Returns
        - True if a mapping exists from a key to the specified value
        """
        ...


    def get(self, key: "Object") -> "V":
        ...


    def put(self, key: "K", value: "V") -> "V":
        ...


    def forcePut(self, key: "K", value: "V") -> "V":
        ...


    def remove(self, key: "Object") -> "V":
        ...


    def clear(self) -> None:
        ...


    def size(self) -> int:
        ...


    def keySet(self) -> set["K"]:
        ...


    def values(self) -> set["V"]:
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def replaceAll(self, function: "BiFunction"["K", "V", "V"]) -> None:
        ...


    def inverse(self) -> "BiMap"["V", "K"]:
        ...
