"""
Python module generated from Java source file com.google.common.collect.Comparators

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import Comparator
from java.util import Iterator
from typing import Any, Callable, Iterable, Tuple


class Comparators:
    """
    Provides static methods for working with Comparator instances. For many other helpful
    comparator utilities, see either `Comparator` itself (for Java 8 or later), or
    `com.google.common.collect.Ordering` (otherwise).
    
    <h3>Relationship to `Ordering`</h3>
    
    In light of the significant enhancements to `Comparator` in Java 8, the overwhelming
    majority of usages of `Ordering` can be written using only built-in JDK APIs. Because of
    this, and because it's awkward to have to convert comparators into `Ordering` instances,
    `Ordering` and its methods are planned for deletion. This class is intended to
    "fill the gap" and provide those features of `Ordering` not already provided by the JDK.

    Author(s)
    - Louis Wasserman

    Since
    - 21.0
    """

    @staticmethod
    def lexicographical(comparator: "Comparator"["T"]) -> "Comparator"[Iterable["S"]]:
        ...


    @staticmethod
    def isInOrder(iterable: Iterable["T"], comparator: "Comparator"["T"]) -> bool:
        """
        Returns `True` if each element in `iterable` after the first is greater than or
        equal to the element that preceded it, according to the specified comparator. Note that this
        is always True when the iterable has fewer than two elements.
        """
        ...


    @staticmethod
    def isInStrictOrder(iterable: Iterable["T"], comparator: "Comparator"["T"]) -> bool:
        """
        Returns `True` if each element in `iterable` after the first is *strictly*
        greater than the element that preceded it, according to the specified comparator. Note that
        this is always True when the iterable has fewer than two elements.
        """
        ...
