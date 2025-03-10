"""
Python module generated from Java source file com.google.common.collect.AllEqualOrdering

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.io import Serializable
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class AllEqualOrdering(Ordering, Serializable):
    """
    An ordering that treats all references as equals, even nulls.

    Author(s)
    - Emily Soldal
    """

    def compare(self, left: "Object", right: "Object") -> int:
        ...


    def sortedCopy(self, iterable: Iterable["E"]) -> list["E"]:
        ...


    def immutableSortedCopy(self, iterable: Iterable["E"]) -> "ImmutableList"["E"]:
        ...


    def reverse(self) -> "Ordering"["S"]:
        ...


    def toString(self) -> str:
        ...
