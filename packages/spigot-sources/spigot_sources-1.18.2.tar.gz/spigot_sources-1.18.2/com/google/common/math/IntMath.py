"""
Python module generated from Java source file com.google.common.math.IntMath

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.math import *
from com.google.common.primitives import Ints
from java.math import BigInteger
from java.math import RoundingMode
from typing import Any, Callable, Iterable, Tuple


class IntMath:
    """
    A class for arithmetic on values of type `int`. Where possible, methods are defined and
    named analogously to their `BigInteger` counterparts.
    
    The implementations of many methods in this class are based on material from Henry S. Warren,
    Jr.'s *Hacker's Delight*, (Addison Wesley, 2002).
    
    Similar functionality for `long` and for BigInteger can be found in LongMath and BigIntegerMath respectively. For other common operations on `int`
    values, see com.google.common.primitives.Ints.

    Author(s)
    - Louis Wasserman

    Since
    - 11.0
    """

    @staticmethod
    def ceilingPowerOfTwo(x: int) -> int:
        """
        Returns the smallest power of two greater than or equal to `x`. This is equivalent to
        `checkedPow(2, log2(x, CEILING))`.

        Raises
        - IllegalArgumentException: if `x <= 0`
        - ArithmeticException: of the next-higher power of two is not representable as an `int`, i.e. when `x > 2^30`

        Since
        - 20.0
        """
        ...


    @staticmethod
    def floorPowerOfTwo(x: int) -> int:
        """
        Returns the largest power of two less than or equal to `x`. This is equivalent to `checkedPow(2, log2(x, FLOOR))`.

        Raises
        - IllegalArgumentException: if `x <= 0`

        Since
        - 20.0
        """
        ...


    @staticmethod
    def isPowerOfTwo(x: int) -> bool:
        """
        Returns `True` if `x` represents a power of two.
        
        This differs from `Integer.bitCount(x) == 1`, because `Integer.bitCount(Integer.MIN_VALUE) == 1`, but Integer.MIN_VALUE is not a power of two.
        """
        ...


    @staticmethod
    def log2(x: int, mode: "RoundingMode") -> int:
        """
        Returns the base-2 logarithm of `x`, rounded according to the specified rounding mode.

        Raises
        - IllegalArgumentException: if `x <= 0`
        - ArithmeticException: if `mode` is RoundingMode.UNNECESSARY and `x`
            is not a power of two
        """
        ...


    @staticmethod
    def log10(x: int, mode: "RoundingMode") -> int:
        """
        Returns the base-10 logarithm of `x`, rounded according to the specified rounding mode.

        Raises
        - IllegalArgumentException: if `x <= 0`
        - ArithmeticException: if `mode` is RoundingMode.UNNECESSARY and `x`
            is not a power of ten
        """
        ...


    @staticmethod
    def pow(b: int, k: int) -> int:
        """
        Returns `b` to the `k`th power. Even if the result overflows, it will be equal to
        `BigInteger.valueOf(b).pow(k).intValue()`. This implementation runs in `O(log k)`
        time.
        
        Compare .checkedPow, which throws an ArithmeticException upon overflow.

        Raises
        - IllegalArgumentException: if `k < 0`
        """
        ...


    @staticmethod
    def sqrt(x: int, mode: "RoundingMode") -> int:
        """
        Returns the square root of `x`, rounded with the specified rounding mode.

        Raises
        - IllegalArgumentException: if `x < 0`
        - ArithmeticException: if `mode` is RoundingMode.UNNECESSARY and `sqrt(x)` is not an integer
        """
        ...


    @staticmethod
    def divide(p: int, q: int, mode: "RoundingMode") -> int:
        """
        Returns the result of dividing `p` by `q`, rounding using the specified `RoundingMode`.

        Raises
        - ArithmeticException: if `q == 0`, or if `mode == UNNECESSARY` and `a`
            is not an integer multiple of `b`
        """
        ...


    @staticmethod
    def mod(x: int, m: int) -> int:
        """
        Returns `x mod m`, a non-negative value less than `m`. This differs from `x %
        m`, which might be negative.
        
        For example:
        
        ````mod(7, 4) == 3
        mod(-7, 4) == 1
        mod(-1, 4) == 3
        mod(-8, 4) == 0
        mod(8, 4) == 0````

        Raises
        - ArithmeticException: if `m <= 0`

        See
        - <a href="http://docs.oracle.com/javase/specs/jls/se7/html/jls-15.html.jls-15.17.3">
            Remainder Operator</a>
        """
        ...


    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        Returns the greatest common divisor of `a, b`. Returns `0` if `a == 0 && b ==
        0`.

        Raises
        - IllegalArgumentException: if `a < 0` or `b < 0`
        """
        ...


    @staticmethod
    def checkedAdd(a: int, b: int) -> int:
        """
        Returns the sum of `a` and `b`, provided it does not overflow.

        Raises
        - ArithmeticException: if `a + b` overflows in signed `int` arithmetic
        """
        ...


    @staticmethod
    def checkedSubtract(a: int, b: int) -> int:
        """
        Returns the difference of `a` and `b`, provided it does not overflow.

        Raises
        - ArithmeticException: if `a - b` overflows in signed `int` arithmetic
        """
        ...


    @staticmethod
    def checkedMultiply(a: int, b: int) -> int:
        """
        Returns the product of `a` and `b`, provided it does not overflow.

        Raises
        - ArithmeticException: if `a * b` overflows in signed `int` arithmetic
        """
        ...


    @staticmethod
    def checkedPow(b: int, k: int) -> int:
        """
        Returns the `b` to the `k`th power, provided it does not overflow.
        
        .pow may be faster, but does not check for overflow.

        Raises
        - ArithmeticException: if `b` to the `k`th power overflows in signed `int` arithmetic
        """
        ...


    @staticmethod
    def saturatedAdd(a: int, b: int) -> int:
        """
        Returns the sum of `a` and `b` unless it would overflow or underflow in which case
        `Integer.MAX_VALUE` or `Integer.MIN_VALUE` is returned, respectively.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def saturatedSubtract(a: int, b: int) -> int:
        """
        Returns the difference of `a` and `b` unless it would overflow or underflow in
        which case `Integer.MAX_VALUE` or `Integer.MIN_VALUE` is returned, respectively.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def saturatedMultiply(a: int, b: int) -> int:
        """
        Returns the product of `a` and `b` unless it would overflow or underflow in which
        case `Integer.MAX_VALUE` or `Integer.MIN_VALUE` is returned, respectively.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def saturatedPow(b: int, k: int) -> int:
        """
        Returns the `b` to the `k`th power, unless it would overflow or underflow in which
        case `Integer.MAX_VALUE` or `Integer.MIN_VALUE` is returned, respectively.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def factorial(n: int) -> int:
        """
        Returns `n!`, that is, the product of the first `n` positive integers, `1` if
        `n == 0`, or Integer.MAX_VALUE if the result does not fit in a `int`.

        Raises
        - IllegalArgumentException: if `n < 0`
        """
        ...


    @staticmethod
    def binomial(n: int, k: int) -> int:
        """
        Returns `n` choose `k`, also known as the binomial coefficient of `n` and
        `k`, or Integer.MAX_VALUE if the result does not fit in an `int`.

        Raises
        - IllegalArgumentException: if `n < 0`, `k < 0` or `k > n`
        """
        ...


    @staticmethod
    def mean(x: int, y: int) -> int:
        """
        Returns the arithmetic mean of `x` and `y`, rounded towards negative infinity. This
        method is overflow resilient.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def isPrime(n: int) -> bool:
        """
        Returns `True` if `n` is a <a
        href="http://mathworld.wolfram.com/PrimeNumber.html">prime number</a>: an integer *greater
        than one* that cannot be factored into a product of *smaller* positive integers.
        Returns `False` if `n` is zero, one, or a composite number (one which *can* be
        factored into smaller positive integers).
        
        To test larger numbers, use LongMath.isPrime or BigInteger.isProbablePrime.

        Raises
        - IllegalArgumentException: if `n` is negative

        Since
        - 20.0
        """
        ...
