"""
Python module generated from Java source file com.google.common.collect.TreeRangeSet

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import MoreObjects
from com.google.common.collect import *
from com.google.errorprone.annotations.concurrent import LazyInit
from java.io import Serializable
from java.util import Comparator
from java.util import Iterator
from java.util import NavigableMap
from java.util import NoSuchElementException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class TreeRangeSet(AbstractRangeSet, Serializable):
    """
    An implementation of RangeSet backed by a TreeMap.

    Author(s)
    - Louis Wasserman

    Since
    - 14.0
    """

    @staticmethod
    def create() -> "TreeRangeSet"["C"]:
        """
        Creates an empty `TreeRangeSet` instance.
        """
        ...


    @staticmethod
    def create(rangeSet: "RangeSet"["C"]) -> "TreeRangeSet"["C"]:
        """
        Returns a `TreeRangeSet` initialized with the ranges in the specified range set.
        """
        ...


    @staticmethod
    def create(ranges: Iterable["Range"["C"]]) -> "TreeRangeSet"["C"]:
        """
        Returns a `TreeRangeSet` representing the union of the specified ranges.
        
        This is the smallest `RangeSet` which encloses each of the specified ranges. An
        element will be contained in this `RangeSet` if and only if it is contained in at least
        one `Range` in `ranges`.

        Since
        - 21.0
        """
        ...


    def asRanges(self) -> set["Range"["C"]]:
        ...


    def asDescendingSetOfRanges(self) -> set["Range"["C"]]:
        ...


    def rangeContaining(self, value: "C") -> "Range"["C"]:
        ...


    def intersects(self, range: "Range"["C"]) -> bool:
        ...


    def encloses(self, range: "Range"["C"]) -> bool:
        ...


    def span(self) -> "Range"["C"]:
        ...


    def add(self, rangeToAdd: "Range"["C"]) -> None:
        ...


    def remove(self, rangeToRemove: "Range"["C"]) -> None:
        ...


    def complement(self) -> "RangeSet"["C"]:
        ...


    def subRangeSet(self, view: "Range"["C"]) -> "RangeSet"["C"]:
        ...
