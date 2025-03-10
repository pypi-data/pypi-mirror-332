"""
Python module generated from Java source file com.google.common.graph.ElementOrder

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import MoreObjects
from com.google.common.base.MoreObjects import ToStringHelper
from com.google.common.base import Objects
from com.google.common.collect import Maps
from com.google.common.collect import Ordering
from com.google.common.graph import *
from enum import Enum
from java.util import Comparator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ElementOrder:
    """
    Used to represent the order of elements in a data structure that supports different options for
    iteration order guarantees.
    
    Example usage:
    
    ````MutableGraph<Integer> graph =
        GraphBuilder.directed().nodeOrder(ElementOrder.<Integer>natural()).build();````

    Author(s)
    - Joshua O'Madadhain

    Since
    - 20.0
    """

    @staticmethod
    def unordered() -> "ElementOrder"["S"]:
        """
        Returns an instance which specifies that no ordering is guaranteed.
        """
        ...


    @staticmethod
    def insertion() -> "ElementOrder"["S"]:
        """
        Returns an instance which specifies that insertion ordering is guaranteed.
        """
        ...


    @staticmethod
    def natural() -> "ElementOrder"["S"]:
        """
        Returns an instance which specifies that the natural ordering of the elements is guaranteed.
        """
        ...


    @staticmethod
    def sorted(comparator: "Comparator"["S"]) -> "ElementOrder"["S"]:
        """
        Returns an instance which specifies that the ordering of the elements is guaranteed to be
        determined by `comparator`.
        """
        ...


    def type(self) -> "Type":
        """
        Returns the type of ordering used.
        """
        ...


    def comparator(self) -> "Comparator"["T"]:
        """
        Returns the Comparator used.

        Raises
        - UnsupportedOperationException: if comparator is not defined
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    class Type(Enum):
        """
        The type of ordering that this object specifies.
        
        
        - UNORDERED: no order is guaranteed.
        - INSERTION: insertion ordering is guaranteed.
        - SORTED: ordering according to a supplied comparator is guaranteed.
        """

        UNORDERED = 0
        INSERTION = 1
        SORTED = 2
