"""
Python module generated from Java source file com.google.common.graph.ImmutableValueGraph

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Function
from com.google.common.collect import ImmutableMap
from com.google.common.collect import Maps
from com.google.common.graph import *
from com.google.errorprone.annotations import Immutable
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableValueGraph(ValueBackedImpl, ValueGraph):
    """
    A ValueGraph whose elements and structural relationships will never change. Instances of
    this class may be obtained with .copyOf(ValueGraph).
    
    See the Guava User's Guide's <a
    href="https://github.com/google/guava/wiki/GraphsExplained#immutable-implementations">discussion
    of the `Immutable*` types</a> for more information on the properties and guarantees
    provided by this class.
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - James Sexton

    Since
    - 20.0
    """

    @staticmethod
    def copyOf(graph: "ValueGraph"["N", "V"]) -> "ImmutableValueGraph"["N", "V"]:
        """
        Returns an immutable copy of `graph`.
        """
        ...


    @staticmethod
    def copyOf(graph: "ImmutableValueGraph"["N", "V"]) -> "ImmutableValueGraph"["N", "V"]:
        """
        Simply returns its argument.

        Deprecated
        - no need to use this
        """
        ...


    def edgeValue(self, nodeU: "Object", nodeV: "Object") -> "V":
        ...


    def edgeValueOrDefault(self, nodeU: "Object", nodeV: "Object", defaultValue: "V") -> "V":
        ...


    def toString(self) -> str:
        ...
