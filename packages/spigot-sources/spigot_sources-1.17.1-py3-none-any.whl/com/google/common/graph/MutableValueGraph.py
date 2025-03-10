"""
Python module generated from Java source file com.google.common.graph.MutableValueGraph

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import CompatibleWith
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
        Adds an edge connecting `nodeU` to `nodeV` if one is not already present; associate
        that edge with `value`. In an undirected graph, the edge will also connect `nodeV`
        to `nodeU`.
        
        Values do not have to be unique. However, values must be non-null.
        
        Behavior if `nodeU` and `nodeV` are not already present in this graph is
        implementation-dependent. Suggested behaviors include (a) silently .addNode(Object)
        adding `nodeU` and `nodeV` to the graph (this is the behavior of the default
        implementations) or (b) throwing `IllegalArgumentException`.

        Returns
        - the value previously associated with the edge connecting `nodeU` to `nodeV`, or null if there was no such edge.

        Raises
        - IllegalArgumentException: if the introduction of the edge would violate .allowsSelfLoops()
        """
        ...


    def removeNode(self, node: "Object") -> bool:
        """
        Removes `node` if it is present; all edges incident to `node` will also be removed.

        Returns
        - `True` if the graph was modified as a result of this call
        """
        ...


    def removeEdge(self, nodeU: "Object", nodeV: "Object") -> "V":
        """
        Removes the edge connecting `nodeU` to `nodeV`, if it is present.

        Returns
        - the value previously associated with the edge connecting `nodeU` to `nodeV`, or null if there was no such edge.
        """
        ...
