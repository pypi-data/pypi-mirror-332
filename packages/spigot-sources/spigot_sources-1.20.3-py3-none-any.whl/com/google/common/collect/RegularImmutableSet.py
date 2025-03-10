"""
Python module generated from Java source file com.google.common.collect.RegularImmutableSet

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from java.util import Spliterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RegularImmutableSet(CachingAsList):
    """
    Implementation of ImmutableSet with two or more elements.

    Author(s)
    - Kevin Bourrillion
    """

    def contains(self, target: "Object") -> bool:
        ...


    def size(self) -> int:
        ...


    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def hashCode(self) -> int:
        ...
