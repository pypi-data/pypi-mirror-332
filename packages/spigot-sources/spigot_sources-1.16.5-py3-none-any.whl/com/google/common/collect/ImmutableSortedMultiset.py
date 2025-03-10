"""
Python module generated from Java source file com.google.common.collect.ImmutableSortedMultiset

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from java.io import Serializable
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util.function import Function
from java.util.function import ToIntFunction
from java.util.stream import Collector
from typing import Any, Callable, Iterable, Tuple


class ImmutableSortedMultiset(ImmutableSortedMultisetFauxverideShim, SortedMultiset):
    """
    A SortedMultiset whose contents will never change, with many other important properties
    detailed at ImmutableCollection.
    
    **Warning:** as with any sorted collection, you are strongly advised not to use a Comparator or Comparable type whose comparison behavior is *inconsistent with
    equals*. That is, `a.compareTo(b)` or `comparator.compare(a, b)` should equal zero
    *if and only if* `a.equals(b)`. If this advice is not followed, the resulting
    collection will not correctly obey its specification.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/ImmutableCollectionsExplained">
    immutable collections</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 12.0
    """

    @staticmethod
    def toImmutableSortedMultiset(comparator: "Comparator"["E"]) -> "Collector"["E", Any, "ImmutableSortedMultiset"["E"]]:
        """
        Returns a `Collector` that accumulates the input elements into a new
        `ImmutableMultiset`.  Elements are sorted by the specified comparator.
        
        **Warning:** `comparator` should be *consistent with `equals`* as explained in the Comparator documentation.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableSortedMultiset"["E"]:
        """
        Returns the empty immutable sorted multiset.
        """
        ...


    @staticmethod
    def of(element: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing a single element.
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by their natural
        ordering.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by their natural
        ordering.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by their natural
        ordering.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by their natural
        ordering.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", *remaining: Tuple["E", ...]) -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by their natural
        ordering.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def copyOf(elements: list["E"]) -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by their natural
        ordering.

        Raises
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(elements: Iterable["E"]) -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by their natural
        ordering. To create a copy of a `SortedMultiset` that preserves the
        comparator, call .copyOfSorted instead. This method iterates over `elements` at
        most once.
        
        Note that if `s` is a `Multiset<String>`, then `ImmutableSortedMultiset.copyOf(s)` returns an `ImmutableSortedMultiset<String>`
        containing each of the strings in `s`, while `ImmutableSortedMultiset.of(s)`
        returns an `ImmutableSortedMultiset<Multiset<String>>` containing one element (the given
        multiset itself).
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.
        
        This method is not type-safe, as it may be called on elements that are not mutually
        comparable.

        Raises
        - ClassCastException: if the elements are not mutually comparable
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(elements: Iterator["E"]) -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by their natural
        ordering.
        
        This method is not type-safe, as it may be called on elements that are not mutually
        comparable.

        Raises
        - ClassCastException: if the elements are not mutually comparable
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(comparator: "Comparator"["E"], elements: Iterator["E"]) -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by the given `Comparator`.

        Raises
        - NullPointerException: if `comparator` or any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(comparator: "Comparator"["E"], elements: Iterable["E"]) -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the given elements sorted by the given `Comparator`. This method iterates over `elements` at most once.
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.

        Raises
        - NullPointerException: if `comparator` or any of `elements` is null
        """
        ...


    @staticmethod
    def copyOfSorted(sortedMultiset: "SortedMultiset"["E"]) -> "ImmutableSortedMultiset"["E"]:
        """
        Returns an immutable sorted multiset containing the elements of a sorted multiset, sorted by
        the same `Comparator`. That behavior differs from .copyOf(Iterable), which
        always uses the natural ordering of the elements.
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.
        
        This method is safe to use even when `sortedMultiset` is a synchronized or concurrent
        collection that is currently being modified by another thread.

        Raises
        - NullPointerException: if `sortedMultiset` or any of its elements is null
        """
        ...


    def comparator(self) -> "Comparator"["E"]:
        ...


    def elementSet(self) -> "ImmutableSortedSet"["E"]:
        ...


    def descendingMultiset(self) -> "ImmutableSortedMultiset"["E"]:
        ...


    def pollFirstEntry(self) -> "Entry"["E"]:
        """
        
        
        This implementation is guaranteed to throw an UnsupportedOperationException.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def pollLastEntry(self) -> "Entry"["E"]:
        """
        
        
        This implementation is guaranteed to throw an UnsupportedOperationException.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def headMultiset(self, upperBound: "E", boundType: "BoundType") -> "ImmutableSortedMultiset"["E"]:
        ...


    def subMultiset(self, lowerBound: "E", lowerBoundType: "BoundType", upperBound: "E", upperBoundType: "BoundType") -> "ImmutableSortedMultiset"["E"]:
        ...


    def tailMultiset(self, lowerBound: "E", boundType: "BoundType") -> "ImmutableSortedMultiset"["E"]:
        ...


    @staticmethod
    def orderedBy(comparator: "Comparator"["E"]) -> "Builder"["E"]:
        """
        Returns a builder that creates immutable sorted multisets with an explicit comparator. If the
        comparator has a more general type than the set being generated, such as creating a `SortedMultiset<Integer>` with a `Comparator<Number>`, use the Builder
        constructor instead.

        Raises
        - NullPointerException: if `comparator` is null
        """
        ...


    @staticmethod
    def reverseOrder() -> "Builder"["E"]:
        """
        Returns a builder that creates immutable sorted multisets whose elements are ordered by the
        reverse of their natural ordering.
        
        Note: the type parameter `E` extends `Comparable<?>` rather than `Comparable<? super E>` as a workaround for javac <a
        href="http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6468354">bug 6468354</a>.
        """
        ...


    @staticmethod
    def naturalOrder() -> "Builder"["E"]:
        """
        Returns a builder that creates immutable sorted multisets whose elements are ordered by their
        natural ordering. The sorted multisets use Ordering.natural() as the comparator. This
        method provides more type-safety than .builder, as it can be called only for classes
        that implement Comparable.
        
        Note: the type parameter `E` extends `Comparable<?>` rather than `Comparable<? super E>` as a workaround for javac <a
        href="http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6468354">bug 6468354</a>.
        """
        ...


    class Builder(Builder):
        """
        A builder for creating immutable multiset instances, especially `public static final`
        multisets ("constant multisets"). Example:
        
        ``` `public static final ImmutableSortedMultiset<Bean> BEANS =
              new ImmutableSortedMultiset.Builder<Bean>(colorComparator())
                  .addCopies(Bean.COCOA, 4)
                  .addCopies(Bean.GARDEN, 6)
                  .addCopies(Bean.RED, 8)
                  .addCopies(Bean.BLACK_EYED, 10)
                  .build();````
        
        Builder instances can be reused; it is safe to call .build multiple times to build
        multiple multisets in series.

        Since
        - 12.0
        """

        def __init__(self, comparator: "Comparator"["E"]):
            """
            Creates a new builder. The returned builder is equivalent to the builder generated by
            ImmutableSortedMultiset.orderedBy(Comparator).
            """
            ...


        def add(self, element: "E") -> "Builder"["E"]:
            """
            Adds `element` to the `ImmutableSortedMultiset`.

            Arguments
            - element: the element to add

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `element` is null
            """
            ...


        def addCopies(self, element: "E", occurrences: int) -> "Builder"["E"]:
            """
            Adds a number of occurrences of an element to this `ImmutableSortedMultiset`.

            Arguments
            - element: the element to add
            - occurrences: the number of occurrences of the element to add. May be zero, in which
                   case no change will be made.

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `element` is null
            - IllegalArgumentException: if `occurrences` is negative, or if this operation
                    would result in more than Integer.MAX_VALUE occurrences of the element
            """
            ...


        def setCount(self, element: "E", count: int) -> "Builder"["E"]:
            """
            Adds or removes the necessary occurrences of an element such that the element attains the
            desired count.

            Arguments
            - element: the element to add or remove occurrences of
            - count: the desired count of the element in this multiset

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `element` is null
            - IllegalArgumentException: if `count` is negative
            """
            ...


        def add(self, *elements: Tuple["E", ...]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSortedMultiset`.

            Arguments
            - elements: the elements to add

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def addAll(self, elements: Iterable["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSortedMultiset`.

            Arguments
            - elements: the `Iterable` to add to the `ImmutableSortedMultiset`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def addAll(self, elements: Iterator["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSortedMultiset`.

            Arguments
            - elements: the elements to add to the `ImmutableSortedMultiset`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def build(self) -> "ImmutableSortedMultiset"["E"]:
            """
            Returns a newly-created `ImmutableSortedMultiset` based on the contents of the `Builder`.
            """
            ...
