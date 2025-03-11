"""
Python module generated from Java source file com.google.common.collect.FilteredMultimapValues

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Objects
from com.google.common.base import Predicate
from com.google.common.base import Predicates
from com.google.common.collect import *
from com.google.j2objc.annotations import Weak
from java.util import AbstractCollection
from java.util import Iterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class FilteredMultimapValues(AbstractCollection):
    """
    Implementation for FilteredMultimap.values().

    Author(s)
    - Louis Wasserman
    """

    def iterator(self) -> Iterator["V"]:
        ...


    def contains(self, o: "Object") -> bool:
        ...


    def size(self) -> int:
        ...


    def remove(self, o: "Object") -> bool:
        ...


    def removeAll(self, c: Iterable[Any]) -> bool:
        ...


    def retainAll(self, c: Iterable[Any]) -> bool:
        ...


    def clear(self) -> None:
        ...
