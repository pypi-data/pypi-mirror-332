"""
Python module generated from Java source file com.google.common.collect.SortedIterables

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import Comparator
from java.util import SortedSet
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class SortedIterables:
    """
    Utilities for dealing with sorted collections of all types.

    Author(s)
    - Louis Wasserman
    """

    @staticmethod
    def hasSameComparator(comparator: "Comparator"[Any], elements: Iterable[Any]) -> bool:
        """
        Returns `True` if `elements` is a sorted collection using an ordering equivalent to
        `comparator`.
        """
        ...


    @staticmethod
    def comparator(sortedSet: "SortedSet"["E"]) -> "Comparator"["E"]:
        ...
