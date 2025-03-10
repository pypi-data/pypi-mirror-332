"""
Python module generated from Java source file java.util.concurrent.atomic.AtomicReferenceArray

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import MethodHandles
from java.lang.invoke import VarHandle
from java.lang.reflect import Array
from java.lang.reflect import Field
from java.util import Arrays
from java.util.concurrent.atomic import *
from java.util.function import BinaryOperator
from java.util.function import UnaryOperator
from typing import Any, Callable, Iterable, Tuple


class AtomicReferenceArray(Serializable):
    """
    An array of object references in which elements may be updated
    atomically.  See the VarHandle specification for
    descriptions of the properties of atomic accesses.
    
    Type `<E>`: The base class of elements held in this array

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self, length: int):
        """
        Creates a new AtomicReferenceArray of the given length, with all
        elements initially null.

        Arguments
        - length: the length of the array
        """
        ...


    def __init__(self, array: list["E"]):
        """
        Creates a new AtomicReferenceArray with the same length as, and
        all elements copied from, the given array.

        Arguments
        - array: the array to copy elements from

        Raises
        - NullPointerException: if array is null
        """
        ...


    def length(self) -> int:
        """
        Returns the length of the array.

        Returns
        - the length of the array
        """
        ...


    def get(self, i: int) -> "E":
        """
        Returns the current value of the element at index `i`,
        with memory effects as specified by VarHandle.getVolatile.

        Arguments
        - i: the index

        Returns
        - the current value
        """
        ...


    def set(self, i: int, newValue: "E") -> None:
        """
        Sets the element at index `i` to `newValue`,
        with memory effects as specified by VarHandle.setVolatile.

        Arguments
        - i: the index
        - newValue: the new value
        """
        ...


    def lazySet(self, i: int, newValue: "E") -> None:
        """
        Sets the element at index `i` to `newValue`,
        with memory effects as specified by VarHandle.setRelease.

        Arguments
        - i: the index
        - newValue: the new value

        Since
        - 1.6
        """
        ...


    def getAndSet(self, i: int, newValue: "E") -> "E":
        """
        Atomically sets the element at index `i` to `newValue` and returns the old value,
        with memory effects as specified by VarHandle.getAndSet.

        Arguments
        - i: the index
        - newValue: the new value

        Returns
        - the previous value
        """
        ...


    def compareAndSet(self, i: int, expectedValue: "E", newValue: "E") -> bool:
        """
        Atomically sets the element at index `i` to `newValue`
        if the element's current value `== expectedValue`,
        with memory effects as specified by VarHandle.compareAndSet.

        Arguments
        - i: the index
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful. False return indicates that
        the actual value was not equal to the expected value.
        """
        ...


    def weakCompareAndSet(self, i: int, expectedValue: "E", newValue: "E") -> bool:
        """
        Possibly atomically sets the element at index `i` to
        `newValue` if the element's current value `== expectedValue`,
        with memory effects as specified by VarHandle.weakCompareAndSetPlain.

        Arguments
        - i: the index
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful

        See
        - .weakCompareAndSetPlain

        Deprecated
        - This method has plain memory effects but the method
        name implies volatile memory effects (see methods such as
        .compareAndExchange and .compareAndSet).  To avoid
        confusion over plain or volatile memory effects it is recommended that
        the method .weakCompareAndSetPlain be used instead.
        """
        ...


    def weakCompareAndSetPlain(self, i: int, expectedValue: "E", newValue: "E") -> bool:
        """
        Possibly atomically sets the element at index `i` to
        `newValue` if the element's current value `== expectedValue`,
        with memory effects as specified by VarHandle.weakCompareAndSetPlain.

        Arguments
        - i: the index
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful

        Since
        - 9
        """
        ...


    def getAndUpdate(self, i: int, updateFunction: "UnaryOperator"["E"]) -> "E":
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the element at index `i` with
        the results of applying the given function, returning the
        previous value. The function should be side-effect-free, since
        it may be re-applied when attempted updates fail due to
        contention among threads.

        Arguments
        - i: the index
        - updateFunction: a side-effect-free function

        Returns
        - the previous value

        Since
        - 1.8
        """
        ...


    def updateAndGet(self, i: int, updateFunction: "UnaryOperator"["E"]) -> "E":
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the element at index `i` with
        the results of applying the given function, returning the
        updated value. The function should be side-effect-free, since it
        may be re-applied when attempted updates fail due to contention
        among threads.

        Arguments
        - i: the index
        - updateFunction: a side-effect-free function

        Returns
        - the updated value

        Since
        - 1.8
        """
        ...


    def getAndAccumulate(self, i: int, x: "E", accumulatorFunction: "BinaryOperator"["E"]) -> "E":
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the element at index `i` with
        the results of applying the given function to the current and
        given values, returning the previous value. The function should
        be side-effect-free, since it may be re-applied when attempted
        updates fail due to contention among threads.  The function is
        applied with the current value of the element at index `i`
        as its first argument, and the given update as the second
        argument.

        Arguments
        - i: the index
        - x: the update value
        - accumulatorFunction: a side-effect-free function of two arguments

        Returns
        - the previous value

        Since
        - 1.8
        """
        ...


    def accumulateAndGet(self, i: int, x: "E", accumulatorFunction: "BinaryOperator"["E"]) -> "E":
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the element at index `i` with
        the results of applying the given function to the current and
        given values, returning the updated value. The function should
        be side-effect-free, since it may be re-applied when attempted
        updates fail due to contention among threads.  The function is
        applied with the current value of the element at index `i`
        as its first argument, and the given update as the second
        argument.

        Arguments
        - i: the index
        - x: the update value
        - accumulatorFunction: a side-effect-free function of two arguments

        Returns
        - the updated value

        Since
        - 1.8
        """
        ...


    def toString(self) -> str:
        """
        Returns the String representation of the current values of array.

        Returns
        - the String representation of the current values of array
        """
        ...


    def getPlain(self, i: int) -> "E":
        """
        Returns the current value of the element at index `i`,
        with memory semantics of reading as if the variable was declared
        non-`volatile`.

        Arguments
        - i: the index

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setPlain(self, i: int, newValue: "E") -> None:
        """
        Sets the element at index `i` to `newValue`,
        with memory semantics of setting as if the variable was
        declared non-`volatile` and non-`final`.

        Arguments
        - i: the index
        - newValue: the new value

        Since
        - 9
        """
        ...


    def getOpaque(self, i: int) -> "E":
        """
        Returns the current value of the element at index `i`,
        with memory effects as specified by VarHandle.getOpaque.

        Arguments
        - i: the index

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setOpaque(self, i: int, newValue: "E") -> None:
        """
        Sets the element at index `i` to `newValue`,
        with memory effects as specified by VarHandle.setOpaque.

        Arguments
        - i: the index
        - newValue: the new value

        Since
        - 9
        """
        ...


    def getAcquire(self, i: int) -> "E":
        """
        Returns the current value of the element at index `i`,
        with memory effects as specified by VarHandle.getAcquire.

        Arguments
        - i: the index

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setRelease(self, i: int, newValue: "E") -> None:
        """
        Sets the element at index `i` to `newValue`,
        with memory effects as specified by VarHandle.setRelease.

        Arguments
        - i: the index
        - newValue: the new value

        Since
        - 9
        """
        ...


    def compareAndExchange(self, i: int, expectedValue: "E", newValue: "E") -> "E":
        """
        Atomically sets the element at index `i` to `newValue`
        if the element's current value, referred to as the *witness
        value*, `== expectedValue`,
        with memory effects as specified by
        VarHandle.compareAndExchange.

        Arguments
        - i: the index
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - the witness value, which will be the same as the
        expected value if successful

        Since
        - 9
        """
        ...


    def compareAndExchangeAcquire(self, i: int, expectedValue: "E", newValue: "E") -> "E":
        """
        Atomically sets the element at index `i` to `newValue`
        if the element's current value, referred to as the *witness
        value*, `== expectedValue`,
        with memory effects as specified by
        VarHandle.compareAndExchangeAcquire.

        Arguments
        - i: the index
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - the witness value, which will be the same as the
        expected value if successful

        Since
        - 9
        """
        ...


    def compareAndExchangeRelease(self, i: int, expectedValue: "E", newValue: "E") -> "E":
        """
        Atomically sets the element at index `i` to `newValue`
        if the element's current value, referred to as the *witness
        value*, `== expectedValue`,
        with memory effects as specified by
        VarHandle.compareAndExchangeRelease.

        Arguments
        - i: the index
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - the witness value, which will be the same as the
        expected value if successful

        Since
        - 9
        """
        ...


    def weakCompareAndSetVolatile(self, i: int, expectedValue: "E", newValue: "E") -> bool:
        """
        Possibly atomically sets the element at index `i` to
        `newValue` if the element's current value `== expectedValue`,
        with memory effects as specified by
        VarHandle.weakCompareAndSet.

        Arguments
        - i: the index
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful

        Since
        - 9
        """
        ...


    def weakCompareAndSetAcquire(self, i: int, expectedValue: "E", newValue: "E") -> bool:
        """
        Possibly atomically sets the element at index `i` to
        `newValue` if the element's current value `== expectedValue`,
        with memory effects as specified by
        VarHandle.weakCompareAndSetAcquire.

        Arguments
        - i: the index
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful

        Since
        - 9
        """
        ...


    def weakCompareAndSetRelease(self, i: int, expectedValue: "E", newValue: "E") -> bool:
        """
        Possibly atomically sets the element at index `i` to
        `newValue` if the element's current value `== expectedValue`,
        with memory effects as specified by
        VarHandle.weakCompareAndSetRelease.

        Arguments
        - i: the index
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful

        Since
        - 9
        """
        ...
