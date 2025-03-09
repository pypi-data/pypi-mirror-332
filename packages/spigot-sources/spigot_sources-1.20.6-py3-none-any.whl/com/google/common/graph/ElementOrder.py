"""
Python module generated from Java source file com.google.common.graph.ElementOrder

Java source file obtained from artifact guava version 32.1.2-jre

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
from com.google.errorprone.annotations import Immutable
from enum import Enum
from java.util import Comparator
from javax.annotation import CheckForNull
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
    def stable() -> "ElementOrder"["S"]:
        """
        Returns an instance which specifies that ordering is guaranteed to be always be the same across
        iterations, and across releases. Some methods may have stronger guarantees.
        
        This instance is only useful in combination with `incidentEdgeOrder`, e.g. `graphBuilder.incidentEdgeOrder(ElementOrder.stable())`.
        
        <h3>In combination with `incidentEdgeOrder`</h3>
        
        `incidentEdgeOrder(ElementOrder.stable())` guarantees the ordering of the returned
        collections of the following methods:
        
        
          - For Graph and ValueGraph:
              
                - `edges()`: Stable order
                - `adjacentNodes(node)`: Connecting edge insertion order
                - `predecessors(node)`: Connecting edge insertion order
                - `successors(node)`: Connecting edge insertion order
                - `incidentEdges(node)`: Edge insertion order
              
          - For Network:
              
                - `adjacentNodes(node)`: Stable order
                - `predecessors(node)`: Connecting edge insertion order
                - `successors(node)`: Connecting edge insertion order
                - `incidentEdges(node)`: Stable order
                - `inEdges(node)`: Edge insertion order
                - `outEdges(node)`: Edge insertion order
                - `adjacentEdges(edge)`: Stable order
                - `edgesConnecting(nodeU, nodeV)`: Edge insertion order
              

        Since
        - 29.0
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
          - STABLE: ordering is guaranteed to follow a pattern that won't change between releases.
              Some methods may have stronger guarantees.
          - INSERTION: insertion ordering is guaranteed.
          - SORTED: ordering according to a supplied comparator is guaranteed.
        """

        UNORDERED = 0
        STABLE = 1
        INSERTION = 2
        SORTED = 3
