"""
Python module generated from Java source file com.google.common.collect.Cut

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.common.primitives import Booleans
from java.io import Serializable
from java.util import NoSuchElementException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Cut(Comparable, Serializable):
    """
    Implementation detail for the internal structure of Range instances. Represents a unique
    way of "cutting" a "number line" (actually of instances of type `C`, not necessarily
    "numbers") into two sections; this can be done below a certain value, above a certain value,
    below all values or above all values. With this object defined in this way, an interval can
    always be represented by a pair of `Cut` instances.

    Author(s)
    - Kevin Bourrillion
    """

    def compareTo(self, that: "Cut"["C"]) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
