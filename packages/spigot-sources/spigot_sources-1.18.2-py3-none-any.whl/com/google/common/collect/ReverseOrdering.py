"""
Python module generated from Java source file com.google.common.collect.ReverseOrdering

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.io import Serializable
from java.util import Iterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ReverseOrdering(Ordering, Serializable):
    """
    An ordering that uses the reverse of a given order.
    """

    def compare(self, a: "T", b: "T") -> int:
        ...


    def reverse(self) -> "Ordering"["S"]:
        ...


    def min(self, a: "E", b: "E") -> "E":
        ...


    def min(self, a: "E", b: "E", c: "E", *rest: Tuple["E", ...]) -> "E":
        ...


    def min(self, iterator: Iterator["E"]) -> "E":
        ...


    def min(self, iterable: Iterable["E"]) -> "E":
        ...


    def max(self, a: "E", b: "E") -> "E":
        ...


    def max(self, a: "E", b: "E", c: "E", *rest: Tuple["E", ...]) -> "E":
        ...


    def max(self, iterator: Iterator["E"]) -> "E":
        ...


    def max(self, iterable: Iterable["E"]) -> "E":
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...
