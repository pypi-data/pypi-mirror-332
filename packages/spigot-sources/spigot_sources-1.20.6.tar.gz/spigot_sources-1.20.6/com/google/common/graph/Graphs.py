"""
Python module generated from Java source file com.google.common.graph.Graphs

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Objects
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Iterables
from com.google.common.collect import Iterators
from com.google.common.collect import Maps
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Iterator
from java.util import Optional
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Graphs:
    """
    Static utility methods for Graph, ValueGraph, and Network instances.

    Author(s)
    - Joshua O'Madadhain

    Since
    - 20.0
    """

    @staticmethod
    def hasCycle(graph: "Graph"["N"]) -> bool:
        """
        Returns True if `graph` has at least one cycle. A cycle is defined as a non-empty subset
        of edges in a graph arranged to form a path (a sequence of adjacent outgoing edges) starting
        and ending with the same node.
        
        This method will detect any non-empty cycle, including self-loops (a cycle of length 1).
        """
        ...


    @staticmethod
    def hasCycle(network: "Network"[Any, Any]) -> bool:
        """
        Returns True if `network` has at least one cycle. A cycle is defined as a non-empty
        subset of edges in a graph arranged to form a path (a sequence of adjacent outgoing edges)
        starting and ending with the same node.
        
        This method will detect any non-empty cycle, including self-loops (a cycle of length 1).
        """
        ...


    @staticmethod
    def transitiveClosure(graph: "Graph"["N"]) -> "Graph"["N"]:
        ...


    @staticmethod
    def reachableNodes(graph: "Graph"["N"], node: "N") -> set["N"]:
        """
        Returns the set of nodes that are reachable from `node`. Node B is defined as reachable
        from node A if there exists a path (a sequence of adjacent outgoing edges) starting at node A
        and ending at node B. Note that a node is always reachable from itself via a zero-length path.
        
        This is a "snapshot" based on the current topology of `graph`, rather than a live view
        of the set of nodes reachable from `node`. In other words, the returned Set will
        not be updated after modifications to `graph`.

        Raises
        - IllegalArgumentException: if `node` is not present in `graph`
        """
        ...


    @staticmethod
    def transpose(graph: "Graph"["N"]) -> "Graph"["N"]:
        """
        Returns a view of `graph` with the direction (if any) of every edge reversed. All other
        properties remain intact, and further updates to `graph` will be reflected in the view.
        """
        ...


    @staticmethod
    def transpose(graph: "ValueGraph"["N", "V"]) -> "ValueGraph"["N", "V"]:
        """
        Returns a view of `graph` with the direction (if any) of every edge reversed. All other
        properties remain intact, and further updates to `graph` will be reflected in the view.
        """
        ...


    @staticmethod
    def transpose(network: "Network"["N", "E"]) -> "Network"["N", "E"]:
        """
        Returns a view of `network` with the direction (if any) of every edge reversed. All other
        properties remain intact, and further updates to `network` will be reflected in the view.
        """
        ...


    @staticmethod
    def inducedSubgraph(graph: "Graph"["N"], nodes: Iterable["N"]) -> "MutableGraph"["N"]:
        """
        Returns the subgraph of `graph` induced by `nodes`. This subgraph is a new graph
        that contains all of the nodes in `nodes`, and all of the Graph.edges() edges
        from `graph` for which both nodes are contained by `nodes`.

        Raises
        - IllegalArgumentException: if any element in `nodes` is not a node in the graph
        """
        ...


    @staticmethod
    def inducedSubgraph(graph: "ValueGraph"["N", "V"], nodes: Iterable["N"]) -> "MutableValueGraph"["N", "V"]:
        """
        Returns the subgraph of `graph` induced by `nodes`. This subgraph is a new graph
        that contains all of the nodes in `nodes`, and all of the Graph.edges() edges
        (and associated edge values) from `graph` for which both nodes are contained by `nodes`.

        Raises
        - IllegalArgumentException: if any element in `nodes` is not a node in the graph
        """
        ...


    @staticmethod
    def inducedSubgraph(network: "Network"["N", "E"], nodes: Iterable["N"]) -> "MutableNetwork"["N", "E"]:
        """
        Returns the subgraph of `network` induced by `nodes`. This subgraph is a new graph
        that contains all of the nodes in `nodes`, and all of the Network.edges() edges
        from `network` for which the Network.incidentNodes(Object) incident nodes are
        both contained by `nodes`.

        Raises
        - IllegalArgumentException: if any element in `nodes` is not a node in the graph
        """
        ...


    @staticmethod
    def copyOf(graph: "Graph"["N"]) -> "MutableGraph"["N"]:
        """
        Creates a mutable copy of `graph` with the same nodes and edges.
        """
        ...


    @staticmethod
    def copyOf(graph: "ValueGraph"["N", "V"]) -> "MutableValueGraph"["N", "V"]:
        """
        Creates a mutable copy of `graph` with the same nodes, edges, and edge values.
        """
        ...


    @staticmethod
    def copyOf(network: "Network"["N", "E"]) -> "MutableNetwork"["N", "E"]:
        """
        Creates a mutable copy of `network` with the same nodes and edges.
        """
        ...
