"""
Python module generated from Java source file com.google.common.collect.NaturalOrdering

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.io import Serializable
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class NaturalOrdering(Ordering, Serializable):
    """
    An ordering that uses the natural order of the values.
    """

    def compare(self, left: "Comparable"[Any], right: "Comparable"[Any]) -> int:
        ...


    def nullsFirst(self) -> "Ordering"["S"]:
        ...


    def nullsLast(self) -> "Ordering"["S"]:
        ...


    def reverse(self) -> "Ordering"["S"]:
        ...


    def toString(self) -> str:
        ...
