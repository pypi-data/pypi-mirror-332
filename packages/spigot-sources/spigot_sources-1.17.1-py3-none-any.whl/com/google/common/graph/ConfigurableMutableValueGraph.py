"""
Python module generated from Java source file com.google.common.graph.ConfigurableMutableValueGraph

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from typing import Any, Callable, Iterable, Tuple


class ConfigurableMutableValueGraph(ConfigurableValueGraph, MutableValueGraph):
    """
    Configurable implementation of MutableValueGraph that supports both directed and
    undirected graphs. Instances of this class should be constructed with ValueGraphBuilder.
    
    Time complexities for mutation methods are all O(1) except for `removeNode(N node)`,
    which is in O(d_node) where d_node is the degree of `node`.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - Omar Darwish
    """

    def addNode(self, node: "N") -> bool:
        ...


    def putEdgeValue(self, nodeU: "N", nodeV: "N", value: "V") -> "V":
        ...


    def removeNode(self, node: "Object") -> bool:
        ...


    def removeEdge(self, nodeU: "Object", nodeV: "Object") -> "V":
        ...
