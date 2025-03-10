"""
Python module generated from Java source file com.google.common.collect.CompactHashSet

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Objects
from com.google.common.base import Preconditions
from com.google.common.collect import *
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util import AbstractSet
from java.util import Arrays
from java.util import Collections
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util import LinkedHashSet
from java.util import NoSuchElementException
from java.util import Spliterator
from java.util.function import Consumer
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CompactHashSet(AbstractSet, Serializable):
    """
    CompactHashSet is an implementation of a Set. All optional operations (adding and removing) are
    supported. The elements can be any objects.
    
    `contains(x)`, `add(x)` and `remove(x)`, are all (expected and amortized)
    constant time operations. Expected in the hashtable sense (depends on the hash function doing a
    good job of distributing the elements to the buckets to a distribution not far from uniform), and
    amortized since some operations can trigger a hash table resize.
    
    Unlike `java.util.HashSet`, iteration is only proportional to the actual `size()`,
    which is optimal, and *not* the size of the internal hashtable, which could be much larger
    than `size()`. Furthermore, this structure only depends on a fixed number of arrays; `add(x)` operations *do not* create objects for the garbage collector to deal with, and for
    every element added, the garbage collector will have to traverse `1.5` references on
    average, in the marking phase, not `5.0` as in `java.util.HashSet`.
    
    If there are no removals, then .iterator iteration order is the same as insertion
    order. Any removal invalidates any ordering guarantees.
    
    This class should not be assumed to be universally superior to `java.util.HashSet`.
    Generally speaking, this class reduces object allocation and memory consumption at the price of
    moderately increased constant factors of CPU. Only use this class when there is a specific reason
    to prioritize memory over CPU.

    Author(s)
    - Jon Noack
    """

    @staticmethod
    def create() -> "CompactHashSet"["E"]:
        """
        Creates an empty `CompactHashSet` instance.
        """
        ...


    @staticmethod
    def create(collection: Iterable["E"]) -> "CompactHashSet"["E"]:
        """
        Creates a *mutable* `CompactHashSet` instance containing the elements of the given
        collection in unspecified order.

        Arguments
        - collection: the elements that the set should contain

        Returns
        - a new `CompactHashSet` containing those elements (minus duplicates)
        """
        ...


    @staticmethod
    def create(*elements: Tuple["E", ...]) -> "CompactHashSet"["E"]:
        """
        Creates a *mutable* `CompactHashSet` instance containing the given elements in
        unspecified order.

        Arguments
        - elements: the elements that the set should contain

        Returns
        - a new `CompactHashSet` containing those elements (minus duplicates)
        """
        ...


    @staticmethod
    def createWithExpectedSize(expectedSize: int) -> "CompactHashSet"["E"]:
        """
        Creates a `CompactHashSet` instance, with a high enough "initial capacity" that it
        *should* hold `expectedSize` elements without growth.

        Arguments
        - expectedSize: the number of elements you expect to add to the returned set

        Returns
        - a new, empty `CompactHashSet` with enough capacity to hold `expectedSize`
            elements without resizing

        Raises
        - IllegalArgumentException: if `expectedSize` is negative
        """
        ...


    def add(self, object: "E") -> bool:
        ...


    def contains(self, object: "Object") -> bool:
        ...


    def remove(self, object: "Object") -> bool:
        ...


    def iterator(self) -> Iterator["E"]:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def forEach(self, action: "Consumer"["E"]) -> None:
        ...


    def size(self) -> int:
        ...


    def isEmpty(self) -> bool:
        ...


    def toArray(self) -> list["Object"]:
        ...


    def toArray(self, a: list["T"]) -> list["T"]:
        ...


    def trimToSize(self) -> None:
        """
        Ensures that this `CompactHashSet` has the smallest representation in memory, given its
        current size.
        """
        ...


    def clear(self) -> None:
        ...
