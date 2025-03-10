"""
Python module generated from Java source file com.google.common.graph.MutableGraph

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from typing import Any, Callable, Iterable, Tuple


class MutableGraph(Graph):
    """
    A subinterface of Graph which adds mutation methods. When mutation is not required, users
    should prefer the Graph interface.
    
    Type `<N>`: Node parameter type

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
        - `True` if the graph was modified as a result of this call
        """
        ...


    def putEdge(self, nodeU: "N", nodeV: "N") -> bool:
        """
        Adds an edge connecting `nodeU` to `nodeV` if one is not already present.
        
        If the graph is directed, the resultant edge will be directed; otherwise, it will be
        undirected.
        
        If `nodeU` and `nodeV` are not already present in this graph, this method will
        silently .addNode(Object) add `nodeU` and `nodeV` to the graph.

        Returns
        - `True` if the graph was modified as a result of this call

        Raises
        - IllegalArgumentException: if the introduction of the edge would violate .allowsSelfLoops()
        """
        ...


    def putEdge(self, endpoints: "EndpointPair"["N"]) -> bool:
        """
        Adds an edge connecting `endpoints` (in the order, if any, specified by `endpoints`) if one is not already present.
        
        If this graph is directed, `endpoints` must be ordered and the added edge will be
        directed; if it is undirected, the added edge will be undirected.
        
        If this graph is directed, `endpoints` must be ordered.
        
        If either or both endpoints are not already present in this graph, this method will silently
        .addNode(Object) add each missing endpoint to the graph.

        Returns
        - `True` if the graph was modified as a result of this call

        Raises
        - IllegalArgumentException: if the introduction of the edge would violate .allowsSelfLoops()
        - IllegalArgumentException: if the endpoints are unordered and the graph is directed

        Since
        - 27.1
        """
        ...


    def removeNode(self, node: "N") -> bool:
        """
        Removes `node` if it is present; all edges incident to `node` will also be removed.

        Returns
        - `True` if the graph was modified as a result of this call
        """
        ...


    def removeEdge(self, nodeU: "N", nodeV: "N") -> bool:
        """
        Removes the edge connecting `nodeU` to `nodeV`, if it is present.

        Returns
        - `True` if the graph was modified as a result of this call
        """
        ...


    def removeEdge(self, endpoints: "EndpointPair"["N"]) -> bool:
        """
        Removes the edge connecting `endpoints`, if it is present.
        
        If this graph is directed, `endpoints` must be ordered.

        Returns
        - `True` if the graph was modified as a result of this call

        Raises
        - IllegalArgumentException: if the endpoints are unordered and the graph is directed

        Since
        - 27.1
        """
        ...
