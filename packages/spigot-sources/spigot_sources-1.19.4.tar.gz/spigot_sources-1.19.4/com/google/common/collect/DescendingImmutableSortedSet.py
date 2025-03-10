"""
Python module generated from Java source file com.google.common.collect.DescendingImmutableSortedSet

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class DescendingImmutableSortedSet(ImmutableSortedSet):
    """
    Skeletal implementation of ImmutableSortedSet.descendingSet().

    Author(s)
    - Louis Wasserman
    """

    def contains(self, object: "Object") -> bool:
        ...


    def size(self) -> int:
        ...


    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def descendingSet(self) -> "ImmutableSortedSet"["E"]:
        ...


    def descendingIterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def lower(self, element: "E") -> "E":
        ...


    def floor(self, element: "E") -> "E":
        ...


    def ceiling(self, element: "E") -> "E":
        ...


    def higher(self, element: "E") -> "E":
        ...
