"""
Python module generated from Java source file com.google.common.graph.EndpointPair

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Objects
from com.google.common.collect import Iterators
from com.google.common.collect import UnmodifiableIterator
from com.google.common.graph import *
from com.google.errorprone.annotations import Immutable
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class EndpointPair(Iterable):
    """
    An immutable pair representing the two endpoints of an edge in a graph. The EndpointPair
    of a directed edge is an ordered pair of nodes (.source() and .target()). The
    EndpointPair of an undirected edge is an unordered pair of nodes (.nodeU() and
    .nodeV()).
    
    The edge is a self-loop if, and only if, the two endpoints are equal.

    Author(s)
    - James Sexton

    Since
    - 20.0
    """

    @staticmethod
    def ordered(source: "N", target: "N") -> "EndpointPair"["N"]:
        """
        Returns an EndpointPair representing the endpoints of a directed edge.
        """
        ...


    @staticmethod
    def unordered(nodeU: "N", nodeV: "N") -> "EndpointPair"["N"]:
        """
        Returns an EndpointPair representing the endpoints of an undirected edge.
        """
        ...


    def source(self) -> "N":
        """
        If this EndpointPair .isOrdered(), returns the node which is the source.

        Raises
        - UnsupportedOperationException: if this EndpointPair is not ordered
        """
        ...


    def target(self) -> "N":
        """
        If this EndpointPair .isOrdered(), returns the node which is the target.

        Raises
        - UnsupportedOperationException: if this EndpointPair is not ordered
        """
        ...


    def nodeU(self) -> "N":
        """
        If this EndpointPair .isOrdered() returns the .source(); otherwise,
        returns an arbitrary (but consistent) endpoint of the origin edge.
        """
        ...


    def nodeV(self) -> "N":
        """
        Returns the node .adjacentNode(Object) adjacent to .nodeU() along the origin
        edge. If this EndpointPair .isOrdered(), this is equal to .target().
        """
        ...


    def adjacentNode(self, node: "N") -> "N":
        """
        Returns the node that is adjacent to `node` along the origin edge.

        Raises
        - IllegalArgumentException: if this EndpointPair does not contain `node`

        Since
        - 20.0 (but the argument type was changed from `Object` to `N` in 31.0)
        """
        ...


    def isOrdered(self) -> bool:
        """
        Returns `True` if this EndpointPair is an ordered pair (i.e. represents the
        endpoints of a directed edge).
        """
        ...


    def iterator(self) -> "UnmodifiableIterator"["N"]:
        """
        Iterates in the order .nodeU(), .nodeV().
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Two ordered EndpointPairs are equal if their .source() and .target()
        are equal. Two unordered EndpointPairs are equal if they contain the same nodes. An
        ordered EndpointPair is never equal to an unordered EndpointPair.
        """
        ...


    def hashCode(self) -> int:
        """
        The hashcode of an ordered EndpointPair is equal to `Objects.hashCode(source(),
        target())`. The hashcode of an unordered EndpointPair is equal to `nodeU().hashCode() + nodeV().hashCode()`.
        """
        ...
