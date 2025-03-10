"""
Python module generated from Java source file com.google.common.collect.SingletonImmutableSet

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Preconditions
from com.google.common.collect import *
from com.google.errorprone.annotations.concurrent import LazyInit
from typing import Any, Callable, Iterable, Tuple


class SingletonImmutableSet(ImmutableSet):
    """
    Implementation of ImmutableSet with exactly one element.

    Author(s)
    - Nick Kralevich
    """

    def size(self) -> int:
        ...


    def contains(self, target: "Object") -> bool:
        ...


    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
