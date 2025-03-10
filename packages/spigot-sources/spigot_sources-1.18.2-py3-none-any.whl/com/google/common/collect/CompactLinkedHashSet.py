"""
Python module generated from Java source file com.google.common.collect.CompactLinkedHashSet

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Arrays
from java.util import Collections
from java.util import Spliterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CompactLinkedHashSet(CompactHashSet):
    """
    CompactLinkedHashSet is an implementation of a Set, which a predictable iteration order that
    matches the insertion order. All optional operations (adding and removing) are supported. All
    elements, including `null`, are permitted.
    
    `contains(x)`, `add(x)` and `remove(x)`, are all (expected and amortized)
    constant time operations. Expected in the hashtable sense (depends on the hash function doing a
    good job of distributing the elements to the buckets to a distribution not far from uniform), and
    amortized since some operations can trigger a hash table resize.
    
    This implementation consumes significantly less memory than `java.util.LinkedHashSet` or
    even `java.util.HashSet`, and places considerably less load on the garbage collector. Like
    `java.util.LinkedHashSet`, it offers insertion-order iteration, with identical behavior.
    
    This class should not be assumed to be universally superior to `java.util.LinkedHashSet`. Generally speaking, this class reduces object allocation and memory
    consumption at the price of moderately increased constant factors of CPU. Only use this class
    when there is a specific reason to prioritize memory over CPU.

    Author(s)
    - Louis Wasserman
    """

    @staticmethod
    def create() -> "CompactLinkedHashSet"["E"]:
        """
        Creates an empty `CompactLinkedHashSet` instance.
        """
        ...


    @staticmethod
    def create(collection: Iterable["E"]) -> "CompactLinkedHashSet"["E"]:
        """
        Creates a *mutable* `CompactLinkedHashSet` instance containing the elements of the
        given collection in the order returned by the collection's iterator.

        Arguments
        - collection: the elements that the set should contain

        Returns
        - a new `CompactLinkedHashSet` containing those elements (minus duplicates)
        """
        ...


    @staticmethod
    def create(*elements: Tuple["E", ...]) -> "CompactLinkedHashSet"["E"]:
        """
        Creates a `CompactLinkedHashSet` instance containing the given elements in unspecified
        order.

        Arguments
        - elements: the elements that the set should contain

        Returns
        - a new `CompactLinkedHashSet` containing those elements (minus duplicates)
        """
        ...


    @staticmethod
    def createWithExpectedSize(expectedSize: int) -> "CompactLinkedHashSet"["E"]:
        """
        Creates a `CompactLinkedHashSet` instance, with a high enough "initial capacity" that it
        *should* hold `expectedSize` elements without rebuilding internal data structures.

        Arguments
        - expectedSize: the number of elements you expect to add to the returned set

        Returns
        - a new, empty `CompactLinkedHashSet` with enough capacity to hold `expectedSize` elements without resizing

        Raises
        - IllegalArgumentException: if `expectedSize` is negative
        """
        ...


    def toArray(self) -> list["Object"]:
        ...


    def toArray(self, a: list["T"]) -> list["T"]:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def clear(self) -> None:
        ...
