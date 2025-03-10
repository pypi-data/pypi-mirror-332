"""
Python module generated from Java source file com.google.common.primitives.Chars

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.primitives import *
from java.io import Serializable
from java.util import AbstractList
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import RandomAccess
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Chars:
    """
    Static utility methods pertaining to `char` primitives, that are not already found in
    either Character or Arrays.
    
    All the operations in this class treat `char` values strictly numerically; they are
    neither Unicode-aware nor locale-dependent.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/PrimitivesExplained">primitive utilities</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    BYTES = Character.SIZE / Byte.SIZE
    """
    The number of bytes required to represent a primitive `char` value.
    
    **Java 8 users:** use Character.BYTES instead.
    """


    @staticmethod
    def hashCode(value: str) -> int:
        """
        Returns a hash code for `value`; equal to the result of invoking `((Character)
        value).hashCode()`.
        
        **Java 8 users:** use Character.hashCode(char) instead.

        Arguments
        - value: a primitive `char` value

        Returns
        - a hash code for the value
        """
        ...


    @staticmethod
    def checkedCast(value: int) -> str:
        """
        Returns the `char` value that is equal to `value`, if possible.

        Arguments
        - value: any value in the range of the `char` type

        Returns
        - the `char` value that equals `value`

        Raises
        - IllegalArgumentException: if `value` is greater than Character.MAX_VALUE
            or less than Character.MIN_VALUE
        """
        ...


    @staticmethod
    def saturatedCast(value: int) -> str:
        """
        Returns the `char` nearest in value to `value`.

        Arguments
        - value: any `long` value

        Returns
        - the same value cast to `char` if it is in the range of the `char` type,
            Character.MAX_VALUE if it is too large, or Character.MIN_VALUE if it is too
            small
        """
        ...


    @staticmethod
    def compare(a: str, b: str) -> int:
        """
        Compares the two specified `char` values. The sign of the value returned is the same as
        that of `((Character) a).compareTo(b)`.
        
        **Note for Java 7 and later:** this method should be treated as deprecated; use the
        equivalent Character.compare method instead.

        Arguments
        - a: the first `char` to compare
        - b: the second `char` to compare

        Returns
        - a negative value if `a` is less than `b`; a positive value if `a` is
            greater than `b`; or zero if they are equal
        """
        ...


    @staticmethod
    def contains(array: list[str], target: str) -> bool:
        """
        Returns `True` if `target` is present as an element anywhere in `array`.

        Arguments
        - array: an array of `char` values, possibly empty
        - target: a primitive `char` value

        Returns
        - `True` if `array[i] == target` for some value of `i`
        """
        ...


    @staticmethod
    def indexOf(array: list[str], target: str) -> int:
        """
        Returns the index of the first appearance of the value `target` in `array`.

        Arguments
        - array: an array of `char` values, possibly empty
        - target: a primitive `char` value

        Returns
        - the least index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def indexOf(array: list[str], target: list[str]) -> int:
        """
        Returns the start position of the first occurrence of the specified `target` within
        `array`, or `-1` if there is no such occurrence.
        
        More formally, returns the lowest index `i` such that `Arrays.copyOfRange(array,
        i, i + target.length)` contains exactly the same elements as `target`.

        Arguments
        - array: the array to search for the sequence `target`
        - target: the array to search for as a sub-sequence of `array`
        """
        ...


    @staticmethod
    def lastIndexOf(array: list[str], target: str) -> int:
        """
        Returns the index of the last appearance of the value `target` in `array`.

        Arguments
        - array: an array of `char` values, possibly empty
        - target: a primitive `char` value

        Returns
        - the greatest index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def min(*array: Tuple[str, ...]) -> str:
        """
        Returns the least value present in `array`.

        Arguments
        - array: a *nonempty* array of `char` values

        Returns
        - the value present in `array` that is less than or equal to every other value in
            the array

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def max(*array: Tuple[str, ...]) -> str:
        """
        Returns the greatest value present in `array`.

        Arguments
        - array: a *nonempty* array of `char` values

        Returns
        - the value present in `array` that is greater than or equal to every other value
            in the array

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def constrainToRange(value: str, min: str, max: str) -> str:
        """
        Returns the value nearest to `value` which is within the closed range `[min..max]`.
        
        If `value` is within the range `[min..max]`, `value` is returned
        unchanged. If `value` is less than `min`, `min` is returned, and if `value` is greater than `max`, `max` is returned.

        Arguments
        - value: the `char` value to constrain
        - min: the lower bound (inclusive) of the range to constrain `value` to
        - max: the upper bound (inclusive) of the range to constrain `value` to

        Raises
        - IllegalArgumentException: if `min > max`

        Since
        - 21.0
        """
        ...


    @staticmethod
    def concat(*arrays: Tuple[list[str], ...]) -> list[str]:
        """
        Returns the values from each provided array combined into a single array. For example, `concat(new char[] {a, b`, new char[] {}, new char[] {c}} returns the array `{a, b, c`}.

        Arguments
        - arrays: zero or more `char` arrays

        Returns
        - a single array containing all the values from the source arrays, in order
        """
        ...


    @staticmethod
    def toByteArray(value: str) -> list[int]:
        """
        Returns a big-endian representation of `value` in a 2-element byte array; equivalent to
        `ByteBuffer.allocate(2).putChar(value).array()`. For example, the input value `'\\u5432'` would yield the byte array `{0x54, 0x32`}.
        
        If you need to convert and concatenate several values (possibly even of different types),
        use a shared java.nio.ByteBuffer instance, or use com.google.common.io.ByteStreams.newDataOutput() to get a growable buffer.
        """
        ...


    @staticmethod
    def fromByteArray(bytes: list[int]) -> str:
        """
        Returns the `char` value whose big-endian representation is stored in the first 2 bytes
        of `bytes`; equivalent to `ByteBuffer.wrap(bytes).getChar()`. For example, the
        input byte array `{0x54, 0x32`} would yield the `char` value `'\\u5432'`.
        
        Arguably, it's preferable to use java.nio.ByteBuffer; that library exposes much more
        flexibility at little cost in readability.

        Raises
        - IllegalArgumentException: if `bytes` has fewer than 2 elements
        """
        ...


    @staticmethod
    def fromBytes(b1: int, b2: int) -> str:
        """
        Returns the `char` value whose byte representation is the given 2 bytes, in big-endian
        order; equivalent to `Chars.fromByteArray(new byte[] {b1, b2`)}.

        Since
        - 7.0
        """
        ...


    @staticmethod
    def ensureCapacity(array: list[str], minLength: int, padding: int) -> list[str]:
        """
        Returns an array containing the same values as `array`, but guaranteed to be of a
        specified minimum length. If `array` already has a length of at least `minLength`,
        it is returned directly. Otherwise, a new array of size `minLength + padding` is
        returned, containing the values of `array`, and zeroes in the remaining places.

        Arguments
        - array: the source array
        - minLength: the minimum length the returned array must guarantee
        - padding: an extra amount to "grow" the array by if growth is necessary

        Returns
        - an array containing the values of `array`, with guaranteed minimum length `minLength`

        Raises
        - IllegalArgumentException: if `minLength` or `padding` is negative
        """
        ...


    @staticmethod
    def join(separator: str, *array: Tuple[str, ...]) -> str:
        """
        Returns a string containing the supplied `char` values separated by `separator`.
        For example, `join("-", '1', '2', '3')` returns the string `"1-2-3"`.

        Arguments
        - separator: the text that should appear between consecutive values in the resulting string
            (but not at the start or end)
        - array: an array of `char` values, possibly empty
        """
        ...


    @staticmethod
    def lexicographicalComparator() -> "Comparator"[list[str]]:
        """
        Returns a comparator that compares two `char` arrays <a
        href="http://en.wikipedia.org/wiki/Lexicographical_order">lexicographically</a>; not advisable
        for sorting user-visible strings as the ordering may not match the conventions of the user's
        locale. That is, it compares, using .compare(char, char)), the first pair of values
        that follow any common prefix, or when one array is a prefix of the other, treats the shorter
        array as the lesser. For example, `[] < ['a'] < ['a', 'b'] < ['b']`.
        
        The returned comparator is inconsistent with Object.equals(Object) (since arrays
        support only identity equality), but it is consistent with Arrays.equals(char[],
        char[]).

        Since
        - 2.0
        """
        ...


    @staticmethod
    def toArray(collection: Iterable["Character"]) -> list[str]:
        """
        Copies a collection of `Character` instances into a new array of primitive `char`
        values.
        
        Elements are copied from the argument collection as if by `collection.toArray()`.
        Calling this method is as thread-safe as calling that method.

        Arguments
        - collection: a collection of `Character` objects

        Returns
        - an array containing the same values as `collection`, in the same order, converted
            to primitives

        Raises
        - NullPointerException: if `collection` or any of its elements is null
        """
        ...


    @staticmethod
    def sortDescending(array: list[str]) -> None:
        """
        Sorts the elements of `array` in descending order.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def sortDescending(array: list[str], fromIndex: int, toIndex: int) -> None:
        """
        Sorts the elements of `array` between `fromIndex` inclusive and `toIndex`
        exclusive in descending order.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def reverse(array: list[str]) -> None:
        """
        Reverses the elements of `array`. This is equivalent to `Collections.reverse(Chars.asList(array))`, but is likely to be more efficient.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def reverse(array: list[str], fromIndex: int, toIndex: int) -> None:
        """
        Reverses the elements of `array` between `fromIndex` inclusive and `toIndex`
        exclusive. This is equivalent to `Collections.reverse(Chars.asList(array).subList(fromIndex, toIndex))`, but is likely to be more
        efficient.

        Raises
        - IndexOutOfBoundsException: if `fromIndex < 0`, `toIndex > array.length`, or
            `toIndex > fromIndex`

        Since
        - 23.1
        """
        ...


    @staticmethod
    def asList(*backingArray: Tuple[str, ...]) -> list["Character"]:
        """
        Returns a fixed-size list backed by the specified array, similar to Arrays.asList(Object[]). The list supports List.set(int, Object), but any attempt to
        set a value to `null` will result in a NullPointerException.
        
        The returned list maintains the values, but not the identities, of `Character` objects
        written to or read from it. For example, whether `list.get(0) == list.get(0)` is True for
        the returned list is unspecified.

        Arguments
        - backingArray: the array to back the list

        Returns
        - a list view of the array
        """
        ...
