"""
Python module generated from Java source file com.google.common.collect.DescendingMultiset

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import WeakOuter
from java.util import Comparator
from java.util import Iterator
from java.util import NavigableSet
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class DescendingMultiset(ForwardingMultiset, SortedMultiset):
    """
    A skeleton implementation of a descending multiset. Only needs `forwardMultiset()` and
    `entryIterator()`.

    Author(s)
    - Louis Wasserman
    """

    def comparator(self) -> "Comparator"["E"]:
        ...


    def elementSet(self) -> "NavigableSet"["E"]:
        ...


    def pollFirstEntry(self) -> "Entry"["E"]:
        ...


    def pollLastEntry(self) -> "Entry"["E"]:
        ...


    def headMultiset(self, toElement: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        ...


    def subMultiset(self, fromElement: "E", fromBoundType: "BoundType", toElement: "E", toBoundType: "BoundType") -> "SortedMultiset"["E"]:
        ...


    def tailMultiset(self, fromElement: "E", boundType: "BoundType") -> "SortedMultiset"["E"]:
        ...


    def descendingMultiset(self) -> "SortedMultiset"["E"]:
        ...


    def firstEntry(self) -> "Entry"["E"]:
        ...


    def lastEntry(self) -> "Entry"["E"]:
        ...


    def entrySet(self) -> set["Entry"["E"]]:
        ...


    def iterator(self) -> Iterator["E"]:
        ...


    def toArray(self) -> list["Object"]:
        ...


    def toArray(self, array: list["T"]) -> list["T"]:
        ...


    def toString(self) -> str:
        ...
