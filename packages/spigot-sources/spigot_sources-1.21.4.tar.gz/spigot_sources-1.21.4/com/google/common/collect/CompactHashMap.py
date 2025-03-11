"""
Python module generated from Java source file com.google.common.collect.CompactHashMap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Objects
from com.google.common.base import Preconditions
from com.google.common.collect import *
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import WeakOuter
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util import Arrays
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Spliterator
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import Consumer
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CompactHashMap(AbstractMap, Serializable):
    """
    CompactHashMap is an implementation of a Map. All optional operations (put and remove) are
    supported. Null keys and values are supported.
    
    `containsKey(k)`, `put(k, v)` and `remove(k)` are all (expected and
    amortized) constant time operations. Expected in the hashtable sense (depends on the hash
    function doing a good job of distributing the elements to the buckets to a distribution not far
    from uniform), and amortized since some operations can trigger a hash table resize.
    
    Unlike `java.util.HashMap`, iteration is only proportional to the actual `size()`,
    which is optimal, and *not* the size of the internal hashtable, which could be much larger
    than `size()`. Furthermore, this structure places significantly reduced load on the garbage
    collector by only using a constant number of internal objects.
    
    If there are no removals, then iteration order for the .entrySet, .keySet, and
    .values views is the same as insertion order. Any removal invalidates any ordering
    guarantees.
    
    This class should not be assumed to be universally superior to `java.util.HashMap`.
    Generally speaking, this class reduces object allocation and memory consumption at the price of
    moderately increased constant factors of CPU. Only use this class when there is a specific reason
    to prioritize memory over CPU.

    Author(s)
    - Jon Noack
    """

    @staticmethod
    def create() -> "CompactHashMap"["K", "V"]:
        """
        Creates an empty `CompactHashMap` instance.
        """
        ...


    @staticmethod
    def createWithExpectedSize(expectedSize: int) -> "CompactHashMap"["K", "V"]:
        """
        Creates a `CompactHashMap` instance, with a high enough "initial capacity" that it
        *should* hold `expectedSize` elements without growth.

        Arguments
        - expectedSize: the number of elements you expect to add to the returned set

        Returns
        - a new, empty `CompactHashMap` with enough capacity to hold `expectedSize`
            elements without resizing

        Raises
        - IllegalArgumentException: if `expectedSize` is negative
        """
        ...


    def put(self, key: "K", value: "V") -> "V":
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def get(self, key: "Object") -> "V":
        ...


    def remove(self, key: "Object") -> "V":
        ...


    def replaceAll(self, function: "BiFunction"["K", "V", "V"]) -> None:
        ...


    def keySet(self) -> set["K"]:
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def entrySet(self) -> set["Entry"["K", "V"]]:
        ...


    def size(self) -> int:
        ...


    def isEmpty(self) -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def values(self) -> Iterable["V"]:
        ...


    def trimToSize(self) -> None:
        """
        Ensures that this `CompactHashMap` has the smallest representation in memory, given its
        current size.
        """
        ...


    def clear(self) -> None:
        ...
