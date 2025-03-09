"""
Python module generated from Java source file com.google.common.graph.DirectedGraphConnections

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Function
from com.google.common.collect import AbstractIterator
from com.google.common.collect import ImmutableList
from com.google.common.collect import Iterators
from com.google.common.collect import UnmodifiableIterator
from com.google.common.graph import *
from java.util import AbstractSet
from java.util import Collections
from java.util import Iterator
from java.util.concurrent.atomic import AtomicBoolean
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class DirectedGraphConnections(GraphConnections):
    """
    An implementation of GraphConnections for directed graphs.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - Jens Nyman
    """

    def adjacentNodes(self) -> set["N"]:
        ...


    def predecessors(self) -> set["N"]:
        ...


    def successors(self) -> set["N"]:
        ...


    def incidentEdgeIterator(self, thisNode: "N") -> Iterator["EndpointPair"["N"]]:
        ...


    def value(self, node: "N") -> "V":
        ...


    def removePredecessor(self, node: "N") -> None:
        ...


    def removeSuccessor(self, node: "Object") -> "V":
        ...


    def addPredecessor(self, node: "N", unused: "V") -> None:
        ...


    def addSuccessor(self, node: "N", value: "V") -> "V":
        ...
