"""
Python module generated from Java source file com.google.common.primitives.Ints

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Converter
from com.google.common.primitives import *
from java.io import Serializable
from java.util import AbstractList
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import RandomAccess
from java.util import Spliterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Ints(IntsMethodsForWeb):
    """
    Static utility methods pertaining to `int` primitives, that are not already found in either
    Integer or Arrays.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/PrimitivesExplained">primitive utilities</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    BYTES = Integer.SIZE / Byte.SIZE
    """
    The number of bytes required to represent a primitive `int` value.
    
    **Java 8 users:** use Integer.BYTES instead.
    """
    MAX_POWER_OF_TWO = 1 << (Integer.SIZE - 2)
    """
    The largest power of two that can be represented as an `int`.

    Since
    - 10.0
    """


    @staticmethod
    def hashCode(value: int) -> int:
        """
        Returns a hash code for `value`; equal to the result of invoking `((Integer)
        value).hashCode()`.
        
        **Java 8 users:** use Integer.hashCode(int) instead.

        Arguments
        - value: a primitive `int` value

        Returns
        - a hash code for the value
        """
        ...


    @staticmethod
    def checkedCast(value: int) -> int:
        """
        Returns the `int` value that is equal to `value`, if possible.

        Arguments
        - value: any value in the range of the `int` type

        Returns
        - the `int` value that equals `value`

        Raises
        - IllegalArgumentException: if `value` is greater than Integer.MAX_VALUE or
            less than Integer.MIN_VALUE
        """
        ...


    @staticmethod
    def saturatedCast(value: int) -> int:
        """
        Returns the `int` nearest in value to `value`.

        Arguments
        - value: any `long` value

        Returns
        - the same value cast to `int` if it is in the range of the `int` type,
            Integer.MAX_VALUE if it is too large, or Integer.MIN_VALUE if it is too
            small
        """
        ...


    @staticmethod
    def compare(a: int, b: int) -> int:
        """
        Compares the two specified `int` values. The sign of the value returned is the same as
        that of `((Integer) a).compareTo(b)`.
        
        **Note for Java 7 and later:** this method should be treated as deprecated; use the
        equivalent Integer.compare method instead.

        Arguments
        - a: the first `int` to compare
        - b: the second `int` to compare

        Returns
        - a negative value if `a` is less than `b`; a positive value if `a` is
            greater than `b`; or zero if they are equal
        """
        ...


    @staticmethod
    def contains(array: list[int], target: int) -> bool:
        """
        Returns `True` if `target` is present as an element anywhere in `array`.

        Arguments
        - array: an array of `int` values, possibly empty
        - target: a primitive `int` value

        Returns
        - `True` if `array[i] == target` for some value of `i`
        """
        ...


    @staticmethod
    def indexOf(array: list[int], target: int) -> int:
        """
        Returns the index of the first appearance of the value `target` in `array`.

        Arguments
        - array: an array of `int` values, possibly empty
        - target: a primitive `int` value

        Returns
        - the least index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def indexOf(array: list[int], target: list[int]) -> int:
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
    def lastIndexOf(array: list[int], target: int) -> int:
        """
        Returns the index of the last appearance of the value `target` in `array`.

        Arguments
        - array: an array of `int` values, possibly empty
        - target: a primitive `int` value

        Returns
        - the greatest index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def min(*array: Tuple[int, ...]) -> int:
        """
        Returns the least value present in `array`.

        Arguments
        - array: a *nonempty* array of `int` values

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
        - array: a *nonempty* array of `int` values

        Returns
        - the value present in `array` that is greater than or equal to every other value
            in the array

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def constrainToRange(value: int, min: int, max: int) -> int:
        """
        Returns the value nearest to `value` which is within the closed range `[min..max]`.
        
        If `value` is within the range `[min..max]`, `value` is returned
        unchanged. If `value` is less than `min`, `min` is returned, and if `value` is greater than `max`, `max` is returned.

        Arguments
        - value: the `int` value to constrain
        - min: the lower bound (inclusive) of the range to constrain `value` to
        - max: the upper bound (inclusive) of the range to constrain `value` to

        Raises
        - IllegalArgumentException: if `min > max`

        Since
        - 21.0
        """
        ...


    @staticmethod
    def concat(*arrays: Tuple[list[int], ...]) -> list[int]:
        """
        Returns the values from each provided array combined into a single array. For example, `concat(new int[] {a, b`, new int[] {}, new int[] {c}} returns the array `{a, b, c`}.

        Arguments
        - arrays: zero or more `int` arrays

        Returns
        - a single array containing all the values from the source arrays, in order
        """
        ...


    @staticmethod
    def toByteArray(value: int) -> list[int]:
        """
        Returns a big-endian representation of `value` in a 4-element byte array; equivalent to
        `ByteBuffer.allocate(4).putInt(value).array()`. For example, the input value `0x12131415` would yield the byte array `{0x12, 0x13, 0x14, 0x15`}.
        
        If you need to convert and concatenate several values (possibly even of different types),
        use a shared java.nio.ByteBuffer instance, or use com.google.common.io.ByteStreams.newDataOutput() to get a growable buffer.
        """
        ...


    @staticmethod
    def fromByteArray(bytes: list[int]) -> int:
        """
        Returns the `int` value whose big-endian representation is stored in the first 4 bytes of
        `bytes`; equivalent to `ByteBuffer.wrap(bytes).getInt()`. For example, the input
        byte array `{0x12, 0x13, 0x14, 0x15, 0x33`} would yield the `int` value `0x12131415`.
        
        Arguably, it's preferable to use java.nio.ByteBuffer; that library exposes much more
        flexibility at little cost in readability.

        Raises
        - IllegalArgumentException: if `bytes` has fewer than 4 elements
        """
        ...


    @staticmethod
    def fromBytes(b1: int, b2: int, b3: int, b4: int) -> int:
        """
        Returns the `int` value whose byte representation is the given 4 bytes, in big-endian
        order; equivalent to `Ints.fromByteArray(new byte[] {b1, b2, b3, b4`)}.

        Since
        - 7.0
        """
        ...


    @staticmethod
    def stringConverter() -> "Converter"[str, "Integer"]:
        """
        Returns a serializable converter object that converts between strings and integers using Integer.decode and Integer.toString(). The returned converter throws NumberFormatException if the input string is invalid.
        
        **Warning:** please see Integer.decode to understand exactly how strings are
        parsed. For example, the string `"0123"` is treated as *octal* and converted to the
        value `83`.

        Since
        - 16.0
        """
        ...


    @staticmethod
    def ensureCapacity(array: list[int], minLength: int, padding: int) -> list[int]:
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
    def join(separator: str, *array: Tuple[int, ...]) -> str:
        """
        Returns a string containing the supplied `int` values separated by `separator`. For
        example, `join("-", 1, 2, 3)` returns the string `"1-2-3"`.

        Arguments
        - separator: the text that should appear between consecutive values in the resulting string
            (but not at the start or end)
        - array: an array of `int` values, possibly empty
        """
        ...


    @staticmethod
    def lexicographicalComparator() -> "Comparator"[list[int]]:
        """
        Returns a comparator that compares two `int` arrays <a
        href="http://en.wikipedia.org/wiki/Lexicographical_order">lexicographically</a>. That is, it
        compares, using .compare(int, int)), the first pair of values that follow any common
        prefix, or when one array is a prefix of the other, treats the shorter array as the lesser. For
        example, `[] < [1] < [1, 2] < [2]`.
        
        The returned comparator is inconsistent with Object.equals(Object) (since arrays
        support only identity equality), but it is consistent with Arrays.equals(int[], int[]).

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


    @staticmethod
    def reverse(array: list[int]) -> None:
        """
        Reverses the elements of `array`. This is equivalent to `Collections.reverse(Ints.asList(array))`, but is likely to be more efficient.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def reverse(array: list[int], fromIndex: int, toIndex: int) -> None:
        """
        Reverses the elements of `array` between `fromIndex` inclusive and `toIndex`
        exclusive. This is equivalent to `Collections.reverse(Ints.asList(array).subList(fromIndex, toIndex))`, but is likely to be more
        efficient.

        Raises
        - IndexOutOfBoundsException: if `fromIndex < 0`, `toIndex > array.length`, or
            `toIndex > fromIndex`

        Since
        - 23.1
        """
        ...


    @staticmethod
    def toArray(collection: Iterable["Number"]) -> list[int]:
        """
        Returns an array containing each value of `collection`, converted to a `int` value
        in the manner of Number.intValue.
        
        Elements are copied from the argument collection as if by `collection.toArray()`.
        Calling this method is as thread-safe as calling that method.

        Arguments
        - collection: a collection of `Number` instances

        Returns
        - an array containing the same values as `collection`, in the same order, converted
            to primitives

        Raises
        - NullPointerException: if `collection` or any of its elements is null

        Since
        - 1.0 (parameter was `Collection<Integer>` before 12.0)
        """
        ...


    @staticmethod
    def asList(*backingArray: Tuple[int, ...]) -> list["Integer"]:
        """
        Returns a fixed-size list backed by the specified array, similar to Arrays.asList(Object[]). The list supports List.set(int, Object), but any attempt to
        set a value to `null` will result in a NullPointerException.
        
        The returned list maintains the values, but not the identities, of `Integer` objects
        written to or read from it. For example, whether `list.get(0) == list.get(0)` is True for
        the returned list is unspecified.
        
        **Note:** when possible, you should represent your data as an ImmutableIntArray
        instead, which has an ImmutableIntArray.asList asList view.

        Arguments
        - backingArray: the array to back the list

        Returns
        - a list view of the array
        """
        ...


    @staticmethod
    def tryParse(string: str) -> "Integer":
        """
        Parses the specified string as a signed decimal integer value. The ASCII character `'-'`
        (`'&#92;u002D'`) is recognized as the minus sign.
        
        Unlike Integer.parseInt(String), this method returns `null` instead of
        throwing an exception if parsing fails. Additionally, this method only accepts ASCII digits,
        and returns `null` if non-ASCII digits are present in the string.
        
        Note that strings prefixed with ASCII `'+'` are rejected, even under JDK 7, despite
        the change to Integer.parseInt(String) for that version.

        Arguments
        - string: the string representation of an integer value

        Returns
        - the integer value represented by `string`, or `null` if `string` has
            a length of zero or cannot be parsed as an integer value

        Raises
        - NullPointerException: if `string` is `null`

        Since
        - 11.0
        """
        ...


    @staticmethod
    def tryParse(string: str, radix: int) -> "Integer":
        """
        Parses the specified string as a signed integer value using the specified radix. The ASCII
        character `'-'` (`'&#92;u002D'`) is recognized as the minus sign.
        
        Unlike Integer.parseInt(String, int), this method returns `null` instead of
        throwing an exception if parsing fails. Additionally, this method only accepts ASCII digits,
        and returns `null` if non-ASCII digits are present in the string.
        
        Note that strings prefixed with ASCII `'+'` are rejected, even under JDK 7, despite
        the change to Integer.parseInt(String, int) for that version.

        Arguments
        - string: the string representation of an integer value
        - radix: the radix to use when parsing

        Returns
        - the integer value represented by `string` using `radix`, or `null` if
            `string` has a length of zero or cannot be parsed as an integer value

        Raises
        - IllegalArgumentException: if `radix < Character.MIN_RADIX` or `radix >
            Character.MAX_RADIX`
        - NullPointerException: if `string` is `null`

        Since
        - 19.0
        """
        ...
