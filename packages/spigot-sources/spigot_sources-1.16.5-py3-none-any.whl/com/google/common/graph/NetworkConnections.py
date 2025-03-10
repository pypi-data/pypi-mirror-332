"""
Python module generated from Java source file com.google.common.graph.NetworkConnections

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from typing import Any, Callable, Iterable, Tuple


class NetworkConnections:
    """
    An interface for representing and manipulating an origin node's adjacent nodes and incident edges
    in a Network.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - James Sexton
    """

    def adjacentNodes(self) -> set["N"]:
        ...


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


    def edgesConnecting(self, node: "Object") -> set["E"]:
        """
        Returns the set of edges connecting the origin node to `node`. For networks without
        parallel edges, this set cannot be of size greater than one.
        """
        ...


    def oppositeNode(self, edge: "Object") -> "N":
        """
        Returns the node that is opposite the origin node along `edge`.
        
        In the directed case, `edge` is assumed to be an outgoing edge.
        """
        ...


    def removeInEdge(self, edge: "Object", isSelfLoop: bool) -> "N":
        """
        Remove `edge` from the set of incoming edges. Returns the former predecessor node.
        
        In the undirected case, returns `null` if `isSelfLoop` is True.
        """
        ...


    def removeOutEdge(self, edge: "Object") -> "N":
        """
        Remove `edge` from the set of outgoing edges. Returns the former successor node.
        """
        ...


    def addInEdge(self, edge: "E", node: "N", isSelfLoop: bool) -> None:
        """
        Add `edge` to the set of incoming edges. Implicitly adds `node` as a predecessor.
        """
        ...


    def addOutEdge(self, edge: "E", node: "N") -> None:
        """
        Add `edge` to the set of outgoing edges. Implicitly adds `node` as a successor.
        """
        ...
