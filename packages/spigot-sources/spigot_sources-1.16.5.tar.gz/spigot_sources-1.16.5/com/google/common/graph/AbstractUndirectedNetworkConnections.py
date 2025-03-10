"""
Python module generated from Java source file com.google.common.graph.AbstractUndirectedNetworkConnections

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from java.util import Collections
from typing import Any, Callable, Iterable, Tuple


class AbstractUndirectedNetworkConnections(NetworkConnections):
    """
    A base implementation of NetworkConnections for undirected networks.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - James Sexton
    """

    def predecessors(self) -> set["N"]:
        ...


    def successors(self) -> set["N"]:
        ...


    def incidentEdges(self) -> set["E"]:
        ...


    def inEdges(self) -> set["E"]:
        ...


    def outEdges(self) -> set["E"]:
        ...


    def oppositeNode(self, edge: "Object") -> "N":
        ...


    def removeInEdge(self, edge: "Object", isSelfLoop: bool) -> "N":
        ...


    def removeOutEdge(self, edge: "Object") -> "N":
        ...


    def addInEdge(self, edge: "E", node: "N", isSelfLoop: bool) -> None:
        ...


    def addOutEdge(self, edge: "E", node: "N") -> None:
        ...
