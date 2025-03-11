"""
Python module generated from Java source file com.google.common.collect.JdkBackedImmutableBiMap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import RetainedWith
from com.google.j2objc.annotations import WeakOuter
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class JdkBackedImmutableBiMap(ImmutableBiMap):
    """
    Implementation of ImmutableBiMap backed by a pair of JDK HashMaps, which have smartness
    protecting against hash flooding.
    """

    def size(self) -> int:
        ...


    def inverse(self) -> "ImmutableBiMap"["V", "K"]:
        ...


    def get(self, key: "Object") -> "V":
        ...
