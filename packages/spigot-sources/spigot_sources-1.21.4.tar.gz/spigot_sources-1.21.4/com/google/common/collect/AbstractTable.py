"""
Python module generated from Java source file com.google.common.collect.AbstractTable

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import WeakOuter
from java.util import AbstractCollection
from java.util import AbstractSet
from java.util import Iterator
from java.util import Spliterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractTable(Table):
    """
    Skeletal, implementation-agnostic implementation of the Table interface.

    Author(s)
    - Louis Wasserman
    """

    def containsRow(self, rowKey: "Object") -> bool:
        ...


    def containsColumn(self, columnKey: "Object") -> bool:
        ...


    def rowKeySet(self) -> set["R"]:
        ...


    def columnKeySet(self) -> set["C"]:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def contains(self, rowKey: "Object", columnKey: "Object") -> bool:
        ...


    def get(self, rowKey: "Object", columnKey: "Object") -> "V":
        ...


    def isEmpty(self) -> bool:
        ...


    def clear(self) -> None:
        ...


    def remove(self, rowKey: "Object", columnKey: "Object") -> "V":
        ...


    def put(self, rowKey: "R", columnKey: "C", value: "V") -> "V":
        ...


    def putAll(self, table: "Table"["R", "C", "V"]) -> None:
        ...


    def cellSet(self) -> set["Cell"["R", "C", "V"]]:
        ...


    def values(self) -> Iterable["V"]:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        """
        Returns the string representation `rowMap().toString()`.
        """
        ...
