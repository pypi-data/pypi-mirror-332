"""
Python module generated from Java source file com.google.gson.internal.NonNullElementWrapperList

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from java.util import AbstractList
from java.util import Objects
from java.util import RandomAccess
from typing import Any, Callable, Iterable, Tuple


class NonNullElementWrapperList(AbstractList, RandomAccess):
    """
    List which wraps another `List` but prevents insertion of
    `null` elements. Methods which only perform checks with the element
    argument (e.g. .contains(Object)) do not throw exceptions for
    `null` arguments.
    """

    def __init__(self, delegate: list["E"]):
        ...


    def get(self, index: int) -> "E":
        ...


    def size(self) -> int:
        ...


    def set(self, index: int, element: "E") -> "E":
        ...


    def add(self, index: int, element: "E") -> None:
        ...


    def remove(self, index: int) -> "E":
        ...


    def clear(self) -> None:
        ...


    def remove(self, o: "Object") -> bool:
        ...


    def removeAll(self, c: Iterable[Any]) -> bool:
        ...


    def retainAll(self, c: Iterable[Any]) -> bool:
        ...


    def contains(self, o: "Object") -> bool:
        ...


    def indexOf(self, o: "Object") -> int:
        ...


    def lastIndexOf(self, o: "Object") -> int:
        ...


    def toArray(self) -> list["Object"]:
        ...


    def toArray(self, a: list["T"]) -> list["T"]:
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
