"""
Python module generated from Java source file com.google.common.graph.ConfigurableValueGraph

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ConfigurableValueGraph(AbstractValueGraph):
    """
    Configurable implementation of ValueGraph that supports the options supplied by AbstractGraphBuilder.
    
    This class maintains a map of nodes to GraphConnections.
    
    Collection-returning accessors return unmodifiable views: the view returned will reflect
    changes to the graph (if the graph is mutable) but may not be modified by the user.
    
    The time complexity of all collection-returning accessors is O(1), since views are returned.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - Omar Darwish
    """

    def nodes(self) -> set["N"]:
        ...


    def isDirected(self) -> bool:
        ...


    def allowsSelfLoops(self) -> bool:
        ...


    def nodeOrder(self) -> "ElementOrder"["N"]:
        ...


    def adjacentNodes(self, node: "Object") -> set["N"]:
        ...


    def predecessors(self, node: "Object") -> set["N"]:
        ...


    def successors(self, node: "Object") -> set["N"]:
        ...


    def edgeValueOrDefault(self, nodeU: "Object", nodeV: "Object", defaultValue: "V") -> "V":
        ...
