"""
Python module generated from Java source file com.google.common.collect.RegularImmutableBiMap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.common.collect.ImmutableMapEntry import NonTerminalImmutableBiMapEntry
from com.google.common.collect.RegularImmutableMap import BucketOverflowException
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import RetainedWith
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.util.function import BiConsumer
from java.util.function import Consumer
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RegularImmutableBiMap(ImmutableBiMap):
    """
    Bimap with zero or more mappings.

    Author(s)
    - Louis Wasserman
    """

    def get(self, key: "Object") -> "V":
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def hashCode(self) -> int:
        ...


    def size(self) -> int:
        ...


    def inverse(self) -> "ImmutableBiMap"["V", "K"]:
        ...
