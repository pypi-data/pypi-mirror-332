"""
Python module generated from Java source file com.google.common.collect.GeneralRange

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Objects
from com.google.common.collect import *
from java.io import Serializable
from java.util import Comparator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class GeneralRange(Serializable):
    """
    A generalized interval on any ordering, for internal use. Supports `null`. Unlike Range, this allows the use of an arbitrary comparator. This is designed for use in the
    implementation of subcollections of sorted collection types.
    
    Whenever possible, use `Range` instead, which is better supported.

    Author(s)
    - Louis Wasserman
    """

    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
