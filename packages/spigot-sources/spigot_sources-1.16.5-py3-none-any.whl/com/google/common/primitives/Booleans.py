"""
Python module generated from Java source file com.google.common.primitives.Booleans

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.primitives import *
from java.io import Serializable
from java.util import AbstractList
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import RandomAccess
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Booleans:
    """
    Static utility methods pertaining to `boolean` primitives, that are not already found in
    either Boolean or Arrays.
    
    See the Guava User Guide article on
    <a href="https://github.com/google/guava/wiki/PrimitivesExplained">primitive utilities</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    @staticmethod
    def trueFirst() -> "Comparator"["Boolean"]:
        """
        Returns a `Comparator<Boolean>` that sorts `True` before `False`.
        
        This is particularly useful in Java 8+ in combination with `Comparators.comparing`,
        e.g. `Comparators.comparing(Foo::hasBar, TrueFirst())`.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def falseFirst() -> "Comparator"["Boolean"]:
        """
        Returns a `Comparator<Boolean>` that sorts `False` before `True`.
        
        This is particularly useful in Java 8+ in combination with `Comparators.comparing`,
        e.g. `Comparators.comparing(Foo::hasBar, FalseFirst())`.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def hashCode(value: bool) -> int:
        """
        Returns a hash code for `value`; equal to the result of invoking
        `((Boolean) value).hashCode()`.
        
        **Java 8 users:** use Boolean.hashCode(boolean) instead.

        Arguments
        - value: a primitive `boolean` value

        Returns
        - a hash code for the value
        """
        ...


    @staticmethod
    def compare(a: bool, b: bool) -> int:
        """
        Compares the two specified `boolean` values in the standard way (`False` is
        considered less than `True`). The sign of the value returned is the same as that of
        `((Boolean) a).compareTo(b)`.
        
        **Note for Java 7 and later:** this method should be treated as deprecated; use the
        equivalent Boolean.compare method instead.

        Arguments
        - a: the first `boolean` to compare
        - b: the second `boolean` to compare

        Returns
        - a positive number if only `a` is `True`, a negative number if only
            `b` is True, or zero if `a == b`
        """
        ...


    @staticmethod
    def contains(array: list[bool], target: bool) -> bool:
        """
        Returns `True` if `target` is present as an element anywhere in `array`.
        
        **Note:** consider representing the array as a java.util.BitSet instead,
        replacing `Booleans.contains(array, True)` with `!bitSet.isEmpty()` and
        `Booleans.contains(array, False)` with `bitSet.nextClearBit(0) == sizeOfBitSet`.

        Arguments
        - array: an array of `boolean` values, possibly empty
        - target: a primitive `boolean` value

        Returns
        - `True` if `array[i] == target` for some value of `i`
        """
        ...


    @staticmethod
    def indexOf(array: list[bool], target: bool) -> int:
        """
        Returns the index of the first appearance of the value `target` in `array`.
        
        **Note:** consider representing the array as a java.util.BitSet instead, and
        using java.util.BitSet.nextSetBit(int) or java.util.BitSet.nextClearBit(int).

        Arguments
        - array: an array of `boolean` values, possibly empty
        - target: a primitive `boolean` value

        Returns
        - the least index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def indexOf(array: list[bool], target: list[bool]) -> int:
        """
        Returns the start position of the first occurrence of the specified `target` within `array`, or `-1` if there is no such occurrence.
        
        More formally, returns the lowest index `i` such that `Arrays.copyOfRange(array, i, i + target.length)` contains exactly the same elements as
        `target`.

        Arguments
        - array: the array to search for the sequence `target`
        - target: the array to search for as a sub-sequence of `array`
        """
        ...


    @staticmethod
    def lastIndexOf(array: list[bool], target: bool) -> int:
        """
        Returns the index of the last appearance of the value `target` in `array`.

        Arguments
        - array: an array of `boolean` values, possibly empty
        - target: a primitive `boolean` value

        Returns
        - the greatest index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def concat(*arrays: Tuple[list[bool], ...]) -> list[bool]:
        """
        Returns the values from each provided array combined into a single array. For example,
        `concat(new boolean[] {a, b`, new boolean[] {}, new boolean[] {c}} returns the array
        `{a, b, c`}.

        Arguments
        - arrays: zero or more `boolean` arrays

        Returns
        - a single array containing all the values from the source arrays, in order
        """
        ...


    @staticmethod
    def ensureCapacity(array: list[bool], minLength: int, padding: int) -> list[bool]:
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
        - an array containing the values of `array`, with guaranteed minimum length
            `minLength`

        Raises
        - IllegalArgumentException: if `minLength` or `padding` is negative
        """
        ...


    @staticmethod
    def join(separator: str, *array: Tuple[bool, ...]) -> str:
        """
        Returns a string containing the supplied `boolean` values separated by `separator`.
        For example, `join("-", False, True, False)` returns the string
        `"False-True-False"`.

        Arguments
        - separator: the text that should appear between consecutive values in the resulting string
            (but not at the start or end)
        - array: an array of `boolean` values, possibly empty
        """
        ...


    @staticmethod
    def lexicographicalComparator() -> "Comparator"[list[bool]]:
        """
        Returns a comparator that compares two `boolean` arrays <a
        href="http://en.wikipedia.org/wiki/Lexicographical_order">lexicographically</a>. That is, it
        compares, using .compare(boolean, boolean)), the first pair of values that follow any
        common prefix, or when one array is a prefix of the other, treats the shorter array as the
        lesser. For example, `[] < [False] < [False, True] < [True]`.
        
        The returned comparator is inconsistent with Object.equals(Object) (since arrays
        support only identity equality), but it is consistent with
        Arrays.equals(boolean[], boolean[]).

        Since
        - 2.0
        """
        ...


    @staticmethod
    def toArray(collection: Iterable["Boolean"]) -> list[bool]:
        """
        Copies a collection of `Boolean` instances into a new array of primitive `boolean`
        values.
        
        Elements are copied from the argument collection as if by `collection.toArray()`. Calling this method is as thread-safe as calling that method.
        
        **Note:** consider representing the collection as a java.util.BitSet instead.

        Arguments
        - collection: a collection of `Boolean` objects

        Returns
        - an array containing the same values as `collection`, in the same order, converted
            to primitives

        Raises
        - NullPointerException: if `collection` or any of its elements is null
        """
        ...


    @staticmethod
    def asList(*backingArray: Tuple[bool, ...]) -> list["Boolean"]:
        """
        Returns a fixed-size list backed by the specified array, similar to
        Arrays.asList(Object[]). The list supports List.set(int, Object), but any
        attempt to set a value to `null` will result in a NullPointerException.
        
        The returned list maintains the values, but not the identities, of `Boolean` objects
        written to or read from it. For example, whether `list.get(0) == list.get(0)` is True for
        the returned list is unspecified.

        Arguments
        - backingArray: the array to back the list

        Returns
        - a list view of the array
        """
        ...


    @staticmethod
    def countTrue(*values: Tuple[bool, ...]) -> int:
        """
        Returns the number of `values` that are `True`.

        Since
        - 16.0
        """
        ...
