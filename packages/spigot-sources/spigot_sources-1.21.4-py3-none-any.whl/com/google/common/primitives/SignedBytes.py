"""
Python module generated from Java source file com.google.common.primitives.SignedBytes

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.primitives import *
from java.util import Arrays
from java.util import Comparator
from typing import Any, Callable, Iterable, Tuple


class SignedBytes:

    MAX_POWER_OF_TWO = 1 << 6
    """
    The largest power of two that can be represented as a signed `byte`.

    Since
    - 10.0
    """


    @staticmethod
    def checkedCast(value: int) -> int:
        """
        Returns the `byte` value that is equal to `value`, if possible.

        Arguments
        - value: any value in the range of the `byte` type

        Returns
        - the `byte` value that equals `value`

        Raises
        - IllegalArgumentException: if `value` is greater than Byte.MAX_VALUE or
            less than Byte.MIN_VALUE
        """
        ...


    @staticmethod
    def saturatedCast(value: int) -> int:
        """
        Returns the `byte` nearest in value to `value`.

        Arguments
        - value: any `long` value

        Returns
        - the same value cast to `byte` if it is in the range of the `byte` type,
            Byte.MAX_VALUE if it is too large, or Byte.MIN_VALUE if it is too small
        """
        ...


    @staticmethod
    def compare(a: int, b: int) -> int:
        """
        Compares the two specified `byte` values. The sign of the value returned is the same as
        that of `((Byte) a).compareTo(b)`.
        
        **Note:** this method behaves identically to the JDK 7 method Byte.compare.

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
        Returns the least value present in `array`.

        Arguments
        - array: a *nonempty* array of `byte` values

        Returns
        - the value present in `array` that is less than or equal to every other value in
            the array

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def max(*array: Tuple[int, ...]) -> int:
        """
        Returns the greatest value present in `array`.

        Arguments
        - array: a *nonempty* array of `byte` values

        Returns
        - the value present in `array` that is greater than or equal to every other value
            in the array

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def join(separator: str, *array: Tuple[int, ...]) -> str:
        """
        Returns a string containing the supplied `byte` values separated by `separator`.
        For example, `join(":", 0x01, 0x02, -0x01)` returns the string `"1:2:-1"`.

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
        example, `[] < [0x01] < [0x01, 0x80] < [0x01, 0x7F] < [0x02]`. Values are treated as
        signed.
        
        The returned comparator is inconsistent with Object.equals(Object) (since arrays
        support only identity equality), but it is consistent with java.util.Arrays.equals(byte[], byte[]).

        Since
        - 2.0
        """
        ...


    @staticmethod
    def sortDescending(array: list[int]) -> None:
        """
        Sorts the elements of `array` in descending order.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def sortDescending(array: list[int], fromIndex: int, toIndex: int) -> None:
        """
        Sorts the elements of `array` between `fromIndex` inclusive and `toIndex`
        exclusive in descending order.

        Since
        - 23.1
        """
        ...
