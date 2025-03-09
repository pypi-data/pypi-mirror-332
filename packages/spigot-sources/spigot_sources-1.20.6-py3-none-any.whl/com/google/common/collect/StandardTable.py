"""
Python module generated from Java source file com.google.common.collect.StandardTable

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Function
from com.google.common.base import Predicate
from com.google.common.base import Supplier
from com.google.common.collect import *
from com.google.common.collect.Maps import IteratorBasedAbstractMap
from com.google.common.collect.Maps import ViewCachingAbstractMap
from com.google.common.collect.Sets import ImprovedAbstractSet
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import WeakOuter
from java.io import Serializable
from java.util import Iterator
from java.util import Spliterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class StandardTable(AbstractTable, Serializable):
    """
    Table implementation backed by a map that associates row keys with column key / value
    secondary maps. This class provides rapid access to records by the row key alone or by both keys,
    but not by just the column key.
    
    The views returned by .column, .columnKeySet(), and .columnMap() have
    iterators that don't support `remove()`. Otherwise, all optional operations are supported.
    Null row keys, columns keys, and values are not supported.
    
    Lookups by row key are often faster than lookups by column key, because the data is stored in
    a `Map<R, Map<C, V>>`. A method call like `column(columnKey).get(rowKey)` still runs
    quickly, since the row key is provided. However, `column(columnKey).size()` takes longer,
    since an iteration across all row keys occurs.
    
    Note that this implementation is not synchronized. If multiple threads access this table
    concurrently and one of the threads modifies the table, it must be synchronized externally.

    Author(s)
    - Jared Levy
    """

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


    def size(self) -> int:
        ...


    def clear(self) -> None:
        ...


    def put(self, rowKey: "R", columnKey: "C", value: "V") -> "V":
        ...


    def remove(self, rowKey: "Object", columnKey: "Object") -> "V":
        ...


    def cellSet(self) -> set["Cell"["R", "C", "V"]]:
        """
        
        
        The set's iterator traverses the mappings for the first row, the mappings for the second
        row, and so on.
        
        Each cell is an immutable snapshot of a row key / column key / value mapping, taken at the
        time the cell is returned by a method call to the set or its iterator.
        """
        ...


    def row(self, rowKey: "R") -> dict["C", "V"]:
        ...


    def column(self, columnKey: "C") -> dict["R", "V"]:
        """
        
        
        The returned map's views have iterators that don't support `remove()`.
        """
        ...


    def rowKeySet(self) -> set["R"]:
        ...


    def columnKeySet(self) -> set["C"]:
        """
        
        
        The returned set has an iterator that does not support `remove()`.
        
        The set's iterator traverses the columns of the first row, the columns of the second row,
        etc., skipping any columns that have appeared previously.
        """
        ...


    def values(self) -> Iterable["V"]:
        """
        
        
        The collection's iterator traverses the values for the first row, the values for the second
        row, and so on.
        """
        ...


    def rowMap(self) -> dict["R", dict["C", "V"]]:
        ...


    def columnMap(self) -> dict["C", dict["R", "V"]]:
        ...
