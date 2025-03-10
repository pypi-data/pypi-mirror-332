"""
Python module generated from Java source file com.google.common.collect.ImmutableEnumSet

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations.concurrent import LazyInit
from java.io import Serializable
from java.util import EnumSet
from java.util import Spliterator
from java.util.function import Consumer
from typing import Any, Callable, Iterable, Tuple


class ImmutableEnumSet(ImmutableSet):
    """
    Implementation of ImmutableSet backed by a non-empty java.util.EnumSet.

    Author(s)
    - Jared Levy
    """

    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def forEach(self, action: "Consumer"["E"]) -> None:
        ...


    def size(self) -> int:
        ...


    def contains(self, object: "Object") -> bool:
        ...


    def containsAll(self, collection: Iterable[Any]) -> bool:
        ...


    def isEmpty(self) -> bool:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
