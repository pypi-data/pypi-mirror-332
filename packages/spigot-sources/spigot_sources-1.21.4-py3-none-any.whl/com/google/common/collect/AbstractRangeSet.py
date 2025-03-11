"""
Python module generated from Java source file com.google.common.collect.AbstractRangeSet

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AbstractRangeSet(RangeSet):
    """
    A skeletal implementation of `RangeSet`.

    Author(s)
    - Louis Wasserman
    """

    def contains(self, value: "C") -> bool:
        ...


    def rangeContaining(self, value: "C") -> "Range"["C"]:
        ...


    def isEmpty(self) -> bool:
        ...


    def add(self, range: "Range"["C"]) -> None:
        ...


    def remove(self, range: "Range"["C"]) -> None:
        ...


    def clear(self) -> None:
        ...


    def enclosesAll(self, other: "RangeSet"["C"]) -> bool:
        ...


    def addAll(self, other: "RangeSet"["C"]) -> None:
        ...


    def removeAll(self, other: "RangeSet"["C"]) -> None:
        ...


    def intersects(self, otherRange: "Range"["C"]) -> bool:
        ...


    def encloses(self, otherRange: "Range"["C"]) -> bool:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
