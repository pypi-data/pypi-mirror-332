"""
Python module generated from Java source file com.google.common.graph.GraphBuilder

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Optional
from com.google.common.graph import *
from typing import Any, Callable, Iterable, Tuple


class GraphBuilder(AbstractGraphBuilder):
    """
    A builder for constructing instances of MutableGraph with user-defined properties.
    
    A graph built by this class will have the following properties by default:
    
    
    - does not allow self-loops
    - orders Graph.nodes() in the order in which the elements were added
    
    
    Example of use:
    
    ````MutableGraph<String> graph = GraphBuilder.undirected().allowsSelfLoops(True).build();
    graph.putEdge("bread", "bread");
    graph.putEdge("chocolate", "peanut butter");
    graph.putEdge("peanut butter", "jelly");````

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


    def allowsSelfLoops(self, allowsSelfLoops: bool) -> "GraphBuilder"["N"]:
        """
        Specifies whether the graph will allow self-loops (edges that connect a node to itself).
        Attempting to add a self-loop to a graph that does not allow them will throw an UnsupportedOperationException.
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
        """
        ...


    def build(self) -> "MutableGraph"["N1"]:
        """
        Returns an empty MutableGraph with the properties of this GraphBuilder.
        """
        ...
