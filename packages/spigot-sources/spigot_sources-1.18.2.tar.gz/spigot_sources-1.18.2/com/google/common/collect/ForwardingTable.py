"""
Python module generated from Java source file com.google.common.collect.ForwardingTable

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingTable(ForwardingObject, Table):
    """
    A table which forwards all its method calls to another table. Subclasses should override one or
    more methods to modify the behavior of the backing map as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.

    Author(s)
    - Gregory Kick

    Since
    - 7.0
    """

    def cellSet(self) -> set["Cell"["R", "C", "V"]]:
        ...


    def clear(self) -> None:
        ...


    def column(self, columnKey: "C") -> dict["R", "V"]:
        ...


    def columnKeySet(self) -> set["C"]:
        ...


    def columnMap(self) -> dict["C", dict["R", "V"]]:
        ...


    def contains(self, rowKey: "Object", columnKey: "Object") -> bool:
        ...


    def containsColumn(self, columnKey: "Object") -> bool:
        ...


    def containsRow(self, rowKey: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def get(self, rowKey: "Object", columnKey: "Object") -> "V":
        ...


    def isEmpty(self) -> bool:
        ...


    def put(self, rowKey: "R", columnKey: "C", value: "V") -> "V":
        ...


    def putAll(self, table: "Table"["R", "C", "V"]) -> None:
        ...


    def remove(self, rowKey: "Object", columnKey: "Object") -> "V":
        ...


    def row(self, rowKey: "R") -> dict["C", "V"]:
        ...


    def rowKeySet(self) -> set["R"]:
        ...


    def rowMap(self) -> dict["R", dict["C", "V"]]:
        ...


    def size(self) -> int:
        ...


    def values(self) -> Iterable["V"]:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
