"""
Python module generated from Java source file com.google.common.collect.EmptyContiguousSet

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.util import NoSuchElementException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class EmptyContiguousSet(ContiguousSet):
    """
    An empty contiguous set.

    Author(s)
    - Gregory Kick
    """

    def first(self) -> "C":
        ...


    def last(self) -> "C":
        ...


    def size(self) -> int:
        ...


    def intersection(self, other: "ContiguousSet"["C"]) -> "ContiguousSet"["C"]:
        ...


    def range(self) -> "Range"["C"]:
        ...


    def range(self, lowerBoundType: "BoundType", upperBoundType: "BoundType") -> "Range"["C"]:
        ...


    def contains(self, object: "Object") -> bool:
        ...


    def iterator(self) -> "UnmodifiableIterator"["C"]:
        ...


    def descendingIterator(self) -> "UnmodifiableIterator"["C"]:
        ...


    def isEmpty(self) -> bool:
        ...


    def asList(self) -> "ImmutableList"["C"]:
        ...


    def toString(self) -> str:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
