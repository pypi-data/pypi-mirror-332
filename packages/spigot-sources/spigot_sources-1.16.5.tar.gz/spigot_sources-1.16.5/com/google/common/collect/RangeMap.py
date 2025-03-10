"""
Python module generated from Java source file com.google.common.collect.RangeMap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class RangeMap:
    """
    A mapping from disjoint nonempty ranges to non-null values. Queries look up the value
    associated with the range (if any) that contains a specified key.
    
    In contrast to RangeSet, no "coalescing" is done of Range.isConnected(Range) connected ranges, even if they are mapped to the same value.

    Author(s)
    - Louis Wasserman

    Since
    - 14.0
    """

    def get(self, key: "K") -> "V":
        """
        Returns the value associated with the specified key, or `null` if there is no
        such value.
        
        Specifically, if any range in this range map contains the specified key, the value
        associated with that range is returned.
        """
        ...


    def getEntry(self, key: "K") -> "Map.Entry"["Range"["K"], "V"]:
        """
        Returns the range containing this key and its associated value, if such a range is present
        in the range map, or `null` otherwise.
        """
        ...


    def span(self) -> "Range"["K"]:
        """
        Returns the minimal range Range.encloses(Range) enclosing the ranges
        in this `RangeMap`.

        Raises
        - NoSuchElementException: if this range map is empty
        """
        ...


    def put(self, range: "Range"["K"], value: "V") -> None:
        """
        Maps a range to a specified value (optional operation).
        
        Specifically, after a call to `put(range, value)`, if
        Range.contains(Comparable) range.contains(k), then .get(Comparable) get(k)
        will return `value`.
        
        If `range` Range.isEmpty() is empty, then this is a no-op.
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
        before and after a call to `remove(range)`.  If `range.contains(k)`, then
        after a call to `remove(range)`, `get(k)` will return `null`.
        """
        ...


    def asMapOfRanges(self) -> dict["Range"["K"], "V"]:
        """
        Returns a view of this range map as an unmodifiable `Map<Range<K>, V>`.
        Modifications to this range map are guaranteed to read through to the returned `Map`.
        
        The returned `Map` iterates over entries in ascending order of the bounds of the
        `Range` entries.
        
        It is guaranteed that no empty ranges will be in the returned `Map`.
        """
        ...


    def asDescendingMapOfRanges(self) -> dict["Range"["K"], "V"]:
        """
        Returns a view of this range map as an unmodifiable `Map<Range<K>, V>`.
        Modifications to this range map are guaranteed to read through to the returned `Map`.
        
        The returned `Map` iterates over entries in descending order of the bounds of the
        `Range` entries.
        
        It is guaranteed that no empty ranges will be in the returned `Map`.

        Since
        - 19.0
        """
        ...


    def subRangeMap(self, range: "Range"["K"]) -> "RangeMap"["K", "V"]:
        """
        Returns a view of the part of this range map that intersects with `range`.
        
        For example, if `rangeMap` had the entries
        `[1, 5] => "foo", (6, 8) => "bar", (10, ∞) => "baz"`
        then `rangeMap.subRangeMap(Range.open(3, 12))` would return a range map
        with the entries `(3, 5) => "foo", (6, 8) => "bar", (10, 12) => "baz"`.
        
        The returned range map supports all optional operations that this range map supports,
        except for `asMapOfRanges().iterator().remove()`.
        
        The returned range map will throw an IllegalArgumentException on an attempt to
        insert a range not Range.encloses(Range) enclosed by `range`.
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Returns `True` if `obj` is another `RangeMap` that has an equivalent
        .asMapOfRanges().
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
