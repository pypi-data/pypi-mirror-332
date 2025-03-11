"""
Python module generated from Java source file com.google.common.collect.TopKSelector

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.common.math import IntMath
from java.math import RoundingMode
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util.stream import Stream
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class TopKSelector:
    """
    An accumulator that selects the "top" `k` elements added to it, relative to a provided
    comparator. "Top" can mean the greatest or the lowest elements, specified in the factory used to
    create the `TopKSelector` instance.
    
    If your input data is available as a Stream, prefer passing Comparators.least(int) to Stream.collect(java.util.stream.Collector). If it is available
    as an Iterable or Iterator, prefer Ordering.leastOf(Iterable, int).
    
    This uses the same efficient implementation as Ordering.leastOf(Iterable, int),
    offering expected O(n + k log k) performance (worst case O(n log k)) for n calls to .offer and a call to .topK, with O(k) memory. In comparison, quickselect has the same
    asymptotics but requires O(n) memory, and a `PriorityQueue` implementation takes O(n log
    k). In benchmarks, this implementation performs at least as well as either implementation, and
    degrades more gracefully for worst-case input.
    
    The implementation does not necessarily use a *stable* sorting algorithm; when multiple
    equivalent elements are added to it, it is undefined which will come first in the output.

    Author(s)
    - Louis Wasserman
    """

    @staticmethod
    def least(k: int) -> "TopKSelector"["T"]:
        """
        Returns a `TopKSelector` that collects the lowest `k` elements added to it,
        relative to the natural ordering of the elements, and returns them via .topK in
        ascending order.

        Raises
        - IllegalArgumentException: if `k < 0` or `k > Integer.MAX_VALUE / 2`
        """
        ...


    @staticmethod
    def least(k: int, comparator: "Comparator"["T"]) -> "TopKSelector"["T"]:
        """
        Returns a `TopKSelector` that collects the lowest `k` elements added to it,
        relative to the specified comparator, and returns them via .topK in ascending order.

        Raises
        - IllegalArgumentException: if `k < 0` or `k > Integer.MAX_VALUE / 2`
        """
        ...


    @staticmethod
    def greatest(k: int) -> "TopKSelector"["T"]:
        """
        Returns a `TopKSelector` that collects the greatest `k` elements added to it,
        relative to the natural ordering of the elements, and returns them via .topK in
        descending order.

        Raises
        - IllegalArgumentException: if `k < 0` or `k > Integer.MAX_VALUE / 2`
        """
        ...


    @staticmethod
    def greatest(k: int, comparator: "Comparator"["T"]) -> "TopKSelector"["T"]:
        """
        Returns a `TopKSelector` that collects the greatest `k` elements added to it,
        relative to the specified comparator, and returns them via .topK in descending order.

        Raises
        - IllegalArgumentException: if `k < 0` or `k > Integer.MAX_VALUE / 2`
        """
        ...


    def offer(self, elem: "T") -> None:
        """
        Adds `elem` as a candidate for the top `k` elements. This operation takes amortized
        O(1) time.
        """
        ...


    def offerAll(self, elements: Iterable["T"]) -> None:
        """
        Adds each member of `elements` as a candidate for the top `k` elements. This
        operation takes amortized linear time in the length of `elements`.
        
        If all input data to this `TopKSelector` is in a single `Iterable`, prefer
        Ordering.leastOf(Iterable, int), which provides a simpler API for that use case.
        """
        ...


    def offerAll(self, elements: Iterator["T"]) -> None:
        """
        Adds each member of `elements` as a candidate for the top `k` elements. This
        operation takes amortized linear time in the length of `elements`. The iterator is
        consumed after this operation completes.
        
        If all input data to this `TopKSelector` is in a single `Iterator`, prefer
        Ordering.leastOf(Iterator, int), which provides a simpler API for that use case.
        """
        ...


    def topK(self) -> list["T"]:
        """
        Returns the top `k` elements offered to this `TopKSelector`, or all elements if
        fewer than `k` have been offered, in the order specified by the factory used to create
        this `TopKSelector`.
        
        The returned list is an unmodifiable copy and will not be affected by further changes to
        this `TopKSelector`. This method returns in O(k log k) time.
        """
        ...
