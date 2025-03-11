"""
Python module generated from Java source file com.google.common.primitives.UnsignedBytes

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.primitives import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.lang.reflect import Field
from java.security import AccessController
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.util import Arrays
from java.util import Comparator
from sun.misc import Unsafe
from typing import Any, Callable, Iterable, Tuple


class UnsignedBytes:
    """
    Static utility methods pertaining to `byte` primitives that interpret values as
    *unsigned* (that is, any negative value `b` is treated as the positive value `256 + b`). The corresponding methods that treat the values as signed are found in SignedBytes, and the methods for which signedness is not an issue are in Bytes.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/PrimitivesExplained">primitive utilities</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 1.0
    """

    MAX_POWER_OF_TWO = (byte) 0x80
    """
    The largest power of two that can be represented as an unsigned `byte`.

    Since
    - 10.0
    """
    MAX_VALUE = (byte) 0xFF
    """
    The largest value that fits into an unsigned byte.

    Since
    - 13.0
    """


    @staticmethod
    def toInt(value: int) -> int:
        """
        Returns the value of the given byte as an integer, when treated as unsigned. That is, returns
        `value + 256` if `value` is negative; `value` itself otherwise.
        
        **Java 8+ users:** use Byte.toUnsignedInt(byte) instead.

        Since
        - 6.0
        """
        ...


    @staticmethod
    def checkedCast(value: int) -> int:
        """
        Returns the `byte` value that, when treated as unsigned, is equal to `value`, if
        possible.

        Arguments
        - value: a value between 0 and 255 inclusive

        Returns
        - the `byte` value that, when treated as unsigned, equals `value`

        Raises
        - IllegalArgumentException: if `value` is negative or greater than 255
        """
        ...


    @staticmethod
    def saturatedCast(value: int) -> int:
        """
        Returns the `byte` value that, when treated as unsigned, is nearest in value to `value`.

        Arguments
        - value: any `long` value

        Returns
        - `(byte) 255` if `value >= 255`, `(byte) 0` if `value <= 0`, and
            `value` cast to `byte` otherwise
        """
        ...


    @staticmethod
    def compare(a: int, b: int) -> int:
        """
        Compares the two specified `byte` values, treating them as unsigned values between 0 and
        255 inclusive. For example, `(byte) -127` is considered greater than `(byte) 127`
        because it is seen as having the value of positive `129`.

        Arguments
        - a: the first `byte` to compare
        - b: the second `byte` to compare

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
        - array: a *nonempty* array of `byte` values

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
        - array: a *nonempty* array of `byte` values

        Returns
        - the value present in `array` that is greater than or equal to every other value
            in the array according to .compare

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def toString(x: int) -> str:
        """
        Returns a string representation of x, where x is treated as unsigned.

        Since
        - 13.0
        """
        ...


    @staticmethod
    def toString(x: int, radix: int) -> str:
        """
        Returns a string representation of `x` for the given radix, where `x` is treated as
        unsigned.

        Arguments
        - x: the value to convert to a string.
        - radix: the radix to use while working with `x`

        Raises
        - IllegalArgumentException: if `radix` is not between Character.MIN_RADIX
            and Character.MAX_RADIX.

        Since
        - 13.0
        """
        ...


    @staticmethod
    def parseUnsignedByte(string: str) -> int:
        """
        Returns the unsigned `byte` value represented by the given decimal string.

        Raises
        - NumberFormatException: if the string does not contain a valid unsigned `byte`
            value
        - NullPointerException: if `string` is null (in contrast to Byte.parseByte(String))

        Since
        - 13.0
        """
        ...


    @staticmethod
    def parseUnsignedByte(string: str, radix: int) -> int:
        """
        Returns the unsigned `byte` value represented by a string with the given radix.

        Arguments
        - string: the string containing the unsigned `byte` representation to be parsed.
        - radix: the radix to use while parsing `string`

        Raises
        - NumberFormatException: if the string does not contain a valid unsigned `byte` with
            the given radix, or if `radix` is not between Character.MIN_RADIX and Character.MAX_RADIX.
        - NullPointerException: if `string` is null (in contrast to Byte.parseByte(String))

        Since
        - 13.0
        """
        ...


    @staticmethod
    def join(separator: str, *array: Tuple[int, ...]) -> str:
        """
        Returns a string containing the supplied `byte` values separated by `separator`.
        For example, `join(":", (byte) 1, (byte) 2, (byte) 255)` returns the string `"1:2:255"`.

        Arguments
        - separator: the text that should appear between consecutive values in the resulting string
            (but not at the start or end)
        - array: an array of `byte` values, possibly empty
        """
        ...


    @staticmethod
    def lexicographicalComparator() -> "Comparator"[list[int]]:
        """
        Returns a comparator that compares two `byte` arrays <a
        href="http://en.wikipedia.org/wiki/Lexicographical_order">lexicographically</a>. That is, it
        compares, using .compare(byte, byte)), the first pair of values that follow any common
        prefix, or when one array is a prefix of the other, treats the shorter array as the lesser. For
        example, `[] < [0x01] < [0x01, 0x7F] < [0x01, 0x80] < [0x02]`. Values are treated as
        unsigned.
        
        The returned comparator is inconsistent with Object.equals(Object) (since arrays
        support only identity equality), but it is consistent with java.util.Arrays.equals(byte[], byte[]).

        Since
        - 2.0
        """
        ...


    @staticmethod
    def sort(array: list[int]) -> None:
        """
        Sorts the array, treating its elements as unsigned bytes.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def sort(array: list[int], fromIndex: int, toIndex: int) -> None:
        """
        Sorts the array between `fromIndex` inclusive and `toIndex` exclusive, treating its
        elements as unsigned bytes.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def sortDescending(array: list[int]) -> None:
        """
        Sorts the elements of `array` in descending order, interpreting them as unsigned 8-bit
        integers.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def sortDescending(array: list[int], fromIndex: int, toIndex: int) -> None:
        """
        Sorts the elements of `array` between `fromIndex` inclusive and `toIndex`
        exclusive in descending order, interpreting them as unsigned 8-bit integers.

        Since
        - 23.1
        """
        ...
