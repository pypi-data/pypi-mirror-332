"""
Python module generated from Java source file com.google.common.collect.FilteredEntryMultimap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import MoreObjects
from com.google.common.base import Predicate
from com.google.common.collect import *
from com.google.common.collect.Maps import ViewCachingAbstractMap
from com.google.j2objc.annotations import WeakOuter
from java.util import Collections
from java.util import Iterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class FilteredEntryMultimap(AbstractMultimap, FilteredMultimap):
    """
    Implementation of Multimaps.filterEntries(Multimap, Predicate).

    Author(s)
    - Louis Wasserman
    """

    def unfiltered(self) -> "Multimap"["K", "V"]:
        ...


    def entryPredicate(self) -> "Predicate"["Entry"["K", "V"]]:
        ...


    def size(self) -> int:
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def removeAll(self, key: "Object") -> Iterable["V"]:
        ...


    def clear(self) -> None:
        ...


    def get(self, key: "K") -> Iterable["V"]:
        ...
