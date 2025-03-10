"""
Python module generated from Java source file com.google.common.graph.GraphConnections

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Iterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class GraphConnections:
    """
    An interface for representing and manipulating an origin node's adjacent nodes and edge values in
    a Graph.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - James Sexton
    """

    def adjacentNodes(self) -> set["N"]:
        ...


    def predecessors(self) -> set["N"]:
        ...


    def successors(self) -> set["N"]:
        ...


    def incidentEdgeIterator(self, thisNode: "N") -> Iterator["EndpointPair"["N"]]:
        """
        Returns an iterator over the incident edges.

        Arguments
        - thisNode: The node that this all of the connections in this class are connected to.
        """
        ...


    def value(self, node: "N") -> "V":
        """
        Returns the value associated with the edge connecting the origin node to `node`, or null
        if there is no such edge.
        """
        ...


    def removePredecessor(self, node: "N") -> None:
        """
        Remove `node` from the set of predecessors.
        """
        ...


    def removeSuccessor(self, node: "N") -> "V":
        """
        Remove `node` from the set of successors. Returns the value previously associated with
        the edge connecting the two nodes.
        """
        ...


    def addPredecessor(self, node: "N", value: "V") -> None:
        """
        Add `node` as a predecessor to the origin node. In the case of an undirected graph, it
        also becomes a successor. Associates `value` with the edge connecting the two nodes.
        """
        ...


    def addSuccessor(self, node: "N", value: "V") -> "V":
        """
        Add `node` as a successor to the origin node. In the case of an undirected graph, it also
        becomes a predecessor. Associates `value` with the edge connecting the two nodes. Returns
        the value previously associated with the edge connecting the two nodes.
        """
        ...
