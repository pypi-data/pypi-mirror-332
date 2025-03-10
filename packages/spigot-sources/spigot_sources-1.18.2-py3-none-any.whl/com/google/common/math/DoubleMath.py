"""
Python module generated from Java source file com.google.common.math.DoubleMath

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.math import *
from com.google.common.primitives import Booleans
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.math import BigInteger
from java.math import RoundingMode
from java.util import Iterator
from typing import Any, Callable, Iterable, Tuple


class DoubleMath:
    """
    A class for arithmetic on doubles that is not covered by java.lang.Math.

    Author(s)
    - Louis Wasserman

    Since
    - 11.0
    """

    @staticmethod
    def roundToInt(x: float, mode: "RoundingMode") -> int:
        """
        Returns the `int` value that is equal to `x` rounded with the specified rounding
        mode, if possible.

        Raises
        - ArithmeticException: if
            
              - `x` is infinite or NaN
              - `x`, after being rounded to a mathematical integer using the specified rounding
                  mode, is either less than `Integer.MIN_VALUE` or greater than `Integer.MAX_VALUE`
              - `x` is not a mathematical integer and `mode` is RoundingMode.UNNECESSARY
            
        """
        ...


    @staticmethod
    def roundToLong(x: float, mode: "RoundingMode") -> int:
        """
        Returns the `long` value that is equal to `x` rounded with the specified rounding
        mode, if possible.

        Raises
        - ArithmeticException: if
            
              - `x` is infinite or NaN
              - `x`, after being rounded to a mathematical integer using the specified rounding
                  mode, is either less than `Long.MIN_VALUE` or greater than `Long.MAX_VALUE`
              - `x` is not a mathematical integer and `mode` is RoundingMode.UNNECESSARY
            
        """
        ...


    @staticmethod
    def roundToBigInteger(x: float, mode: "RoundingMode") -> "BigInteger":
        ...


    @staticmethod
    def isPowerOfTwo(x: float) -> bool:
        """
        Returns `True` if `x` is exactly equal to `2^k` for some finite integer
        `k`.
        """
        ...


    @staticmethod
    def log2(x: float) -> float:
        """
        Returns the base 2 logarithm of a double value.
        
        Special cases:
        
        
          - If `x` is NaN or less than zero, the result is NaN.
          - If `x` is positive infinity, the result is positive infinity.
          - If `x` is positive or negative zero, the result is negative infinity.
        
        
        The computed result is within 1 ulp of the exact result.
        
        If the result of this method will be immediately rounded to an `int`, .log2(double, RoundingMode) is faster.
        """
        ...


    @staticmethod
    def log2(x: float, mode: "RoundingMode") -> int:
        """
        Returns the base 2 logarithm of a double value, rounded with the specified rounding mode to an
        `int`.
        
        Regardless of the rounding mode, this is faster than `(int) log2(x)`.

        Raises
        - IllegalArgumentException: if `x <= 0.0`, `x` is NaN, or `x` is
            infinite
        """
        ...


    @staticmethod
    def isMathematicalInteger(x: float) -> bool:
        """
        Returns `True` if `x` represents a mathematical integer.
        
        This is equivalent to, but not necessarily implemented as, the expression `!Double.isNaN(x) && !Double.isInfinite(x) && x == Math.rint(x)`.
        """
        ...


    @staticmethod
    def factorial(n: int) -> float:
        """
        Returns `n!`, that is, the product of the first `n` positive integers, `1` if
        `n == 0`, or `n!`, or Double.POSITIVE_INFINITY if `n! >
        Double.MAX_VALUE`.
        
        The result is within 1 ulp of the True value.

        Raises
        - IllegalArgumentException: if `n < 0`
        """
        ...


    @staticmethod
    def fuzzyEquals(a: float, b: float, tolerance: float) -> bool:
        """
        Returns `True` if `a` and `b` are within `tolerance` of each other.
        
        Technically speaking, this is equivalent to `Math.abs(a - b) <= tolerance ||
        Double.valueOf(a).equals(Double.valueOf(b))`.
        
        Notable special cases include:
        
        
          - All NaNs are fuzzily equal.
          - If `a == b`, then `a` and `b` are always fuzzily equal.
          - Positive and negative zero are always fuzzily equal.
          - If `tolerance` is zero, and neither `a` nor `b` is NaN, then `a`
              and `b` are fuzzily equal if and only if `a == b`.
          - With Double.POSITIVE_INFINITY tolerance, all non-NaN values are fuzzily equal.
          - With finite tolerance, `Double.POSITIVE_INFINITY` and `Double.NEGATIVE_INFINITY` are fuzzily equal only to themselves.
        
        
        This is reflexive and symmetric, but *not* transitive, so it is *not* an
        equivalence relation and *not* suitable for use in Object.equals
        implementations.

        Raises
        - IllegalArgumentException: if `tolerance` is `< 0` or NaN

        Since
        - 13.0
        """
        ...


    @staticmethod
    def fuzzyCompare(a: float, b: float, tolerance: float) -> int:
        """
        Compares `a` and `b` "fuzzily," with a tolerance for nearly-equal values.
        
        This method is equivalent to `fuzzyEquals(a, b, tolerance) ? 0 : Double.compare(a,
        b)`. In particular, like Double.compare(double, double), it treats all NaN values as
        equal and greater than all other values (including Double.POSITIVE_INFINITY).
        
        This is *not* a total ordering and is *not* suitable for use in Comparable.compareTo implementations. In particular, it is not transitive.

        Raises
        - IllegalArgumentException: if `tolerance` is `< 0` or NaN

        Since
        - 13.0
        """
        ...


    @staticmethod
    def mean(*values: Tuple[float, ...]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of
        `values`.
        
        If these values are a sample drawn from a population, this is also an unbiased estimator of
        the arithmetic mean of the population.

        Arguments
        - values: a nonempty series of values

        Raises
        - IllegalArgumentException: if `values` is empty or contains any non-finite value

        Deprecated
        - Use Stats.meanOf instead, noting the less strict handling of non-finite
            values.
        """
        ...


    @staticmethod
    def mean(*values: Tuple[int, ...]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of
        `values`.
        
        If these values are a sample drawn from a population, this is also an unbiased estimator of
        the arithmetic mean of the population.

        Arguments
        - values: a nonempty series of values

        Raises
        - IllegalArgumentException: if `values` is empty

        Deprecated
        - Use Stats.meanOf instead, noting the less strict handling of non-finite
            values.
        """
        ...


    @staticmethod
    def mean(*values: Tuple[int, ...]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of
        `values`.
        
        If these values are a sample drawn from a population, this is also an unbiased estimator of
        the arithmetic mean of the population.

        Arguments
        - values: a nonempty series of values, which will be converted to `double` values
            (this may cause loss of precision for longs of magnitude over 2^53 (slightly over 9e15))

        Raises
        - IllegalArgumentException: if `values` is empty

        Deprecated
        - Use Stats.meanOf instead, noting the less strict handling of non-finite
            values.
        """
        ...


    @staticmethod
    def mean(values: Iterable["Number"]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of
        `values`.
        
        If these values are a sample drawn from a population, this is also an unbiased estimator of
        the arithmetic mean of the population.

        Arguments
        - values: a nonempty series of values, which will be converted to `double` values
            (this may cause loss of precision)

        Raises
        - IllegalArgumentException: if `values` is empty or contains any non-finite value

        Deprecated
        - Use Stats.meanOf instead, noting the less strict handling of non-finite
            values.
        """
        ...


    @staticmethod
    def mean(values: Iterator["Number"]) -> float:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean</a> of
        `values`.
        
        If these values are a sample drawn from a population, this is also an unbiased estimator of
        the arithmetic mean of the population.

        Arguments
        - values: a nonempty series of values, which will be converted to `double` values
            (this may cause loss of precision)

        Raises
        - IllegalArgumentException: if `values` is empty or contains any non-finite value

        Deprecated
        - Use Stats.meanOf instead, noting the less strict handling of non-finite
            values.
        """
        ...
