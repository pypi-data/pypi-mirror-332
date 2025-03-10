"""
Python module generated from Java source file com.google.common.collect.HashBasedTable

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Supplier
from com.google.common.collect import *
from java.io import Serializable
from typing import Any, Callable, Iterable, Tuple


class HashBasedTable(StandardTable):
    """
    Implementation of Table using linked hash tables. This guarantees predictable iteration
    order of the various views.
    
    The views returned by .column, .columnKeySet(), and .columnMap() have
    iterators that don't support `remove()`. Otherwise, all optional operations are supported.
    Null row keys, columns keys, and values are not supported.
    
    Lookups by row key are often faster than lookups by column key, because the data is stored in
    a `Map<R, Map<C, V>>`. A method call like `column(columnKey).get(rowKey)` still runs
    quickly, since the row key is provided. However, `column(columnKey).size()` takes longer,
    since an iteration across all row keys occurs.
    
    Note that this implementation is not synchronized. If multiple threads access this table
    concurrently and one of the threads modifies the table, it must be synchronized externally.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#table">`Table`</a>.

    Author(s)
    - Jared Levy

    Since
    - 7.0
    """

    @staticmethod
    def create() -> "HashBasedTable"["R", "C", "V"]:
        """
        Creates an empty `HashBasedTable`.
        """
        ...


    @staticmethod
    def create(expectedRows: int, expectedCellsPerRow: int) -> "HashBasedTable"["R", "C", "V"]:
        """
        Creates an empty `HashBasedTable` with the specified map sizes.

        Arguments
        - expectedRows: the expected number of distinct row keys
        - expectedCellsPerRow: the expected number of column key / value mappings in each row

        Raises
        - IllegalArgumentException: if `expectedRows` or `expectedCellsPerRow` is
            negative
        """
        ...


    @staticmethod
    def create(table: "Table"["R", "C", "V"]) -> "HashBasedTable"["R", "C", "V"]:
        """
        Creates a `HashBasedTable` with the same mappings as the specified table.

        Arguments
        - table: the table to copy

        Raises
        - NullPointerException: if any of the row keys, column keys, or values in `table` is
            null
        """
        ...
