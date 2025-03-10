"""
Python module generated from Java source file com.google.common.collect.RangeMap

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotMock
from java.util import NoSuchElementException
from java.util.function import BiFunction
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RangeMap:
    """
    A mapping from disjoint nonempty ranges to non-null values. Queries look up the value associated
    with the range (if any) that contains a specified key.
    
    In contrast to RangeSet, no "coalescing" is done of Range.isConnected(Range) connected ranges, even if they are mapped to the same value.

    Author(s)
    - Louis Wasserman

    Since
    - 14.0
    """

    def get(self, key: "K") -> "V":
        """
        Returns the value associated with the specified key, or `null` if there is no such value.
        
        Specifically, if any range in this range map contains the specified key, the value
        associated with that range is returned.
        """
        ...


    def getEntry(self, key: "K") -> "Entry"["Range"["K"], "V"]:
        """
        Returns the range containing this key and its associated value, if such a range is present in
        the range map, or `null` otherwise.
        """
        ...


    def span(self) -> "Range"["K"]:
        """
        Returns the minimal range Range.encloses(Range) enclosing the ranges in this
        `RangeMap`.

        Raises
        - NoSuchElementException: if this range map is empty
        """
        ...


    def put(self, range: "Range"["K"], value: "V") -> None:
        """
        Maps a range to a specified value (optional operation).
        
        Specifically, after a call to `put(range, value)`, if Range.contains(Comparable) range.contains(k), then .get(Comparable) get(k) will return
        `value`.
        
        If `range` Range.isEmpty() is empty, then this is a no-op.
        """
        ...


    def putCoalescing(self, range: "Range"["K"], value: "V") -> None:
        """
        Maps a range to a specified value, coalescing this range with any existing ranges with the same
        value that are Range.isConnected connected to this range.
        
        The behavior of .get(Comparable) get(k) after calling this method is identical to
        the behavior described in .put(Range, Object) put(range, value), however the ranges
        returned from .asMapOfRanges will be different if there were existing entries which
        connect to the given range and value.
        
        Even if the input range is empty, if it is connected on both sides by ranges mapped to the
        same value those two ranges will be coalesced.
        
        **Note:** coalescing requires calling `.equals()` on any connected values, which
        may be expensive depending on the value type. Using this method on range maps with large values
        such as Collection types is discouraged.

        Since
        - 22.0
        """
        ...


    def putAll(self, rangeMap: "RangeMap"["K", "V"]) -> None:
        """
        Puts all the associations from `rangeMap` into this range map (optional operation).
        """
        ...


    def clear(self) -> None:
        """
        Removes all associations from this range map (optional operation).
        """
        ...


    def remove(self, range: "Range"["K"]) -> None:
        """
        Removes all associations from this range map in the specified range (optional operation).
        
        If `!range.contains(k)`, .get(Comparable) get(k) will return the same result
        before and after a call to `remove(range)`. If `range.contains(k)`, then after a
        call to `remove(range)`, `get(k)` will return `null`.
        """
        ...


    def merge(self, range: "Range"["K"], value: "V", remappingFunction: "BiFunction"["V", "V", "V"]) -> None:
        """
        Merges a value into a part of the map by applying a remapping function.
        
        If any parts of the range are already present in this map, those parts are mapped to new
        values by applying the remapping function. The remapping function accepts the map's existing
        value for that part of the range and the given value. It returns the value to be associated
        with that part of the map, or it returns `null` to clear that part of the map.
        
        Any parts of the range not already present in this map are mapped to the specified value,
        unless the value is `null`.
        
        Any existing entry spanning either range boundary may be split at the boundary, even if the
        merge does not affect its value. For example, if `rangeMap` had one entry `[1, 5]
        => 3` then `rangeMap.merge(Range.closed(0,2), 3, Math::max)` could yield a map with the
        entries `[0, 1) => 3, [1, 2] => 3, (2, 5] => 3`.

        Since
        - 28.1
        """
        ...


    def asMapOfRanges(self) -> dict["Range"["K"], "V"]:
        """
        Returns a view of this range map as an unmodifiable `Map<Range<K>, V>`. Modifications to
        this range map are guaranteed to read through to the returned `Map`.
        
        The returned `Map` iterates over entries in ascending order of the bounds of the
        `Range` entries.
        
        It is guaranteed that no empty ranges will be in the returned `Map`.
        """
        ...


    def asDescendingMapOfRanges(self) -> dict["Range"["K"], "V"]:
        """
        Returns a view of this range map as an unmodifiable `Map<Range<K>, V>`. Modifications to
        this range map are guaranteed to read through to the returned `Map`.
        
        The returned `Map` iterates over entries in descending order of the bounds of the
        `Range` entries.
        
        It is guaranteed that no empty ranges will be in the returned `Map`.

        Since
        - 19.0
        """
        ...


    def subRangeMap(self, range: "Range"["K"]) -> "RangeMap"["K", "V"]:
        ...


    def equals(self, o: "Object") -> bool:
        """
        Returns `True` if `obj` is another `RangeMap` that has an equivalent .asMapOfRanges().
        """
        ...


    def hashCode(self) -> int:
        """
        Returns `asMapOfRanges().hashCode()`.
        """
        ...


    def toString(self) -> str:
        """
        Returns a readable string representation of this range map.
        """
        ...
