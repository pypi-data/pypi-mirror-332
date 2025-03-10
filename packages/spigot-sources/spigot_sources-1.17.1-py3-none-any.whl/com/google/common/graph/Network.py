"""
Python module generated from Java source file com.google.common.graph.Network

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from com.google.errorprone.annotations import CompatibleWith
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Network:
    """
    An interface for <a
    href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)">graph</a>-structured data,
    whose edges are unique objects.
    
    A graph is composed of a set of nodes and a set of edges connecting pairs of nodes.
    
    There are three main interfaces provided to represent graphs. In order of increasing
    complexity they are: Graph, ValueGraph, and Network. You should generally
    prefer the simplest interface that satisfies your use case. See the <a
    href="https://github.com/google/guava/wiki/GraphsExplained#choosing-the-right-graph-type">
    "Choosing the right graph type"</a> section of the Guava User Guide for more details.
    
    <h3>Capabilities</h3>
    
    `Network` supports the following use cases (<a
    href="https://github.com/google/guava/wiki/GraphsExplained#definitions">definitions of
    terms</a>):
    
    
      - directed graphs
      - undirected graphs
      - graphs that do/don't allow parallel edges
      - graphs that do/don't allow self-loops
      - graphs whose nodes/edges are insertion-ordered, sorted, or unordered
      - graphs whose edges are unique objects
    
    
    <h3>Building a `Network`</h3>
    
    The implementation classes that `common.graph` provides are not public, by design. To create
    an instance of one of the built-in implementations of `Network`, use the NetworkBuilder class:
    
    ````MutableNetwork<Integer, MyEdge> graph = NetworkBuilder.directed().build();````
    
    NetworkBuilder.build() returns an instance of MutableNetwork, which is a
    subtype of `Network` that provides methods for adding and removing nodes and edges. If you
    do not need to mutate a graph (e.g. if you write a method than runs a read-only algorithm on the
    graph), you should use the non-mutating Network interface, or an ImmutableNetwork.
    
    You can create an immutable copy of an existing `Network` using ImmutableNetwork.copyOf(Network):
    
    ````ImmutableNetwork<Integer, MyEdge> immutableGraph = ImmutableNetwork.copyOf(graph);````
    
    Instances of ImmutableNetwork do not implement MutableNetwork (obviously!) and
    are contractually guaranteed to be unmodifiable and thread-safe.
    
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
    
    Type `<E>`: Edge parameter type

    Author(s)
    - Joshua O'Madadhain

    Since
    - 20.0
    """

    def nodes(self) -> set["N"]:
        """
        Returns all nodes in this network, in the order specified by .nodeOrder().
        """
        ...


    def edges(self) -> set["E"]:
        """
        Returns all edges in this network, in the order specified by .edgeOrder().
        """
        ...


    def asGraph(self) -> "Graph"["N"]:
        """
        Returns a live view of this network as a Graph. The resulting Graph will have
        an edge connecting node A to node B if this Network has an edge connecting A to B.
        
        If this network .allowsParallelEdges() allows parallel edges, parallel edges will be
        treated as if collapsed into a single edge. For example, the .degree(Object) of a node
        in the Graph view may be less than the degree of the same node in this Network.
        """
        ...


    def isDirected(self) -> bool:
        """
        Returns True if the edges in this network are directed. Directed edges connect a EndpointPair.source() source node to a EndpointPair.target() target node, while
        undirected edges connect a pair of nodes to each other.
        """
        ...


    def allowsParallelEdges(self) -> bool:
        """
        Returns True if this network allows parallel edges. Attempting to add a parallel edge to a
        network that does not allow them will throw an UnsupportedOperationException.
        """
        ...


    def allowsSelfLoops(self) -> bool:
        """
        Returns True if this network allows self-loops (edges that connect a node to itself).
        Attempting to add a self-loop to a network that does not allow them will throw an UnsupportedOperationException.
        """
        ...


    def nodeOrder(self) -> "ElementOrder"["N"]:
        """
        Returns the order of iteration for the elements of .nodes().
        """
        ...


    def edgeOrder(self) -> "ElementOrder"["E"]:
        """
        Returns the order of iteration for the elements of .edges().
        """
        ...


    def adjacentNodes(self, node: "Object") -> set["N"]:
        """
        Returns the nodes which have an incident edge in common with `node` in this network.

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def predecessors(self, node: "Object") -> set["N"]:
        """
        Returns all nodes in this network adjacent to `node` which can be reached by traversing
        `node`'s incoming edges *against* the direction (if any) of the edge.
        
        In an undirected network, this is equivalent to .adjacentNodes(Object).

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def successors(self, node: "Object") -> set["N"]:
        """
        Returns all nodes in this network adjacent to `node` which can be reached by traversing
        `node`'s outgoing edges in the direction (if any) of the edge.
        
        In an undirected network, this is equivalent to .adjacentNodes(Object).
        
        This is *not* the same as "all nodes reachable from `node` by following outgoing
        edges". For that functionality, see Graphs.reachableNodes(Graph, Object).

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def incidentEdges(self, node: "Object") -> set["E"]:
        """
        Returns the edges whose .incidentNodes(Object) incident nodes in this network include
        `node`.

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def inEdges(self, node: "Object") -> set["E"]:
        """
        Returns all edges in this network which can be traversed in the direction (if any) of the edge
        to end at `node`.
        
        In a directed network, an incoming edge's EndpointPair.target() equals `node`.
        
        In an undirected network, this is equivalent to .incidentEdges(Object).

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def outEdges(self, node: "Object") -> set["E"]:
        """
        Returns all edges in this network which can be traversed in the direction (if any) of the edge
        starting from `node`.
        
        In a directed network, an outgoing edge's EndpointPair.source() equals `node`.
        
        In an undirected network, this is equivalent to .incidentEdges(Object).

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def degree(self, node: "Object") -> int:
        """
        Returns the count of `node`'s .incidentEdges(Object) incident edges, counting
        self-loops twice (equivalently, the number of times an edge touches `node`).
        
        For directed networks, this is equal to `inDegree(node) + outDegree(node)`.
        
        For undirected networks, this is equal to `incidentEdges(node).size()` + (number of
        self-loops incident to `node`).
        
        If the count is greater than `Integer.MAX_VALUE`, returns `Integer.MAX_VALUE`.

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def inDegree(self, node: "Object") -> int:
        """
        Returns the count of `node`'s .inEdges(Object) incoming edges in a directed
        network. In an undirected network, returns the .degree(Object).
        
        If the count is greater than `Integer.MAX_VALUE`, returns `Integer.MAX_VALUE`.

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def outDegree(self, node: "Object") -> int:
        """
        Returns the count of `node`'s .outEdges(Object) outgoing edges in a directed
        network. In an undirected network, returns the .degree(Object).
        
        If the count is greater than `Integer.MAX_VALUE`, returns `Integer.MAX_VALUE`.

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def incidentNodes(self, edge: "Object") -> "EndpointPair"["N"]:
        """
        Returns the nodes which are the endpoints of `edge` in this network.

        Raises
        - IllegalArgumentException: if `edge` is not an element of this network
        """
        ...


    def adjacentEdges(self, edge: "Object") -> set["E"]:
        """
        Returns the edges which have an .incidentNodes(Object) incident node in common with
        `edge`. An edge is not considered adjacent to itself.

        Raises
        - IllegalArgumentException: if `edge` is not an element of this network
        """
        ...


    def edgesConnecting(self, nodeU: "Object", nodeV: "Object") -> set["E"]:
        """
        Returns the set of edges directly connecting `nodeU` to `nodeV`.
        
        In an undirected network, this is equal to `edgesConnecting(nodeV, nodeU)`.
        
        The resulting set of edges will be parallel (i.e. have equal .incidentNodes(Object).
        If this network does not .allowsParallelEdges() allow parallel edges, the resulting set
        will contain at most one edge.

        Raises
        - IllegalArgumentException: if `nodeU` or `nodeV` is not an element of this
            network
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        For the default Network implementations, returns True if `this == object`
        (reference equality). External implementations are free to define this method as they see fit,
        as long as they satisfy the Object.equals(Object) contract.
        
        To compare two Networks based on their contents rather than their references, see
        Graphs.equivalent(Network, Network).
        """
        ...


    def hashCode(self) -> int:
        """
        For the default Network implementations, returns `System.identityHashCode(this)`.
        External implementations are free to define this method as they see fit, as long as they
        satisfy the Object.hashCode() contract.
        """
        ...
