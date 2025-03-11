"""
Python module generated from Java source file com.google.common.collect.Count

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.io import Serializable
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Count(Serializable):
    """
    A mutable value of type `int`, for multisets to use in tracking counts of values.

    Author(s)
    - Louis Wasserman
    """

    def get(self) -> int:
        ...


    def add(self, delta: int) -> None:
        ...


    def addAndGet(self, delta: int) -> int:
        ...


    def set(self, newValue: int) -> None:
        ...


    def getAndSet(self, newValue: int) -> int:
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...
