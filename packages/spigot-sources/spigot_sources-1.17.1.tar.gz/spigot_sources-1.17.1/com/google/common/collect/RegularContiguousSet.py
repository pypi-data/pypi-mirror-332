"""
Python module generated from Java source file com.google.common.collect.RegularContiguousSet

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.io import Serializable
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class RegularContiguousSet(ContiguousSet):
    """
    An implementation of ContiguousSet that contains one or more elements.

    Author(s)
    - Gregory Kick
    """

    def iterator(self) -> "UnmodifiableIterator"["C"]:
        ...


    def descendingIterator(self) -> "UnmodifiableIterator"["C"]:
        ...


    def first(self) -> "C":
        ...


    def last(self) -> "C":
        ...


    def size(self) -> int:
        ...


    def contains(self, object: "Object") -> bool:
        ...


    def containsAll(self, targets: Iterable[Any]) -> bool:
        ...


    def isEmpty(self) -> bool:
        ...


    def intersection(self, other: "ContiguousSet"["C"]) -> "ContiguousSet"["C"]:
        ...


    def range(self) -> "Range"["C"]:
        ...


    def range(self, lowerBoundType: "BoundType", upperBoundType: "BoundType") -> "Range"["C"]:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
