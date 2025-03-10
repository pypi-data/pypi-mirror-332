"""
Python module generated from Java source file com.google.common.collect.SortedIterable

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import Comparator
from java.util import Iterator
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class SortedIterable(Iterable):
    """
    An `Iterable` whose elements are sorted relative to a `Comparator`, typically
    provided at creation time.

    Author(s)
    - Louis Wasserman
    """

    def comparator(self) -> "Comparator"["T"]:
        """
        Returns the `Comparator` by which the elements of this iterable are ordered, or `Ordering.natural()` if the elements are ordered by their natural ordering.
        """
        ...


    def iterator(self) -> Iterator["T"]:
        """
        Returns an iterator over elements of type `T`. The elements are returned in nondecreasing
        order according to the associated .comparator.
        """
        ...
