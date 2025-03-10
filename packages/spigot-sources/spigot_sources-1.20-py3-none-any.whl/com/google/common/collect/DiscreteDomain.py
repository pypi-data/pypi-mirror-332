"""
Python module generated from Java source file com.google.common.collect.DiscreteDomain

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import Serializable
from java.math import BigInteger
from java.util import NoSuchElementException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class DiscreteDomain:
    """
    A descriptor for a *discrete* `Comparable` domain such as all Integer
    instances. A discrete domain is one that supports the three basic operations: .next,
    .previous and .distance, according to their specifications. The methods .minValue and .maxValue should also be overridden for bounded types.
    
    A discrete domain always represents the *entire* set of values of its type; it cannot
    represent partial domains such as "prime integers" or "strings of length 5."
    
    See the Guava User Guide section on <a href=
    "https://github.com/google/guava/wiki/RangesExplained#discrete-domains">`DiscreteDomain`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 10.0
    """

    @staticmethod
    def integers() -> "DiscreteDomain"["Integer"]:
        """
        Returns the discrete domain for values of type `Integer`.

        Since
        - 14.0 (since 10.0 as `DiscreteDomains.integers()`)
        """
        ...


    @staticmethod
    def longs() -> "DiscreteDomain"["Long"]:
        """
        Returns the discrete domain for values of type `Long`.

        Since
        - 14.0 (since 10.0 as `DiscreteDomains.longs()`)
        """
        ...


    @staticmethod
    def bigIntegers() -> "DiscreteDomain"["BigInteger"]:
        """
        Returns the discrete domain for values of type `BigInteger`.

        Since
        - 15.0
        """
        ...


    def next(self, value: "C") -> "C":
        """
        Returns the unique least value of type `C` that is greater than `value`, or `null` if none exists. Inverse operation to .previous.

        Arguments
        - value: any value of type `C`

        Returns
        - the least value greater than `value`, or `null` if `value` is `maxValue()`
        """
        ...


    def previous(self, value: "C") -> "C":
        """
        Returns the unique greatest value of type `C` that is less than `value`, or `null` if none exists. Inverse operation to .next.

        Arguments
        - value: any value of type `C`

        Returns
        - the greatest value less than `value`, or `null` if `value` is `minValue()`
        """
        ...


    def distance(self, start: "C", end: "C") -> int:
        """
        Returns a signed value indicating how many nested invocations of .next (if positive) or
        .previous (if negative) are needed to reach `end` starting from `start`.
        For example, if `end = next(next(next(start)))`, then `distance(start, end) == 3`
        and `distance(end, start) == -3`. As well, `distance(a, a)` is always zero.
        
        Note that this function is necessarily well-defined for any discrete type.

        Returns
        - the distance as described above, or Long.MIN_VALUE or Long.MAX_VALUE if
            the distance is too small or too large, respectively.
        """
        ...


    def minValue(self) -> "C":
        """
        Returns the minimum value of type `C`, if it has one. The minimum value is the unique
        value for which Comparable.compareTo(Object) never returns a positive value for any
        input of type `C`.
        
        The default implementation throws `NoSuchElementException`.

        Returns
        - the minimum value of type `C`; never null

        Raises
        - NoSuchElementException: if the type has no (practical) minimum value; for example,
            java.math.BigInteger
        """
        ...


    def maxValue(self) -> "C":
        """
        Returns the maximum value of type `C`, if it has one. The maximum value is the unique
        value for which Comparable.compareTo(Object) never returns a negative value for any
        input of type `C`.
        
        The default implementation throws `NoSuchElementException`.

        Returns
        - the maximum value of type `C`; never null

        Raises
        - NoSuchElementException: if the type has no (practical) maximum value; for example,
            java.math.BigInteger
        """
        ...
