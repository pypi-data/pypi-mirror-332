"""
Python module generated from Java source file com.google.common.collect.RegularImmutableList

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from java.util import Spliterator
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RegularImmutableList(ImmutableList):
    """
    Implementation of ImmutableList backed by a simple array.

    Author(s)
    - Kevin Bourrillion
    """

    def size(self) -> int:
        ...


    def get(self, index: int) -> "E":
        ...


    def listIterator(self, index: int) -> "UnmodifiableListIterator"["E"]:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...
