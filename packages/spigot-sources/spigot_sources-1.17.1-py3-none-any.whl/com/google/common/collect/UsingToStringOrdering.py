"""
Python module generated from Java source file com.google.common.collect.UsingToStringOrdering

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.io import Serializable
from typing import Any, Callable, Iterable, Tuple


class UsingToStringOrdering(Ordering, Serializable):
    """
    An ordering that uses the natural order of the string representation of the
    values.
    """

    def compare(self, left: "Object", right: "Object") -> int:
        ...


    def toString(self) -> str:
        ...
