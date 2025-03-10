"""
Python module generated from Java source file com.google.common.graph.AbstractGraph

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.collect import UnmodifiableIterator
from com.google.common.graph import *
from com.google.common.math import IntMath
from com.google.common.primitives import Ints
from java.util import AbstractSet
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractGraph(Graph):
    """
    This class provides a skeletal implementation of Graph. It is recommended to extend this
    class rather than implement Graph directly.
    
    Type `<N>`: Node parameter type

    Author(s)
    - James Sexton

    Since
    - 20.0
    """

    def edges(self) -> set["EndpointPair"["N"]]:
        """
        A reasonable default implementation of Graph.edges() defined in terms of .nodes() and .successors(Object).
        """
        ...


    def degree(self, node: "Object") -> int:
        ...


    def inDegree(self, node: "Object") -> int:
        ...


    def outDegree(self, node: "Object") -> int:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this graph.
        """
        ...
