"""
Python module generated from Java source file com.google.common.graph.ImmutableGraph

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Function
from com.google.common.base import Functions
from com.google.common.collect import ImmutableMap
from com.google.common.collect import Maps
from com.google.common.graph import *
from com.google.common.graph.GraphConstants import Presence
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import Immutable
from typing import Any, Callable, Iterable, Tuple


class ImmutableGraph(ForwardingGraph):
    """
    A Graph whose elements and structural relationships will never change. Instances of this
    class may be obtained with .copyOf(Graph).
    
    See the Guava User's Guide's <a
    href="https://github.com/google/guava/wiki/GraphsExplained#immutable-implementations">discussion
    of the `Immutable*` types</a> for more information on the properties and guarantees
    provided by this class.
    
    Type `<N>`: Node parameter type

    Author(s)
    - Jens Nyman

    Since
    - 20.0
    """

    @staticmethod
    def copyOf(graph: "Graph"["N"]) -> "ImmutableGraph"["N"]:
        """
        Returns an immutable copy of `graph`.
        """
        ...


    @staticmethod
    def copyOf(graph: "ImmutableGraph"["N"]) -> "ImmutableGraph"["N"]:
        """
        Simply returns its argument.

        Deprecated
        - no need to use this
        """
        ...


    def incidentEdgeOrder(self) -> "ElementOrder"["N"]:
        ...


    class Builder:
        """
        A builder for creating ImmutableGraph instances, especially `static final`
        graphs. Example:
        
        ````static final ImmutableGraph<Country> COUNTRY_ADJACENCY_GRAPH =
            GraphBuilder.undirected()
                .<Country>immutable()
                .putEdge(FRANCE, GERMANY)
                .putEdge(FRANCE, BELGIUM)
                .putEdge(GERMANY, BELGIUM)
                .addNode(ICELAND)
                .build();````
        
        Builder instances can be reused; it is safe to call .build multiple times to build
        multiple graphs in series. Each new graph contains all the elements of the ones created before
        it.

        Since
        - 28.0
        """

        def addNode(self, node: "N") -> "Builder"["N"]:
            """
            Adds `node` if it is not already present.
            
            **Nodes must be unique**, just as `Map` keys must be. They must also be non-null.

            Returns
            - this `Builder` object
            """
            ...


        def putEdge(self, nodeU: "N", nodeV: "N") -> "Builder"["N"]:
            """
            Adds an edge connecting `nodeU` to `nodeV` if one is not already present.
            
            If the graph is directed, the resultant edge will be directed; otherwise, it will be
            undirected.
            
            If `nodeU` and `nodeV` are not already present in this graph, this method will
            silently .addNode(Object) add `nodeU` and `nodeV` to the graph.

            Returns
            - this `Builder` object

            Raises
            - IllegalArgumentException: if the introduction of the edge would violate .allowsSelfLoops()
            """
            ...


        def putEdge(self, endpoints: "EndpointPair"["N"]) -> "Builder"["N"]:
            """
            Adds an edge connecting `endpoints` (in the order, if any, specified by `endpoints`) if one is not already present.
            
            If this graph is directed, `endpoints` must be ordered and the added edge will be
            directed; if it is undirected, the added edge will be undirected.
            
            If this graph is directed, `endpoints` must be ordered.
            
            If either or both endpoints are not already present in this graph, this method will
            silently .addNode(Object) add each missing endpoint to the graph.

            Returns
            - this `Builder` object

            Raises
            - IllegalArgumentException: if the introduction of the edge would violate .allowsSelfLoops()
            - IllegalArgumentException: if the endpoints are unordered and the graph is directed
            """
            ...


        def build(self) -> "ImmutableGraph"["N"]:
            """
            Returns a newly-created `ImmutableGraph` based on the contents of this `Builder`.
            """
            ...
