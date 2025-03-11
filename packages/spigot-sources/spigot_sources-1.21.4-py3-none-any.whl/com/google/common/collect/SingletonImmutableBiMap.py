"""
Python module generated from Java source file com.google.common.collect.SingletonImmutableBiMap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import RetainedWith
from java.util.function import BiConsumer
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class SingletonImmutableBiMap(ImmutableBiMap):
    """
    Implementation of ImmutableMap with exactly one entry.

    Author(s)
    - Kevin Bourrillion
    """

    def get(self, key: "Object") -> "V":
        ...


    def size(self) -> int:
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def inverse(self) -> "ImmutableBiMap"["V", "K"]:
        ...
