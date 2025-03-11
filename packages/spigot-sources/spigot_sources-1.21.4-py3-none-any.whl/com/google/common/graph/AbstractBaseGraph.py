"""
Python module generated from Java source file com.google.common.graph.AbstractBaseGraph

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Iterators
from com.google.common.collect import Sets
from com.google.common.collect import UnmodifiableIterator
from com.google.common.graph import *
from com.google.common.math import IntMath
from com.google.common.primitives import Ints
from java.util import AbstractSet
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AbstractBaseGraph(BaseGraph):
    """
    This class provides a skeletal implementation of BaseGraph.
    
    The methods implemented in this class should not be overridden unless the subclass admits a
    more efficient implementation.
    
    Type `<N>`: Node parameter type

    Author(s)
    - James Sexton
    """

    def edges(self) -> set["EndpointPair"["N"]]:
        """
        An implementation of BaseGraph.edges() defined in terms of Graph.nodes() and
        .successors(Object).
        """
        ...


    def incidentEdgeOrder(self) -> "ElementOrder"["N"]:
        ...


    def incidentEdges(self, node: "N") -> set["EndpointPair"["N"]]:
        ...


    def degree(self, node: "N") -> int:
        ...


    def inDegree(self, node: "N") -> int:
        ...


    def outDegree(self, node: "N") -> int:
        ...


    def hasEdgeConnecting(self, nodeU: "N", nodeV: "N") -> bool:
        ...


    def hasEdgeConnecting(self, endpoints: "EndpointPair"["N"]) -> bool:
        ...
