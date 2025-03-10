"""
Python module generated from Java source file com.google.common.primitives.UnsignedLongs

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.primitives import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.math import BigInteger
from java.util import Arrays
from java.util import Comparator
from typing import Any, Callable, Iterable, Tuple


class UnsignedLongs:
    """
    Static utility methods pertaining to `long` primitives that interpret values as
    *unsigned* (that is, any negative value `x` is treated as the positive value `2^64 + x`). The methods for which signedness is not an issue are in Longs, as well as
    signed versions of methods for which signedness is an issue.
    
    In addition, this class provides several static methods for converting a `long` to a
    `String` and a `String` to a `long` that treat the `long` as an unsigned
    number.
    
    Users of these utilities must be *extremely careful* not to mix up signed and unsigned
    `long` values. When possible, it is recommended that the UnsignedLong wrapper class
    be used, at a small efficiency penalty, to enforce the distinction in the type system.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/PrimitivesExplained#unsigned-support">unsigned
    primitive utilities</a>.

    Author(s)
    - Colin Evans

    Since
    - 10.0
    """

    MAX_VALUE = -1L


    @staticmethod
    def compare(a: int, b: int) -> int:
        """
        Compares the two specified `long` values, treating them as unsigned values between `0` and `2^64 - 1` inclusive.
        
        **Java 8 users:** use Long.compareUnsigned(long, long) instead.

        Arguments
        - a: the first unsigned `long` to compare
        - b: the second unsigned `long` to compare

        Returns
        - a negative value if `a` is less than `b`; a positive value if `a` is
            greater than `b`; or zero if they are equal
        """
        ...


    @staticmethod
    def min(*array: Tuple[int, ...]) -> int:
        """
        Returns the least value present in `array`, treating values as unsigned.

        Arguments
        - array: a *nonempty* array of unsigned `long` values

        Returns
        - the value present in `array` that is less than or equal to every other value in
            the array according to .compare

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def max(*array: Tuple[int, ...]) -> int:
        """
        Returns the greatest value present in `array`, treating values as unsigned.

        Arguments
        - array: a *nonempty* array of unsigned `long` values

        Returns
        - the value present in `array` that is greater than or equal to every other value
            in the array according to .compare

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def join(separator: str, *array: Tuple[int, ...]) -> str:
        """
        Returns a string containing the supplied unsigned `long` values separated by `separator`. For example, `join("-", 1, 2, 3)` returns the string `"1-2-3"`.

        Arguments
        - separator: the text that should appear between consecutive values in the resulting string
            (but not at the start or end)
        - array: an array of unsigned `long` values, possibly empty
        """
        ...


    @staticmethod
    def lexicographicalComparator() -> "Comparator"[list[int]]:
        """
        Returns a comparator that compares two arrays of unsigned `long` values <a
        href="http://en.wikipedia.org/wiki/Lexicographical_order">lexicographically</a>. That is, it
        compares, using .compare(long, long)), the first pair of values that follow any common
        prefix, or when one array is a prefix of the other, treats the shorter array as the lesser. For
        example, `[] < [1L] < [1L, 2L] < [2L] < [1L << 63]`.
        
        The returned comparator is inconsistent with Object.equals(Object) (since arrays
        support only identity equality), but it is consistent with Arrays.equals(long[],
        long[]).
        """
        ...


    @staticmethod
    def sort(array: list[int]) -> None:
        """
        Sorts the array, treating its elements as unsigned 64-bit integers.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def sort(array: list[int], fromIndex: int, toIndex: int) -> None:
        """
        Sorts the array between `fromIndex` inclusive and `toIndex` exclusive, treating its
        elements as unsigned 64-bit integers.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def sortDescending(array: list[int]) -> None:
        """
        Sorts the elements of `array` in descending order, interpreting them as unsigned 64-bit
        integers.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def sortDescending(array: list[int], fromIndex: int, toIndex: int) -> None:
        """
        Sorts the elements of `array` between `fromIndex` inclusive and `toIndex`
        exclusive in descending order, interpreting them as unsigned 64-bit integers.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def divide(dividend: int, divisor: int) -> int:
        """
        Returns dividend / divisor, where the dividend and divisor are treated as unsigned 64-bit
        quantities.
        
        **Java 8 users:** use Long.divideUnsigned(long, long) instead.

        Arguments
        - dividend: the dividend (numerator)
        - divisor: the divisor (denominator)

        Raises
        - ArithmeticException: if divisor is 0
        """
        ...


    @staticmethod
    def remainder(dividend: int, divisor: int) -> int:
        """
        Returns dividend % divisor, where the dividend and divisor are treated as unsigned 64-bit
        quantities.
        
        **Java 8 users:** use Long.remainderUnsigned(long, long) instead.

        Arguments
        - dividend: the dividend (numerator)
        - divisor: the divisor (denominator)

        Raises
        - ArithmeticException: if divisor is 0

        Since
        - 11.0
        """
        ...


    @staticmethod
    def parseUnsignedLong(string: str) -> int:
        """
        Returns the unsigned `long` value represented by the given decimal string.
        
        **Java 8 users:** use Long.parseUnsignedLong(String) instead.

        Raises
        - NumberFormatException: if the string does not contain a valid unsigned `long`
            value
        - NullPointerException: if `string` is null (in contrast to Long.parseLong(String))
        """
        ...


    @staticmethod
    def parseUnsignedLong(string: str, radix: int) -> int:
        """
        Returns the unsigned `long` value represented by a string with the given radix.
        
        **Java 8 users:** use Long.parseUnsignedLong(String, int) instead.

        Arguments
        - string: the string containing the unsigned `long` representation to be parsed.
        - radix: the radix to use while parsing `string`

        Raises
        - NumberFormatException: if the string does not contain a valid unsigned `long` with
            the given radix, or if `radix` is not between Character.MIN_RADIX and Character.MAX_RADIX.
        - NullPointerException: if `string` is null (in contrast to Long.parseLong(String))
        """
        ...


    @staticmethod
    def decode(stringValue: str) -> int:
        """
        Returns the unsigned `long` value represented by the given string.
        
        Accepts a decimal, hexadecimal, or octal number given by specifying the following prefix:
        
        
          - `0x`*HexDigits*
          - `0X`*HexDigits*
          - `.`*HexDigits*
          - `0`*OctalDigits*

        Raises
        - NumberFormatException: if the string does not contain a valid unsigned `long`
            value

        Since
        - 13.0
        """
        ...


    @staticmethod
    def toString(x: int) -> str:
        """
        Returns a string representation of x, where x is treated as unsigned.
        
        **Java 8 users:** use Long.toUnsignedString(long) instead.
        """
        ...


    @staticmethod
    def toString(x: int, radix: int) -> str:
        """
        Returns a string representation of `x` for the given radix, where `x` is treated as
        unsigned.
        
        **Java 8 users:** use Long.toUnsignedString(long, int) instead.

        Arguments
        - x: the value to convert to a string.
        - radix: the radix to use while working with `x`

        Raises
        - IllegalArgumentException: if `radix` is not between Character.MIN_RADIX
            and Character.MAX_RADIX.
        """
        ...
