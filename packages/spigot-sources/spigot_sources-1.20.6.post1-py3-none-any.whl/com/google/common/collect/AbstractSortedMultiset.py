"""
Python module generated from Java source file com.google.common.collect.AbstractSortedMultiset

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


class AbstractSortedMultiset(AbstractMultiset, SortedMultiset):
    """
    This class provides a skeletal implementation of the SortedMultiset interface.
    
    The .count and .size implementations all iterate across the set returned by
    Multiset.entrySet(), as do many methods acting on the set returned by .elementSet(). Override those methods for better performance.

    Author(s)
    - Louis Wasserman
    """

    def elementSet(self) -> "NavigableSet"["E"]:
        ...


    def comparator(self) -> "Comparator"["E"]:
        ...


    def firstEntry(self) -> "Entry"["E"]:
        ...


    def lastEntry(self) -> "Entry"["E"]:
        ...


    def pollFirstEntry(self) -> "Entry"["E"]:
        ...


    def pollLastEntry(self) -> "Entry"["E"]:
        ...


    def subMultiset(self, fromElement: "E", fromBoundType: "BoundType", toElement: "E", toBoundType: "BoundType") -> "SortedMultiset"["E"]:
        ...


    def descendingMultiset(self) -> "SortedMultiset"["E"]:
        ...
