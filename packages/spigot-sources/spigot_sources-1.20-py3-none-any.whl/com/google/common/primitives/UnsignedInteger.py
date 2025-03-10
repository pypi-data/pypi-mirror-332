"""
Python module generated from Java source file com.google.common.primitives.UnsignedInteger

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.primitives import *
from java.math import BigInteger
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class UnsignedInteger(Number, Comparable):
    """
    A wrapper class for unsigned `int` values, supporting arithmetic operations.
    
    In some cases, when speed is more important than code readability, it may be faster simply to
    treat primitive `int` values as unsigned, using the methods from UnsignedInts.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/PrimitivesExplained#unsigned-support">unsigned
    primitive utilities</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 11.0
    """

    ZERO = fromIntBits(0)
    ONE = fromIntBits(1)
    MAX_VALUE = fromIntBits(-1)


    @staticmethod
    def fromIntBits(bits: int) -> "UnsignedInteger":
        """
        Returns an `UnsignedInteger` corresponding to a given bit representation. The argument is
        interpreted as an unsigned 32-bit value. Specifically, the sign bit of `bits` is
        interpreted as a normal bit, and all other bits are treated as usual.
        
        If the argument is nonnegative, the returned result will be equal to `bits`,
        otherwise, the result will be equal to `2^32 + bits`.
        
        To represent unsigned decimal constants, consider .valueOf(long) instead.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def valueOf(value: int) -> "UnsignedInteger":
        """
        Returns an `UnsignedInteger` that is equal to `value`, if possible. The inverse
        operation of .longValue().
        """
        ...


    @staticmethod
    def valueOf(value: "BigInteger") -> "UnsignedInteger":
        """
        Returns a `UnsignedInteger` representing the same value as the specified BigInteger. This is the inverse operation of .bigIntegerValue().

        Raises
        - IllegalArgumentException: if `value` is negative or `value >= 2^32`
        """
        ...


    @staticmethod
    def valueOf(string: str) -> "UnsignedInteger":
        """
        Returns an `UnsignedInteger` holding the value of the specified `String`, parsed as
        an unsigned `int` value.

        Raises
        - NumberFormatException: if the string does not contain a parsable unsigned `int`
            value
        """
        ...


    @staticmethod
    def valueOf(string: str, radix: int) -> "UnsignedInteger":
        """
        Returns an `UnsignedInteger` holding the value of the specified `String`, parsed as
        an unsigned `int` value in the specified radix.

        Raises
        - NumberFormatException: if the string does not contain a parsable unsigned `int`
            value
        """
        ...


    def plus(self, val: "UnsignedInteger") -> "UnsignedInteger":
        """
        Returns the result of adding this and `val`. If the result would have more than 32 bits,
        returns the low 32 bits of the result.

        Since
        - 14.0
        """
        ...


    def minus(self, val: "UnsignedInteger") -> "UnsignedInteger":
        """
        Returns the result of subtracting this and `val`. If the result would be negative,
        returns the low 32 bits of the result.

        Since
        - 14.0
        """
        ...


    def times(self, val: "UnsignedInteger") -> "UnsignedInteger":
        """
        Returns the result of multiplying this and `val`. If the result would have more than 32
        bits, returns the low 32 bits of the result.

        Since
        - 14.0
        """
        ...


    def dividedBy(self, val: "UnsignedInteger") -> "UnsignedInteger":
        """
        Returns the result of dividing this by `val`.

        Raises
        - ArithmeticException: if `val` is zero

        Since
        - 14.0
        """
        ...


    def mod(self, val: "UnsignedInteger") -> "UnsignedInteger":
        """
        Returns this mod `val`.

        Raises
        - ArithmeticException: if `val` is zero

        Since
        - 14.0
        """
        ...


    def intValue(self) -> int:
        """
        Returns the value of this `UnsignedInteger` as an `int`. This is an inverse
        operation to .fromIntBits.
        
        Note that if this `UnsignedInteger` holds a value `>= 2^31`, the returned value
        will be equal to `this - 2^32`.
        """
        ...


    def longValue(self) -> int:
        """
        Returns the value of this `UnsignedInteger` as a `long`.
        """
        ...


    def floatValue(self) -> float:
        """
        Returns the value of this `UnsignedInteger` as a `float`, analogous to a widening
        primitive conversion from `int` to `float`, and correctly rounded.
        """
        ...


    def doubleValue(self) -> float:
        """
        Returns the value of this `UnsignedInteger` as a `float`, analogous to a widening
        primitive conversion from `int` to `double`, and correctly rounded.
        """
        ...


    def bigIntegerValue(self) -> "BigInteger":
        """
        Returns the value of this `UnsignedInteger` as a BigInteger.
        """
        ...


    def compareTo(self, other: "UnsignedInteger") -> int:
        """
        Compares this unsigned integer to another unsigned integer. Returns `0` if they are
        equal, a negative number if `this < other`, and a positive number if `this >
        other`.
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of the `UnsignedInteger` value, in base 10.
        """
        ...


    def toString(self, radix: int) -> str:
        """
        Returns a string representation of the `UnsignedInteger` value, in base `radix`. If
        `radix < Character.MIN_RADIX` or `radix > Character.MAX_RADIX`, the radix `10` is used.
        """
        ...
