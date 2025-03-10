"""
Python module generated from Java source file com.google.common.collect.ArrayTable

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Objects
from com.google.common.collect import *
from com.google.common.collect.Maps import IteratorBasedAbstractMap
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import WeakOuter
from java.io import Serializable
from java.lang.reflect import Array
from java.util import Arrays
from java.util import Iterator
from java.util import Spliterator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ArrayTable(AbstractTable, Serializable):
    """
    Fixed-size Table implementation backed by a two-dimensional array.
    
    The allowed row and column keys must be supplied when the table is
    created. The table always contains a mapping for every row key / column pair.
    The value corresponding to a given row and column is null unless another
    value is provided.
    
    The table's size is constant: the product of the number of supplied row
    keys and the number of supplied column keys. The `remove` and `clear` methods are not supported by the table or its views. The .erase and .eraseAll methods may be used instead.
    
    The ordering of the row and column keys provided when the table is
    constructed determines the iteration ordering across rows and columns in the
    table's views. None of the view iterators support Iterator.remove.
    If the table is modified after an iterator is created, the iterator remains
    valid.
    
    This class requires less memory than the HashBasedTable and TreeBasedTable implementations, except when the table is sparse.
    
    Null row keys or column keys are not permitted.
    
    This class provides methods involving the underlying array structure,
    where the array indices correspond to the position of a row or column in the
    lists of allowed keys and values. See the .at, .set, .toArray, .rowKeyList, and .columnKeyList methods for more
    details.
    
    Note that this implementation is not synchronized. If multiple threads
    access the same cell of an `ArrayTable` concurrently and one of the
    threads modifies its value, there is no guarantee that the new value will be
    fully visible to the other threads. To guarantee that modifications are
    visible, synchronize access to the table. Unlike other `Table`
    implementations, synchronization is unnecessary between a thread that writes
    to one cell and a thread that reads from another.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#table">
    `Table`</a>.

    Author(s)
    - Jared Levy

    Since
    - 10.0
    """

    @staticmethod
    def create(rowKeys: Iterable["R"], columnKeys: Iterable["C"]) -> "ArrayTable"["R", "C", "V"]:
        """
        Creates an empty `ArrayTable`.

        Arguments
        - rowKeys: row keys that may be stored in the generated table
        - columnKeys: column keys that may be stored in the generated table

        Raises
        - NullPointerException: if any of the provided keys is null
        - IllegalArgumentException: if `rowKeys` or `columnKeys`
            contains duplicates or is empty
        """
        ...


    @staticmethod
    def create(table: "Table"["R", "C", "V"]) -> "ArrayTable"["R", "C", "V"]:
        """
        Creates an `ArrayTable` with the mappings in the provided table.
        
        If `table` includes a mapping with row key `r` and a
        separate mapping with column key `c`, the returned table contains a
        mapping with row key `r` and column key `c`. If that row key /
        column key pair in not in `table`, the pair maps to `null` in
        the generated table.
        
        The returned table allows subsequent `put` calls with the row keys
        in `table.rowKeySet()` and the column keys in `table.columnKeySet()`. Calling .put with other keys leads to an
        `IllegalArgumentException`.
        
        The ordering of `table.rowKeySet()` and `table.columnKeySet()` determines the row and column iteration ordering of
        the returned table.

        Raises
        - NullPointerException: if `table` has a null key
        - IllegalArgumentException: if the provided table is empty
        """
        ...


    def rowKeyList(self) -> "ImmutableList"["R"]:
        """
        Returns, as an immutable list, the row keys provided when the table was
        constructed, including those that are mapped to null values only.
        """
        ...


    def columnKeyList(self) -> "ImmutableList"["C"]:
        """
        Returns, as an immutable list, the column keys provided when the table was
        constructed, including those that are mapped to null values only.
        """
        ...


    def at(self, rowIndex: int, columnIndex: int) -> "V":
        """
        Returns the value corresponding to the specified row and column indices.
        The same value is returned by `get(rowKeyList().get(rowIndex), columnKeyList().get(columnIndex))`, but
        this method runs more quickly.

        Arguments
        - rowIndex: position of the row key in .rowKeyList()
        - columnIndex: position of the row key in .columnKeyList()

        Returns
        - the value with the specified row and column

        Raises
        - IndexOutOfBoundsException: if either index is negative, `rowIndex` is greater then or equal to the number of allowed row keys,
            or `columnIndex` is greater then or equal to the number of
            allowed column keys
        """
        ...


    def set(self, rowIndex: int, columnIndex: int, value: "V") -> "V":
        """
        Associates `value` with the specified row and column indices. The
        logic `put(rowKeyList().get(rowIndex), columnKeyList().get(columnIndex), value)`
        has the same behavior, but this method runs more quickly.

        Arguments
        - rowIndex: position of the row key in .rowKeyList()
        - columnIndex: position of the row key in .columnKeyList()
        - value: value to store in the table

        Returns
        - the previous value with the specified row and column

        Raises
        - IndexOutOfBoundsException: if either index is negative, `rowIndex` is greater then or equal to the number of allowed row keys,
            or `columnIndex` is greater then or equal to the number of
            allowed column keys
        """
        ...


    def toArray(self, valueClass: type["V"]) -> list[list["V"]]:
        """
        Returns a two-dimensional array with the table contents. The row and column
        indices correspond to the positions of the row and column in the iterables
        provided during table construction. If the table lacks a mapping for a
        given row and column, the corresponding array element is null.
        
        Subsequent table changes will not modify the array, and vice versa.

        Arguments
        - valueClass: class of values stored in the returned array
        """
        ...


    def clear(self) -> None:
        """
        Not supported. Use .eraseAll instead.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Use .eraseAll
        """
        ...


    def eraseAll(self) -> None:
        """
        Associates the value `null` with every pair of allowed row and column
        keys.
        """
        ...


    def contains(self, rowKey: "Object", columnKey: "Object") -> bool:
        """
        Returns `True` if the provided keys are among the keys provided when
        the table was constructed.
        """
        ...


    def containsColumn(self, columnKey: "Object") -> bool:
        """
        Returns `True` if the provided column key is among the column keys
        provided when the table was constructed.
        """
        ...


    def containsRow(self, rowKey: "Object") -> bool:
        """
        Returns `True` if the provided row key is among the row keys
        provided when the table was constructed.
        """
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def get(self, rowKey: "Object", columnKey: "Object") -> "V":
        ...


    def isEmpty(self) -> bool:
        """
        Always returns `False`.
        """
        ...


    def put(self, rowKey: "R", columnKey: "C", value: "V") -> "V":
        """
        Raises
        - IllegalArgumentException: if `rowKey` is not in .rowKeySet() or `columnKey` is not in .columnKeySet().
        """
        ...


    def putAll(self, table: "Table"["R", "C", "V"]) -> None:
        """
        
        
        If `table` is an `ArrayTable`, its null values will be
        stored in this table, possibly replacing values that were previously
        non-null.

        Raises
        - NullPointerException: if `table` has a null key
        - IllegalArgumentException: if any of the provided table's row keys or
            column keys is not in .rowKeySet() or .columnKeySet()
        """
        ...


    def remove(self, rowKey: "Object", columnKey: "Object") -> "V":
        """
        Not supported. Use .erase instead.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Use .erase
        """
        ...


    def erase(self, rowKey: "Object", columnKey: "Object") -> "V":
        """
        Associates the value `null` with the specified keys, assuming both
        keys are valid. If either key is null or isn't among the keys provided
        during construction, this method has no effect.
        
        This method is equivalent to `put(rowKey, columnKey, null)` when
        both provided keys are valid.

        Arguments
        - rowKey: row key of mapping to be erased
        - columnKey: column key of mapping to be erased

        Returns
        - the value previously associated with the keys, or `null` if
            no mapping existed for the keys
        """
        ...


    def size(self) -> int:
        ...


    def cellSet(self) -> set["Cell"["R", "C", "V"]]:
        """
        Returns an unmodifiable set of all row key / column key / value
        triplets. Changes to the table will update the returned set.
        
        The returned set's iterator traverses the mappings with the first row
        key, the mappings with the second row key, and so on.
        
        The value in the returned cells may change if the table subsequently
        changes.

        Returns
        - set of table cells consisting of row key / column key / value
            triplets
        """
        ...


    def column(self, columnKey: "C") -> dict["R", "V"]:
        """
        Returns a view of all mappings that have the given column key. If the
        column key isn't in .columnKeySet(), an empty immutable map is
        returned.
        
        Otherwise, for each row key in .rowKeySet(), the returned map
        associates the row key with the corresponding value in the table. Changes
        to the returned map will update the underlying table, and vice versa.

        Arguments
        - columnKey: key of column to search for in the table

        Returns
        - the corresponding map from row keys to values
        """
        ...


    def columnKeySet(self) -> "ImmutableSet"["C"]:
        """
        Returns an immutable set of the valid column keys, including those that
        are associated with null values only.

        Returns
        - immutable set of column keys
        """
        ...


    def columnMap(self) -> dict["C", dict["R", "V"]]:
        ...


    def row(self, rowKey: "R") -> dict["C", "V"]:
        """
        Returns a view of all mappings that have the given row key. If the
        row key isn't in .rowKeySet(), an empty immutable map is
        returned.
        
        Otherwise, for each column key in .columnKeySet(), the returned
        map associates the column key with the corresponding value in the
        table. Changes to the returned map will update the underlying table, and
        vice versa.

        Arguments
        - rowKey: key of row to search for in the table

        Returns
        - the corresponding map from column keys to values
        """
        ...


    def rowKeySet(self) -> "ImmutableSet"["R"]:
        """
        Returns an immutable set of the valid row keys, including those that are
        associated with null values only.

        Returns
        - immutable set of row keys
        """
        ...


    def rowMap(self) -> dict["R", dict["C", "V"]]:
        ...


    def values(self) -> Iterable["V"]:
        """
        Returns an unmodifiable collection of all values, which may contain
        duplicates. Changes to the table will update the returned collection.
        
        The returned collection's iterator traverses the values of the first row
        key, the values of the second row key, and so on.

        Returns
        - collection of values
        """
        ...
