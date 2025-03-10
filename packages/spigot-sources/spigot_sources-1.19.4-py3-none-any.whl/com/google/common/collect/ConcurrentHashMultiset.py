"""
Python module generated from Java source file com.google.common.collect.ConcurrentHashMultiset

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.common.collect.Serialization import FieldSetter
from com.google.common.math import IntMath
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import WeakOuter
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util import Iterator
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from java.util.concurrent.atomic import AtomicInteger
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ConcurrentHashMultiset(AbstractMultiset, Serializable):
    """
    A multiset that supports concurrent modifications and that provides atomic versions of most
    `Multiset` operations (exceptions where noted). Null elements are not supported.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multiset">`Multiset`</a>.

    Author(s)
    - mike nonemacher

    Since
    - 2.0
    """

    @staticmethod
    def create() -> "ConcurrentHashMultiset"["E"]:
        """
        Creates a new, empty `ConcurrentHashMultiset` using the default initial capacity, load
        factor, and concurrency settings.
        """
        ...


    @staticmethod
    def create(elements: Iterable["E"]) -> "ConcurrentHashMultiset"["E"]:
        """
        Creates a new `ConcurrentHashMultiset` containing the specified elements, using the
        default initial capacity, load factor, and concurrency settings.
        
        This implementation is highly efficient when `elements` is itself a Multiset.

        Arguments
        - elements: the elements that the multiset should contain
        """
        ...


    @staticmethod
    def create(countMap: "ConcurrentMap"["E", "AtomicInteger"]) -> "ConcurrentHashMultiset"["E"]:
        """
        Creates a new, empty `ConcurrentHashMultiset` using `countMap` as the internal
        backing map.
        
        This instance will assume ownership of `countMap`, and other code should not maintain
        references to the map or modify it in any way.
        
        The returned multiset is serializable if the input map is.

        Arguments
        - countMap: backing map for storing the elements in the multiset and their counts. It must
            be empty.

        Raises
        - IllegalArgumentException: if `countMap` is not empty

        Since
        - 20.0
        """
        ...


    def count(self, element: "Object") -> int:
        """
        Returns the number of occurrences of `element` in this multiset.

        Arguments
        - element: the element to look for

        Returns
        - the nonnegative number of occurrences of the element
        """
        ...


    def size(self) -> int:
        """
        
        
        If the data in the multiset is modified by any other threads during this method, it is
        undefined which (if any) of these modifications will be reflected in the result.
        """
        ...


    def toArray(self) -> list["Object"]:
        ...


    def toArray(self, array: list["T"]) -> list["T"]:
        ...


    def add(self, element: "E", occurrences: int) -> int:
        """
        Adds a number of occurrences of the specified element to this multiset.

        Arguments
        - element: the element to add
        - occurrences: the number of occurrences to add

        Returns
        - the previous count of the element before the operation; possibly zero

        Raises
        - IllegalArgumentException: if `occurrences` is negative, or if the resulting amount
            would exceed Integer.MAX_VALUE
        """
        ...


    def remove(self, element: "Object", occurrences: int) -> int:
        ...


    def removeExactly(self, element: "Object", occurrences: int) -> bool:
        """
        Removes exactly the specified number of occurrences of `element`, or makes no change if
        this is not possible.
        
        This method, in contrast to .remove(Object, int), has no effect when the element
        count is smaller than `occurrences`.

        Arguments
        - element: the element to remove
        - occurrences: the number of occurrences of `element` to remove

        Returns
        - `True` if the removal was possible (including if `occurrences` is zero)

        Raises
        - IllegalArgumentException: if `occurrences` is negative
        """
        ...


    def setCount(self, element: "E", count: int) -> int:
        """
        Adds or removes occurrences of `element` such that the .count of the element
        becomes `count`.

        Returns
        - the count of `element` in the multiset before this call

        Raises
        - IllegalArgumentException: if `count` is negative
        """
        ...


    def setCount(self, element: "E", expectedOldCount: int, newCount: int) -> bool:
        """
        Sets the number of occurrences of `element` to `newCount`, but only if the count is
        currently `expectedOldCount`. If `element` does not appear in the multiset exactly
        `expectedOldCount` times, no changes will be made.

        Returns
        - `True` if the change was successful. This usually indicates that the multiset has
            been modified, but not always: in the case that `expectedOldCount == newCount`, the
            method will return `True` if the condition was met.

        Raises
        - IllegalArgumentException: if `expectedOldCount` or `newCount` is negative
        """
        ...


    def createEntrySet(self) -> set["Multiset.Entry"["E"]]:
        """
        Deprecated
        - Internal method, use .entrySet().
        """
        ...


    def isEmpty(self) -> bool:
        ...


    def iterator(self) -> Iterator["E"]:
        ...


    def clear(self) -> None:
        ...
