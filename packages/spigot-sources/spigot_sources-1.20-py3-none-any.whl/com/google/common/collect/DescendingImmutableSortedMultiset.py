"""
Python module generated from Java source file com.google.common.collect.DescendingImmutableSortedMultiset

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class DescendingImmutableSortedMultiset(ImmutableSortedMultiset):
    """
    A descending wrapper around an `ImmutableSortedMultiset`

    Author(s)
    - Louis Wasserman
    """

    def count(self, element: "Object") -> int:
        ...


    def firstEntry(self) -> "Entry"["E"]:
        ...


    def lastEntry(self) -> "Entry"["E"]:
        ...


    def size(self) -> int:
        ...


    def elementSet(self) -> "ImmutableSortedSet"["E"]:
        ...


    def descendingMultiset(self) -> "ImmutableSortedMultiset"["E"]:
        ...


    def headMultiset(self, upperBound: "E", boundType: "BoundType") -> "ImmutableSortedMultiset"["E"]:
        ...


    def tailMultiset(self, lowerBound: "E", boundType: "BoundType") -> "ImmutableSortedMultiset"["E"]:
        ...
