"""
Python module generated from Java source file com.google.common.collect.CartesianList

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from com.google.common.math import IntMath
from java.util import AbstractList
from java.util import ListIterator
from java.util import RandomAccess
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class CartesianList(AbstractList, RandomAccess):
    """
    Implementation of Lists.cartesianProduct(List).

    Author(s)
    - Louis Wasserman
    """

    def indexOf(self, o: "Object") -> int:
        ...


    def lastIndexOf(self, o: "Object") -> int:
        ...


    def get(self, index: int) -> "ImmutableList"["E"]:
        ...


    def size(self) -> int:
        ...


    def contains(self, object: "Object") -> bool:
        ...
