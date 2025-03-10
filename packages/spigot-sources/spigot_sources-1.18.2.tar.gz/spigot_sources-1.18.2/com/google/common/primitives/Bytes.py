"""
Python module generated from Java source file com.google.common.primitives.Bytes

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.primitives import *
from java.io import Serializable
from java.util import AbstractList
from java.util import Arrays
from java.util import Collections
from java.util import RandomAccess
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Bytes:

    @staticmethod
    def hashCode(value: int) -> int:
        """
        Returns a hash code for `value`; equal to the result of invoking `((Byte)
        value).hashCode()`.
        
        **Java 8 users:** use Byte.hashCode(byte) instead.

        Arguments
        - value: a primitive `byte` value

        Returns
        - a hash code for the value
        """
        ...


    @staticmethod
    def contains(array: list[int], target: int) -> bool:
        """
        Returns `True` if `target` is present as an element anywhere in `array`.

        Arguments
        - array: an array of `byte` values, possibly empty
        - target: a primitive `byte` value

        Returns
        - `True` if `array[i] == target` for some value of `i`
        """
        ...


    @staticmethod
    def indexOf(array: list[int], target: int) -> int:
        """
        Returns the index of the first appearance of the value `target` in `array`.

        Arguments
        - array: an array of `byte` values, possibly empty
        - target: a primitive `byte` value

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
        - array: an array of `byte` values, possibly empty
        - target: a primitive `byte` value

        Returns
        - the greatest index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def concat(*arrays: Tuple[list[int], ...]) -> list[int]:
        """
        Returns the values from each provided array combined into a single array. For example, `concat(new byte[] {a, b`, new byte[] {}, new byte[] {c}} returns the array `{a, b, c`}.

        Arguments
        - arrays: zero or more `byte` arrays

        Returns
        - a single array containing all the values from the source arrays, in order
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
    def toArray(collection: Iterable["Number"]) -> list[int]:
        """
        Returns an array containing each value of `collection`, converted to a `byte` value
        in the manner of Number.byteValue.
        
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
        - 1.0 (parameter was `Collection<Byte>` before 12.0)
        """
        ...


    @staticmethod
    def asList(*backingArray: Tuple[int, ...]) -> list["Byte"]:
        """
        Returns a fixed-size list backed by the specified array, similar to Arrays.asList(Object[]). The list supports List.set(int, Object), but any attempt to
        set a value to `null` will result in a NullPointerException.
        
        The returned list maintains the values, but not the identities, of `Byte` objects
        written to or read from it. For example, whether `list.get(0) == list.get(0)` is True for
        the returned list is unspecified.

        Arguments
        - backingArray: the array to back the list

        Returns
        - a list view of the array
        """
        ...


    @staticmethod
    def reverse(array: list[int]) -> None:
        """
        Reverses the elements of `array`. This is equivalent to `Collections.reverse(Bytes.asList(array))`, but is likely to be more efficient.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def reverse(array: list[int], fromIndex: int, toIndex: int) -> None:
        """
        Reverses the elements of `array` between `fromIndex` inclusive and `toIndex`
        exclusive. This is equivalent to `Collections.reverse(Bytes.asList(array).subList(fromIndex, toIndex))`, but is likely to be more
        efficient.

        Raises
        - IndexOutOfBoundsException: if `fromIndex < 0`, `toIndex > array.length`, or
            `toIndex > fromIndex`

        Since
        - 23.1
        """
        ...
