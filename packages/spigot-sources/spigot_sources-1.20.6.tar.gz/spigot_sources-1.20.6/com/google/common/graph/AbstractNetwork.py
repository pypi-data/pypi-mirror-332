"""
Python module generated from Java source file com.google.common.graph.AbstractNetwork

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Predicate
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Iterators
from com.google.common.collect import Maps
from com.google.common.collect import Sets
from com.google.common.graph import *
from com.google.common.math import IntMath
from java.util import AbstractSet
from java.util import Iterator
from java.util import Optional
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AbstractNetwork(Network):
    """
    This class provides a skeletal implementation of Network. It is recommended to extend
    this class rather than implement Network directly.
    
    The methods implemented in this class should not be overridden unless the subclass admits a
    more efficient implementation.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - James Sexton

    Since
    - 20.0
    """

    def asGraph(self) -> "Graph"["N"]:
        ...


    def degree(self, node: "N") -> int:
        ...


    def inDegree(self, node: "N") -> int:
        ...


    def outDegree(self, node: "N") -> int:
        ...


    def adjacentEdges(self, edge: "E") -> set["E"]:
        ...


    def edgesConnecting(self, nodeU: "N", nodeV: "N") -> set["E"]:
        ...


    def edgesConnecting(self, endpoints: "EndpointPair"["N"]) -> set["E"]:
        ...


    def edgeConnecting(self, nodeU: "N", nodeV: "N") -> "Optional"["E"]:
        ...


    def edgeConnecting(self, endpoints: "EndpointPair"["N"]) -> "Optional"["E"]:
        ...


    def edgeConnectingOrNull(self, nodeU: "N", nodeV: "N") -> "E":
        ...


    def edgeConnectingOrNull(self, endpoints: "EndpointPair"["N"]) -> "E":
        ...


    def hasEdgeConnecting(self, nodeU: "N", nodeV: "N") -> bool:
        ...


    def hasEdgeConnecting(self, endpoints: "EndpointPair"["N"]) -> bool:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this network.
        """
        ...
