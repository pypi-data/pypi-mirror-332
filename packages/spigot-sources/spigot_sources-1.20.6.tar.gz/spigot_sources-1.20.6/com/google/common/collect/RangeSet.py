"""
Python module generated from Java source file com.google.common.collect.RangeSet

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotMock
from java.util import NoSuchElementException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class RangeSet:
    """
    A set comprising zero or more Range.isEmpty nonempty, Range.isConnected(Range) disconnected ranges of type `C`.
    
    Implementations that choose to support the .add(Range) operation are required to
    ignore empty ranges and coalesce connected ranges. For example:
    
    ````RangeSet<Integer> rangeSet = TreeRangeSet.create();
    rangeSet.add(Range.closed(1, 10)); // {[1, 10]`
    rangeSet.add(Range.closedOpen(11, 15)); // disconnected range; {[1, 10], [11, 15)}
    rangeSet.add(Range.closedOpen(15, 20)); // connected range; {[1, 10], [11, 20)}
    rangeSet.add(Range.openClosed(0, 0)); // empty range; {[1, 10], [11, 20)}
    rangeSet.remove(Range.open(5, 10)); // splits [1, 10]; {[1, 5], [10, 10], [11, 20)}
    }```
    
    Note that the behavior of Range.isEmpty() and Range.isConnected(Range) may not
    be as expected on discrete ranges. See the Javadoc of those methods for details.
    
    For a Set whose contents are specified by a Range, see ContiguousSet.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#rangeset">RangeSets</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 14.0
    """

    def contains(self, value: "C") -> bool:
        """
        Determines whether any of this range set's member ranges contains `value`.
        """
        ...


    def rangeContaining(self, value: "C") -> "Range"["C"]:
        """
        Returns the unique range from this range set that Range.contains contains `value`, or `null` if this range set does not contain `value`.
        """
        ...


    def intersects(self, otherRange: "Range"["C"]) -> bool:
        """
        Returns `True` if there exists a non-empty range enclosed by both a member range in this
        range set and the specified range. This is equivalent to calling `subRangeSet(otherRange)` and testing whether the resulting range set is non-empty.

        Since
        - 20.0
        """
        ...


    def encloses(self, otherRange: "Range"["C"]) -> bool:
        """
        Returns `True` if there exists a member range in this range set which Range.encloses encloses the specified range.
        """
        ...


    def enclosesAll(self, other: "RangeSet"["C"]) -> bool:
        """
        Returns `True` if for each member range in `other` there exists a member range in
        this range set which Range.encloses encloses it. It follows that `this.contains(value)` whenever `other.contains(value)`. Returns `True` if `other` is empty.
        
        This is equivalent to checking if this range set .encloses each of the ranges in
        `other`.
        """
        ...


    def enclosesAll(self, other: Iterable["Range"["C"]]) -> bool:
        """
        Returns `True` if for each range in `other` there exists a member range in this
        range set which Range.encloses encloses it. Returns `True` if `other`
        is empty.
        
        This is equivalent to checking if this range set .encloses each range in `other`.

        Since
        - 21.0
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if this range set contains no ranges.
        """
        ...


    def span(self) -> "Range"["C"]:
        """
        Returns the minimal range which Range.encloses(Range) encloses all ranges in this
        range set.

        Raises
        - NoSuchElementException: if this range set is .isEmpty() empty
        """
        ...


    def asRanges(self) -> set["Range"["C"]]:
        """
        Returns a view of the Range.isConnected disconnected ranges that make up this
        range set. The returned set may be empty. The iterators returned by its Iterable.iterator method return the ranges in increasing order of lower bound (equivalently,
        of upper bound).
        """
        ...


    def asDescendingSetOfRanges(self) -> set["Range"["C"]]:
        """
        Returns a descending view of the Range.isConnected disconnected ranges that make
        up this range set. The returned set may be empty. The iterators returned by its Iterable.iterator method return the ranges in decreasing order of lower bound (equivalently,
        of upper bound).

        Since
        - 19.0
        """
        ...


    def complement(self) -> "RangeSet"["C"]:
        """
        Returns a view of the complement of this `RangeSet`.
        
        The returned view supports the .add operation if this `RangeSet` supports
        .remove, and vice versa.
        """
        ...


    def subRangeSet(self, view: "Range"["C"]) -> "RangeSet"["C"]:
        """
        Returns a view of the intersection of this `RangeSet` with the specified range.
        
        The returned view supports all optional operations supported by this `RangeSet`, with
        the caveat that an IllegalArgumentException is thrown on an attempt to .add(Range) add any range not Range.encloses(Range) enclosed by `view`.
        """
        ...


    def add(self, range: "Range"["C"]) -> None:
        """
        Adds the specified range to this `RangeSet` (optional operation). That is, for equal
        range sets a and b, the result of `a.add(range)` is that `a` will be the minimal
        range set for which both `a.enclosesAll(b)` and `a.encloses(range)`.
        
        Note that `range` will be Range.span(Range) coalesced with any ranges in
        the range set that are Range.isConnected(Range) connected with it. Moreover, if
        `range` is empty, this is a no-op.

        Raises
        - UnsupportedOperationException: if this range set does not support the `add`
            operation
        """
        ...


    def remove(self, range: "Range"["C"]) -> None:
        """
        Removes the specified range from this `RangeSet` (optional operation). After this
        operation, if `range.contains(c)`, `this.contains(c)` will return `False`.
        
        If `range` is empty, this is a no-op.

        Raises
        - UnsupportedOperationException: if this range set does not support the `remove`
            operation
        """
        ...


    def clear(self) -> None:
        """
        Removes all ranges from this `RangeSet` (optional operation). After this operation,
        `this.contains(c)` will return False for all `c`.
        
        This is equivalent to `remove(Range.all())`.

        Raises
        - UnsupportedOperationException: if this range set does not support the `clear`
            operation
        """
        ...


    def addAll(self, other: "RangeSet"["C"]) -> None:
        """
        Adds all of the ranges from the specified range set to this range set (optional operation).
        After this operation, this range set is the minimal range set that .enclosesAll(RangeSet) encloses both the original range set and `other`.
        
        This is equivalent to calling .add on each of the ranges in `other` in turn.

        Raises
        - UnsupportedOperationException: if this range set does not support the `addAll`
            operation
        """
        ...


    def addAll(self, ranges: Iterable["Range"["C"]]) -> None:
        """
        Adds all of the specified ranges to this range set (optional operation). After this operation,
        this range set is the minimal range set that .enclosesAll(RangeSet) encloses both
        the original range set and each range in `other`.
        
        This is equivalent to calling .add on each of the ranges in `other` in turn.

        Raises
        - UnsupportedOperationException: if this range set does not support the `addAll`
            operation

        Since
        - 21.0
        """
        ...


    def removeAll(self, other: "RangeSet"["C"]) -> None:
        """
        Removes all of the ranges from the specified range set from this range set (optional
        operation). After this operation, if `other.contains(c)`, `this.contains(c)` will
        return `False`.
        
        This is equivalent to calling .remove on each of the ranges in `other` in
        turn.

        Raises
        - UnsupportedOperationException: if this range set does not support the `removeAll`
            operation
        """
        ...


    def removeAll(self, ranges: Iterable["Range"["C"]]) -> None:
        """
        Removes all of the specified ranges from this range set (optional operation).
        
        This is equivalent to calling .remove on each of the ranges in `other` in
        turn.

        Raises
        - UnsupportedOperationException: if this range set does not support the `removeAll`
            operation

        Since
        - 21.0
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Returns `True` if `obj` is another `RangeSet` that contains the same ranges
        according to Range.equals(Object).
        """
        ...


    def hashCode(self) -> int:
        """
        Returns `asRanges().hashCode()`.
        """
        ...


    def toString(self) -> str:
        """
        Returns a readable string representation of this range set. For example, if this `RangeSet` consisted of `Range.closed(1, 3)` and `Range.greaterThan(4)`, this might
        return `" [1..3](4..+∞)`"}.
        """
        ...
