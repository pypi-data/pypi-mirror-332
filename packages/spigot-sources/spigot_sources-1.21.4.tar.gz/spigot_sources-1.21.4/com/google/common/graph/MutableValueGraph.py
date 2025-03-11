"""
Python module generated from Java source file com.google.common.graph.MutableValueGraph

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MutableValueGraph(ValueGraph):
    """
    A subinterface of ValueGraph which adds mutation methods. When mutation is not required,
    users should prefer the ValueGraph interface.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - James Sexton

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


    def putEdgeValue(self, nodeU: "N", nodeV: "N", value: "V") -> "V":
        """
        Adds an edge connecting `nodeU` to `nodeV` if one is not already present, and sets
        a value for that edge to `value` (overwriting the existing value, if any).
        
        If the graph is directed, the resultant edge will be directed; otherwise, it will be
        undirected.
        
        Values do not have to be unique. However, values must be non-null.
        
        If `nodeU` and `nodeV` are not already present in this graph, this method will
        silently .addNode(Object) add `nodeU` and `nodeV` to the graph.

        Returns
        - the value previously associated with the edge connecting `nodeU` to `nodeV`, or null if there was no such edge.

        Raises
        - IllegalArgumentException: if the introduction of the edge would violate .allowsSelfLoops()
        """
        ...


    def putEdgeValue(self, endpoints: "EndpointPair"["N"], value: "V") -> "V":
        """
        Adds an edge connecting `endpoints` if one is not already present, and sets a value for
        that edge to `value` (overwriting the existing value, if any).
        
        If the graph is directed, the resultant edge will be directed; otherwise, it will be
        undirected.
        
        If this graph is directed, `endpoints` must be ordered.
        
        Values do not have to be unique. However, values must be non-null.
        
        If either or both endpoints are not already present in this graph, this method will silently
        .addNode(Object) add each missing endpoint to the graph.

        Returns
        - the value previously associated with the edge connecting `nodeU` to `nodeV`, or null if there was no such edge.

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


    def removeEdge(self, nodeU: "N", nodeV: "N") -> "V":
        """
        Removes the edge connecting `nodeU` to `nodeV`, if it is present.

        Returns
        - the value previously associated with the edge connecting `nodeU` to `nodeV`, or null if there was no such edge.
        """
        ...


    def removeEdge(self, endpoints: "EndpointPair"["N"]) -> "V":
        """
        Removes the edge connecting `endpoints`, if it is present.
        
        If this graph is directed, `endpoints` must be ordered.

        Returns
        - the value previously associated with the edge connecting `endpoints`, or null if
            there was no such edge.

        Since
        - 27.1
        """
        ...
