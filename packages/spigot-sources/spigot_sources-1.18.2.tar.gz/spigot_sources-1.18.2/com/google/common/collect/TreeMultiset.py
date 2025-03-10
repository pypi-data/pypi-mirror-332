"""
Python module generated from Java source file com.google.common.collect.TreeMultiset

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import MoreObjects
from com.google.common.collect import *
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util import Comparator
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util import NoSuchElementException
from java.util.function import ObjIntConsumer
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class TreeMultiset(AbstractSortedMultiset, Serializable):
    """
    A multiset which maintains the ordering of its elements, according to either their natural order
    or an explicit Comparator. In all cases, this implementation uses Comparable.compareTo or Comparator.compare instead of Object.equals to determine
    equivalence of instances.
    
    **Warning:** The comparison must be *consistent with equals* as explained by the
    Comparable class specification. Otherwise, the resulting multiset will violate the java.util.Collection contract, which is specified in terms of Object.equals.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multiset"> `Multiset`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def create() -> "TreeMultiset"["E"]:
        """
        Creates a new, empty multiset, sorted according to the elements' natural order. All elements
        inserted into the multiset must implement the `Comparable` interface. Furthermore, all
        such elements must be *mutually comparable*: `e1.compareTo(e2)` must not throw a
        `ClassCastException` for any elements `e1` and `e2` in the multiset. If the
        user attempts to add an element to the multiset that violates this constraint (for example, the
        user attempts to add a string element to a set whose elements are integers), the `add(Object)` call will throw a `ClassCastException`.
        
        The type specification is `<E extends Comparable>`, instead of the more specific
        `<E extends Comparable<? super E>>`, to support classes defined without generics.
        """
        ...


    @staticmethod
    def create(comparator: "Comparator"["E"]) -> "TreeMultiset"["E"]:
        """
        Creates a new, empty multiset, sorted according to the specified comparator. All elements
        inserted into the multiset must be *mutually comparable* by the specified comparator:
        `comparator.compare(e1, e2)` must not throw a `ClassCastException` for any elements
        `e1` and `e2` in the multiset. If the user attempts to add an element to the
        multiset that violates this constraint, the `add(Object)` call will throw a `ClassCastException`.

        Arguments
        - comparator: the comparator that will be used to sort this multiset. A null value
            indicates that the elements' *natural ordering* should be used.
        """
        ...


    @staticmethod
    def create(elements: Iterable["E"]) -> "TreeMultiset"["E"]:
        """
        Creates an empty multiset containing the given initial elements, sorted according to the
        elements' natural order.
        
        This implementation is highly efficient when `elements` is itself a Multiset.
        
        The type specification is `<E extends Comparable>`, instead of the more specific
        `<E extends Comparable<? super E>>`, to support classes defined without generics.
        """
        ...


    def size(self) -> int:
        ...


    def count(self, element: "Object") -> int:
        ...


    def add(self, element: "E", occurrences: int) -> int:
        ...


    def remove(self, element: "Object", occurrences: int) -> int:
        ...


    def setCount(self, element: "E", count: int) -> int:
        ...


    def setCount(self, element: "E", oldCount: int, newCount: int) -> bool:
        ...


    def clear(self) -> None:
        ...


    def forEachEntry(self, action: "ObjIntConsumer"["E"]) -> None:
        ...


    def iterator(self) -> Iterator["E"]:
        ...


    def headMultiset(self, upperBound: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        ...


    def tailMultiset(self, lowerBound: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        ...
