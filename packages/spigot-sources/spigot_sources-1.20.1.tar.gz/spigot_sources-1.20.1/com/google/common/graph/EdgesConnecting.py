"""
Python module generated from Java source file com.google.common.graph.EdgesConnecting

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Iterators
from com.google.common.collect import UnmodifiableIterator
from com.google.common.graph import *
from java.util import AbstractSet
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class EdgesConnecting(AbstractSet):
    """
    A class to represent the set of edges connecting an (implicit) origin node to a target node.
    
    The .nodeToOutEdge map means this class only works on networks without parallel edges.
    See MultiEdgesConnecting for a class that works with parallel edges.
    
    Type `<E>`: Edge parameter type

    Author(s)
    - James Sexton
    """

    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def size(self) -> int:
        ...


    def contains(self, edge: "Object") -> bool:
        ...
