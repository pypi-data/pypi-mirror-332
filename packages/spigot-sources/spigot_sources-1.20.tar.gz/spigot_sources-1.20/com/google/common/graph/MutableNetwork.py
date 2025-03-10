"""
Python module generated from Java source file com.google.common.graph.MutableNetwork

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from typing import Any, Callable, Iterable, Tuple


class MutableNetwork(Network):
    """
    A subinterface of Network which adds mutation methods. When mutation is not required,
    users should prefer the Network interface.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - Joshua O'Madadhain

    Since
    - 20.0
    """

    def addNode(self, node: "N") -> bool:
        """
        Adds `node` if it is not already present.
        
        **Nodes must be unique**, just as `Map` keys must be. They must also be non-null.

        Returns
        - `True` if the network was modified as a result of this call
        """
        ...


    def addEdge(self, nodeU: "N", nodeV: "N", edge: "E") -> bool:
        """
        Adds `edge` connecting `nodeU` to `nodeV`.
        
        If the graph is directed, `edge` will be directed in this graph; otherwise, it will be
        undirected.
        
        **`edge` must be unique to this graph**, just as a `Map` key must be. It must
        also be non-null.
        
        If `nodeU` and `nodeV` are not already present in this graph, this method will
        silently .addNode(Object) add `nodeU` and `nodeV` to the graph.
        
        If `edge` already connects `nodeU` to `nodeV` (in the specified order if
        this network .isDirected(), else in any order), then this method will have no effect.

        Returns
        - `True` if the network was modified as a result of this call

        Raises
        - IllegalArgumentException: if `edge` already exists in the graph and does not
            connect `nodeU` to `nodeV`
        - IllegalArgumentException: if the introduction of the edge would violate .allowsParallelEdges() or .allowsSelfLoops()
        """
        ...


    def addEdge(self, endpoints: "EndpointPair"["N"], edge: "E") -> bool:
        """
        Adds `edge` connecting `endpoints`. In an undirected network, `edge` will
        also connect `nodeV` to `nodeU`.
        
        If this graph is directed, `edge` will be directed in this graph; if it is undirected,
        `edge` will be undirected in this graph.
        
        If this graph is directed, `endpoints` must be ordered.
        
        **`edge` must be unique to this graph**, just as a `Map` key must be. It must
        also be non-null.
        
        If either or both endpoints are not already present in this graph, this method will silently
        .addNode(Object) add each missing endpoint to the graph.
        
        If `edge` already connects an endpoint pair equal to `endpoints`, then this
        method will have no effect.

        Returns
        - `True` if the network was modified as a result of this call

        Raises
        - IllegalArgumentException: if `edge` already exists in the graph and connects some
            other endpoint pair that is not equal to `endpoints`
        - IllegalArgumentException: if the introduction of the edge would violate .allowsParallelEdges() or .allowsSelfLoops()
        - IllegalArgumentException: if the endpoints are unordered and the graph is directed

        Since
        - 27.1
        """
        ...


    def removeNode(self, node: "N") -> bool:
        """
        Removes `node` if it is present; all edges incident to `node` will also be removed.

        Returns
        - `True` if the network was modified as a result of this call
        """
        ...


    def removeEdge(self, edge: "E") -> bool:
        """
        Removes `edge` from this network, if it is present.

        Returns
        - `True` if the network was modified as a result of this call
        """
        ...
