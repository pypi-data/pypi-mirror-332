"""
Python module generated from Java source file java.util.concurrent.atomic.AtomicLong

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import VarHandle
from java.util.concurrent.atomic import *
from java.util.function import LongBinaryOperator
from java.util.function import LongUnaryOperator
from jdk.internal.misc import Unsafe
from typing import Any, Callable, Iterable, Tuple


class AtomicLong(Number, Serializable):
    """
    A `long` value that may be updated atomically.  See the
    VarHandle specification for descriptions of the properties
    of atomic accesses. An `AtomicLong` is used in applications
    such as atomically incremented sequence numbers, and cannot be used
    as a replacement for a java.lang.Long. However, this class
    does extend `Number` to allow uniform access by tools and
    utilities that deal with numerically-based classes.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self, initialValue: int):
        """
        Creates a new AtomicLong with the given initial value.

        Arguments
        - initialValue: the initial value
        """
        ...


    def __init__(self):
        """
        Creates a new AtomicLong with initial value `0`.
        """
        ...


    def get(self) -> int:
        """
        Returns the current value,
        with memory effects as specified by VarHandle.getVolatile.

        Returns
        - the current value
        """
        ...


    def set(self, newValue: int) -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setVolatile.

        Arguments
        - newValue: the new value
        """
        ...


    def lazySet(self, newValue: int) -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setRelease.

        Arguments
        - newValue: the new value

        Since
        - 1.6
        """
        ...


    def getAndSet(self, newValue: int) -> int:
        """
        Atomically sets the value to `newValue` and returns the old value,
        with memory effects as specified by VarHandle.getAndSet.

        Arguments
        - newValue: the new value

        Returns
        - the previous value
        """
        ...


    def compareAndSet(self, expectedValue: int, newValue: int) -> bool:
        """
        Atomically sets the value to `newValue`
        if the current value `== expectedValue`,
        with memory effects as specified by VarHandle.compareAndSet.

        Arguments
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful. False return indicates that
        the actual value was not equal to the expected value.
        """
        ...


    def weakCompareAndSet(self, expectedValue: int, newValue: int) -> bool:
        """
        Possibly atomically sets the value to `newValue`
        if the current value `== expectedValue`,
        with memory effects as specified by VarHandle.weakCompareAndSetPlain.

        Arguments
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


    def weakCompareAndSetPlain(self, expectedValue: int, newValue: int) -> bool:
        """
        Possibly atomically sets the value to `newValue`
        if the current value `== expectedValue`,
        with memory effects as specified by VarHandle.weakCompareAndSetPlain.

        Arguments
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful

        Since
        - 9
        """
        ...


    def getAndIncrement(self) -> int:
        """
        Atomically increments the current value,
        with memory effects as specified by VarHandle.getAndAdd.
        
        Equivalent to `getAndAdd(1)`.

        Returns
        - the previous value
        """
        ...


    def getAndDecrement(self) -> int:
        """
        Atomically decrements the current value,
        with memory effects as specified by VarHandle.getAndAdd.
        
        Equivalent to `getAndAdd(-1)`.

        Returns
        - the previous value
        """
        ...


    def getAndAdd(self, delta: int) -> int:
        """
        Atomically adds the given value to the current value,
        with memory effects as specified by VarHandle.getAndAdd.

        Arguments
        - delta: the value to add

        Returns
        - the previous value
        """
        ...


    def incrementAndGet(self) -> int:
        """
        Atomically increments the current value,
        with memory effects as specified by VarHandle.getAndAdd.
        
        Equivalent to `addAndGet(1)`.

        Returns
        - the updated value
        """
        ...


    def decrementAndGet(self) -> int:
        """
        Atomically decrements the current value,
        with memory effects as specified by VarHandle.getAndAdd.
        
        Equivalent to `addAndGet(-1)`.

        Returns
        - the updated value
        """
        ...


    def addAndGet(self, delta: int) -> int:
        """
        Atomically adds the given value to the current value,
        with memory effects as specified by VarHandle.getAndAdd.

        Arguments
        - delta: the value to add

        Returns
        - the updated value
        """
        ...


    def getAndUpdate(self, updateFunction: "LongUnaryOperator") -> int:
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the current value with the results of
        applying the given function, returning the previous value. The
        function should be side-effect-free, since it may be re-applied
        when attempted updates fail due to contention among threads.

        Arguments
        - updateFunction: a side-effect-free function

        Returns
        - the previous value

        Since
        - 1.8
        """
        ...


    def updateAndGet(self, updateFunction: "LongUnaryOperator") -> int:
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the current value with the results of
        applying the given function, returning the updated value. The
        function should be side-effect-free, since it may be re-applied
        when attempted updates fail due to contention among threads.

        Arguments
        - updateFunction: a side-effect-free function

        Returns
        - the updated value

        Since
        - 1.8
        """
        ...


    def getAndAccumulate(self, x: int, accumulatorFunction: "LongBinaryOperator") -> int:
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the current value with the results of
        applying the given function to the current and given values,
        returning the previous value. The function should be
        side-effect-free, since it may be re-applied when attempted
        updates fail due to contention among threads.  The function is
        applied with the current value as its first argument, and the
        given update as the second argument.

        Arguments
        - x: the update value
        - accumulatorFunction: a side-effect-free function of two arguments

        Returns
        - the previous value

        Since
        - 1.8
        """
        ...


    def accumulateAndGet(self, x: int, accumulatorFunction: "LongBinaryOperator") -> int:
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the current value with the results of
        applying the given function to the current and given values,
        returning the updated value. The function should be
        side-effect-free, since it may be re-applied when attempted
        updates fail due to contention among threads.  The function is
        applied with the current value as its first argument, and the
        given update as the second argument.

        Arguments
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
        Returns the String representation of the current value.

        Returns
        - the String representation of the current value
        """
        ...


    def intValue(self) -> int:
        """
        Returns the current value of this `AtomicLong` as an `int`
        after a narrowing primitive conversion,
        with memory effects as specified by VarHandle.getVolatile.

        Unknown Tags
        - 5.1.3 Narrowing Primitive Conversion
        """
        ...


    def longValue(self) -> int:
        """
        Returns the current value of this `AtomicLong` as a `long`,
        with memory effects as specified by VarHandle.getVolatile.
        Equivalent to .get().
        """
        ...


    def floatValue(self) -> float:
        """
        Returns the current value of this `AtomicLong` as a `float`
        after a widening primitive conversion,
        with memory effects as specified by VarHandle.getVolatile.

        Unknown Tags
        - 5.1.2 Widening Primitive Conversion
        """
        ...


    def doubleValue(self) -> float:
        """
        Returns the current value of this `AtomicLong` as a `double`
        after a widening primitive conversion,
        with memory effects as specified by VarHandle.getVolatile.

        Unknown Tags
        - 5.1.2 Widening Primitive Conversion
        """
        ...


    def getPlain(self) -> int:
        """
        Returns the current value, with memory semantics of reading as if the
        variable was declared non-`volatile`.

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setPlain(self, newValue: int) -> None:
        """
        Sets the value to `newValue`, with memory semantics
        of setting as if the variable was declared non-`volatile`
        and non-`final`.

        Arguments
        - newValue: the new value

        Since
        - 9
        """
        ...


    def getOpaque(self) -> int:
        """
        Returns the current value,
        with memory effects as specified by VarHandle.getOpaque.

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setOpaque(self, newValue: int) -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setOpaque.

        Arguments
        - newValue: the new value

        Since
        - 9
        """
        ...


    def getAcquire(self) -> int:
        """
        Returns the current value,
        with memory effects as specified by VarHandle.getAcquire.

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setRelease(self, newValue: int) -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setRelease.

        Arguments
        - newValue: the new value

        Since
        - 9
        """
        ...


    def compareAndExchange(self, expectedValue: int, newValue: int) -> int:
        """
        Atomically sets the value to `newValue` if the current value,
        referred to as the *witness value*, `== expectedValue`,
        with memory effects as specified by
        VarHandle.compareAndExchange.

        Arguments
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - the witness value, which will be the same as the
        expected value if successful

        Since
        - 9
        """
        ...


    def compareAndExchangeAcquire(self, expectedValue: int, newValue: int) -> int:
        """
        Atomically sets the value to `newValue` if the current value,
        referred to as the *witness value*, `== expectedValue`,
        with memory effects as specified by
        VarHandle.compareAndExchangeAcquire.

        Arguments
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - the witness value, which will be the same as the
        expected value if successful

        Since
        - 9
        """
        ...


    def compareAndExchangeRelease(self, expectedValue: int, newValue: int) -> int:
        """
        Atomically sets the value to `newValue` if the current value,
        referred to as the *witness value*, `== expectedValue`,
        with memory effects as specified by
        VarHandle.compareAndExchangeRelease.

        Arguments
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - the witness value, which will be the same as the
        expected value if successful

        Since
        - 9
        """
        ...


    def weakCompareAndSetVolatile(self, expectedValue: int, newValue: int) -> bool:
        """
        Possibly atomically sets the value to `newValue`
        if the current value `== expectedValue`,
        with memory effects as specified by
        VarHandle.weakCompareAndSet.

        Arguments
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful

        Since
        - 9
        """
        ...


    def weakCompareAndSetAcquire(self, expectedValue: int, newValue: int) -> bool:
        """
        Possibly atomically sets the value to `newValue`
        if the current value `== expectedValue`,
        with memory effects as specified by
        VarHandle.weakCompareAndSetAcquire.

        Arguments
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful

        Since
        - 9
        """
        ...


    def weakCompareAndSetRelease(self, expectedValue: int, newValue: int) -> bool:
        """
        Possibly atomically sets the value to `newValue`
        if the current value `== expectedValue`,
        with memory effects as specified by
        VarHandle.weakCompareAndSetRelease.

        Arguments
        - expectedValue: the expected value
        - newValue: the new value

        Returns
        - `True` if successful

        Since
        - 9
        """
        ...
