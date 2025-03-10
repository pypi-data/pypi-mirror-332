"""
Python module generated from Java source file com.google.common.collect.ImmutableRangeSet

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from com.google.common.collect.SortedLists import KeyAbsentBehavior
from com.google.common.collect.SortedLists import KeyPresentBehavior
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from com.google.errorprone.annotations.concurrent import LazyInit
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.util import Collections
from java.util import Iterator
from java.util import NoSuchElementException
from java.util.stream import Collector
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ImmutableRangeSet(AbstractRangeSet, Serializable):
    """
    A RangeSet whose contents will never change, with many other important properties
    detailed at ImmutableCollection.

    Author(s)
    - Louis Wasserman

    Since
    - 14.0
    """

    @staticmethod
    def toImmutableRangeSet() -> "Collector"["Range"["E"], Any, "ImmutableRangeSet"["E"]]:
        """
        Returns a `Collector` that accumulates the input elements into a new `ImmutableRangeSet`. As in Builder, overlapping ranges are not permitted and adjacent
        ranges will be merged.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def of() -> "ImmutableRangeSet"["C"]:
        """
        Returns an empty immutable range set.
        
        **Performance note:** the instance returned is a singleton.
        """
        ...


    @staticmethod
    def of(range: "Range"["C"]) -> "ImmutableRangeSet"["C"]:
        """
        Returns an immutable range set containing the specified single range. If Range.isEmpty()
        range.isEmpty(), this is equivalent to ImmutableRangeSet.of().
        """
        ...


    @staticmethod
    def copyOf(rangeSet: "RangeSet"["C"]) -> "ImmutableRangeSet"["C"]:
        """
        Returns an immutable copy of the specified `RangeSet`.
        """
        ...


    @staticmethod
    def copyOf(ranges: Iterable["Range"["C"]]) -> "ImmutableRangeSet"["C"]:
        """
        Returns an `ImmutableRangeSet` containing each of the specified disjoint ranges.
        Overlapping ranges and empty ranges are forbidden, though adjacent ranges are permitted and
        will be merged.

        Raises
        - IllegalArgumentException: if any ranges overlap or are empty

        Since
        - 21.0
        """
        ...


    @staticmethod
    def unionOf(ranges: Iterable["Range"["C"]]) -> "ImmutableRangeSet"["C"]:
        """
        Returns an `ImmutableRangeSet` representing the union of the specified ranges.
        
        This is the smallest `RangeSet` which encloses each of the specified ranges. Duplicate
        or connected ranges are permitted, and will be coalesced in the result.

        Since
        - 21.0
        """
        ...


    def intersects(self, otherRange: "Range"["C"]) -> bool:
        ...


    def encloses(self, otherRange: "Range"["C"]) -> bool:
        ...


    def rangeContaining(self, value: "C") -> "Range"["C"]:
        ...


    def span(self) -> "Range"["C"]:
        ...


    def isEmpty(self) -> bool:
        ...


    def add(self, range: "Range"["C"]) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeSet` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def addAll(self, other: "RangeSet"["C"]) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeSet` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def addAll(self, other: Iterable["Range"["C"]]) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeSet` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def remove(self, range: "Range"["C"]) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeSet` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def removeAll(self, other: "RangeSet"["C"]) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeSet` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def removeAll(self, other: Iterable["Range"["C"]]) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeSet` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def asRanges(self) -> "ImmutableSet"["Range"["C"]]:
        ...


    def asDescendingSetOfRanges(self) -> "ImmutableSet"["Range"["C"]]:
        ...


    def complement(self) -> "ImmutableRangeSet"["C"]:
        ...


    def union(self, other: "RangeSet"["C"]) -> "ImmutableRangeSet"["C"]:
        """
        Returns a new range set consisting of the union of this range set and `other`.
        
        This is essentially the same as `TreeRangeSet.create(this).addAll(other)` except it
        returns an `ImmutableRangeSet`.

        Since
        - 21.0
        """
        ...


    def intersection(self, other: "RangeSet"["C"]) -> "ImmutableRangeSet"["C"]:
        """
        Returns a new range set consisting of the intersection of this range set and `other`.
        
        This is essentially the same as `TreeRangeSet.create(this).removeAll(other.complement())` except it returns an `ImmutableRangeSet`.

        Since
        - 21.0
        """
        ...


    def difference(self, other: "RangeSet"["C"]) -> "ImmutableRangeSet"["C"]:
        """
        Returns a new range set consisting of the difference of this range set and `other`.
        
        This is essentially the same as `TreeRangeSet.create(this).removeAll(other)` except it
        returns an `ImmutableRangeSet`.

        Since
        - 21.0
        """
        ...


    def subRangeSet(self, range: "Range"["C"]) -> "ImmutableRangeSet"["C"]:
        """
        Returns a view of the intersection of this range set with the given range.
        """
        ...


    def asSet(self, domain: "DiscreteDomain"["C"]) -> "ImmutableSortedSet"["C"]:
        """
        Returns an ImmutableSortedSet containing the same values in the given domain
        RangeSet.contains contained by this range set.
        
        **Note:** `a.asSet(d).equals(b.asSet(d))` does not imply `a.equals(b)`! For
        example, `a` and `b` could be `[2..4]` and `(1..5)`, or the empty
        ranges `[3..3)` and `[4..4)`.
        
        **Warning:** Be extremely careful what you do with the `asSet` view of a large
        range set (such as `ImmutableRangeSet.of(Range.greaterThan(0))`). Certain operations on
        such a set can be performed efficiently, but others (such as Set.hashCode or Collections.frequency) can cause major performance problems.
        
        The returned set's Object.toString method returns a shorthand form of the set's
        contents, such as `"[1..100]`"}.

        Raises
        - IllegalArgumentException: if neither this range nor the domain has a lower bound, or if
            neither has an upper bound
        """
        ...


    @staticmethod
    def builder() -> "Builder"["C"]:
        """
        Returns a new builder for an immutable range set.
        """
        ...


    class Builder:
        """
        A builder for immutable range sets.

        Since
        - 14.0
        """

        def __init__(self):
            ...


        def add(self, range: "Range"["C"]) -> "Builder"["C"]:
            """
            Add the specified range to this builder. Adjacent ranges are permitted and will be merged,
            but overlapping ranges will cause an exception when .build() is called.

            Raises
            - IllegalArgumentException: if `range` is empty
            """
            ...


        def addAll(self, ranges: "RangeSet"["C"]) -> "Builder"["C"]:
            """
            Add all ranges from the specified range set to this builder. Adjacent ranges are permitted
            and will be merged, but overlapping ranges will cause an exception when .build() is
            called.
            """
            ...


        def addAll(self, ranges: Iterable["Range"["C"]]) -> "Builder"["C"]:
            """
            Add all of the specified ranges to this builder. Adjacent ranges are permitted and will be
            merged, but overlapping ranges will cause an exception when .build() is called.

            Raises
            - IllegalArgumentException: if any inserted ranges are empty

            Since
            - 21.0
            """
            ...


        def build(self) -> "ImmutableRangeSet"["C"]:
            """
            Returns an `ImmutableRangeSet` containing the ranges added to this builder.

            Raises
            - IllegalArgumentException: if any input ranges have nonempty overlap
            """
            ...
