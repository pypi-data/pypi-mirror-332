"""
Python module generated from Java source file com.google.common.primitives.Floats

Java source file obtained from artifact guava version 21.0

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
from javax.annotation import CheckForNull
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Floats:
    """
    Static utility methods pertaining to `float` primitives, that are not already found in
    either Float or Arrays.
    
    See the Guava User Guide article on
    <a href="https://github.com/google/guava/wiki/PrimitivesExplained">primitive utilities</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    BYTES = Float.SIZE / Byte.SIZE
    """
    The number of bytes required to represent a primitive `float` value.
    
    **Java 8 users:** use Float.BYTES instead.

    Since
    - 10.0
    """


    @staticmethod
    def hashCode(value: float) -> int:
        """
        Returns a hash code for `value`; equal to the result of invoking
        `((Float) value).hashCode()`.
        
        **Java 8 users:** use Float.hashCode(float) instead.

        Arguments
        - value: a primitive `float` value

        Returns
        - a hash code for the value
        """
        ...


    @staticmethod
    def compare(a: float, b: float) -> int:
        """
        Compares the two specified `float` values using Float.compare(float, float). You
        may prefer to invoke that method directly; this method exists only for consistency with the
        other utilities in this package.
        
        **Note:** this method simply delegates to the JDK method Float.compare. It is
        provided for consistency with the other primitive types, whose compare methods were not added
        to the JDK until JDK 7.

        Arguments
        - a: the first `float` to compare
        - b: the second `float` to compare

        Returns
        - the result of invoking Float.compare(float, float)
        """
        ...


    @staticmethod
    def isFinite(value: float) -> bool:
        """
        Returns `True` if `value` represents a real number. This is equivalent to, but not
        necessarily implemented as, `!(Float.isInfinite(value) || Float.isNaN(value))`.
        
        **Java 8 users:** use Float.isFinite(float) instead.

        Since
        - 10.0
        """
        ...


    @staticmethod
    def contains(array: list[float], target: float) -> bool:
        """
        Returns `True` if `target` is present as an element anywhere in `array`. Note
        that this always returns `False` when `target` is `NaN`.

        Arguments
        - array: an array of `float` values, possibly empty
        - target: a primitive `float` value

        Returns
        - `True` if `array[i] == target` for some value of `i`
        """
        ...


    @staticmethod
    def indexOf(array: list[float], target: float) -> int:
        """
        Returns the index of the first appearance of the value `target` in `array`. Note
        that this always returns `-1` when `target` is `NaN`.

        Arguments
        - array: an array of `float` values, possibly empty
        - target: a primitive `float` value

        Returns
        - the least index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def indexOf(array: list[float], target: list[float]) -> int:
        """
        Returns the start position of the first occurrence of the specified `target` within `array`, or `-1` if there is no such occurrence.
        
        More formally, returns the lowest index `i` such that
        `Arrays.copyOfRange(array, i, i + target.length)` contains exactly the same elements as
        `target`.
        
        Note that this always returns `-1` when `target` contains `NaN`.

        Arguments
        - array: the array to search for the sequence `target`
        - target: the array to search for as a sub-sequence of `array`
        """
        ...


    @staticmethod
    def lastIndexOf(array: list[float], target: float) -> int:
        """
        Returns the index of the last appearance of the value `target` in `array`. Note
        that this always returns `-1` when `target` is `NaN`.

        Arguments
        - array: an array of `float` values, possibly empty
        - target: a primitive `float` value

        Returns
        - the greatest index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def min(*array: Tuple[float, ...]) -> float:
        """
        Returns the least value present in `array`, using the same rules of comparison as
        Math.min(float, float).

        Arguments
        - array: a *nonempty* array of `float` values

        Returns
        - the value present in `array` that is less than or equal to every other value in
            the array

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def max(*array: Tuple[float, ...]) -> float:
        """
        Returns the greatest value present in `array`, using the same rules of comparison as
        Math.max(float, float).

        Arguments
        - array: a *nonempty* array of `float` values

        Returns
        - the value present in `array` that is greater than or equal to every other value
            in the array

        Raises
        - IllegalArgumentException: if `array` is empty
        """
        ...


    @staticmethod
    def constrainToRange(value: float, min: float, max: float) -> float:
        """
        Returns the value nearest to `value` which is within the closed range `[min..max]`.
        
        If `value` is within the range `[min..max]`, `value` is returned
        unchanged. If `value` is less than `min`, `min` is returned, and if
        `value` is greater than `max`, `max` is returned.

        Arguments
        - value: the `float` value to constrain
        - min: the lower bound (inclusive) of the range to constrain `value` to
        - max: the upper bound (inclusive) of the range to constrain `value` to

        Raises
        - IllegalArgumentException: if `min > max`

        Since
        - 21.0
        """
        ...


    @staticmethod
    def concat(*arrays: Tuple[list[float], ...]) -> list[float]:
        """
        Returns the values from each provided array combined into a single array. For example,
        `concat(new float[] {a, b`, new float[] {}, new float[] {c}} returns the array `{a,
        b, c`}.

        Arguments
        - arrays: zero or more `float` arrays

        Returns
        - a single array containing all the values from the source arrays, in order
        """
        ...


    @staticmethod
    def stringConverter() -> "Converter"[str, "Float"]:
        """
        Returns a serializable converter object that converts between strings and floats using
        Float.valueOf and Float.toString().

        Since
        - 16.0
        """
        ...


    @staticmethod
    def ensureCapacity(array: list[float], minLength: int, padding: int) -> list[float]:
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
    def join(separator: str, *array: Tuple[float, ...]) -> str:
        """
        Returns a string containing the supplied `float` values, converted to strings as
        specified by Float.toString(float), and separated by `separator`. For example,
        `join("-", 1.0f, 2.0f, 3.0f)` returns the string `"1.0-2.0-3.0"`.
        
        Note that Float.toString(float) formats `float` differently in GWT. In the
        previous example, it returns the string `"1-2-3"`.

        Arguments
        - separator: the text that should appear between consecutive values in the resulting string
            (but not at the start or end)
        - array: an array of `float` values, possibly empty
        """
        ...


    @staticmethod
    def lexicographicalComparator() -> "Comparator"[list[float]]:
        """
        Returns a comparator that compares two `float` arrays <a
        href="http://en.wikipedia.org/wiki/Lexicographical_order">lexicographically</a>. That is, it
        compares, using .compare(float, float)), the first pair of values that follow any
        common prefix, or when one array is a prefix of the other, treats the shorter array as the
        lesser. For example, `[] < [1.0f] < [1.0f, 2.0f] < [2.0f]`.
        
        The returned comparator is inconsistent with Object.equals(Object) (since arrays
        support only identity equality), but it is consistent with
        Arrays.equals(float[], float[]).

        Since
        - 2.0
        """
        ...


    @staticmethod
    def toArray(collection: Iterable["Number"]) -> list[float]:
        """
        Returns an array containing each value of `collection`, converted to a `float`
        value in the manner of Number.floatValue.
        
        Elements are copied from the argument collection as if by `collection.toArray()`. Calling this method is as thread-safe as calling that method.

        Arguments
        - collection: a collection of `Number` instances

        Returns
        - an array containing the same values as `collection`, in the same order, converted
            to primitives

        Raises
        - NullPointerException: if `collection` or any of its elements is null

        Since
        - 1.0 (parameter was `Collection<Float>` before 12.0)
        """
        ...


    @staticmethod
    def asList(*backingArray: Tuple[float, ...]) -> list["Float"]:
        """
        Returns a fixed-size list backed by the specified array, similar to
        Arrays.asList(Object[]). The list supports List.set(int, Object), but any
        attempt to set a value to `null` will result in a NullPointerException.
        
        The returned list maintains the values, but not the identities, of `Float` objects
        written to or read from it. For example, whether `list.get(0) == list.get(0)` is True for
        the returned list is unspecified.
        
        The returned list may have unexpected behavior if it contains `NaN`, or if `NaN` is used as a parameter to any of its methods.

        Arguments
        - backingArray: the array to back the list

        Returns
        - a list view of the array
        """
        ...


    @staticmethod
    def tryParse(string: str) -> "Float":
        """
        Parses the specified string as a single-precision floating point value. The ASCII character
        `'-'` (`'&#92;u002D'`) is recognized as the minus sign.
        
        Unlike Float.parseFloat(String), this method returns `null` instead of
        throwing an exception if parsing fails. Valid inputs are exactly those accepted by
        Float.valueOf(String), except that leading and trailing whitespace is not permitted.
        
        This implementation is likely to be faster than `Float.parseFloat` if many failures are expected.

        Arguments
        - string: the string representation of a `float` value

        Returns
        - the floating point value represented by `string`, or `null` if
            `string` has a length of zero or cannot be parsed as a `float` value

        Since
        - 14.0
        """
        ...
