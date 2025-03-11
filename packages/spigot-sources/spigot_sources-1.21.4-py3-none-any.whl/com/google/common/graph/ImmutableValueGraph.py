"""
Python module generated from Java source file com.google.common.graph.ImmutableValueGraph

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Function
from com.google.common.collect import ImmutableMap
from com.google.common.collect import Maps
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import Immutable
from typing import Any, Callable, Iterable, Tuple


class ImmutableValueGraph(StandardValueGraph):
    """
    A ValueGraph whose elements and structural relationships will never change. Instances of
    this class may be obtained with .copyOf(ValueGraph).
    
    See the Guava User's Guide's <a
    href="https://github.com/google/guava/wiki/GraphsExplained#immutable-implementations">discussion
    of the `Immutable*` types</a> for more information on the properties and guarantees
    provided by this class.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - Jens Nyman

    Since
    - 20.0
    """

    @staticmethod
    def copyOf(graph: "ValueGraph"["N", "V"]) -> "ImmutableValueGraph"["N", "V"]:
        """
        Returns an immutable copy of `graph`.
        """
        ...


    @staticmethod
    def copyOf(graph: "ImmutableValueGraph"["N", "V"]) -> "ImmutableValueGraph"["N", "V"]:
        """
        Simply returns its argument.

        Deprecated
        - no need to use this
        """
        ...


    def incidentEdgeOrder(self) -> "ElementOrder"["N"]:
        ...


    def asGraph(self) -> "ImmutableGraph"["N"]:
        ...


    class Builder:
        """
        A builder for creating ImmutableValueGraph instances, especially `static final`
        graphs. Example:
        
        ````static final ImmutableValueGraph<City, Distance> CITY_ROAD_DISTANCE_GRAPH =
            ValueGraphBuilder.undirected()
                .<City, Distance>immutable()
                .putEdgeValue(PARIS, BERLIN, kilometers(1060))
                .putEdgeValue(PARIS, BRUSSELS, kilometers(317))
                .putEdgeValue(BERLIN, BRUSSELS, kilometers(764))
                .addNode(REYKJAVIK)
                .build();````
        
        Builder instances can be reused; it is safe to call .build multiple times to build
        multiple graphs in series. Each new graph contains all the elements of the ones created before
        it.

        Since
        - 28.0
        """

        def addNode(self, node: "N") -> "ImmutableValueGraph.Builder"["N", "V"]:
            """
            Adds `node` if it is not already present.
            
            **Nodes must be unique**, just as `Map` keys must be. They must also be non-null.

            Returns
            - this `Builder` object
            """
            ...


        def putEdgeValue(self, nodeU: "N", nodeV: "N", value: "V") -> "ImmutableValueGraph.Builder"["N", "V"]:
            """
            Adds an edge connecting `nodeU` to `nodeV` if one is not already present, and
            sets a value for that edge to `value` (overwriting the existing value, if any).
            
            If the graph is directed, the resultant edge will be directed; otherwise, it will be
            undirected.
            
            Values do not have to be unique. However, values must be non-null.
            
            If `nodeU` and `nodeV` are not already present in this graph, this method will
            silently .addNode(Object) add `nodeU` and `nodeV` to the graph.

            Returns
            - this `Builder` object

            Raises
            - IllegalArgumentException: if the introduction of the edge would violate .allowsSelfLoops()
            """
            ...


        def putEdgeValue(self, endpoints: "EndpointPair"["N"], value: "V") -> "ImmutableValueGraph.Builder"["N", "V"]:
            """
            Adds an edge connecting `endpoints` if one is not already present, and sets a value for
            that edge to `value` (overwriting the existing value, if any).
            
            If the graph is directed, the resultant edge will be directed; otherwise, it will be
            undirected.
            
            If this graph is directed, `endpoints` must be ordered.
            
            Values do not have to be unique. However, values must be non-null.
            
            If either or both endpoints are not already present in this graph, this method will
            silently .addNode(Object) add each missing endpoint to the graph.

            Returns
            - this `Builder` object

            Raises
            - IllegalArgumentException: if the introduction of the edge would violate .allowsSelfLoops()
            - IllegalArgumentException: if the endpoints are unordered and the graph is directed
            """
            ...


        def build(self) -> "ImmutableValueGraph"["N", "V"]:
            """
            Returns a newly-created `ImmutableValueGraph` based on the contents of this `Builder`.
            """
            ...
