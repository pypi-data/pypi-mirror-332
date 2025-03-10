"""
Python module generated from Java source file com.google.common.collect.Comparators

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import Comparator
from java.util import Iterator
from java.util import Optional
from java.util.stream import Collector
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Comparators:
    """
    Provides static methods for working with Comparator instances. For many other helpful
    comparator utilities, see either `Comparator` itself (for Java 8 or later), or `com.google.common.collect.Ordering` (otherwise).
    
    <h3>Relationship to `Ordering`</h3>
    
    In light of the significant enhancements to `Comparator` in Java 8, the overwhelming
    majority of usages of `Ordering` can be written using only built-in JDK APIs. This class is
    intended to "fill the gap" and provide those features of `Ordering` not already provided by
    the JDK.

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
        equal to the element that preceded it, according to the specified comparator. Note that this is
        always True when the iterable has fewer than two elements.
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


    @staticmethod
    def least(k: int, comparator: "Comparator"["T"]) -> "Collector"["T", Any, list["T"]]:
        """
        Returns a `Collector` that returns the `k` smallest (relative to the specified
        `Comparator`) input elements, in ascending order, as an unmodifiable `List`. Ties
        are broken arbitrarily.
        
        For example:
        
        ````Stream.of("foo", "quux", "banana", "elephant")
            .collect(least(2, comparingInt(String::length)))
        // returns {"foo", "quux"`
        }```
        
        This `Collector` uses O(k) memory and takes expected time O(n) (worst-case O(n log
        k)), as opposed to e.g. `Stream.sorted(comparator).limit(k)`, which currently takes O(n
        log n) time and O(n) space.

        Raises
        - IllegalArgumentException: if `k < 0`

        Since
        - 22.0
        """
        ...


    @staticmethod
    def greatest(k: int, comparator: "Comparator"["T"]) -> "Collector"["T", Any, list["T"]]:
        """
        Returns a `Collector` that returns the `k` greatest (relative to the specified
        `Comparator`) input elements, in descending order, as an unmodifiable `List`. Ties
        are broken arbitrarily.
        
        For example:
        
        ````Stream.of("foo", "quux", "banana", "elephant")
            .collect(greatest(2, comparingInt(String::length)))
        // returns {"elephant", "banana"`
        }```
        
        This `Collector` uses O(k) memory and takes expected time O(n) (worst-case O(n log
        k)), as opposed to e.g. `Stream.sorted(comparator.reversed()).limit(k)`, which currently
        takes O(n log n) time and O(n) space.

        Raises
        - IllegalArgumentException: if `k < 0`

        Since
        - 22.0
        """
        ...


    @staticmethod
    def emptiesFirst(valueComparator: "Comparator"["T"]) -> "Comparator"["Optional"["T"]]:
        """
        Returns a comparator of Optional values which treats Optional.empty as less
        than all other values, and orders the rest using `valueComparator` on the contained
        value.

        Since
        - 22.0
        """
        ...


    @staticmethod
    def emptiesLast(valueComparator: "Comparator"["T"]) -> "Comparator"["Optional"["T"]]:
        """
        Returns a comparator of Optional values which treats Optional.empty as greater
        than all other values, and orders the rest using `valueComparator` on the contained
        value.

        Since
        - 22.0
        """
        ...


    @staticmethod
    def min(a: "T", b: "T") -> "T":
        """
        Returns the minimum of the two values. If the values compare as 0, the first is returned.
        
        The recommended solution for finding the `minimum` of some values depends on the type
        of your data and the number of elements you have. Read more in the Guava User Guide article on
        <a href="https://github.com/google/guava/wiki/CollectionUtilitiesExplained#comparators">`Comparators`</a>.

        Arguments
        - a: first value to compare, returned if less than or equal to b.
        - b: second value to compare.

        Raises
        - ClassCastException: if the parameters are not *mutually comparable*.

        Since
        - 30.0
        """
        ...


    @staticmethod
    def min(a: "T", b: "T", comparator: "Comparator"["T"]) -> "T":
        """
        Returns the minimum of the two values, according to the given comparator. If the values compare
        as equal, the first is returned.
        
        The recommended solution for finding the `minimum` of some values depends on the type
        of your data and the number of elements you have. Read more in the Guava User Guide article on
        <a href="https://github.com/google/guava/wiki/CollectionUtilitiesExplained#comparators">`Comparators`</a>.

        Arguments
        - a: first value to compare, returned if less than or equal to b
        - b: second value to compare.

        Raises
        - ClassCastException: if the parameters are not *mutually comparable* using the given
            comparator.

        Since
        - 30.0
        """
        ...


    @staticmethod
    def max(a: "T", b: "T") -> "T":
        """
        Returns the maximum of the two values. If the values compare as 0, the first is returned.
        
        The recommended solution for finding the `maximum` of some values depends on the type
        of your data and the number of elements you have. Read more in the Guava User Guide article on
        <a href="https://github.com/google/guava/wiki/CollectionUtilitiesExplained#comparators">`Comparators`</a>.

        Arguments
        - a: first value to compare, returned if greater than or equal to b.
        - b: second value to compare.

        Raises
        - ClassCastException: if the parameters are not *mutually comparable*.

        Since
        - 30.0
        """
        ...


    @staticmethod
    def max(a: "T", b: "T", comparator: "Comparator"["T"]) -> "T":
        """
        Returns the maximum of the two values, according to the given comparator. If the values compare
        as equal, the first is returned.
        
        The recommended solution for finding the `maximum` of some values depends on the type
        of your data and the number of elements you have. Read more in the Guava User Guide article on
        <a href="https://github.com/google/guava/wiki/CollectionUtilitiesExplained#comparators">`Comparators`</a>.

        Arguments
        - a: first value to compare, returned if greater than or equal to b.
        - b: second value to compare.

        Raises
        - ClassCastException: if the parameters are not *mutually comparable* using the given
            comparator.

        Since
        - 30.0
        """
        ...
