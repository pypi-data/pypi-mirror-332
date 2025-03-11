"""
Python module generated from Java source file com.google.common.graph.BaseGraph

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from typing import Any, Callable, Iterable, Tuple


class BaseGraph(SuccessorsFunction, PredecessorsFunction):
    """
    A non-public interface for the methods shared between Graph and ValueGraph.
    
    Type `<N>`: Node parameter type

    Author(s)
    - James Sexton
    """

    def nodes(self) -> set["N"]:
        """
        Returns all nodes in this graph, in the order specified by .nodeOrder().
        """
        ...


    def edges(self) -> set["EndpointPair"["N"]]:
        """
        Returns all edges in this graph.
        """
        ...


    def isDirected(self) -> bool:
        """
        Returns True if the edges in this graph are directed. Directed edges connect a EndpointPair.source() source node to a EndpointPair.target() target node, while
        undirected edges connect a pair of nodes to each other.
        """
        ...


    def allowsSelfLoops(self) -> bool:
        """
        Returns True if this graph allows self-loops (edges that connect a node to itself). Attempting
        to add a self-loop to a graph that does not allow them will throw an IllegalArgumentException.
        """
        ...


    def nodeOrder(self) -> "ElementOrder"["N"]:
        """
        Returns the order of iteration for the elements of .nodes().
        """
        ...


    def incidentEdgeOrder(self) -> "ElementOrder"["N"]:
        """
        Returns an ElementOrder that specifies the order of iteration for the elements of
        .edges(), .adjacentNodes(Object), .predecessors(Object), .successors(Object) and .incidentEdges(Object).

        Since
        - 29.0
        """
        ...


    def adjacentNodes(self, node: "N") -> set["N"]:
        """
        Returns a live view of the nodes which have an incident edge in common with `node` in
        this graph.
        
        This is equal to the union of .predecessors(Object) and .successors(Object).
        
        If `node` is removed from the graph after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `node` is re-added to the graph after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...


    def predecessors(self, node: "N") -> set["N"]:
        """
        Returns a live view of all nodes in this graph adjacent to `node` which can be reached by
        traversing `node`'s incoming edges *against* the direction (if any) of the edge.
        
        In an undirected graph, this is equivalent to .adjacentNodes(Object).
        
        If `node` is removed from the graph after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `node` is re-added to the graph after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...


    def successors(self, node: "N") -> set["N"]:
        """
        Returns a live view of all nodes in this graph adjacent to `node` which can be reached by
        traversing `node`'s outgoing edges in the direction (if any) of the edge.
        
        In an undirected graph, this is equivalent to .adjacentNodes(Object).
        
        This is *not* the same as "all nodes reachable from `node` by following outgoing
        edges". For that functionality, see Graphs.reachableNodes(Graph, Object).
        
        If `node` is removed from the graph after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `node` is re-added to the graph after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...


    def incidentEdges(self, node: "N") -> set["EndpointPair"["N"]]:
        """
        Returns a live view of the edges in this graph whose endpoints include `node`.
        
        This is equal to the union of incoming and outgoing edges.
        
        If `node` is removed from the graph after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `node` is re-added to the graph after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph

        Since
        - 24.0
        """
        ...


    def degree(self, node: "N") -> int:
        """
        Returns the count of `node`'s incident edges, counting self-loops twice (equivalently,
        the number of times an edge touches `node`).
        
        For directed graphs, this is equal to `inDegree(node) + outDegree(node)`.
        
        For undirected graphs, this is equal to `incidentEdges(node).size()` + (number of
        self-loops incident to `node`).
        
        If the count is greater than `Integer.MAX_VALUE`, returns `Integer.MAX_VALUE`.

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...


    def inDegree(self, node: "N") -> int:
        """
        Returns the count of `node`'s incoming edges (equal to `predecessors(node).size()`)
        in a directed graph. In an undirected graph, returns the .degree(Object).
        
        If the count is greater than `Integer.MAX_VALUE`, returns `Integer.MAX_VALUE`.

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...


    def outDegree(self, node: "N") -> int:
        """
        Returns the count of `node`'s outgoing edges (equal to `successors(node).size()`)
        in a directed graph. In an undirected graph, returns the .degree(Object).
        
        If the count is greater than `Integer.MAX_VALUE`, returns `Integer.MAX_VALUE`.

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...


    def hasEdgeConnecting(self, nodeU: "N", nodeV: "N") -> bool:
        """
        Returns True if there is an edge that directly connects `nodeU` to `nodeV`. This is
        equivalent to `nodes().contains(nodeU) && successors(nodeU).contains(nodeV)`.
        
        In an undirected graph, this is equal to `hasEdgeConnecting(nodeV, nodeU)`.

        Since
        - 23.0
        """
        ...


    def hasEdgeConnecting(self, endpoints: "EndpointPair"["N"]) -> bool:
        """
        Returns True if there is an edge that directly connects `endpoints` (in the order, if
        any, specified by `endpoints`). This is equivalent to `edges().contains(endpoints)`.
        
        Unlike the other `EndpointPair`-accepting methods, this method does not throw if the
        endpoints are unordered; it simply returns False. This is for consistency with the behavior of
        Collection.contains(Object) (which does not generally throw if the object cannot be
        present in the collection), and the desire to have this method's behavior be compatible with
        `edges().contains(endpoints)`.

        Since
        - 27.1
        """
        ...
