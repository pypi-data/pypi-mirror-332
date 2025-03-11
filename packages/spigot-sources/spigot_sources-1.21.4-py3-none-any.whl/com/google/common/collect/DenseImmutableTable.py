"""
Python module generated from Java source file com.google.common.collect.DenseImmutableTable

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from com.google.common.collect.ImmutableMap import IteratorBasedImmutableMap
from com.google.errorprone.annotations import Immutable
from com.google.j2objc.annotations import WeakOuter
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class DenseImmutableTable(RegularImmutableTable):
    """
    A `RegularImmutableTable` optimized for dense data.
    """

    def columnMap(self) -> "ImmutableMap"["C", dict["R", "V"]]:
        ...


    def rowMap(self) -> "ImmutableMap"["R", dict["C", "V"]]:
        ...


    def get(self, rowKey: "Object", columnKey: "Object") -> "V":
        ...


    def size(self) -> int:
        ...
