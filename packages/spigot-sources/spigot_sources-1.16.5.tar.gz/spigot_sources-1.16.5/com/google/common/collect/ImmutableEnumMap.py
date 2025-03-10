"""
Python module generated from Java source file com.google.common.collect.ImmutableEnumMap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.common.collect.ImmutableMap import IteratorBasedImmutableMap
from java.io import Serializable
from java.util import EnumMap
from java.util import Spliterator
from java.util.function import BiConsumer
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableEnumMap(IteratorBasedImmutableMap):
    """
    Implementation of ImmutableMap backed by a non-empty java.util.EnumMap.

    Author(s)
    - Louis Wasserman
    """

    def size(self) -> int:
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def get(self, key: "Object") -> "V":
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...
