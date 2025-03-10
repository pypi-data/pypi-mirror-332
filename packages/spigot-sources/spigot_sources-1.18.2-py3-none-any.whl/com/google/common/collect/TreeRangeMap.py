"""
Python module generated from Java source file com.google.common.collect.TreeRangeMap

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import MoreObjects
from com.google.common.base import Predicate
from com.google.common.collect import *
from com.google.common.collect.Maps import IteratorBasedAbstractMap
from java.util import Collections
from java.util import Iterator
from java.util import NavigableMap
from java.util import NoSuchElementException
from java.util.function import BiFunction
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class TreeRangeMap(RangeMap):
    """
    An implementation of `RangeMap` based on a `TreeMap`, supporting all optional
    operations.
    
    Like all `RangeMap` implementations, this supports neither null keys nor null values.

    Author(s)
    - Louis Wasserman

    Since
    - 14.0
    """

    @staticmethod
    def create() -> "TreeRangeMap"["K", "V"]:
        ...


    def get(self, key: "K") -> "V":
        ...


    def getEntry(self, key: "K") -> "Entry"["Range"["K"], "V"]:
        ...


    def put(self, range: "Range"["K"], value: "V") -> None:
        ...


    def putCoalescing(self, range: "Range"["K"], value: "V") -> None:
        ...


    def putAll(self, rangeMap: "RangeMap"["K", "V"]) -> None:
        ...


    def clear(self) -> None:
        ...


    def span(self) -> "Range"["K"]:
        ...


    def remove(self, rangeToRemove: "Range"["K"]) -> None:
        ...


    def merge(self, range: "Range"["K"], value: "V", remappingFunction: "BiFunction"["V", "V", "V"]) -> None:
        ...


    def asMapOfRanges(self) -> dict["Range"["K"], "V"]:
        ...


    def asDescendingMapOfRanges(self) -> dict["Range"["K"], "V"]:
        ...


    def subRangeMap(self, subRange: "Range"["K"]) -> "RangeMap"["K", "V"]:
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
