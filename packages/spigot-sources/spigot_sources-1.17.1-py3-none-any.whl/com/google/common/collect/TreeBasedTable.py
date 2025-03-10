"""
Python module generated from Java source file com.google.common.collect.TreeBasedTable

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Function
from com.google.common.base import Supplier
from com.google.common.collect import *
from java.io import Serializable
from java.util import Comparator
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import SortedMap
from java.util import SortedSet
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class TreeBasedTable(StandardRowSortedTable):
    """
    Implementation of `Table` whose row keys and column keys are ordered
    by their natural ordering or by supplied comparators. When constructing a
    `TreeBasedTable`, you may provide comparators for the row keys and
    the column keys, or you may use natural ordering for both.
    
    The .rowKeySet method returns a SortedSet and the .rowMap method returns a SortedMap, instead of the Set and
    Map specified by the Table interface.
    
    The views returned by .column, .columnKeySet(), and .columnMap() have iterators that don't support `remove()`. Otherwise,
    all optional operations are supported. Null row keys, columns keys, and
    values are not supported.
    
    Lookups by row key are often faster than lookups by column key, because
    the data is stored in a `Map<R, Map<C, V>>`. A method call like `column(columnKey).get(rowKey)` still runs quickly, since the row key is
    provided. However, `column(columnKey).size()` takes longer, since an
    iteration across all row keys occurs.
    
    Because a `TreeBasedTable` has unique sorted values for a given
    row, both `row(rowKey)` and `rowMap().get(rowKey)` are SortedMap instances, instead of the Map specified in the Table interface.
    
    Note that this implementation is not synchronized. If multiple threads
    access this table concurrently and one of the threads modifies the table, it
    must be synchronized externally.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#table">
    `Table`</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 7.0
    """

    @staticmethod
    def create() -> "TreeBasedTable"["R", "C", "V"]:
        """
        Creates an empty `TreeBasedTable` that uses the natural orderings
        of both row and column keys.
        
        The method signature specifies `R extends Comparable` with a raw
        Comparable, instead of `R extends Comparable<? super R>`,
        and the same for `C`. That's necessary to support classes defined
        without generics.
        """
        ...


    @staticmethod
    def create(rowComparator: "Comparator"["R"], columnComparator: "Comparator"["C"]) -> "TreeBasedTable"["R", "C", "V"]:
        """
        Creates an empty `TreeBasedTable` that is ordered by the specified
        comparators.

        Arguments
        - rowComparator: the comparator that orders the row keys
        - columnComparator: the comparator that orders the column keys
        """
        ...


    @staticmethod
    def create(table: "TreeBasedTable"["R", "C", "V"]) -> "TreeBasedTable"["R", "C", "V"]:
        """
        Creates a `TreeBasedTable` with the same mappings and sort order
        as the specified `TreeBasedTable`.
        """
        ...


    def rowComparator(self) -> "Comparator"["R"]:
        """
        Returns the comparator that orders the rows. With natural ordering, Ordering.natural()
        is returned.

        Deprecated
        - Use `table.rowKeySet().comparator()` instead. This method is scheduled for
            removal in April 2019.
        """
        ...


    def columnComparator(self) -> "Comparator"["C"]:
        """
        Returns the comparator that orders the columns. With natural ordering, Ordering.natural() is returned.

        Deprecated
        - Store the Comparator alongside the Table. Or, if you know that the
            Table contains at least one value, you can retrieve the Comparator with:
            `((SortedMap<C, V>) table.rowMap().values().iterator().next()).comparator();`. This
            method is scheduled for removal in April 2019.
        """
        ...


    def row(self, rowKey: "R") -> "SortedMap"["C", "V"]:
        """
        
        
        Because a `TreeBasedTable` has unique sorted values for a given
        row, this method returns a SortedMap, instead of the Map
        specified in the Table interface.

        Since
        - 10.0
            (<a href="https://github.com/google/guava/wiki/Compatibility"
            >mostly source-compatible</a> since 7.0)
        """
        ...


    def rowKeySet(self) -> "SortedSet"["R"]:
        ...


    def rowMap(self) -> "SortedMap"["R", dict["C", "V"]]:
        ...
