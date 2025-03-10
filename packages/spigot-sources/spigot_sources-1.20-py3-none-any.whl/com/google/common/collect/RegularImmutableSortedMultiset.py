"""
Python module generated from Java source file com.google.common.collect.RegularImmutableSortedMultiset

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.common.primitives import Ints
from java.util import Comparator
from java.util.function import ObjIntConsumer
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class RegularImmutableSortedMultiset(ImmutableSortedMultiset):
    """
    An immutable sorted multiset with one or more distinct elements.

    Author(s)
    - Louis Wasserman
    """

    def forEachEntry(self, action: "ObjIntConsumer"["E"]) -> None:
        ...


    def firstEntry(self) -> "Entry"["E"]:
        ...


    def lastEntry(self) -> "Entry"["E"]:
        ...


    def count(self, element: "Object") -> int:
        ...


    def size(self) -> int:
        ...


    def elementSet(self) -> "ImmutableSortedSet"["E"]:
        ...


    def headMultiset(self, upperBound: "E", boundType: "BoundType") -> "ImmutableSortedMultiset"["E"]:
        ...


    def tailMultiset(self, lowerBound: "E", boundType: "BoundType") -> "ImmutableSortedMultiset"["E"]:
        ...
