"""
Python module generated from Java source file com.google.common.collect.ByFunctionOrdering

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Function
from com.google.common.base import Objects
from com.google.common.collect import *
from java.io import Serializable
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ByFunctionOrdering(Ordering, Serializable):
    """
    An ordering that orders elements by applying an order to the result of a function on those
    elements.
    """

    def compare(self, left: "F", right: "F") -> int:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
