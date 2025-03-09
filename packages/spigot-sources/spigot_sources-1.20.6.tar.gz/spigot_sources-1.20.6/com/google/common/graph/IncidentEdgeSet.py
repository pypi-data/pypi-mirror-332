"""
Python module generated from Java source file com.google.common.graph.IncidentEdgeSet

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from java.util import AbstractSet
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class IncidentEdgeSet(AbstractSet):
    """
    Abstract base class for an incident edges set that allows different implementations of AbstractSet.iterator().
    """

    def remove(self, o: "Object") -> bool:
        ...


    def size(self) -> int:
        ...


    def contains(self, obj: "Object") -> bool:
        ...
