"""
Python module generated from Java source file com.google.common.collect.ImmutableSortedAsList

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from java.util import Comparator
from java.util import Spliterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ImmutableSortedAsList(RegularImmutableAsList, SortedIterable):
    """
    List returned by `ImmutableSortedSet.asList()` when the set isn't empty.

    Author(s)
    - Louis Wasserman
    """

    def comparator(self) -> "Comparator"["E"]:
        ...


    def indexOf(self, target: "Object") -> int:
        ...


    def lastIndexOf(self, target: "Object") -> int:
        ...


    def contains(self, target: "Object") -> bool:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...
