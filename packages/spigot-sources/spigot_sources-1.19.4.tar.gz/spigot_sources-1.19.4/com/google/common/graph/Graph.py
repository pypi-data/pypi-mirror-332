"""
Python module generated from Java source file com.google.common.graph.Graph

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from com.google.errorprone.annotations import DoNotMock
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Graph(BaseGraph):
    """
    An interface for <a
    href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)">graph</a>-structured data,
    whose edges are anonymous entities with no identity or information of their own.
    
    A graph is composed of a set of nodes and a set of edges connecting pairs of nodes.
    
    There are three primary interfaces provided to represent graphs. In order of increasing
    complexity they are: Graph, ValueGraph, and Network. You should generally
    prefer the simplest interface that satisfies your use case. See the <a
    href="https://github.com/google/guava/wiki/GraphsExplained#choosing-the-right-graph-type">
    "Choosing the right graph type"</a> section of the Guava User Guide for more details.
    
    <h3>Capabilities</h3>
    
    `Graph` supports the following use cases (<a
    href="https://github.com/google/guava/wiki/GraphsExplained#definitions">definitions of
    terms</a>):
    
    
      - directed graphs
      - undirected graphs
      - graphs that do/don't allow self-loops
      - graphs whose nodes/edges are insertion-ordered, sorted, or unordered
    
    
    `Graph` explicitly does not support parallel edges, and forbids implementations or
    extensions with parallel edges. If you need parallel edges, use Network.
    
    <h3>Building a `Graph`</h3>
    
    The implementation classes that `common.graph` provides are not public, by design. To
    create an instance of one of the built-in implementations of `Graph`, use the GraphBuilder class:
    
    ````MutableGraph<Integer> graph = GraphBuilder.undirected().build();````
    
    GraphBuilder.build() returns an instance of MutableGraph, which is a subtype
    of `Graph` that provides methods for adding and removing nodes and edges. If you do not
    need to mutate a graph (e.g. if you write a method than runs a read-only algorithm on the graph),
    you should use the non-mutating Graph interface, or an ImmutableGraph.
    
    You can create an immutable copy of an existing `Graph` using ImmutableGraph.copyOf(Graph):
    
    ````ImmutableGraph<Integer> immutableGraph = ImmutableGraph.copyOf(graph);````
    
    Instances of ImmutableGraph do not implement MutableGraph (obviously!) and are
    contractually guaranteed to be unmodifiable and thread-safe.
    
    The Guava User Guide has <a
    href="https://github.com/google/guava/wiki/GraphsExplained#building-graph-instances">more
    information on (and examples of) building graphs</a>.
    
    <h3>Additional documentation</h3>
    
    See the Guava User Guide for the `common.graph` package (<a
    href="https://github.com/google/guava/wiki/GraphsExplained">"Graphs Explained"</a>) for
    additional documentation, including:
    
    
      - <a
          href="https://github.com/google/guava/wiki/GraphsExplained#equals-hashcode-and-graph-equivalence">
          `equals()`, `hashCode()`, and graph equivalence</a>
      - <a href="https://github.com/google/guava/wiki/GraphsExplained#synchronization">
          Synchronization policy</a>
      - <a href="https://github.com/google/guava/wiki/GraphsExplained#notes-for-implementors">Notes
          for implementors</a>
    
    
    Type `<N>`: Node parameter type

    Author(s)
    - Joshua O'Madadhain

    Since
    - 20.0
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
        Returns the nodes which have an incident edge in common with `node` in this graph.
        
        This is equal to the union of .predecessors(Object) and .successors(Object).

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...


    def predecessors(self, node: "N") -> set["N"]:
        """
        Returns all nodes in this graph adjacent to `node` which can be reached by traversing
        `node`'s incoming edges *against* the direction (if any) of the edge.
        
        In an undirected graph, this is equivalent to .adjacentNodes(Object).

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...


    def successors(self, node: "N") -> set["N"]:
        """
        Returns all nodes in this graph adjacent to `node` which can be reached by traversing
        `node`'s outgoing edges in the direction (if any) of the edge.
        
        In an undirected graph, this is equivalent to .adjacentNodes(Object).
        
        This is *not* the same as "all nodes reachable from `node` by following outgoing
        edges". For that functionality, see Graphs.reachableNodes(Graph, Object).

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...


    def incidentEdges(self, node: "N") -> set["EndpointPair"["N"]]:
        """
        Returns the edges in this graph whose endpoints include `node`.
        
        This is equal to the union of incoming and outgoing edges.

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
        endpoints are unordered and the graph is directed; it simply returns `False`. This is for
        consistency with the behavior of Collection.contains(Object) (which does not generally
        throw if the object cannot be present in the collection), and the desire to have this method's
        behavior be compatible with `edges().contains(endpoints)`.

        Since
        - 27.1
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Returns `True` iff `object` is a Graph that has the same elements and the
        same structural relationships as those in this graph.
        
        Thus, two graphs A and B are equal if **all** of the following are True:
        
        
          - A and B have equal .isDirected() directedness.
          - A and B have equal .nodes() node sets.
          - A and B have equal .edges() edge sets.
        
        
        Graph properties besides .isDirected() directedness do **not** affect equality.
        For example, two graphs may be considered equal even if one allows self-loops and the other
        doesn't. Additionally, the order in which nodes or edges are added to the graph, and the order
        in which they are iterated over, are irrelevant.
        
        A reference implementation of this is provided by AbstractGraph.equals(Object).
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code for this graph. The hash code of a graph is defined as the hash code of
        the set returned by .edges().
        
        A reference implementation of this is provided by AbstractGraph.hashCode().
        """
        ...
