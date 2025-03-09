"""
Python module generated from Java source file com.google.common.graph.DirectedMultiNetworkConnections

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import HashMultiset
from com.google.common.collect import ImmutableMap
from com.google.common.collect import Multiset
from com.google.common.graph import *
from com.google.errorprone.annotations.concurrent import LazyInit
from java.lang.ref import Reference
from java.lang.ref import SoftReference
from java.util import Collections
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class DirectedMultiNetworkConnections(AbstractDirectedNetworkConnections):
    """
    An implementation of NetworkConnections for directed networks with parallel edges.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - James Sexton
    """

    def predecessors(self) -> set["N"]:
        ...


    def successors(self) -> set["N"]:
        ...


    def edgesConnecting(self, node: "N") -> set["E"]:
        ...


    def removeInEdge(self, edge: "E", isSelfLoop: bool) -> "N":
        ...


    def removeOutEdge(self, edge: "E") -> "N":
        ...


    def addInEdge(self, edge: "E", node: "N", isSelfLoop: bool) -> None:
        ...


    def addOutEdge(self, edge: "E", node: "N") -> None:
        ...
