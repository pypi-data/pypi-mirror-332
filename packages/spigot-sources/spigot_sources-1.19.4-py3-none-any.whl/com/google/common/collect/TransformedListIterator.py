"""
Python module generated from Java source file com.google.common.collect.TransformedListIterator

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Function
from com.google.common.collect import *
from java.util import ListIterator
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class TransformedListIterator(TransformedIterator, ListIterator):
    """
    An iterator that transforms a backing list iterator; for internal use. This avoids the object
    overhead of constructing a Function for internal methods.

    Author(s)
    - Louis Wasserman
    """

    def hasPrevious(self) -> bool:
        ...


    def previous(self) -> "T":
        ...


    def nextIndex(self) -> int:
        ...


    def previousIndex(self) -> int:
        ...


    def set(self, element: "T") -> None:
        ...


    def add(self, element: "T") -> None:
        ...
