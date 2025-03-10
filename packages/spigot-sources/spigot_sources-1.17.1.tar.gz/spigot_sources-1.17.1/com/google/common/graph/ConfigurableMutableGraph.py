"""
Python module generated from Java source file com.google.common.graph.ConfigurableMutableGraph

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from com.google.common.graph.GraphConstants import Presence
from typing import Any, Callable, Iterable, Tuple


class ConfigurableMutableGraph(ForwardingGraph, MutableGraph):
    """
    Configurable implementation of MutableGraph that supports both directed and undirected
    graphs. Instances of this class should be constructed with GraphBuilder.
    
    Time complexities for mutation methods are all O(1) except for `removeNode(N node)`,
    which is in O(d_node) where d_node is the degree of `node`.
    
    Type `<N>`: Node parameter type

    Author(s)
    - James Sexton
    """

    def addNode(self, node: "N") -> bool:
        ...


    def putEdge(self, nodeU: "N", nodeV: "N") -> bool:
        ...


    def removeNode(self, node: "Object") -> bool:
        ...


    def removeEdge(self, nodeU: "Object", nodeV: "Object") -> bool:
        ...
