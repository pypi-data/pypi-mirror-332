"""
Python module generated from Java source file com.google.common.graph.DirectedGraphConnections

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import AbstractIterator
from com.google.common.collect import ImmutableMap
from com.google.common.collect import UnmodifiableIterator
from com.google.common.graph import *
from java.util import AbstractSet
from java.util import Collections
from java.util import Iterator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class DirectedGraphConnections(GraphConnections):
    """
    An implementation of GraphConnections for directed graphs.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - James Sexton
    """

    def adjacentNodes(self) -> set["N"]:
        ...


    def predecessors(self) -> set["N"]:
        ...


    def successors(self) -> set["N"]:
        ...


    def value(self, node: "Object") -> "V":
        ...


    def removePredecessor(self, node: "Object") -> None:
        ...


    def removeSuccessor(self, node: "Object") -> "V":
        ...


    def addPredecessor(self, node: "N", unused: "V") -> None:
        ...


    def addSuccessor(self, node: "N", value: "V") -> "V":
        ...
