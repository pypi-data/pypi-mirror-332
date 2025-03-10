"""
Python module generated from Java source file com.google.common.collect.ExplicitOrdering

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.io import Serializable
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ExplicitOrdering(Ordering, Serializable):
    """
    An ordering that compares objects according to a given order.
    """

    def compare(self, left: "T", right: "T") -> int:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
