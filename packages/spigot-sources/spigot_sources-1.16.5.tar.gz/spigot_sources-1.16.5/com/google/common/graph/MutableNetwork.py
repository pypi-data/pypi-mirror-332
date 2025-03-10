"""
Python module generated from Java source file com.google.common.graph.MutableNetwork

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
        Adds `edge` connecting `nodeU` to `nodeV`. In an undirected network, the edge
        will also connect `nodeV` to `nodeU`.
        
        **Edges must be unique**, just as `Map` keys must be. They must also be non-null.
        
        Behavior if `nodeU` and `nodeV` are not already present in this network is
        implementation-dependent. Suggested behaviors include (a) silently .addNode(Object)
        adding `nodeU` and `nodeV` to the network (this is the behavior of the default
        implementations) or (b) throwing `IllegalArgumentException`.
        
        If `edge` already connects `nodeU` to `nodeV` (in the specified order if
        this network .isDirected(), else in any order), then this method will have no effect.

        Returns
        - `True` if the network was modified as a result of this call

        Raises
        - IllegalArgumentException: if `edge` already exists and does not connect `nodeU` to `nodeV`, or if the introduction of the edge would violate .allowsParallelEdges() or .allowsSelfLoops()
        """
        ...


    def removeNode(self, node: "Object") -> bool:
        """
        Removes `node` if it is present; all edges incident to `node` will also be removed.

        Returns
        - `True` if the network was modified as a result of this call
        """
        ...


    def removeEdge(self, edge: "Object") -> bool:
        """
        Removes `edge` from this network, if it is present.

        Returns
        - `True` if the network was modified as a result of this call
        """
        ...
