"""
Python module generated from Java source file com.google.common.collect.AbstractMapEntry

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Objects
from com.google.common.collect import *
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractMapEntry(Entry):
    """
    Implementation of the `equals`, `hashCode`, and `toString`
    methods of `Entry`.

    Author(s)
    - Jared Levy
    """

    def getKey(self) -> "K":
        ...


    def getValue(self) -> "V":
        ...


    def setValue(self, value: "V") -> "V":
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of the form `{key`={value}}.
        """
        ...
