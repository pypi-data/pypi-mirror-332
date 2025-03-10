"""
Python module generated from Java source file com.google.common.primitives.Doubles

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


class Doubles(DoublesMethodsForWeb):
    """
    Static utility methods pertaining to `double` primitives, that are not already found in
    either Double or Arrays.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/PrimitivesExplained">primitive utilities</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    BYTES = Double.SIZE / Byte.SIZE
    """
    The number of bytes required to represent a primitive `double` value.
    
    **Java 8 users:** use Double.BYTES instead.

    Since
    - 10.0
    """


    @staticmethod
    def hashCode(value: float) -> int:
        """
        Returns a hash code for `value`; equal to the result of invoking `((Double)
        value).hashCode()`.
        
        **Java 8 users:** use Double.hashCode(double) instead.

        Arguments
        - value: a primitive `double` value

        Returns
        - a hash code for the value
        """
        ...


    @staticmethod
    def compare(a: float, b: float) -> int:
        """
        Compares the two specified `double` values. The sign of the value returned is the same as
        that of `((Double) a).Double.compareTo compareTo(b)`. As with that
        method, `NaN` is treated as greater than all other values, and `0.0 > -0.0`.
        
        **Note:** this method simply delegates to the JDK method Double.compare. It is
        provided for consistency with the other primitive types, whose compare methods were not added
        to the JDK until JDK 7.

        Arguments
        - a: the first `double` to compare
        - b: the second `double` to compare

        Returns
        - a negative value if `a` is less than `b`; a positive value if `a` is
            greater than `b`; or zero if they are equal
        """
        ...


    @staticmethod
    def isFinite(value: float) -> bool:
        """
        Returns `True` if `value` represents a real number. This is equivalent to, but not
        necessarily implemented as, `!(Double.isInfinite(value) || Double.isNaN(value))`.
        
        **Java 8 users:** use Double.isFinite(double) instead.

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
        - array: an array of `double` values, possibly empty
        - target: a primitive `double` value

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
        - array: an array of `double` values, possibly empty
        - target: a primitive `double` value

        Returns
        - the least index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def indexOf(array: list[float], target: list[float]) -> int:
        """
        Returns the start position of the first occurrence of the specified `target` within
        `array`, or `-1` if there is no such occurrence.
        
        More formally, returns the lowest index `i` such that `Arrays.copyOfRange(array,
        i, i + target.length)` contains exactly the same elements as `target`.
        
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
        - array: an array of `double` values, possibly empty
        - target: a primitive `double` value

        Returns
        - the greatest index `i` for which `array[i] == target`, or `-1` if no
            such index exists.
        """
        ...


    @staticmethod
    def min(*array: Tuple[float, ...]) -> float:
        """
        Returns the least value present in `array`, using the same rules of comparison as Math.min(double, double).

        Arguments
        - array: a *nonempty* array of `double` values

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
        Math.max(double, double).

        Arguments
        - array: a *nonempty* array of `double` values

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
        unchanged. If `value` is less than `min`, `min` is returned, and if `value` is greater than `max`, `max` is returned.

        Arguments
        - value: the `double` value to constrain
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
        Returns the values from each provided array combined into a single array. For example, `concat(new double[] {a, b`, new double[] {}, new double[] {c}} returns the array `{a, b,
        c`}.

        Arguments
        - arrays: zero or more `double` arrays

        Returns
        - a single array containing all the values from the source arrays, in order
        """
        ...


    @staticmethod
    def stringConverter() -> "Converter"[str, "Double"]:
        """
        Returns a serializable converter object that converts between strings and doubles using Double.valueOf and Double.toString().

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
        - an array containing the values of `array`, with guaranteed minimum length `minLength`

        Raises
        - IllegalArgumentException: if `minLength` or `padding` is negative
        """
        ...


    @staticmethod
    def join(separator: str, *array: Tuple[float, ...]) -> str:
        """
        Returns a string containing the supplied `double` values, converted to strings as
        specified by Double.toString(double), and separated by `separator`. For example,
        `join("-", 1.0, 2.0, 3.0)` returns the string `"1.0-2.0-3.0"`.
        
        Note that Double.toString(double) formats `double` differently in GWT
        sometimes. In the previous example, it returns the string `"1-2-3"`.

        Arguments
        - separator: the text that should appear between consecutive values in the resulting string
            (but not at the start or end)
        - array: an array of `double` values, possibly empty
        """
        ...


    @staticmethod
    def lexicographicalComparator() -> "Comparator"[list[float]]:
        """
        Returns a comparator that compares two `double` arrays <a
        href="http://en.wikipedia.org/wiki/Lexicographical_order">lexicographically</a>. That is, it
        compares, using .compare(double, double)), the first pair of values that follow any
        common prefix, or when one array is a prefix of the other, treats the shorter array as the
        lesser. For example, `[] < [1.0] < [1.0, 2.0] < [2.0]`.
        
        The returned comparator is inconsistent with Object.equals(Object) (since arrays
        support only identity equality), but it is consistent with Arrays.equals(double[],
        double[]).

        Since
        - 2.0
        """
        ...


    @staticmethod
    def sortDescending(array: list[float]) -> None:
        """
        Sorts the elements of `array` in descending order.
        
        Note that this method uses the total order imposed by Double.compare, which treats
        all NaN values as equal and 0.0 as greater than -0.0.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def sortDescending(array: list[float], fromIndex: int, toIndex: int) -> None:
        """
        Sorts the elements of `array` between `fromIndex` inclusive and `toIndex`
        exclusive in descending order.
        
        Note that this method uses the total order imposed by Double.compare, which treats
        all NaN values as equal and 0.0 as greater than -0.0.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def reverse(array: list[float]) -> None:
        """
        Reverses the elements of `array`. This is equivalent to `Collections.reverse(Doubles.asList(array))`, but is likely to be more efficient.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def reverse(array: list[float], fromIndex: int, toIndex: int) -> None:
        """
        Reverses the elements of `array` between `fromIndex` inclusive and `toIndex`
        exclusive. This is equivalent to `Collections.reverse(Doubles.asList(array).subList(fromIndex, toIndex))`, but is likely to be
        more efficient.

        Raises
        - IndexOutOfBoundsException: if `fromIndex < 0`, `toIndex > array.length`, or
            `toIndex > fromIndex`

        Since
        - 23.1
        """
        ...


    @staticmethod
    def toArray(collection: Iterable["Number"]) -> list[float]:
        """
        Returns an array containing each value of `collection`, converted to a `double`
        value in the manner of Number.doubleValue.
        
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
        - 1.0 (parameter was `Collection<Double>` before 12.0)
        """
        ...


    @staticmethod
    def asList(*backingArray: Tuple[float, ...]) -> list["Double"]:
        """
        Returns a fixed-size list backed by the specified array, similar to Arrays.asList(Object[]). The list supports List.set(int, Object), but any attempt to
        set a value to `null` will result in a NullPointerException.
        
        The returned list maintains the values, but not the identities, of `Double` objects
        written to or read from it. For example, whether `list.get(0) == list.get(0)` is True for
        the returned list is unspecified.
        
        The returned list may have unexpected behavior if it contains `NaN`, or if `NaN`
        is used as a parameter to any of its methods.
        
        **Note:** when possible, you should represent your data as an ImmutableDoubleArray instead, which has an ImmutableDoubleArray.asList asList view.

        Arguments
        - backingArray: the array to back the list

        Returns
        - a list view of the array
        """
        ...


    @staticmethod
    def tryParse(string: str) -> "Double":
        """
        Parses the specified string as a double-precision floating point value. The ASCII character
        `'-'` (`'&#92;u002D'`) is recognized as the minus sign.
        
        Unlike Double.parseDouble(String), this method returns `null` instead of
        throwing an exception if parsing fails. Valid inputs are exactly those accepted by Double.valueOf(String), except that leading and trailing whitespace is not permitted.
        
        This implementation is likely to be faster than `Double.parseDouble` if many failures
        are expected.

        Arguments
        - string: the string representation of a `double` value

        Returns
        - the floating point value represented by `string`, or `null` if `string` has a length of zero or cannot be parsed as a `double` value

        Raises
        - NullPointerException: if `string` is `null`

        Since
        - 14.0
        """
        ...
