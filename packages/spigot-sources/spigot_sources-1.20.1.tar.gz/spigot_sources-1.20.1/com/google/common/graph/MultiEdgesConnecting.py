"""
Python module generated from Java source file com.google.common.graph.MultiEdgesConnecting

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import AbstractIterator
from com.google.common.collect import UnmodifiableIterator
from com.google.common.graph import *
from java.util import AbstractSet
from java.util import Iterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MultiEdgesConnecting(AbstractSet):
    """
    A class to represent the set of edges connecting an (implicit) origin node to a target node.
    
    The .outEdgeToNode map allows this class to work on networks with parallel edges. See
    EdgesConnecting for a class that is more efficient but forbids parallel edges.
    
    Type `<E>`: Edge parameter type

    Author(s)
    - James Sexton
    """

    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def contains(self, edge: "Object") -> bool:
        ...
