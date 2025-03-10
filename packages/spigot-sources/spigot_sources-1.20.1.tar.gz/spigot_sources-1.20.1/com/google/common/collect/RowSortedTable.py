"""
Python module generated from Java source file com.google.common.collect.RowSortedTable

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import SortedMap
from java.util import SortedSet
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RowSortedTable(Table):
    """
    Interface that extends `Table` and whose rows are sorted.
    
    The .rowKeySet method returns a SortedSet and the .rowMap method
    returns a SortedMap, instead of the Set and Map specified by the Table interface.

    Author(s)
    - Warren Dukes

    Since
    - 8.0
    """

    def rowKeySet(self) -> "SortedSet"["R"]:
        """
        
        
        This method returns a SortedSet, instead of the `Set` specified in the Table interface.
        """
        ...


    def rowMap(self) -> "SortedMap"["R", dict["C", "V"]]:
        """
        
        
        This method returns a SortedMap, instead of the `Map` specified in the Table interface.
        """
        ...
