"""
Python module generated from Java source file com.google.common.graph.AbstractDirectedNetworkConnections

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Iterables
from com.google.common.collect import Iterators
from com.google.common.collect import Sets
from com.google.common.collect import UnmodifiableIterator
from com.google.common.graph import *
from com.google.common.math import IntMath
from java.util import AbstractSet
from java.util import Collections
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AbstractDirectedNetworkConnections(NetworkConnections):
    """
    A base implementation of NetworkConnections for directed networks.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - James Sexton
    """

    def adjacentNodes(self) -> set["N"]:
        ...


    def incidentEdges(self) -> set["E"]:
        ...


    def inEdges(self) -> set["E"]:
        ...


    def outEdges(self) -> set["E"]:
        ...


    def adjacentNode(self, edge: "E") -> "N":
        ...


    def removeInEdge(self, edge: "E", isSelfLoop: bool) -> "N":
        ...


    def removeOutEdge(self, edge: "E") -> "N":
        ...


    def addInEdge(self, edge: "E", node: "N", isSelfLoop: bool) -> None:
        ...


    def addOutEdge(self, edge: "E", node: "N") -> None:
        ...
