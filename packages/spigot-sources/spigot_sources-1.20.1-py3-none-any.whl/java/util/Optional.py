"""
Python module generated from Java source file java.util.Optional

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from java.util.function import Consumer
from java.util.function import Function
from java.util.function import Predicate
from java.util.function import Supplier
from java.util.stream import Stream
from typing import Any, Callable, Iterable, Tuple


class Optional:
    """
    A container object which may or may not contain a non-`null` value.
    If a value is present, `isPresent()` returns `True`. If no
    value is present, the object is considered *empty* and
    `isPresent()` returns `False`.
    
    Additional methods that depend on the presence or absence of a contained
    value are provided, such as .orElse(Object) orElse()
    (returns a default value if no value is present) and
    .ifPresent(Consumer) ifPresent() (performs an
    action if a value is present).
    
    This is a <a href="/java.base/java/lang/doc-files/ValueBased.html">value-based</a>
    class; programmers should treat instances that are
    .equals(Object) equal as interchangeable and should not
    use instances for synchronization, or unpredictable behavior may
    occur. For example, in a future release, synchronization may fail.
    
    Type `<T>`: the type of value

    Since
    - 1.8

    Unknown Tags
    - `Optional` is primarily intended for use as a method return type where
    there is a clear need to represent "no result," and where using `null`
    is likely to cause errors. A variable whose type is `Optional` should
    never itself be `null`; it should always point to an `Optional`
    instance.
    """

    @staticmethod
    def empty() -> "Optional"["T"]:
        """
        Returns an empty `Optional` instance.  No value is present for this
        `Optional`.
        
        Type `<T>`: The type of the non-existent value

        Returns
        - an empty `Optional`

        Unknown Tags
        - Though it may be tempting to do so, avoid testing if an object is empty
        by comparing with `==` or `!=` against instances returned by
        `Optional.empty()`.  There is no guarantee that it is a singleton.
        Instead, use .isEmpty() or .isPresent().
        """
        ...


    @staticmethod
    def of(value: "T") -> "Optional"["T"]:
        """
        Returns an `Optional` describing the given non-`null`
        value.
        
        Type `<T>`: the type of the value

        Arguments
        - value: the value to describe, which must be non-`null`

        Returns
        - an `Optional` with the value present

        Raises
        - NullPointerException: if value is `null`
        """
        ...


    @staticmethod
    def ofNullable(value: "T") -> "Optional"["T"]:
        """
        Returns an `Optional` describing the given value, if
        non-`null`, otherwise returns an empty `Optional`.
        
        Type `<T>`: the type of the value

        Arguments
        - value: the possibly-`null` value to describe

        Returns
        - an `Optional` with a present value if the specified value
                is non-`null`, otherwise an empty `Optional`
        """
        ...


    def get(self) -> "T":
        """
        If a value is present, returns the value, otherwise throws
        `NoSuchElementException`.

        Returns
        - the non-`null` value described by this `Optional`

        Raises
        - NoSuchElementException: if no value is present

        Unknown Tags
        - The preferred alternative to this method is .orElseThrow().
        """
        ...


    def isPresent(self) -> bool:
        """
        If a value is present, returns `True`, otherwise `False`.

        Returns
        - `True` if a value is present, otherwise `False`
        """
        ...


    def isEmpty(self) -> bool:
        """
        If a value is  not present, returns `True`, otherwise
        `False`.

        Returns
        - `True` if a value is not present, otherwise `False`

        Since
        - 11
        """
        ...


    def ifPresent(self, action: "Consumer"["T"]) -> None:
        """
        If a value is present, performs the given action with the value,
        otherwise does nothing.

        Arguments
        - action: the action to be performed, if a value is present

        Raises
        - NullPointerException: if value is present and the given action is
                `null`
        """
        ...


    def ifPresentOrElse(self, action: "Consumer"["T"], emptyAction: "Runnable") -> None:
        """
        If a value is present, performs the given action with the value,
        otherwise performs the given empty-based action.

        Arguments
        - action: the action to be performed, if a value is present
        - emptyAction: the empty-based action to be performed, if no value is
               present

        Raises
        - NullPointerException: if a value is present and the given action
                is `null`, or no value is present and the given empty-based
                action is `null`.

        Since
        - 9
        """
        ...


    def filter(self, predicate: "Predicate"["T"]) -> "Optional"["T"]:
        """
        If a value is present, and the value matches the given predicate,
        returns an `Optional` describing the value, otherwise returns an
        empty `Optional`.

        Arguments
        - predicate: the predicate to apply to a value, if present

        Returns
        - an `Optional` describing the value of this
                `Optional`, if a value is present and the value matches the
                given predicate, otherwise an empty `Optional`

        Raises
        - NullPointerException: if the predicate is `null`
        """
        ...


    def map(self, mapper: "Function"["T", "U"]) -> "Optional"["U"]:
        """
        If a value is present, returns an `Optional` describing (as if by
        .ofNullable) the result of applying the given mapping function to
        the value, otherwise returns an empty `Optional`.
        
        If the mapping function returns a `null` result then this method
        returns an empty `Optional`.
        
        Type `<U>`: The type of the value returned from the mapping function

        Arguments
        - mapper: the mapping function to apply to a value, if present

        Returns
        - an `Optional` describing the result of applying a mapping
                function to the value of this `Optional`, if a value is
                present, otherwise an empty `Optional`

        Raises
        - NullPointerException: if the mapping function is `null`

        Unknown Tags
        - This method supports post-processing on `Optional` values, without
        the need to explicitly check for a return status.  For example, the
        following code traverses a stream of URIs, selects one that has not
        yet been processed, and creates a path from that URI, returning
        an `Optional<Path>`:
        
        ````Optional<Path> p =
                uris.stream().filter(uri -> !isProcessedYet(uri))
                              .findFirst()
                              .map(Paths::get);````
        
        Here, `findFirst` returns an `Optional<URI>`, and then
        `map` returns an `Optional<Path>` for the desired
        URI if one exists.
        """
        ...


    def flatMap(self, mapper: "Function"["T", "Optional"["U"]]) -> "Optional"["U"]:
        """
        If a value is present, returns the result of applying the given
        `Optional`-bearing mapping function to the value, otherwise returns
        an empty `Optional`.
        
        This method is similar to .map(Function), but the mapping
        function is one whose result is already an `Optional`, and if
        invoked, `flatMap` does not wrap it within an additional
        `Optional`.
        
        Type `<U>`: The type of value of the `Optional` returned by the
                   mapping function

        Arguments
        - mapper: the mapping function to apply to a value, if present

        Returns
        - the result of applying an `Optional`-bearing mapping
                function to the value of this `Optional`, if a value is
                present, otherwise an empty `Optional`

        Raises
        - NullPointerException: if the mapping function is `null` or
                returns a `null` result
        """
        ...


    def or(self, supplier: "Supplier"["Optional"["T"]]) -> "Optional"["T"]:
        """
        If a value is present, returns an `Optional` describing the value,
        otherwise returns an `Optional` produced by the supplying function.

        Arguments
        - supplier: the supplying function that produces an `Optional`
               to be returned

        Returns
        - returns an `Optional` describing the value of this
                `Optional`, if a value is present, otherwise an
                `Optional` produced by the supplying function.

        Raises
        - NullPointerException: if the supplying function is `null` or
                produces a `null` result

        Since
        - 9
        """
        ...


    def stream(self) -> "Stream"["T"]:
        """
        If a value is present, returns a sequential Stream containing
        only that value, otherwise returns an empty `Stream`.

        Returns
        - the optional value as a `Stream`

        Since
        - 9

        Unknown Tags
        - This method can be used to transform a `Stream` of optional
        elements to a `Stream` of present value elements:
        ````Stream<Optional<T>> os = ..
            Stream<T> s = os.flatMap(Optional::stream)````
        """
        ...


    def orElse(self, other: "T") -> "T":
        """
        If a value is present, returns the value, otherwise returns
        `other`.

        Arguments
        - other: the value to be returned, if no value is present.
               May be `null`.

        Returns
        - the value, if present, otherwise `other`
        """
        ...


    def orElseGet(self, supplier: "Supplier"["T"]) -> "T":
        """
        If a value is present, returns the value, otherwise returns the result
        produced by the supplying function.

        Arguments
        - supplier: the supplying function that produces a value to be returned

        Returns
        - the value, if present, otherwise the result produced by the
                supplying function

        Raises
        - NullPointerException: if no value is present and the supplying
                function is `null`
        """
        ...


    def orElseThrow(self) -> "T":
        """
        If a value is present, returns the value, otherwise throws
        `NoSuchElementException`.

        Returns
        - the non-`null` value described by this `Optional`

        Raises
        - NoSuchElementException: if no value is present

        Since
        - 10
        """
        ...


    def orElseThrow(self, exceptionSupplier: "Supplier"["X"]) -> "T":
        """
        If a value is present, returns the value, otherwise throws an exception
        produced by the exception supplying function.
        
        Type `<X>`: Type of the exception to be thrown

        Arguments
        - exceptionSupplier: the supplying function that produces an
               exception to be thrown

        Returns
        - the value, if present

        Raises
        - X: if no value is present
        - NullPointerException: if no value is present and the exception
                 supplying function is `null`

        Unknown Tags
        - A method reference to the exception constructor with an empty argument
        list can be used as the supplier. For example,
        `IllegalStateException::new`
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Indicates whether some other object is "equal to" this `Optional`.
        The other object is considered equal if:
        
        - it is also an `Optional` and;
        - both instances have no value present or;
        - the present values are "equal to" each other via `equals()`.

        Arguments
        - obj: an object to be tested for equality

        Returns
        - `True` if the other object is "equal to" this object
                otherwise `False`
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code of the value, if present, otherwise `0`
        (zero) if no value is present.

        Returns
        - hash code value of the present value or `0` if no value is
                present
        """
        ...


    def toString(self) -> str:
        """
        Returns a non-empty string representation of this `Optional`
        suitable for debugging.  The exact presentation format is unspecified and
        may vary between implementations and versions.

        Returns
        - the string representation of this instance

        Unknown Tags
        - If a value is present the result must include its string representation
        in the result.  Empty and present `Optional`s must be unambiguously
        differentiable.
        """
        ...
