"""
Python module generated from Java source file com.google.common.math.BigIntegerMath

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.math import *
from java.math import BigDecimal
from java.math import BigInteger
from java.math import RoundingMode
from typing import Any, Callable, Iterable, Tuple


class BigIntegerMath:
    """
    A class for arithmetic on values of type `BigInteger`.
    
    The implementations of many methods in this class are based on material from Henry S. Warren,
    Jr.'s *Hacker's Delight*, (Addison Wesley, 2002).
    
    Similar functionality for `int` and for `long` can be found in IntMath and
    LongMath respectively.

    Author(s)
    - Louis Wasserman

    Since
    - 11.0
    """

    @staticmethod
    def ceilingPowerOfTwo(x: "BigInteger") -> "BigInteger":
        """
        Returns the smallest power of two greater than or equal to `x`. This is equivalent to
        `BigInteger.valueOf(2).pow(log2(x, CEILING))`.

        Raises
        - IllegalArgumentException: if `x <= 0`

        Since
        - 20.0
        """
        ...


    @staticmethod
    def floorPowerOfTwo(x: "BigInteger") -> "BigInteger":
        """
        Returns the largest power of two less than or equal to `x`. This is equivalent to `BigInteger.valueOf(2).pow(log2(x, FLOOR))`.

        Raises
        - IllegalArgumentException: if `x <= 0`

        Since
        - 20.0
        """
        ...


    @staticmethod
    def isPowerOfTwo(x: "BigInteger") -> bool:
        """
        Returns `True` if `x` represents a power of two.
        """
        ...


    @staticmethod
    def log2(x: "BigInteger", mode: "RoundingMode") -> int:
        """
        Returns the base-2 logarithm of `x`, rounded according to the specified rounding mode.

        Raises
        - IllegalArgumentException: if `x <= 0`
        - ArithmeticException: if `mode` is RoundingMode.UNNECESSARY and `x`
            is not a power of two
        """
        ...


    @staticmethod
    def log10(x: "BigInteger", mode: "RoundingMode") -> int:
        """
        Returns the base-10 logarithm of `x`, rounded according to the specified rounding mode.

        Raises
        - IllegalArgumentException: if `x <= 0`
        - ArithmeticException: if `mode` is RoundingMode.UNNECESSARY and `x`
            is not a power of ten
        """
        ...


    @staticmethod
    def sqrt(x: "BigInteger", mode: "RoundingMode") -> "BigInteger":
        """
        Returns the square root of `x`, rounded with the specified rounding mode.

        Raises
        - IllegalArgumentException: if `x < 0`
        - ArithmeticException: if `mode` is RoundingMode.UNNECESSARY and `sqrt(x)` is not an integer
        """
        ...


    @staticmethod
    def roundToDouble(x: "BigInteger", mode: "RoundingMode") -> float:
        """
        Returns `x`, rounded to a `double` with the specified rounding mode. If `x`
        is precisely representable as a `double`, its `double` value will be returned;
        otherwise, the rounding will choose between the two nearest representable values with `mode`.
        
        For the case of RoundingMode.HALF_DOWN, `HALF_UP`, and `HALF_EVEN`,
        infinite `double` values are considered infinitely far away. For example, 2^2000 is not
        representable as a double, but `roundToDouble(BigInteger.valueOf(2).pow(2000), HALF_UP)`
        will return `Double.MAX_VALUE`, not `Double.POSITIVE_INFINITY`.
        
        For the case of RoundingMode.HALF_EVEN, this implementation uses the IEEE 754
        default rounding mode: if the two nearest representable values are equally near, the one with
        the least significant bit zero is chosen. (In such cases, both of the nearest representable
        values are even integers; this method returns the one that is a multiple of a greater power of
        two.)

        Raises
        - ArithmeticException: if `mode` is RoundingMode.UNNECESSARY and `x`
            is not precisely representable as a `double`

        Since
        - 30.0
        """
        ...


    @staticmethod
    def divide(p: "BigInteger", q: "BigInteger", mode: "RoundingMode") -> "BigInteger":
        """
        Returns the result of dividing `p` by `q`, rounding using the specified `RoundingMode`.

        Raises
        - ArithmeticException: if `q == 0`, or if `mode == UNNECESSARY` and `a`
            is not an integer multiple of `b`
        """
        ...


    @staticmethod
    def factorial(n: int) -> "BigInteger":
        """
        Returns `n!`, that is, the product of the first `n` positive integers, or `1`
        if `n == 0`.
        
        **Warning:** the result takes *O(n log n)* space, so use cautiously.
        
        This uses an efficient binary recursive algorithm to compute the factorial with balanced
        multiplies. It also removes all the 2s from the intermediate products (shifting them back in at
        the end).

        Raises
        - IllegalArgumentException: if `n < 0`
        """
        ...


    @staticmethod
    def binomial(n: int, k: int) -> "BigInteger":
        """
        Returns `n` choose `k`, also known as the binomial coefficient of `n` and
        `k`, that is, `n! / (k! (n - k)!)`.
        
        **Warning:** the result can take as much as *O(k log n)* space.

        Raises
        - IllegalArgumentException: if `n < 0`, `k < 0`, or `k > n`
        """
        ...
