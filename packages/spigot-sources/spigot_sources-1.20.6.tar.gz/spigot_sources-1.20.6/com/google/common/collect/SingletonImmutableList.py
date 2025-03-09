"""
Python module generated from Java source file com.google.common.collect.SingletonImmutableList

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Preconditions
from com.google.common.collect import *
from java.util import Collections
from java.util import Spliterator
from typing import Any, Callable, Iterable, Tuple


class SingletonImmutableList(ImmutableList):
    """
    Implementation of ImmutableList with exactly one element.

    Author(s)
    - Hayward Chan
    """

    def get(self, index: int) -> "E":
        ...


    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def size(self) -> int:
        ...


    def subList(self, fromIndex: int, toIndex: int) -> "ImmutableList"["E"]:
        ...


    def toString(self) -> str:
        ...
