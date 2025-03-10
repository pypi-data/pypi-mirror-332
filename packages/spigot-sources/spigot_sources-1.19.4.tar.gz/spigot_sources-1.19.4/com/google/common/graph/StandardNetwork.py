"""
Python module generated from Java source file com.google.common.graph.StandardNetwork

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableSet
from com.google.common.graph import *
from typing import Any, Callable, Iterable, Tuple


class StandardNetwork(AbstractNetwork):
    """
    Standard implementation of Network that supports the options supplied by NetworkBuilder.
    
    This class maintains a map of nodes to NetworkConnections. This class also maintains a
    map of edges to reference nodes. The reference node is defined to be the edge's source node on
    directed graphs, and an arbitrary endpoint of the edge on undirected graphs.
    
    Collection-returning accessors return unmodifiable views: the view returned will reflect
    changes to the graph (if the graph is mutable) but may not be modified by the user.
    
    The time complexity of all collection-returning accessors is O(1), since views are returned.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - Omar Darwish
    """

    def nodes(self) -> set["N"]:
        ...


    def edges(self) -> set["E"]:
        ...


    def isDirected(self) -> bool:
        ...


    def allowsParallelEdges(self) -> bool:
        ...


    def allowsSelfLoops(self) -> bool:
        ...


    def nodeOrder(self) -> "ElementOrder"["N"]:
        ...


    def edgeOrder(self) -> "ElementOrder"["E"]:
        ...


    def incidentEdges(self, node: "N") -> set["E"]:
        ...


    def incidentNodes(self, edge: "E") -> "EndpointPair"["N"]:
        ...


    def adjacentNodes(self, node: "N") -> set["N"]:
        ...


    def edgesConnecting(self, nodeU: "N", nodeV: "N") -> set["E"]:
        ...


    def inEdges(self, node: "N") -> set["E"]:
        ...


    def outEdges(self, node: "N") -> set["E"]:
        ...


    def predecessors(self, node: "N") -> set["N"]:
        ...


    def successors(self, node: "N") -> set["N"]:
        ...
