"""
Python module generated from Java source file com.google.common.collect.AbstractSortedKeySortedSetMultimap

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import SortedMap
from java.util import SortedSet
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractSortedKeySortedSetMultimap(AbstractSortedSetMultimap):
    """
    Basic implementation of a SortedSetMultimap with a sorted key set.
    
    This superclass allows `TreeMultimap` to override methods to return navigable set and
    map types in non-GWT only, while GWT code will inherit the SortedMap/SortedSet overrides.

    Author(s)
    - Louis Wasserman
    """

    def asMap(self) -> "SortedMap"["K", Iterable["V"]]:
        ...


    def keySet(self) -> "SortedSet"["K"]:
        ...
