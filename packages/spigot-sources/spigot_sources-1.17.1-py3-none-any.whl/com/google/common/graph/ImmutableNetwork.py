"""
Python module generated from Java source file com.google.common.graph.ImmutableNetwork

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
from typing import Any, Callable, Iterable, Tuple


class ImmutableNetwork(ConfigurableNetwork):
    """
    A Network whose elements and structural relationships will never change. Instances of
    this class may be obtained with .copyOf(Network).
    
    See the Guava User's Guide's <a
    href="https://github.com/google/guava/wiki/GraphsExplained#immutable-implementations">discussion
    of the `Immutable*` types</a> for more information on the properties and guarantees
    provided by this class.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - Omar Darwish

    Since
    - 20.0
    """

    @staticmethod
    def copyOf(network: "Network"["N", "E"]) -> "ImmutableNetwork"["N", "E"]:
        """
        Returns an immutable copy of `network`.
        """
        ...


    @staticmethod
    def copyOf(network: "ImmutableNetwork"["N", "E"]) -> "ImmutableNetwork"["N", "E"]:
        """
        Simply returns its argument.

        Deprecated
        - no need to use this
        """
        ...


    def asGraph(self) -> "ImmutableGraph"["N"]:
        ...
