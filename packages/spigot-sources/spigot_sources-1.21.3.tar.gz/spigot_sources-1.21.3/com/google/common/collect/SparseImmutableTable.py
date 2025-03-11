"""
Python module generated from Java source file com.google.common.collect.SparseImmutableTable

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import Immutable
from typing import Any, Callable, Iterable, Tuple


class SparseImmutableTable(RegularImmutableTable):
    """
    A `RegularImmutableTable` optimized for sparse data.
    """

    def columnMap(self) -> "ImmutableMap"["C", dict["R", "V"]]:
        ...


    def rowMap(self) -> "ImmutableMap"["R", dict["C", "V"]]:
        ...


    def size(self) -> int:
        ...
