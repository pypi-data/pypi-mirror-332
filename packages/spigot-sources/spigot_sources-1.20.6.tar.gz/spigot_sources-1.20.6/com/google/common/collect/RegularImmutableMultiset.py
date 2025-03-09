"""
Python module generated from Java source file com.google.common.collect.RegularImmutableMultiset

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Objects
from com.google.common.collect import *
from com.google.common.collect.Multisets import ImmutableEntry
from com.google.common.primitives import Ints
from com.google.errorprone.annotations.concurrent import LazyInit
from java.util import Arrays
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RegularImmutableMultiset(ImmutableMultiset):
    """
    Implementation of ImmutableMultiset with zero or more elements.

    Author(s)
    - Louis Wasserman
    """

    def count(self, element: "Object") -> int:
        ...


    def size(self) -> int:
        ...


    def elementSet(self) -> "ImmutableSet"["E"]:
        ...


    def hashCode(self) -> int:
        ...
