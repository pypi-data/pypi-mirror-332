"""
Python module generated from Java source file com.google.common.graph.ValueGraphBuilder

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Optional
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from typing import Any, Callable, Iterable, Tuple


class ValueGraphBuilder(AbstractGraphBuilder):
    """
    A builder for constructing instances of MutableValueGraph or ImmutableValueGraph
    with user-defined properties.
    
    A `ValueGraph` built by this class has the following default properties:
    
    
      - does not allow self-loops
      - orders ValueGraph.nodes() in the order in which the elements were added (insertion
          order)
    
    
    `ValueGraph`s built by this class also guarantee that each collection-returning accessor
    returns a **(live) unmodifiable view**; see <a
    href="https://github.com/google/guava/wiki/GraphsExplained#accessor-behavior">the external
    documentation</a> for details.
    
    Examples of use:
    
    ````// Building a mutable value graph
    MutableValueGraph<String, Double> graph =
        ValueGraphBuilder.undirected().allowsSelfLoops(True).build();
    graph.putEdgeValue("San Francisco", "San Francisco", 0.0);
    graph.putEdgeValue("San Jose", "San Jose", 0.0);
    graph.putEdgeValue("San Francisco", "San Jose", 48.4);
    
    // Building an immutable value graph
    ImmutableValueGraph<String, Double> immutableGraph =
        ValueGraphBuilder.undirected()
            .allowsSelfLoops(True)
            .<String, Double>immutable()
            .putEdgeValue("San Francisco", "San Francisco", 0.0)
            .putEdgeValue("San Jose", "San Jose", 0.0)
            .putEdgeValue("San Francisco", "San Jose", 48.4)
            .build();````
    
    Type `<N>`: The most general node type this builder will support. This is normally `Object`
        unless it is constrained by using a method like .nodeOrder, or the builder is
        constructed based on an existing `ValueGraph` using .from(ValueGraph).
    
    Type `<V>`: The most general value type this builder will support. This is normally `Object`
        unless the builder is constructed based on an existing `Graph` using .from(ValueGraph).

    Author(s)
    - Joshua O'Madadhain

    Since
    - 20.0
    """

    @staticmethod
    def directed() -> "ValueGraphBuilder"["Object", "Object"]:
        """
        Returns a ValueGraphBuilder for building directed graphs.
        """
        ...


    @staticmethod
    def undirected() -> "ValueGraphBuilder"["Object", "Object"]:
        """
        Returns a ValueGraphBuilder for building undirected graphs.
        """
        ...


    @staticmethod
    def from(graph: "ValueGraph"["N", "V"]) -> "ValueGraphBuilder"["N", "V"]:
        """
        Returns a ValueGraphBuilder initialized with all properties queryable from `graph`.
        
        The "queryable" properties are those that are exposed through the ValueGraph
        interface, such as ValueGraph.isDirected(). Other properties, such as .expectedNodeCount(int), are not set in the new builder.
        """
        ...


    def immutable(self) -> "ImmutableValueGraph.Builder"["N1", "V1"]:
        """
        Returns an ImmutableValueGraph.Builder with the properties of this ValueGraphBuilder.
        
        The returned builder can be used for populating an ImmutableValueGraph.
        
        Note that the returned builder will always have .incidentEdgeOrder set to ElementOrder.stable(), regardless of the value that was set in this builder.

        Since
        - 28.0
        """
        ...


    def allowsSelfLoops(self, allowsSelfLoops: bool) -> "ValueGraphBuilder"["N", "V"]:
        """
        Specifies whether the graph will allow self-loops (edges that connect a node to itself).
        Attempting to add a self-loop to a graph that does not allow them will throw an UnsupportedOperationException.
        
        The default value is `False`.
        """
        ...


    def expectedNodeCount(self, expectedNodeCount: int) -> "ValueGraphBuilder"["N", "V"]:
        """
        Specifies the expected number of nodes in the graph.

        Raises
        - IllegalArgumentException: if `expectedNodeCount` is negative
        """
        ...


    def nodeOrder(self, nodeOrder: "ElementOrder"["N1"]) -> "ValueGraphBuilder"["N1", "V"]:
        """
        Specifies the order of iteration for the elements of Graph.nodes().
        
        The default value is ElementOrder.insertion() insertion order.
        """
        ...


    def incidentEdgeOrder(self, incidentEdgeOrder: "ElementOrder"["N1"]) -> "ValueGraphBuilder"["N1", "V"]:
        """
        Specifies the order of iteration for the elements of ValueGraph.edges(), ValueGraph.adjacentNodes(Object), ValueGraph.predecessors(Object), ValueGraph.successors(Object) and ValueGraph.incidentEdges(Object).
        
        The default value is ElementOrder.unordered() unordered for mutable graphs. For
        immutable graphs, this value is ignored; they always have a ElementOrder.stable()
        stable order.

        Raises
        - IllegalArgumentException: if `incidentEdgeOrder` is not either `ElementOrder.unordered()` or `ElementOrder.stable()`.

        Since
        - 29.0
        """
        ...


    def build(self) -> "MutableValueGraph"["N1", "V1"]:
        """
        Returns an empty MutableValueGraph with the properties of this ValueGraphBuilder.
        """
        ...
