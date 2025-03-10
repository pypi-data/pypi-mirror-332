"""
Python module generated from Java source file java.util.Objects

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from java.util.function import Supplier
from jdk.internal.util import Preconditions
from jdk.internal.vm.annotation import ForceInline
from typing import Any, Callable, Iterable, Tuple


class Objects:
    """
    This class consists of `static` utility methods for operating
    on objects, or checking certain conditions before operation.  These utilities
    include `null`-safe or `null`-tolerant methods for computing the
    hash code of an object, returning a string for an object, comparing two
    objects, and checking if indexes or sub-range values are out of bounds.

    Since
    - 1.7
    """

    @staticmethod
    def equals(a: "Object", b: "Object") -> bool:
        """
        Returns `True` if the arguments are equal to each other
        and `False` otherwise.
        Consequently, if both arguments are `null`, `True`
        is returned.  Otherwise, if the first argument is not `null`, equality is determined by calling the Object.equals equals method of the first argument with the
        second argument of this method. Otherwise, `False` is
        returned.

        Arguments
        - a: an object
        - b: an object to be compared with `a` for equality

        Returns
        - `True` if the arguments are equal to each other
        and `False` otherwise

        See
        - Object.equals(Object)
        """
        ...


    @staticmethod
    def deepEquals(a: "Object", b: "Object") -> bool:
        """
        Returns `True` if the arguments are deeply equal to each other
        and `False` otherwise.
        
        Two `null` values are deeply equal.  If both arguments are
        arrays, the algorithm in Arrays.deepEquals(Object[],
        Object[]) Arrays.deepEquals is used to determine equality.
        Otherwise, equality is determined by using the Object.equals equals method of the first argument.

        Arguments
        - a: an object
        - b: an object to be compared with `a` for deep equality

        Returns
        - `True` if the arguments are deeply equal to each other
        and `False` otherwise

        See
        - Objects.equals(Object, Object)
        """
        ...


    @staticmethod
    def hashCode(o: "Object") -> int:
        """
        Returns the hash code of a non-`null` argument and 0 for
        a `null` argument.

        Arguments
        - o: an object

        Returns
        - the hash code of a non-`null` argument and 0 for
        a `null` argument

        See
        - Object.hashCode
        """
        ...


    @staticmethod
    def hash(*values: Tuple["Object", ...]) -> int:
        """
        Generates a hash code for a sequence of input values. The hash
        code is generated as if all the input values were placed into an
        array, and that array were hashed by calling Arrays.hashCode(Object[]).
        
        This method is useful for implementing Object.hashCode() on objects containing multiple fields. For
        example, if an object that has three fields, `x`, `y`, and `z`, one could write:
        
        <blockquote>```
        &#064;Override public int hashCode() {
            return Objects.hash(x, y, z);
        }
        ```</blockquote>
        
        **Warning: When a single object reference is supplied, the returned
        value does not equal the hash code of that object reference.** This
        value can be computed by calling .hashCode(Object).

        Arguments
        - values: the values to be hashed

        Returns
        - a hash value of the sequence of input values

        See
        - List.hashCode
        """
        ...


    @staticmethod
    def toString(o: "Object") -> str:
        """
        Returns the result of calling `toString` for a non-`null` argument and `"null"` for a `null` argument.

        Arguments
        - o: an object

        Returns
        - the result of calling `toString` for a non-`null` argument and `"null"` for a `null` argument

        See
        - String.valueOf(Object)
        """
        ...


    @staticmethod
    def toString(o: "Object", nullDefault: str) -> str:
        """
        Returns the result of calling `toString` on the first
        argument if the first argument is not `null` and returns
        the second argument otherwise.

        Arguments
        - o: an object
        - nullDefault: string to return if the first argument is
               `null`

        Returns
        - the result of calling `toString` on the first
        argument if it is not `null` and the second argument
        otherwise.

        See
        - Objects.toString(Object)
        """
        ...


    @staticmethod
    def compare(a: "T", b: "T", c: "Comparator"["T"]) -> int:
        """
        Returns 0 if the arguments are identical and `c.compare(a, b)` otherwise.
        Consequently, if both arguments are `null` 0
        is returned.
        
        Note that if one of the arguments is `null`, a `NullPointerException` may or may not be thrown depending on
        what ordering policy, if any, the Comparator Comparator
        chooses to have for `null` values.
        
        Type `<T>`: the type of the objects being compared

        Arguments
        - a: an object
        - b: an object to be compared with `a`
        - c: the `Comparator` to compare the first two arguments

        Returns
        - 0 if the arguments are identical and `c.compare(a, b)` otherwise.

        See
        - Comparator
        """
        ...


    @staticmethod
    def requireNonNull(obj: "T") -> "T":
        """
        Checks that the specified object reference is not `null`. This
        method is designed primarily for doing parameter validation in methods
        and constructors, as demonstrated below:
        <blockquote>```
        public Foo(Bar bar) {
            this.bar = Objects.requireNonNull(bar);
        }
        ```</blockquote>
        
        Type `<T>`: the type of the reference

        Arguments
        - obj: the object reference to check for nullity

        Returns
        - `obj` if not `null`

        Raises
        - NullPointerException: if `obj` is `null`
        """
        ...


    @staticmethod
    def requireNonNull(obj: "T", message: str) -> "T":
        """
        Checks that the specified object reference is not `null` and
        throws a customized NullPointerException if it is. This method
        is designed primarily for doing parameter validation in methods and
        constructors with multiple parameters, as demonstrated below:
        <blockquote>```
        public Foo(Bar bar, Baz baz) {
            this.bar = Objects.requireNonNull(bar, "bar must not be null");
            this.baz = Objects.requireNonNull(baz, "baz must not be null");
        }
        ```</blockquote>
        
        Type `<T>`: the type of the reference

        Arguments
        - obj: the object reference to check for nullity
        - message: detail message to be used in the event that a `NullPointerException` is thrown

        Returns
        - `obj` if not `null`

        Raises
        - NullPointerException: if `obj` is `null`
        """
        ...


    @staticmethod
    def isNull(obj: "Object") -> bool:
        """
        Returns `True` if the provided reference is `null` otherwise
        returns `False`.

        Arguments
        - obj: a reference to be checked against `null`

        Returns
        - `True` if the provided reference is `null` otherwise
        `False`

        See
        - java.util.function.Predicate

        Since
        - 1.8

        Unknown Tags
        - This method exists to be used as a
        java.util.function.Predicate, `filter(Objects::isNull)`
        """
        ...


    @staticmethod
    def nonNull(obj: "Object") -> bool:
        """
        Returns `True` if the provided reference is non-`null`
        otherwise returns `False`.

        Arguments
        - obj: a reference to be checked against `null`

        Returns
        - `True` if the provided reference is non-`null`
        otherwise `False`

        See
        - java.util.function.Predicate

        Since
        - 1.8

        Unknown Tags
        - This method exists to be used as a
        java.util.function.Predicate, `filter(Objects::nonNull)`
        """
        ...


    @staticmethod
    def requireNonNullElse(obj: "T", defaultObj: "T") -> "T":
        """
        Returns the first argument if it is non-`null` and
        otherwise returns the non-`null` second argument.
        
        Type `<T>`: the type of the reference

        Arguments
        - obj: an object
        - defaultObj: a non-`null` object to return if the first argument
                          is `null`

        Returns
        - the first argument if it is non-`null` and
               otherwise the second argument if it is non-`null`

        Raises
        - NullPointerException: if both `obj` is null and
               `defaultObj` is `null`

        Since
        - 9
        """
        ...


    @staticmethod
    def requireNonNullElseGet(obj: "T", supplier: "Supplier"["T"]) -> "T":
        """
        Returns the first argument if it is non-`null` and otherwise
        returns the non-`null` value of `supplier.get()`.
        
        Type `<T>`: the type of the first argument and return type

        Arguments
        - obj: an object
        - supplier: of a non-`null` object to return if the first argument
                        is `null`

        Returns
        - the first argument if it is non-`null` and otherwise
                the value from `supplier.get()` if it is non-`null`

        Raises
        - NullPointerException: if both `obj` is null and
               either the `supplier` is `null` or
               the `supplier.get()` value is `null`

        Since
        - 9
        """
        ...


    @staticmethod
    def requireNonNull(obj: "T", messageSupplier: "Supplier"[str]) -> "T":
        """
        Checks that the specified object reference is not `null` and
        throws a customized NullPointerException if it is.
        
        Unlike the method .requireNonNull(Object, String),
        this method allows creation of the message to be deferred until
        after the null check is made. While this may confer a
        performance advantage in the non-null case, when deciding to
        call this method care should be taken that the costs of
        creating the message supplier are less than the cost of just
        creating the string message directly.
        
        Type `<T>`: the type of the reference

        Arguments
        - obj: the object reference to check for nullity
        - messageSupplier: supplier of the detail message to be
        used in the event that a `NullPointerException` is thrown

        Returns
        - `obj` if not `null`

        Raises
        - NullPointerException: if `obj` is `null`

        Since
        - 1.8
        """
        ...


    @staticmethod
    def checkIndex(index: int, length: int) -> int:
        """
        Checks if the `index` is within the bounds of the range from
        `0` (inclusive) to `length` (exclusive).
        
        The `index` is defined to be out of bounds if any of the
        following inequalities is True:
        
         - `index < 0`
         - `index >= length`
         - `length < 0`, which is implied from the former inequalities

        Arguments
        - index: the index
        - length: the upper-bound (exclusive) of the range

        Returns
        - `index` if it is within bounds of the range

        Raises
        - IndexOutOfBoundsException: if the `index` is out of bounds

        Since
        - 9
        """
        ...


    @staticmethod
    def checkFromToIndex(fromIndex: int, toIndex: int, length: int) -> int:
        """
        Checks if the sub-range from `fromIndex` (inclusive) to
        `toIndex` (exclusive) is within the bounds of range from `0`
        (inclusive) to `length` (exclusive).
        
        The sub-range is defined to be out of bounds if any of the following
        inequalities is True:
        
         - `fromIndex < 0`
         - `fromIndex > toIndex`
         - `toIndex > length`
         - `length < 0`, which is implied from the former inequalities

        Arguments
        - fromIndex: the lower-bound (inclusive) of the sub-range
        - toIndex: the upper-bound (exclusive) of the sub-range
        - length: the upper-bound (exclusive) the range

        Returns
        - `fromIndex` if the sub-range within bounds of the range

        Raises
        - IndexOutOfBoundsException: if the sub-range is out of bounds

        Since
        - 9
        """
        ...


    @staticmethod
    def checkFromIndexSize(fromIndex: int, size: int, length: int) -> int:
        """
        Checks if the sub-range from `fromIndex` (inclusive) to
        `fromIndex + size` (exclusive) is within the bounds of range from
        `0` (inclusive) to `length` (exclusive).
        
        The sub-range is defined to be out of bounds if any of the following
        inequalities is True:
        
         - `fromIndex < 0`
         - `size < 0`
         - `fromIndex + size > length`, taking into account integer overflow
         - `length < 0`, which is implied from the former inequalities

        Arguments
        - fromIndex: the lower-bound (inclusive) of the sub-interval
        - size: the size of the sub-range
        - length: the upper-bound (exclusive) of the range

        Returns
        - `fromIndex` if the sub-range within bounds of the range

        Raises
        - IndexOutOfBoundsException: if the sub-range is out of bounds

        Since
        - 9
        """
        ...


    @staticmethod
    def checkIndex(index: int, length: int) -> int:
        """
        Checks if the `index` is within the bounds of the range from
        `0` (inclusive) to `length` (exclusive).
        
        The `index` is defined to be out of bounds if any of the
        following inequalities is True:
        
         - `index < 0`
         - `index >= length`
         - `length < 0`, which is implied from the former inequalities

        Arguments
        - index: the index
        - length: the upper-bound (exclusive) of the range

        Returns
        - `index` if it is within bounds of the range

        Raises
        - IndexOutOfBoundsException: if the `index` is out of bounds

        Since
        - 16
        """
        ...


    @staticmethod
    def checkFromToIndex(fromIndex: int, toIndex: int, length: int) -> int:
        """
        Checks if the sub-range from `fromIndex` (inclusive) to
        `toIndex` (exclusive) is within the bounds of range from `0`
        (inclusive) to `length` (exclusive).
        
        The sub-range is defined to be out of bounds if any of the following
        inequalities is True:
        
         - `fromIndex < 0`
         - `fromIndex > toIndex`
         - `toIndex > length`
         - `length < 0`, which is implied from the former inequalities

        Arguments
        - fromIndex: the lower-bound (inclusive) of the sub-range
        - toIndex: the upper-bound (exclusive) of the sub-range
        - length: the upper-bound (exclusive) the range

        Returns
        - `fromIndex` if the sub-range within bounds of the range

        Raises
        - IndexOutOfBoundsException: if the sub-range is out of bounds

        Since
        - 16
        """
        ...


    @staticmethod
    def checkFromIndexSize(fromIndex: int, size: int, length: int) -> int:
        """
        Checks if the sub-range from `fromIndex` (inclusive) to
        `fromIndex + size` (exclusive) is within the bounds of range from
        `0` (inclusive) to `length` (exclusive).
        
        The sub-range is defined to be out of bounds if any of the following
        inequalities is True:
        
         - `fromIndex < 0`
         - `size < 0`
         - `fromIndex + size > length`, taking into account integer overflow
         - `length < 0`, which is implied from the former inequalities

        Arguments
        - fromIndex: the lower-bound (inclusive) of the sub-interval
        - size: the size of the sub-range
        - length: the upper-bound (exclusive) of the range

        Returns
        - `fromIndex` if the sub-range within bounds of the range

        Raises
        - IndexOutOfBoundsException: if the sub-range is out of bounds

        Since
        - 16
        """
        ...
