"""
Python module generated from Java source file com.google.common.graph.DirectedNetworkConnections

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import BiMap
from com.google.common.collect import HashBiMap
from com.google.common.collect import ImmutableBiMap
from com.google.common.graph import *
from java.util import Collections
from typing import Any, Callable, Iterable, Tuple


class DirectedNetworkConnections(AbstractDirectedNetworkConnections):
    """
    An implementation of NetworkConnections for directed networks.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - James Sexton
    """

    def predecessors(self) -> set["N"]:
        ...


    def successors(self) -> set["N"]:
        ...


    def edgesConnecting(self, node: "N") -> set["E"]:
        ...
