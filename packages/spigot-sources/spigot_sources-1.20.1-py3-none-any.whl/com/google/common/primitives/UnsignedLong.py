"""
Python module generated from Java source file com.google.common.primitives.UnsignedLong

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.primitives import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import Serializable
from java.math import BigInteger
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class UnsignedLong(Number, Comparable, Serializable):
    """
    A wrapper class for unsigned `long` values, supporting arithmetic operations.
    
    In some cases, when speed is more important than code readability, it may be faster simply to
    treat primitive `long` values as unsigned, using the methods from UnsignedLongs.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/PrimitivesExplained#unsigned-support">unsigned
    primitive utilities</a>.

    Author(s)
    - Colin Evans

    Since
    - 11.0
    """

    ZERO = UnsignedLong(0)
    ONE = UnsignedLong(1)
    MAX_VALUE = UnsignedLong(-1L)


    @staticmethod
    def fromLongBits(bits: int) -> "UnsignedLong":
        """
        Returns an `UnsignedLong` corresponding to a given bit representation. The argument is
        interpreted as an unsigned 64-bit value. Specifically, the sign bit of `bits` is
        interpreted as a normal bit, and all other bits are treated as usual.
        
        If the argument is nonnegative, the returned result will be equal to `bits`,
        otherwise, the result will be equal to `2^64 + bits`.
        
        To represent decimal constants less than `2^63`, consider .valueOf(long)
        instead.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def valueOf(value: int) -> "UnsignedLong":
        """
        Returns an `UnsignedLong` representing the same value as the specified `long`.

        Raises
        - IllegalArgumentException: if `value` is negative

        Since
        - 14.0
        """
        ...


    @staticmethod
    def valueOf(value: "BigInteger") -> "UnsignedLong":
        """
        Returns a `UnsignedLong` representing the same value as the specified `BigInteger`.
        This is the inverse operation of .bigIntegerValue().

        Raises
        - IllegalArgumentException: if `value` is negative or `value >= 2^64`
        """
        ...


    @staticmethod
    def valueOf(string: str) -> "UnsignedLong":
        """
        Returns an `UnsignedLong` holding the value of the specified `String`, parsed as an
        unsigned `long` value.

        Raises
        - NumberFormatException: if the string does not contain a parsable unsigned `long`
            value
        """
        ...


    @staticmethod
    def valueOf(string: str, radix: int) -> "UnsignedLong":
        """
        Returns an `UnsignedLong` holding the value of the specified `String`, parsed as an
        unsigned `long` value in the specified radix.

        Raises
        - NumberFormatException: if the string does not contain a parsable unsigned `long`
            value, or `radix` is not between Character.MIN_RADIX and Character.MAX_RADIX
        """
        ...


    def plus(self, val: "UnsignedLong") -> "UnsignedLong":
        """
        Returns the result of adding this and `val`. If the result would have more than 64 bits,
        returns the low 64 bits of the result.

        Since
        - 14.0
        """
        ...


    def minus(self, val: "UnsignedLong") -> "UnsignedLong":
        """
        Returns the result of subtracting this and `val`. If the result would have more than 64
        bits, returns the low 64 bits of the result.

        Since
        - 14.0
        """
        ...


    def times(self, val: "UnsignedLong") -> "UnsignedLong":
        """
        Returns the result of multiplying this and `val`. If the result would have more than 64
        bits, returns the low 64 bits of the result.

        Since
        - 14.0
        """
        ...


    def dividedBy(self, val: "UnsignedLong") -> "UnsignedLong":
        """
        Returns the result of dividing this by `val`.

        Since
        - 14.0
        """
        ...


    def mod(self, val: "UnsignedLong") -> "UnsignedLong":
        """
        Returns this modulo `val`.

        Since
        - 14.0
        """
        ...


    def intValue(self) -> int:
        """
        Returns the value of this `UnsignedLong` as an `int`.
        """
        ...


    def longValue(self) -> int:
        """
        Returns the value of this `UnsignedLong` as a `long`. This is an inverse operation
        to .fromLongBits.
        
        Note that if this `UnsignedLong` holds a value `>= 2^63`, the returned value
        will be equal to `this - 2^64`.
        """
        ...


    def floatValue(self) -> float:
        """
        Returns the value of this `UnsignedLong` as a `float`, analogous to a widening
        primitive conversion from `long` to `float`, and correctly rounded.
        """
        ...


    def doubleValue(self) -> float:
        """
        Returns the value of this `UnsignedLong` as a `double`, analogous to a widening
        primitive conversion from `long` to `double`, and correctly rounded.
        """
        ...


    def bigIntegerValue(self) -> "BigInteger":
        """
        Returns the value of this `UnsignedLong` as a BigInteger.
        """
        ...


    def compareTo(self, o: "UnsignedLong") -> int:
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of the `UnsignedLong` value, in base 10.
        """
        ...


    def toString(self, radix: int) -> str:
        """
        Returns a string representation of the `UnsignedLong` value, in base `radix`. If
        `radix < Character.MIN_RADIX` or `radix > Character.MAX_RADIX`, the radix `10` is used.
        """
        ...
