"""
Python module generated from Java source file com.google.common.collect.FilteredKeySetMultimap

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Predicate
from com.google.common.collect import *
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class FilteredKeySetMultimap(FilteredKeyMultimap, FilteredSetMultimap):
    """
    Implementation of Multimaps.filterKeys(SetMultimap, Predicate).

    Author(s)
    - Louis Wasserman
    """

    def unfiltered(self) -> "SetMultimap"["K", "V"]:
        ...


    def get(self, key: "K") -> set["V"]:
        ...


    def removeAll(self, key: "Object") -> set["V"]:
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> set["V"]:
        ...


    def entries(self) -> set["Entry"["K", "V"]]:
        ...
