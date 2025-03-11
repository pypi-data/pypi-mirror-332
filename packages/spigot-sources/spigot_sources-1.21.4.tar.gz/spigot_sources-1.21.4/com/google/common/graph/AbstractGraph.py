"""
Python module generated from Java source file com.google.common.graph.AbstractGraph

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AbstractGraph(AbstractBaseGraph, Graph):
    """
    This class provides a skeletal implementation of Graph. It is recommended to extend this
    class rather than implement Graph directly.
    
    Type `<N>`: Node parameter type

    Author(s)
    - James Sexton

    Since
    - 20.0
    """

    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this graph.
        """
        ...
