"""
Python module generated from Java source file com.google.common.collect.ContiguousSet

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotCall
from java.util import Collections
from java.util import NoSuchElementException
from typing import Any, Callable, Iterable, Tuple


class ContiguousSet(ImmutableSortedSet):
    """
    A sorted set of contiguous values in a given DiscreteDomain. Example:
    
    ````ContiguousSet.create(Range.closed(5, 42), DiscreteDomain.integers())````
    
    Note that because bounded ranges over `int` and `long` values are so common, this
    particular example can be written as just:
    
    ````ContiguousSet.closed(5, 42)````
    
    **Warning:** Be extremely careful what you do with conceptually large instances (such as
    `ContiguousSet.create(Range.greaterThan(0), DiscreteDomain.integers()`). Certain operations
    on such a set can be performed efficiently, but others (such as Set.hashCode or Collections.frequency) can cause major performance problems.

    Author(s)
    - Gregory Kick

    Since
    - 10.0
    """

    @staticmethod
    def create(range: "Range"["C"], domain: "DiscreteDomain"["C"]) -> "ContiguousSet"["C"]:
        """
        Returns a `ContiguousSet` containing the same values in the given domain Range.contains contained by the range.

        Raises
        - IllegalArgumentException: if neither range nor the domain has a lower bound, or if
            neither has an upper bound

        Since
        - 13.0
        """
        ...


    @staticmethod
    def closed(lower: int, upper: int) -> "ContiguousSet"["Integer"]:
        """
        Returns a nonempty contiguous set containing all `int` values from `lower`
        (inclusive) to `upper` (inclusive). (These are the same values contained in `Range.closed(lower, upper)`.)

        Raises
        - IllegalArgumentException: if `lower` is greater than `upper`

        Since
        - 23.0
        """
        ...


    @staticmethod
    def closed(lower: int, upper: int) -> "ContiguousSet"["Long"]:
        """
        Returns a nonempty contiguous set containing all `long` values from `lower`
        (inclusive) to `upper` (inclusive). (These are the same values contained in `Range.closed(lower, upper)`.)

        Raises
        - IllegalArgumentException: if `lower` is greater than `upper`

        Since
        - 23.0
        """
        ...


    @staticmethod
    def closedOpen(lower: int, upper: int) -> "ContiguousSet"["Integer"]:
        """
        Returns a contiguous set containing all `int` values from `lower` (inclusive) to
        `upper` (exclusive). If the endpoints are equal, an empty set is returned. (These are the
        same values contained in `Range.closedOpen(lower, upper)`.)

        Raises
        - IllegalArgumentException: if `lower` is greater than `upper`

        Since
        - 23.0
        """
        ...


    @staticmethod
    def closedOpen(lower: int, upper: int) -> "ContiguousSet"["Long"]:
        """
        Returns a contiguous set containing all `long` values from `lower` (inclusive) to
        `upper` (exclusive). If the endpoints are equal, an empty set is returned. (These are the
        same values contained in `Range.closedOpen(lower, upper)`.)

        Raises
        - IllegalArgumentException: if `lower` is greater than `upper`

        Since
        - 23.0
        """
        ...


    def headSet(self, toElement: "C") -> "ContiguousSet"["C"]:
        ...


    def headSet(self, toElement: "C", inclusive: bool) -> "ContiguousSet"["C"]:
        """
        Since
        - 12.0
        """
        ...


    def subSet(self, fromElement: "C", toElement: "C") -> "ContiguousSet"["C"]:
        ...


    def subSet(self, fromElement: "C", fromInclusive: bool, toElement: "C", toInclusive: bool) -> "ContiguousSet"["C"]:
        """
        Since
        - 12.0
        """
        ...


    def tailSet(self, fromElement: "C") -> "ContiguousSet"["C"]:
        ...


    def tailSet(self, fromElement: "C", inclusive: bool) -> "ContiguousSet"["C"]:
        """
        Since
        - 12.0
        """
        ...


    def intersection(self, other: "ContiguousSet"["C"]) -> "ContiguousSet"["C"]:
        """
        Returns the set of values that are contained in both this set and the other.
        
        This method should always be used instead of Sets.intersection for ContiguousSet instances.
        """
        ...


    def range(self) -> "Range"["C"]:
        """
        Returns a range, closed on both ends, whose endpoints are the minimum and maximum values
        contained in this set. This is equivalent to `range(CLOSED, CLOSED)`.

        Raises
        - NoSuchElementException: if this set is empty
        """
        ...


    def range(self, lowerBoundType: "BoundType", upperBoundType: "BoundType") -> "Range"["C"]:
        """
        Returns the minimal range with the given boundary types for which all values in this set are
        Range.contains(Comparable) contained within the range.
        
        Note that this method will return ranges with unbounded endpoints if BoundType.OPEN
        is requested for a domain minimum or maximum. For example, if `set` was created from the
        range `[1..Integer.MAX_VALUE]` then `set.range(CLOSED, OPEN)` must return `[1..∞)`.

        Raises
        - NoSuchElementException: if this set is empty
        """
        ...


    def toString(self) -> str:
        """
        Returns a short-hand representation of the contents such as `"[1..100]"`.
        """
        ...


    @staticmethod
    def builder() -> "ImmutableSortedSet.Builder"["E"]:
        """
        Not supported. `ContiguousSet` instances are constructed with .create. This
        method exists only to hide ImmutableSet.builder from consumers of `ContiguousSet`.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Use .create.
        """
        ...
