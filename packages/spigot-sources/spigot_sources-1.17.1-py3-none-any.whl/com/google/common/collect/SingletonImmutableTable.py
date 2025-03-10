"""
Python module generated from Java source file com.google.common.collect.SingletonImmutableTable

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from typing import Any, Callable, Iterable, Tuple


class SingletonImmutableTable(ImmutableTable):
    """
    An implementation of ImmutableTable that holds a single cell.

    Author(s)
    - Gregory Kick
    """

    def column(self, columnKey: "C") -> "ImmutableMap"["R", "V"]:
        ...


    def columnMap(self) -> "ImmutableMap"["C", dict["R", "V"]]:
        ...


    def rowMap(self) -> "ImmutableMap"["R", dict["C", "V"]]:
        ...


    def size(self) -> int:
        ...
