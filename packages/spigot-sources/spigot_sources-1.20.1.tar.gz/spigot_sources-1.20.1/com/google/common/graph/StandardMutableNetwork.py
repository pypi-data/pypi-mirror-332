"""
Python module generated from Java source file com.google.common.graph.StandardMutableNetwork

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableList
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from typing import Any, Callable, Iterable, Tuple


class StandardMutableNetwork(StandardNetwork, MutableNetwork):
    """
    Standard implementation of MutableNetwork that supports both directed and undirected
    graphs. Instances of this class should be constructed with NetworkBuilder.
    
    Time complexities for mutation methods are all O(1) except for `removeNode(N node)`,
    which is in O(d_node) where d_node is the degree of `node`.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - Omar Darwish
    """

    def addNode(self, node: "N") -> bool:
        ...


    def addEdge(self, nodeU: "N", nodeV: "N", edge: "E") -> bool:
        ...


    def addEdge(self, endpoints: "EndpointPair"["N"], edge: "E") -> bool:
        ...


    def removeNode(self, node: "N") -> bool:
        ...


    def removeEdge(self, edge: "E") -> bool:
        ...
