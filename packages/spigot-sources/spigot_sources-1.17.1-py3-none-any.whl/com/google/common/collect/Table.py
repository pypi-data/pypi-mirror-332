"""
Python module generated from Java source file com.google.common.collect.Table

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Objects
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import CompatibleWith
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Table:
    """
    A collection that associates an ordered pair of keys, called a row key and a
    column key, with a single value. A table may be sparse, with only a small
    fraction of row key / column key pairs possessing a corresponding value.
    
    The mappings corresponding to a given row key may be viewed as a Map whose keys are the columns. The reverse is also available, associating a
    column with a row key / value map. Note that, in some implementations, data
    access by column key may have fewer supported operations or worse performance
    than data access by row key.
    
    The methods returning collections or maps always return views of the
    underlying table. Updating the table can change the contents of those
    collections, and updating the collections will change the table.
    
    All methods that modify the table are optional, and the views returned by
    the table may or may not be modifiable. When modification isn't supported,
    those methods will throw an UnsupportedOperationException.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#table">
    `Table`</a>.
    
    Type `<R>`: the type of the table row keys
    
    Type `<C>`: the type of the table column keys
    
    Type `<V>`: the type of the mapped values

    Author(s)
    - Jared Levy

    Since
    - 7.0
    """

    def contains(self, rowKey: "Object", columnKey: "Object") -> bool:
        """
        Returns `True` if the table contains a mapping with the specified row and column keys.

        Arguments
        - rowKey: key of row to search for
        - columnKey: key of column to search for
        """
        ...


    def containsRow(self, rowKey: "Object") -> bool:
        """
        Returns `True` if the table contains a mapping with the specified row key.

        Arguments
        - rowKey: key of row to search for
        """
        ...


    def containsColumn(self, columnKey: "Object") -> bool:
        """
        Returns `True` if the table contains a mapping with the specified column.

        Arguments
        - columnKey: key of column to search for
        """
        ...


    def containsValue(self, value: "Object") -> bool:
        """
        Returns `True` if the table contains a mapping with the specified value.

        Arguments
        - value: value to search for
        """
        ...


    def get(self, rowKey: "Object", columnKey: "Object") -> "V":
        """
        Returns the value corresponding to the given row and column keys, or `null` if no such
        mapping exists.

        Arguments
        - rowKey: key of row to search for
        - columnKey: key of column to search for
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if the table contains no mappings.
        """
        ...


    def size(self) -> int:
        """
        Returns the number of row key / column key / value mappings in the table.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares the specified object with this table for equality. Two tables are
        equal when their cell views, as returned by .cellSet, are equal.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code for this table. The hash code of a table is defined
        as the hash code of its cell view, as returned by .cellSet.
        """
        ...


    def clear(self) -> None:
        """
        Removes all mappings from the table.
        """
        ...


    def put(self, rowKey: "R", columnKey: "C", value: "V") -> "V":
        """
        Associates the specified value with the specified keys. If the table
        already contained a mapping for those keys, the old value is replaced with
        the specified value.

        Arguments
        - rowKey: row key that the value should be associated with
        - columnKey: column key that the value should be associated with
        - value: value to be associated with the specified keys

        Returns
        - the value previously associated with the keys, or `null` if
            no mapping existed for the keys
        """
        ...


    def putAll(self, table: "Table"["R", "C", "V"]) -> None:
        """
        Copies all mappings from the specified table to this table. The effect is
        equivalent to calling .put with each row key / column key / value
        mapping in `table`.

        Arguments
        - table: the table to add to this table
        """
        ...


    def remove(self, rowKey: "Object", columnKey: "Object") -> "V":
        """
        Removes the mapping, if any, associated with the given keys.

        Arguments
        - rowKey: row key of mapping to be removed
        - columnKey: column key of mapping to be removed

        Returns
        - the value previously associated with the keys, or `null` if no such value existed
        """
        ...


    def row(self, rowKey: "R") -> dict["C", "V"]:
        """
        Returns a view of all mappings that have the given row key. For each row
        key / column key / value mapping in the table with that row key, the
        returned map associates the column key with the value. If no mappings in
        the table have the provided row key, an empty map is returned.
        
        Changes to the returned map will update the underlying table, and vice
        versa.

        Arguments
        - rowKey: key of row to search for in the table

        Returns
        - the corresponding map from column keys to values
        """
        ...


    def column(self, columnKey: "C") -> dict["R", "V"]:
        """
        Returns a view of all mappings that have the given column key. For each row
        key / column key / value mapping in the table with that column key, the
        returned map associates the row key with the value. If no mappings in the
        table have the provided column key, an empty map is returned.
        
        Changes to the returned map will update the underlying table, and vice
        versa.

        Arguments
        - columnKey: key of column to search for in the table

        Returns
        - the corresponding map from row keys to values
        """
        ...


    def cellSet(self) -> set["Cell"["R", "C", "V"]]:
        """
        Returns a set of all row key / column key / value triplets. Changes to the
        returned set will update the underlying table, and vice versa. The cell set
        does not support the `add` or `addAll` methods.

        Returns
        - set of table cells consisting of row key / column key / value
            triplets
        """
        ...


    def rowKeySet(self) -> set["R"]:
        """
        Returns a set of row keys that have one or more values in the table.
        Changes to the set will update the underlying table, and vice versa.

        Returns
        - set of row keys
        """
        ...


    def columnKeySet(self) -> set["C"]:
        """
        Returns a set of column keys that have one or more values in the table.
        Changes to the set will update the underlying table, and vice versa.

        Returns
        - set of column keys
        """
        ...


    def values(self) -> Iterable["V"]:
        """
        Returns a collection of all values, which may contain duplicates. Changes
        to the returned collection will update the underlying table, and vice
        versa.

        Returns
        - collection of values
        """
        ...


    def rowMap(self) -> dict["R", dict["C", "V"]]:
        """
        Returns a view that associates each row key with the corresponding map from
        column keys to values. Changes to the returned map will update this table.
        The returned map does not support `put()` or `putAll()`, or
        `setValue()` on its entries.
        
        In contrast, the maps returned by `rowMap().get()` have the same
        behavior as those returned by .row. Those maps may support `setValue()`, `put()`, and `putAll()`.

        Returns
        - a map view from each row key to a secondary map from column keys to
            values
        """
        ...


    def columnMap(self) -> dict["C", dict["R", "V"]]:
        """
        Returns a view that associates each column key with the corresponding map
        from row keys to values. Changes to the returned map will update this
        table. The returned map does not support `put()` or `putAll()`,
        or `setValue()` on its entries.
        
        In contrast, the maps returned by `columnMap().get()` have the
        same behavior as those returned by .column. Those maps may support
        `setValue()`, `put()`, and `putAll()`.

        Returns
        - a map view from each column key to a secondary map from row keys to
            values
        """
        ...
