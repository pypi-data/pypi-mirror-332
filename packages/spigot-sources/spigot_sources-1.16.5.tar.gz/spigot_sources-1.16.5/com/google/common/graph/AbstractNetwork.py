"""
Python module generated from Java source file com.google.common.graph.AbstractNetwork

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Function
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Iterators
from com.google.common.collect import Maps
from com.google.common.collect import Sets
from com.google.common.graph import *
from com.google.common.math import IntMath
from java.util import AbstractSet
from java.util import Iterator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractNetwork(Network):
    """
    This class provides a skeletal implementation of Network. It is recommended to extend
    this class rather than implement Network directly.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - James Sexton

    Since
    - 20.0
    """

    def asGraph(self) -> "Graph"["N"]:
        ...


    def degree(self, node: "Object") -> int:
        ...


    def inDegree(self, node: "Object") -> int:
        ...


    def outDegree(self, node: "Object") -> int:
        ...


    def adjacentEdges(self, edge: "Object") -> set["E"]:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this network.
        """
        ...
