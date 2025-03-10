"""
Python module generated from Java source file com.google.common.collect.RegularImmutableSortedSet

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Spliterator
from java.util.function import Consumer
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RegularImmutableSortedSet(ImmutableSortedSet):
    """
    An immutable sorted set with one or more elements. TODO(jlevy): Consider separate class for a
    single-element sorted set.

    Author(s)
    - Louis Wasserman
    """

    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def descendingIterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def forEach(self, action: "Consumer"["E"]) -> None:
        ...


    def size(self) -> int:
        ...


    def contains(self, o: "Object") -> bool:
        ...


    def containsAll(self, targets: Iterable[Any]) -> bool:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def first(self) -> "E":
        ...


    def last(self) -> "E":
        ...


    def lower(self, element: "E") -> "E":
        ...


    def floor(self, element: "E") -> "E":
        ...


    def ceiling(self, element: "E") -> "E":
        ...


    def higher(self, element: "E") -> "E":
        ...
