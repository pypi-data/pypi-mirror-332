"""
Python module generated from Java source file com.google.common.collect.ImmutableSortedSet

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from com.google.errorprone.annotations.concurrent import LazyInit
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util import NavigableSet
from java.util import SortedSet
from java.util import Spliterator
from java.util.function import Consumer
from java.util.stream import Collector
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableSortedSet(ImmutableSortedSetFauxverideShim, NavigableSet, SortedIterable):

    @staticmethod
    def toImmutableSortedSet(comparator: "Comparator"["E"]) -> "Collector"["E", Any, "ImmutableSortedSet"["E"]]:
        """
        Returns a `Collector` that accumulates the input elements into a new `ImmutableSortedSet`, ordered by the specified comparator.
        
        If the elements contain duplicates (according to the comparator), only the first duplicate
        in encounter order will appear in the result.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableSortedSet"["E"]:
        """
        Returns the empty immutable sorted set.
        
        **Performance note:** the instance returned is a singleton.
        """
        ...


    @staticmethod
    def of(element: "E") -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing a single element.
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E") -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by their natural ordering.
        When multiple elements are equivalent according to Comparable.compareTo, only the first
        one specified is included.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E") -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by their natural ordering.
        When multiple elements are equivalent according to Comparable.compareTo, only the first
        one specified is included.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E") -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by their natural ordering.
        When multiple elements are equivalent according to Comparable.compareTo, only the first
        one specified is included.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E") -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by their natural ordering.
        When multiple elements are equivalent according to Comparable.compareTo, only the first
        one specified is included.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", *remaining: Tuple["E", ...]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by their natural ordering.
        When multiple elements are equivalent according to Comparable.compareTo, only the first
        one specified is included.

        Raises
        - NullPointerException: if any element is null

        Since
        - 3.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def copyOf(elements: list["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by their natural ordering.
        When multiple elements are equivalent according to Comparable.compareTo, only the first
        one specified is included.

        Raises
        - NullPointerException: if any of `elements` is null

        Since
        - 3.0
        """
        ...


    @staticmethod
    def copyOf(elements: Iterable["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by their natural ordering.
        When multiple elements are equivalent according to `compareTo()`, only the first one
        specified is included. To create a copy of a `SortedSet` that preserves the comparator,
        call .copyOfSorted instead. This method iterates over `elements` at most once.
        
        Note that if `s` is a `Set<String>`, then `ImmutableSortedSet.copyOf(s)`
        returns an `ImmutableSortedSet<String>` containing each of the strings in `s`,
        while `ImmutableSortedSet.of(s)` returns an `ImmutableSortedSet<Set<String>>`
        containing one element (the given set itself).
        
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
    def copyOf(elements: Iterable["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by their natural ordering.
        When multiple elements are equivalent according to `compareTo()`, only the first one
        specified is included. To create a copy of a `SortedSet` that preserves the comparator,
        call .copyOfSorted instead. This method iterates over `elements` at most once.
        
        Note that if `s` is a `Set<String>`, then `ImmutableSortedSet.copyOf(s)`
        returns an `ImmutableSortedSet<String>` containing each of the strings in `s`,
        while `ImmutableSortedSet.of(s)` returns an `ImmutableSortedSet<Set<String>>`
        containing one element (the given set itself).
        
        **Note:** Despite what the method name suggests, if `elements` is an `ImmutableSortedSet`, it may be returned instead of a copy.
        
        This method is not type-safe, as it may be called on elements that are not mutually
        comparable.
        
        This method is safe to use even when `elements` is a synchronized or concurrent
        collection that is currently being modified by another thread.

        Raises
        - ClassCastException: if the elements are not mutually comparable
        - NullPointerException: if any of `elements` is null

        Since
        - 7.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def copyOf(elements: Iterator["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by their natural ordering.
        When multiple elements are equivalent according to `compareTo()`, only the first one
        specified is included.
        
        This method is not type-safe, as it may be called on elements that are not mutually
        comparable.

        Raises
        - ClassCastException: if the elements are not mutually comparable
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(comparator: "Comparator"["E"], elements: Iterator["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by the given `Comparator`. When multiple elements are equivalent according to `compareTo()`, only the
        first one specified is included.

        Raises
        - NullPointerException: if `comparator` or any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(comparator: "Comparator"["E"], elements: Iterable["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by the given `Comparator`. When multiple elements are equivalent according to `compare()`, only the
        first one specified is included. This method iterates over `elements` at most once.
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.

        Raises
        - NullPointerException: if `comparator` or any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(comparator: "Comparator"["E"], elements: Iterable["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the given elements sorted by the given `Comparator`. When multiple elements are equivalent according to `compareTo()`, only the
        first one specified is included.
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.
        
        This method is safe to use even when `elements` is a synchronized or concurrent
        collection that is currently being modified by another thread.

        Raises
        - NullPointerException: if `comparator` or any of `elements` is null

        Since
        - 7.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def copyOfSorted(sortedSet: "SortedSet"["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Returns an immutable sorted set containing the elements of a sorted set, sorted by the same
        `Comparator`. That behavior differs from .copyOf(Iterable), which always uses the
        natural ordering of the elements.
        
        Despite the method name, this method attempts to avoid actually copying the data when it is
        safe to do so. The exact circumstances under which a copy will or will not be performed are
        undocumented and subject to change.
        
        This method is safe to use even when `sortedSet` is a synchronized or concurrent
        collection that is currently being modified by another thread.

        Raises
        - NullPointerException: if `sortedSet` or any of its elements is null
        """
        ...


    @staticmethod
    def orderedBy(comparator: "Comparator"["E"]) -> "Builder"["E"]:
        """
        Returns a builder that creates immutable sorted sets with an explicit comparator. If the
        comparator has a more general type than the set being generated, such as creating a `SortedSet<Integer>` with a `Comparator<Number>`, use the Builder constructor
        instead.

        Raises
        - NullPointerException: if `comparator` is null
        """
        ...


    @staticmethod
    def reverseOrder() -> "Builder"["E"]:
        """
        Returns a builder that creates immutable sorted sets whose elements are ordered by the reverse
        of their natural ordering.
        """
        ...


    @staticmethod
    def naturalOrder() -> "Builder"["E"]:
        """
        Returns a builder that creates immutable sorted sets whose elements are ordered by their
        natural ordering. The sorted sets use Ordering.natural() as the comparator. This method
        provides more type-safety than .builder, as it can be called only for classes that
        implement Comparable.
        """
        ...


    def comparator(self) -> "Comparator"["E"]:
        """
        Returns the comparator that orders the elements, which is Ordering.natural() when the
        natural ordering of the elements is used. Note that its behavior is not consistent with SortedSet.comparator(), which returns `null` to indicate natural ordering.
        """
        ...


    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def headSet(self, toElement: "E") -> "ImmutableSortedSet"["E"]:
        """
        
        
        This method returns a serializable `ImmutableSortedSet`.
        
        The SortedSet.headSet documentation states that a subset of a subset throws an
        IllegalArgumentException if passed a `toElement` greater than an earlier `toElement`. However, this method doesn't throw an exception in that situation, but instead
        keeps the original `toElement`.
        """
        ...


    def headSet(self, toElement: "E", inclusive: bool) -> "ImmutableSortedSet"["E"]:
        """
        Since
        - 12.0
        """
        ...


    def subSet(self, fromElement: "E", toElement: "E") -> "ImmutableSortedSet"["E"]:
        """
        
        
        This method returns a serializable `ImmutableSortedSet`.
        
        The SortedSet.subSet documentation states that a subset of a subset throws an IllegalArgumentException if passed a `fromElement` smaller than an earlier `fromElement`. However, this method doesn't throw an exception in that situation, but instead
        keeps the original `fromElement`. Similarly, this method keeps the original `toElement`, instead of throwing an exception, if passed a `toElement` greater than an
        earlier `toElement`.
        """
        ...


    def subSet(self, fromElement: "E", fromInclusive: bool, toElement: "E", toInclusive: bool) -> "ImmutableSortedSet"["E"]:
        """
        Since
        - 12.0
        """
        ...


    def tailSet(self, fromElement: "E") -> "ImmutableSortedSet"["E"]:
        """
        
        
        This method returns a serializable `ImmutableSortedSet`.
        
        The SortedSet.tailSet documentation states that a subset of a subset throws an
        IllegalArgumentException if passed a `fromElement` smaller than an earlier `fromElement`. However, this method doesn't throw an exception in that situation, but instead
        keeps the original `fromElement`.
        """
        ...


    def tailSet(self, fromElement: "E", inclusive: bool) -> "ImmutableSortedSet"["E"]:
        """
        Since
        - 12.0
        """
        ...


    def lower(self, e: "E") -> "E":
        """
        Since
        - 12.0
        """
        ...


    def floor(self, e: "E") -> "E":
        """
        Since
        - 12.0
        """
        ...


    def ceiling(self, e: "E") -> "E":
        """
        Since
        - 12.0
        """
        ...


    def higher(self, e: "E") -> "E":
        """
        Since
        - 12.0
        """
        ...


    def first(self) -> "E":
        ...


    def last(self) -> "E":
        ...


    def pollFirst(self) -> "E":
        """
        Guaranteed to throw an exception and leave the set unmodified.

        Raises
        - UnsupportedOperationException: always

        Since
        - 12.0

        Deprecated
        - Unsupported operation.
        """
        ...


    def pollLast(self) -> "E":
        """
        Guaranteed to throw an exception and leave the set unmodified.

        Raises
        - UnsupportedOperationException: always

        Since
        - 12.0

        Deprecated
        - Unsupported operation.
        """
        ...


    def descendingSet(self) -> "ImmutableSortedSet"["E"]:
        """
        Since
        - 12.0
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def descendingIterator(self) -> "UnmodifiableIterator"["E"]:
        """
        Since
        - 12.0
        """
        ...


    class Builder(Builder):
        """
        A builder for creating immutable sorted set instances, especially `public static final`
        sets ("constant sets"), with a given comparator. Example:
        
        ````public static final ImmutableSortedSet<Number> LUCKY_NUMBERS =
            new ImmutableSortedSet.Builder<Number>(ODDS_FIRST_COMPARATOR)
                .addAll(SINGLE_DIGIT_PRIMES)
                .add(42)
                .build();````
        
        Builder instances can be reused; it is safe to call .build multiple times to build
        multiple sets in series. Each set is a superset of the set created before it.

        Since
        - 2.0
        """

        def __init__(self, comparator: "Comparator"["E"]):
            """
            Creates a new builder. The returned builder is equivalent to the builder generated by ImmutableSortedSet.orderedBy.
            """
            ...


        def add(self, element: "E") -> "Builder"["E"]:
            """
            Adds `element` to the `ImmutableSortedSet`. If the `ImmutableSortedSet`
            already contains `element`, then `add` has no effect. (only the previously added
            element is retained).

            Arguments
            - element: the element to add

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `element` is null
            """
            ...


        def add(self, *elements: Tuple["E", ...]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSortedSet`, ignoring duplicate
            elements (only the first duplicate element is added).

            Arguments
            - elements: the elements to add

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` contains a null element
            """
            ...


        def addAll(self, elements: Iterable["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSortedSet`, ignoring duplicate
            elements (only the first duplicate element is added).

            Arguments
            - elements: the elements to add to the `ImmutableSortedSet`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` contains a null element
            """
            ...


        def addAll(self, elements: Iterator["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSortedSet`, ignoring duplicate
            elements (only the first duplicate element is added).

            Arguments
            - elements: the elements to add to the `ImmutableSortedSet`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` contains a null element
            """
            ...


        def build(self) -> "ImmutableSortedSet"["E"]:
            """
            Returns a newly-created `ImmutableSortedSet` based on the contents of the `Builder` and its comparator.
            """
            ...
