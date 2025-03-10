"""
Python module generated from Java source file com.google.common.graph.AbstractValueGraph

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Function
from com.google.common.collect import Maps
from com.google.common.graph import *
from java.util import Optional
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AbstractValueGraph(AbstractBaseGraph, ValueGraph):
    """
    This class provides a skeletal implementation of ValueGraph. It is recommended to extend
    this class rather than implement ValueGraph directly.
    
    The methods implemented in this class should not be overridden unless the subclass admits a
    more efficient implementation.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - James Sexton

    Since
    - 20.0
    """

    def asGraph(self) -> "Graph"["N"]:
        ...


    def edgeValue(self, nodeU: "N", nodeV: "N") -> "Optional"["V"]:
        ...


    def edgeValue(self, endpoints: "EndpointPair"["N"]) -> "Optional"["V"]:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this graph.
        """
        ...
