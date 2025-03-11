"""
Python module generated from Java source file com.google.common.collect.SortedLists

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Function
from com.google.common.collect import *
from java.util import Collections
from java.util import Comparator
from java.util import RandomAccess
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class SortedLists:
    """
    Static methods pertaining to sorted List instances.
    
    In this documentation, the terms *greatest*, *greater*, *least*, and
    *lesser* are considered to refer to the comparator on the elements, and the terms
    *first* and *last* are considered to refer to the elements' ordering in a list.

    Author(s)
    - Louis Wasserman
    """

    @staticmethod
    def binarySearch(list: list["E"], e: "E", presentBehavior: "KeyPresentBehavior", absentBehavior: "KeyAbsentBehavior") -> int:
        """
        Searches the specified naturally ordered list for the specified object using the binary search
        algorithm.
        
        Equivalent to .binarySearch(List, Function, Object, Comparator, KeyPresentBehavior,
        KeyAbsentBehavior) using Ordering.natural.
        """
        ...


    @staticmethod
    def binarySearch(list: list["E"], keyFunction: "Function"["E", "K"], key: "K", presentBehavior: "KeyPresentBehavior", absentBehavior: "KeyAbsentBehavior") -> int:
        """
        Binary searches the list for the specified key, using the specified key function.
        
        Equivalent to .binarySearch(List, Function, Object, Comparator, KeyPresentBehavior,
        KeyAbsentBehavior) using Ordering.natural.
        """
        ...


    @staticmethod
    def binarySearch(list: list["E"], keyFunction: "Function"["E", "K"], key: "K", keyComparator: "Comparator"["K"], presentBehavior: "KeyPresentBehavior", absentBehavior: "KeyAbsentBehavior") -> int:
        """
        Binary searches the list for the specified key, using the specified key function.
        
        Equivalent to .binarySearch(List, Object, Comparator, KeyPresentBehavior,
        KeyAbsentBehavior) using Lists.transform(List, Function) Lists.transform(list,
        keyFunction).
        """
        ...


    @staticmethod
    def binarySearch(list: list["E"], key: "E", comparator: "Comparator"["E"], presentBehavior: "KeyPresentBehavior", absentBehavior: "KeyAbsentBehavior") -> int:
        """
        Searches the specified list for the specified object using the binary search algorithm. The
        list must be sorted into ascending order according to the specified comparator (as by the
        Collections.sort(List, Comparator) Collections.sort(List, Comparator) method), prior to
        making this call. If it is not sorted, the results are undefined.
        
        If there are elements in the list which compare as equal to the key, the choice of KeyPresentBehavior decides which index is returned. If no elements compare as equal to the
        key, the choice of KeyAbsentBehavior decides which index is returned.
        
        This method runs in log(n) time on random-access lists, which offer near-constant-time
        access to each list element.

        Arguments
        - list: the list to be searched.
        - key: the value to be searched for.
        - comparator: the comparator by which the list is ordered.
        - presentBehavior: the specification for what to do if at least one element of the list
            compares as equal to the key.
        - absentBehavior: the specification for what to do if no elements of the list compare as
            equal to the key.

        Returns
        - the index determined by the `KeyPresentBehavior`, if the key is in the list;
            otherwise the index determined by the `KeyAbsentBehavior`.
        """
        ...
