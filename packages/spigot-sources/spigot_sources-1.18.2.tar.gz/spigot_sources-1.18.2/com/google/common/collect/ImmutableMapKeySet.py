"""
Python module generated from Java source file com.google.common.collect.ImmutableMapKeySet

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.io import Serializable
from java.util import Spliterator
from java.util.function import Consumer
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ImmutableMapKeySet(IndexedImmutableSet):
    """
    `keySet()` implementation for ImmutableMap.

    Author(s)
    - Kevin Bourrillion
    """

    def size(self) -> int:
        ...


    def iterator(self) -> "UnmodifiableIterator"["K"]:
        ...


    def spliterator(self) -> "Spliterator"["K"]:
        ...


    def contains(self, object: "Object") -> bool:
        ...


    def forEach(self, action: "Consumer"["K"]) -> None:
        ...
