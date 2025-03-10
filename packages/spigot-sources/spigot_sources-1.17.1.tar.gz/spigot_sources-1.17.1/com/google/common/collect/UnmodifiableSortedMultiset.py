"""
Python module generated from Java source file com.google.common.collect.UnmodifiableSortedMultiset

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.common.collect.Multisets import UnmodifiableMultiset
from java.util import Comparator
from java.util import NavigableSet
from typing import Any, Callable, Iterable, Tuple


class UnmodifiableSortedMultiset(UnmodifiableMultiset, SortedMultiset):
    """
    Implementation of Multisets.unmodifiableSortedMultiset(SortedMultiset),
    split out into its own file so it can be GWT emulated (to deal with the differing
    elementSet() types in GWT and non-GWT).

    Author(s)
    - Louis Wasserman
    """

    def comparator(self) -> "Comparator"["E"]:
        ...


    def elementSet(self) -> "NavigableSet"["E"]:
        ...


    def descendingMultiset(self) -> "SortedMultiset"["E"]:
        ...


    def firstEntry(self) -> "Entry"["E"]:
        ...


    def lastEntry(self) -> "Entry"["E"]:
        ...


    def pollFirstEntry(self) -> "Entry"["E"]:
        ...


    def pollLastEntry(self) -> "Entry"["E"]:
        ...


    def headMultiset(self, upperBound: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        ...


    def subMultiset(self, lowerBound: "E", lowerBoundType: "BoundType", upperBound: "E", upperBoundType: "BoundType") -> "SortedMultiset"["E"]:
        ...


    def tailMultiset(self, lowerBound: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        ...
