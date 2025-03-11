"""
Python module generated from Java source file com.google.common.graph.Network

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from com.google.errorprone.annotations import DoNotMock
from java.util import Optional
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Network(SuccessorsFunction, PredecessorsFunction):
    """
    An interface for <a
    href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)">graph</a>-structured data,
    whose edges are unique objects.
    
    A graph is composed of a set of nodes and a set of edges connecting pairs of nodes.
    
    There are three primary interfaces provided to represent graphs. In order of increasing
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
    
    The implementation classes that `common.graph` provides are not public, by design. To
    create an instance of one of the built-in implementations of `Network`, use the NetworkBuilder class:
    
    ````MutableNetwork<Integer, MyEdge> network = NetworkBuilder.directed().build();````
    
    NetworkBuilder.build() returns an instance of MutableNetwork, which is a
    subtype of `Network` that provides methods for adding and removing nodes and edges. If you
    do not need to mutate a network (e.g. if you write a method than runs a read-only algorithm on
    the network), you should use the non-mutating Network interface, or an ImmutableNetwork.
    
    You can create an immutable copy of an existing `Network` using ImmutableNetwork.copyOf(Network):
    
    ````ImmutableNetwork<Integer, MyEdge> immutableGraph = ImmutableNetwork.copyOf(network);````
    
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
        network that does not allow them will throw an IllegalArgumentException.
        """
        ...


    def allowsSelfLoops(self) -> bool:
        """
        Returns True if this network allows self-loops (edges that connect a node to itself).
        Attempting to add a self-loop to a network that does not allow them will throw an IllegalArgumentException.
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


    def adjacentNodes(self, node: "N") -> set["N"]:
        """
        Returns a live view of the nodes which have an incident edge in common with `node` in
        this graph.
        
        This is equal to the union of .predecessors(Object) and .successors(Object).
        
        If `node` is removed from the network after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `node` is re-added to the network after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def predecessors(self, node: "N") -> set["N"]:
        """
        Returns a live view of all nodes in this network adjacent to `node` which can be reached
        by traversing `node`'s incoming edges *against* the direction (if any) of the edge.
        
        In an undirected network, this is equivalent to .adjacentNodes(Object).
        
        If `node` is removed from the network after this method is called, the `Set` returned
        by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in
        any way.

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def successors(self, node: "N") -> set["N"]:
        """
        Returns a live view of all nodes in this network adjacent to `node` which can be reached
        by traversing `node`'s outgoing edges in the direction (if any) of the edge.
        
        In an undirected network, this is equivalent to .adjacentNodes(Object).
        
        This is *not* the same as "all nodes reachable from `node` by following outgoing
        edges". For that functionality, see Graphs.reachableNodes(Graph, Object).
        
        If `node` is removed from the network after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `node` is re-added to the network after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def incidentEdges(self, node: "N") -> set["E"]:
        """
        Returns a live view of the edges whose .incidentNodes(Object) incident nodes in this
        network include `node`.
        
        This is equal to the union of .inEdges(Object) and .outEdges(Object).
        
        If `node` is removed from the network after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `node` is re-added to the network after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `node` is not an element of this network

        Since
        - 24.0
        """
        ...


    def inEdges(self, node: "N") -> set["E"]:
        """
        Returns a live view of all edges in this network which can be traversed in the direction (if
        any) of the edge to end at `node`.
        
        In a directed network, an incoming edge's EndpointPair.target() equals `node`.
        
        In an undirected network, this is equivalent to .incidentEdges(Object).
        
        If `node` is removed from the network after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `node` is re-added to the network after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def outEdges(self, node: "N") -> set["E"]:
        """
        Returns a live view of all edges in this network which can be traversed in the direction (if
        any) of the edge starting from `node`.
        
        In a directed network, an outgoing edge's EndpointPair.source() equals `node`.
        
        In an undirected network, this is equivalent to .incidentEdges(Object).
        
        If `node` is removed from the network after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `node` is re-added to the network after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def degree(self, node: "N") -> int:
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


    def inDegree(self, node: "N") -> int:
        """
        Returns the count of `node`'s .inEdges(Object) incoming edges in a directed
        network. In an undirected network, returns the .degree(Object).
        
        If the count is greater than `Integer.MAX_VALUE`, returns `Integer.MAX_VALUE`.

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def outDegree(self, node: "N") -> int:
        """
        Returns the count of `node`'s .outEdges(Object) outgoing edges in a directed
        network. In an undirected network, returns the .degree(Object).
        
        If the count is greater than `Integer.MAX_VALUE`, returns `Integer.MAX_VALUE`.

        Raises
        - IllegalArgumentException: if `node` is not an element of this network
        """
        ...


    def incidentNodes(self, edge: "E") -> "EndpointPair"["N"]:
        """
        Returns the nodes which are the endpoints of `edge` in this network.

        Raises
        - IllegalArgumentException: if `edge` is not an element of this network
        """
        ...


    def adjacentEdges(self, edge: "E") -> set["E"]:
        """
        Returns a live view of the edges which have an .incidentNodes(Object) incident node in
        common with `edge`. An edge is not considered adjacent to itself.
        
        If `edge` is removed from the network after this method is called, the `Set`
        `view` returned by this method will be invalidated, and will throw `IllegalStateException` if it is accessed in any way, with the following exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `edge` is re-added to the network after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if `edge` is not an element of this network
        """
        ...


    def edgesConnecting(self, nodeU: "N", nodeV: "N") -> set["E"]:
        """
        Returns a live view of the set of edges that each directly connect `nodeU` to `nodeV`.
        
        In an undirected network, this is equal to `edgesConnecting(nodeV, nodeU)`.
        
        The resulting set of edges will be parallel (i.e. have equal .incidentNodes(Object)). If this network does not .allowsParallelEdges() allow parallel
        edges, the resulting set will contain at most one edge (equivalent to `edgeConnecting(nodeU, nodeV).asSet()`).
        
        If either `nodeU` or `nodeV` are removed from the network after this method is
        called, the `Set` `view` returned by this method will be invalidated, and will
        throw `IllegalStateException` if it is accessed in any way, with the following
        exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if `nodeU` or `nodeV` are re-added to the network after having been removed,
              `view`'s behavior is undefined

        Raises
        - IllegalArgumentException: if `nodeU` or `nodeV` is not an element of this
            network
        """
        ...


    def edgesConnecting(self, endpoints: "EndpointPair"["N"]) -> set["E"]:
        """
        Returns a live view of the set of edges that each directly connect `endpoints` (in the
        order, if any, specified by `endpoints`).
        
        The resulting set of edges will be parallel (i.e. have equal .incidentNodes(Object)). If this network does not .allowsParallelEdges() allow parallel
        edges, the resulting set will contain at most one edge (equivalent to `edgeConnecting(endpoints).asSet()`).
        
        If this network is directed, `endpoints` must be ordered.
        
        If either element of `endpoints` is removed from the network after this method is
        called, the `Set` `view` returned by this method will be invalidated, and will
        throw `IllegalStateException` if it is accessed in any way, with the following
        exceptions:
        
        
          - `view.equals(view)` evaluates to `True` (but any other `equals()` expression
              involving `view` will throw)
          - `hashCode()` does not throw
          - if either endpoint is re-added to the network after having been removed, `view`'s
              behavior is undefined

        Raises
        - IllegalArgumentException: if either endpoint is not an element of this network
        - IllegalArgumentException: if the endpoints are unordered and the network is directed

        Since
        - 27.1
        """
        ...


    def edgeConnecting(self, nodeU: "N", nodeV: "N") -> "Optional"["E"]:
        """
        Returns the single edge that directly connects `nodeU` to `nodeV`, if one is
        present, or `Optional.empty()` if no such edge exists.
        
        In an undirected network, this is equal to `edgeConnecting(nodeV, nodeU)`.

        Raises
        - IllegalArgumentException: if there are multiple parallel edges connecting `nodeU`
            to `nodeV`
        - IllegalArgumentException: if `nodeU` or `nodeV` is not an element of this
            network

        Since
        - 23.0
        """
        ...


    def edgeConnecting(self, endpoints: "EndpointPair"["N"]) -> "Optional"["E"]:
        """
        Returns the single edge that directly connects `endpoints` (in the order, if any,
        specified by `endpoints`), if one is present, or `Optional.empty()` if no such edge
        exists.
        
        If this network is directed, the endpoints must be ordered.

        Raises
        - IllegalArgumentException: if there are multiple parallel edges connecting `nodeU`
            to `nodeV`
        - IllegalArgumentException: if either endpoint is not an element of this network
        - IllegalArgumentException: if the endpoints are unordered and the network is directed

        Since
        - 27.1
        """
        ...


    def edgeConnectingOrNull(self, nodeU: "N", nodeV: "N") -> "E":
        """
        Returns the single edge that directly connects `nodeU` to `nodeV`, if one is
        present, or `null` if no such edge exists.
        
        In an undirected network, this is equal to `edgeConnectingOrNull(nodeV, nodeU)`.

        Raises
        - IllegalArgumentException: if there are multiple parallel edges connecting `nodeU`
            to `nodeV`
        - IllegalArgumentException: if `nodeU` or `nodeV` is not an element of this
            network

        Since
        - 23.0
        """
        ...


    def edgeConnectingOrNull(self, endpoints: "EndpointPair"["N"]) -> "E":
        """
        Returns the single edge that directly connects `endpoints` (in the order, if any,
        specified by `endpoints`), if one is present, or `null` if no such edge exists.
        
        If this network is directed, the endpoints must be ordered.

        Raises
        - IllegalArgumentException: if there are multiple parallel edges connecting `nodeU`
            to `nodeV`
        - IllegalArgumentException: if either endpoint is not an element of this network
        - IllegalArgumentException: if the endpoints are unordered and the network is directed

        Since
        - 27.1
        """
        ...


    def hasEdgeConnecting(self, nodeU: "N", nodeV: "N") -> bool:
        """
        Returns True if there is an edge that directly connects `nodeU` to `nodeV`. This is
        equivalent to `nodes().contains(nodeU) && successors(nodeU).contains(nodeV)`, and to
        `edgeConnectingOrNull(nodeU, nodeV) != null`.
        
        In an undirected network, this is equal to `hasEdgeConnecting(nodeV, nodeU)`.

        Since
        - 23.0
        """
        ...


    def hasEdgeConnecting(self, endpoints: "EndpointPair"["N"]) -> bool:
        """
        Returns True if there is an edge that directly connects `endpoints` (in the order, if
        any, specified by `endpoints`).
        
        Unlike the other `EndpointPair`-accepting methods, this method does not throw if the
        endpoints are unordered and the network is directed; it simply returns `False`. This is
        for consistency with Graph.hasEdgeConnecting(EndpointPair) and ValueGraph.hasEdgeConnecting(EndpointPair).

        Since
        - 27.1
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Returns `True` iff `object` is a Network that has the same elements and the
        same structural relationships as those in this network.
        
        Thus, two networks A and B are equal if **all** of the following are True:
        
        
          - A and B have equal .isDirected() directedness.
          - A and B have equal .nodes() node sets.
          - A and B have equal .edges() edge sets.
          - Every edge in A and B connects the same nodes in the same direction (if any).
        
        
        Network properties besides .isDirected() directedness do **not** affect equality.
        For example, two networks may be considered equal even if one allows parallel edges and the
        other doesn't. Additionally, the order in which nodes or edges are added to the network, and
        the order in which they are iterated over, are irrelevant.
        
        A reference implementation of this is provided by AbstractNetwork.equals(Object).
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code for this network. The hash code of a network is defined as the hash code
        of a map from each of its .edges() edges to their .incidentNodes(Object)
        incident nodes.
        
        A reference implementation of this is provided by AbstractNetwork.hashCode().
        """
        ...
