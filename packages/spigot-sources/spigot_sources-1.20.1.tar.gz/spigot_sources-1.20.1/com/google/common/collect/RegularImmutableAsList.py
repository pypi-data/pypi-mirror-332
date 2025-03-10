"""
Python module generated from Java source file com.google.common.collect.RegularImmutableAsList

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.util.function import Consumer
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RegularImmutableAsList(ImmutableAsList):
    """
    An ImmutableAsList implementation specialized for when the delegate collection is already
    backed by an `ImmutableList` or array.

    Author(s)
    - Louis Wasserman
    """

    def listIterator(self, index: int) -> "UnmodifiableListIterator"["E"]:
        ...


    def forEach(self, action: "Consumer"["E"]) -> None:
        ...


    def get(self, index: int) -> "E":
        ...
