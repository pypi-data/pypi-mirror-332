"""
Python module generated from Java source file com.google.common.collect.ImmutableEntry

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.io import Serializable
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableEntry(AbstractMapEntry, Serializable):
    """
    See
    - com.google.common.collect.Maps.immutableEntry(Object, Object)
    """

    def getKey(self) -> "K":
        ...


    def getValue(self) -> "V":
        ...


    def setValue(self, value: "V") -> "V":
        ...
