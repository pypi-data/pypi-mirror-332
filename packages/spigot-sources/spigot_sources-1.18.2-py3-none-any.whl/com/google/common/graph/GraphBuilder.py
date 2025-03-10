"""
Python module generated from Java source file com.google.common.graph.GraphBuilder

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Optional
from com.google.common.graph import *
from com.google.errorprone.annotations import DoNotMock
from typing import Any, Callable, Iterable, Tuple


class GraphBuilder(AbstractGraphBuilder):
    """
    A builder for constructing instances of MutableGraph or ImmutableGraph with
    user-defined properties.
    
    A graph built by this class will have the following properties by default:
    
    
      - does not allow self-loops
      - orders Graph.nodes() in the order in which the elements were added
    
    
    Examples of use:
    
    ````// Building a mutable graph
    MutableGraph<String> graph = GraphBuilder.undirected().allowsSelfLoops(True).build();
    graph.putEdge("bread", "bread");
    graph.putEdge("chocolate", "peanut butter");
    graph.putEdge("peanut butter", "jelly");
    
    // Building an immutable graph
    ImmutableGraph<String> immutableGraph =
        GraphBuilder.undirected()
            .allowsSelfLoops(True)
            .<String>immutable()
            .putEdge("bread", "bread")
            .putEdge("chocolate", "peanut butter")
            .putEdge("peanut butter", "jelly")
            .build();````
    
    Type `<N>`: The most general node type this builder will support. This is normally `Object`
        unless it is constrained by using a method like .nodeOrder, or the builder is
        constructed based on an existing `Graph` using .from(Graph).

    Author(s)
    - Joshua O'Madadhain

    Since
    - 20.0
    """

    @staticmethod
    def directed() -> "GraphBuilder"["Object"]:
        """
        Returns a GraphBuilder for building directed graphs.
        """
        ...


    @staticmethod
    def undirected() -> "GraphBuilder"["Object"]:
        """
        Returns a GraphBuilder for building undirected graphs.
        """
        ...


    @staticmethod
    def from(graph: "Graph"["N"]) -> "GraphBuilder"["N"]:
        """
        Returns a GraphBuilder initialized with all properties queryable from `graph`.
        
        The "queryable" properties are those that are exposed through the Graph interface,
        such as Graph.isDirected(). Other properties, such as .expectedNodeCount(int),
        are not set in the new builder.
        """
        ...


    def immutable(self) -> "ImmutableGraph.Builder"["N1"]:
        """
        Returns an ImmutableGraph.Builder with the properties of this GraphBuilder.
        
        The returned builder can be used for populating an ImmutableGraph.
        
        Note that the returned builder will always have .incidentEdgeOrder set to ElementOrder.stable(), regardless of the value that was set in this builder.

        Since
        - 28.0
        """
        ...


    def allowsSelfLoops(self, allowsSelfLoops: bool) -> "GraphBuilder"["N"]:
        """
        Specifies whether the graph will allow self-loops (edges that connect a node to itself).
        Attempting to add a self-loop to a graph that does not allow them will throw an UnsupportedOperationException.
        
        The default value is `False`.
        """
        ...


    def expectedNodeCount(self, expectedNodeCount: int) -> "GraphBuilder"["N"]:
        """
        Specifies the expected number of nodes in the graph.

        Raises
        - IllegalArgumentException: if `expectedNodeCount` is negative
        """
        ...


    def nodeOrder(self, nodeOrder: "ElementOrder"["N1"]) -> "GraphBuilder"["N1"]:
        """
        Specifies the order of iteration for the elements of Graph.nodes().
        
        The default value is ElementOrder.insertion() insertion order.
        """
        ...


    def incidentEdgeOrder(self, incidentEdgeOrder: "ElementOrder"["N1"]) -> "GraphBuilder"["N1"]:
        """
        Specifies the order of iteration for the elements of Graph.edges(), Graph.adjacentNodes(Object), Graph.predecessors(Object), Graph.successors(Object) and Graph.incidentEdges(Object).
        
        The default value is ElementOrder.unordered() unordered for mutable graphs. For
        immutable graphs, this value is ignored; they always have a ElementOrder.stable()
        stable order.

        Raises
        - IllegalArgumentException: if `incidentEdgeOrder` is not either `ElementOrder.unordered()` or `ElementOrder.stable()`.

        Since
        - 29.0
        """
        ...


    def build(self) -> "MutableGraph"["N1"]:
        """
        Returns an empty MutableGraph with the properties of this GraphBuilder.
        """
        ...
