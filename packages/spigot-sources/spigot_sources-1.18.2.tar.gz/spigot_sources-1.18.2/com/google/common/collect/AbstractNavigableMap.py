"""
Python module generated from Java source file com.google.common.collect.AbstractNavigableMap

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.common.collect.Maps import IteratorBasedAbstractMap
from java.util import Iterator
from java.util import NavigableMap
from java.util import NavigableSet
from java.util import NoSuchElementException
from java.util import SortedMap
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractNavigableMap(IteratorBasedAbstractMap, NavigableMap):
    """
    Skeletal implementation of NavigableMap.

    Author(s)
    - Louis Wasserman
    """

    def get(self, key: "Object") -> "V":
        ...


    def firstEntry(self) -> "Entry"["K", "V"]:
        ...


    def lastEntry(self) -> "Entry"["K", "V"]:
        ...


    def pollFirstEntry(self) -> "Entry"["K", "V"]:
        ...


    def pollLastEntry(self) -> "Entry"["K", "V"]:
        ...


    def firstKey(self) -> "K":
        ...


    def lastKey(self) -> "K":
        ...


    def lowerEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def floorEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def ceilingEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def higherEntry(self, key: "K") -> "Entry"["K", "V"]:
        ...


    def lowerKey(self, key: "K") -> "K":
        ...


    def floorKey(self, key: "K") -> "K":
        ...


    def ceilingKey(self, key: "K") -> "K":
        ...


    def higherKey(self, key: "K") -> "K":
        ...


    def subMap(self, fromKey: "K", toKey: "K") -> "SortedMap"["K", "V"]:
        ...


    def headMap(self, toKey: "K") -> "SortedMap"["K", "V"]:
        ...


    def tailMap(self, fromKey: "K") -> "SortedMap"["K", "V"]:
        ...


    def navigableKeySet(self) -> "NavigableSet"["K"]:
        ...


    def keySet(self) -> set["K"]:
        ...


    def descendingKeySet(self) -> "NavigableSet"["K"]:
        ...


    def descendingMap(self) -> "NavigableMap"["K", "V"]:
        ...
