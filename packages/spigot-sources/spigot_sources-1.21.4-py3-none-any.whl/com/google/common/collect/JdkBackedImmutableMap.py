"""
Python module generated from Java source file com.google.common.collect.JdkBackedImmutableMap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from java.util.function import BiConsumer
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class JdkBackedImmutableMap(ImmutableMap):
    """
    Implementation of ImmutableMap backed by a JDK HashMap, which has smartness protecting against
    hash flooding.
    """

    def size(self) -> int:
        ...


    def get(self, key: "Object") -> "V":
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...
