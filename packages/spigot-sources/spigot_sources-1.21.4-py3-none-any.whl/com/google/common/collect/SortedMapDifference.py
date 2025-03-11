"""
Python module generated from Java source file com.google.common.collect.SortedMapDifference

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import SortedMap
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class SortedMapDifference(MapDifference):
    """
    An object representing the differences between two sorted maps.

    Author(s)
    - Louis Wasserman

    Since
    - 8.0
    """

    def entriesOnlyOnLeft(self) -> "SortedMap"["K", "V"]:
        ...


    def entriesOnlyOnRight(self) -> "SortedMap"["K", "V"]:
        ...


    def entriesInCommon(self) -> "SortedMap"["K", "V"]:
        ...


    def entriesDiffering(self) -> "SortedMap"["K", "ValueDifference"["V"]]:
        ...
