"""
Python module generated from Java source file com.google.common.graph.StandardMutableValueGraph

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class StandardMutableValueGraph(StandardValueGraph, MutableValueGraph):
    """
    Standard implementation of MutableValueGraph that supports both directed and undirected
    graphs. Instances of this class should be constructed with ValueGraphBuilder.
    
    Time complexities for mutation methods are all O(1) except for `removeNode(N node)`,
    which is in O(d_node) where d_node is the degree of `node`.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - Omar Darwish
    """

    def incidentEdgeOrder(self) -> "ElementOrder"["N"]:
        ...


    def addNode(self, node: "N") -> bool:
        ...


    def putEdgeValue(self, nodeU: "N", nodeV: "N", value: "V") -> "V":
        ...


    def putEdgeValue(self, endpoints: "EndpointPair"["N"], value: "V") -> "V":
        ...


    def removeNode(self, node: "N") -> bool:
        ...


    def removeEdge(self, nodeU: "N", nodeV: "N") -> "V":
        ...


    def removeEdge(self, endpoints: "EndpointPair"["N"]) -> "V":
        ...
