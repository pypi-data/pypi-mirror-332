"""
Python module generated from Java source file com.google.common.collect.StandardRowSortedTable

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Supplier
from com.google.common.collect import *
from com.google.j2objc.annotations import WeakOuter
from java.util import Comparator
from java.util import SortedMap
from java.util import SortedSet
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class StandardRowSortedTable(StandardTable, RowSortedTable):
    """
    Implementation of `Table` whose iteration ordering across row keys is sorted by their
    natural ordering or by a supplied comparator. Note that iterations across the columns keys for a
    single row key may or may not be ordered, depending on the implementation. When rows and columns
    are both sorted, it's easier to use the TreeBasedTable subclass.
    
    The .rowKeySet method returns a SortedSet and the .rowMap method
    returns a SortedMap, instead of the Set and Map specified by the Table interface.
    
    Null keys and values are not supported.
    
    See the StandardTable superclass for more information about the behavior of this
    class.

    Author(s)
    - Jared Levy
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
