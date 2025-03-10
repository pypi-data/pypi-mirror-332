"""
Python module generated from Java source file java.util.OptionalDouble

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from java.util.function import DoubleConsumer
from java.util.function import DoubleSupplier
from java.util.function import Supplier
from java.util.stream import DoubleStream
from typing import Any, Callable, Iterable, Tuple


class OptionalDouble:
    """
    A container object which may or may not contain a `double` value.
    If a value is present, `isPresent()` returns `True`. If no
    value is present, the object is considered *empty* and
    `isPresent()` returns `False`.
    
    Additional methods that depend on the presence or absence of a contained
    value are provided, such as .orElse(double) orElse()
    (returns a default value if no value is present) and
    .ifPresent(DoubleConsumer) ifPresent() (performs
    an action if a value is present).
    
    This is a <a href="/java.base/java/lang/doc-files/ValueBased.html">value-based</a>
    class; programmers should treat instances that are
    .equals(Object) equal as interchangeable and should not
    use instances for synchronization, or unpredictable behavior may
    occur. For example, in a future release, synchronization may fail.

    Since
    - 1.8

    Unknown Tags
    - `OptionalDouble` is primarily intended for use as a method return type where
    there is a clear need to represent "no result." A variable whose type is
    `OptionalDouble` should never itself be `null`; it should always point
    to an `OptionalDouble` instance.
    """

    @staticmethod
    def empty() -> "OptionalDouble":
        """
        Returns an empty `OptionalDouble` instance.  No value is present
        for this `OptionalDouble`.

        Returns
        - an empty `OptionalDouble`.

        Unknown Tags
        - Though it may be tempting to do so, avoid testing if an object is empty
        by comparing with `==` or `!=` against instances returned by
        `OptionalDouble.empty()`.  There is no guarantee that it is a singleton.
        Instead, use .isEmpty() or .isPresent().
        """
        ...


    @staticmethod
    def of(value: float) -> "OptionalDouble":
        """
        Returns an `OptionalDouble` describing the given value.

        Arguments
        - value: the value to describe

        Returns
        - an `OptionalDouble` with the value present
        """
        ...


    def getAsDouble(self) -> float:
        """
        If a value is present, returns the value, otherwise throws
        `NoSuchElementException`.

        Returns
        - the value described by this `OptionalDouble`

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
        If a value is not present, returns `True`, otherwise
        `False`.

        Returns
        - `True` if a value is not present, otherwise `False`

        Since
        - 11
        """
        ...


    def ifPresent(self, action: "DoubleConsumer") -> None:
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


    def ifPresentOrElse(self, action: "DoubleConsumer", emptyAction: "Runnable") -> None:
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


    def stream(self) -> "DoubleStream":
        """
        If a value is present, returns a sequential DoubleStream
        containing only that value, otherwise returns an empty
        `DoubleStream`.

        Returns
        - the optional value as a `DoubleStream`

        Since
        - 9

        Unknown Tags
        - This method can be used to transform a `Stream` of optional doubles
        to a `DoubleStream` of present doubles:
        ````Stream<OptionalDouble> os = ..
            DoubleStream s = os.flatMapToDouble(OptionalDouble::stream)````
        """
        ...


    def orElse(self, other: float) -> float:
        """
        If a value is present, returns the value, otherwise returns
        `other`.

        Arguments
        - other: the value to be returned, if no value is present

        Returns
        - the value, if present, otherwise `other`
        """
        ...


    def orElseGet(self, supplier: "DoubleSupplier") -> float:
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


    def orElseThrow(self) -> float:
        """
        If a value is present, returns the value, otherwise throws
        `NoSuchElementException`.

        Returns
        - the value described by this `OptionalDouble`

        Raises
        - NoSuchElementException: if no value is present

        Since
        - 10
        """
        ...


    def orElseThrow(self, exceptionSupplier: "Supplier"["X"]) -> float:
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
        Indicates whether some other object is "equal to" this
        `OptionalDouble`. The other object is considered equal if:
        
        - it is also an `OptionalDouble` and;
        - both instances have no value present or;
        - the present values are "equal to" each other via
        `Double.compare() == 0`.

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
        Returns a non-empty string representation of this `OptionalDouble`
        suitable for debugging.  The exact presentation format is unspecified and
        may vary between implementations and versions.

        Returns
        - the string representation of this instance

        Unknown Tags
        - If a value is present the result must include its string representation
        in the result.  Empty and present `OptionalDouble`s must be
        unambiguously differentiable.
        """
        ...
