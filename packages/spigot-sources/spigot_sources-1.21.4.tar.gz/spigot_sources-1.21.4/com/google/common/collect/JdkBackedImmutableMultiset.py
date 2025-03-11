"""
Python module generated from Java source file com.google.common.collect.JdkBackedImmutableMultiset

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from com.google.common.primitives import Ints
from com.google.errorprone.annotations.concurrent import LazyInit
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class JdkBackedImmutableMultiset(ImmutableMultiset):
    """
    An implementation of ImmutableMultiset backed by a JDK Map and a list of entries. Used to protect
    against hash flooding attacks.

    Author(s)
    - Louis Wasserman
    """

    def count(self, element: "Object") -> int:
        ...


    def elementSet(self) -> "ImmutableSet"["E"]:
        ...


    def size(self) -> int:
        ...
