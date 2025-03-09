"""
Python module generated from Java source file java.util.concurrent.atomic.AtomicReference

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import MethodHandles
from java.lang.invoke import VarHandle
from java.util.concurrent.atomic import *
from java.util.function import BinaryOperator
from java.util.function import UnaryOperator
from typing import Any, Callable, Iterable, Tuple


class AtomicReference(Serializable):
    """
    An object reference that may be updated atomically.  See the VarHandle specification for descriptions of the properties of
    atomic accesses.
    
    Type `<V>`: The type of object referred to by this reference

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self, initialValue: "V"):
        """
        Creates a new AtomicReference with the given initial value.

        Arguments
        - initialValue: the initial value
        """
        ...


    def __init__(self):
        """
        Creates a new AtomicReference with null initial value.
        """
        ...


    def get(self) -> "V":
        """
        Returns the current value,
        with memory effects as specified by VarHandle.getVolatile.

        Returns
        - the current value
        """
        ...


    def set(self, newValue: "V") -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setVolatile.

        Arguments
        - newValue: the new value
        """
        ...


    def lazySet(self, newValue: "V") -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setRelease.

        Arguments
        - newValue: the new value

        Since
        - 1.6
        """
        ...


    def compareAndSet(self, expectedValue: "V", newValue: "V") -> bool:
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


    def weakCompareAndSet(self, expectedValue: "V", newValue: "V") -> bool:
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


    def weakCompareAndSetPlain(self, expectedValue: "V", newValue: "V") -> bool:
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


    def getAndSet(self, newValue: "V") -> "V":
        """
        Atomically sets the value to `newValue` and returns the old value,
        with memory effects as specified by VarHandle.getAndSet.

        Arguments
        - newValue: the new value

        Returns
        - the previous value
        """
        ...


    def getAndUpdate(self, updateFunction: "UnaryOperator"["V"]) -> "V":
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


    def updateAndGet(self, updateFunction: "UnaryOperator"["V"]) -> "V":
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


    def getAndAccumulate(self, x: "V", accumulatorFunction: "BinaryOperator"["V"]) -> "V":
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


    def accumulateAndGet(self, x: "V", accumulatorFunction: "BinaryOperator"["V"]) -> "V":
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


    def getPlain(self) -> "V":
        """
        Returns the current value, with memory semantics of reading as
        if the variable was declared non-`volatile`.

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setPlain(self, newValue: "V") -> None:
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


    def getOpaque(self) -> "V":
        """
        Returns the current value,
        with memory effects as specified by VarHandle.getOpaque.

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setOpaque(self, newValue: "V") -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setOpaque.

        Arguments
        - newValue: the new value

        Since
        - 9
        """
        ...


    def getAcquire(self) -> "V":
        """
        Returns the current value,
        with memory effects as specified by VarHandle.getAcquire.

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setRelease(self, newValue: "V") -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setRelease.

        Arguments
        - newValue: the new value

        Since
        - 9
        """
        ...


    def compareAndExchange(self, expectedValue: "V", newValue: "V") -> "V":
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


    def compareAndExchangeAcquire(self, expectedValue: "V", newValue: "V") -> "V":
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


    def compareAndExchangeRelease(self, expectedValue: "V", newValue: "V") -> "V":
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


    def weakCompareAndSetVolatile(self, expectedValue: "V", newValue: "V") -> bool:
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


    def weakCompareAndSetAcquire(self, expectedValue: "V", newValue: "V") -> bool:
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


    def weakCompareAndSetRelease(self, expectedValue: "V", newValue: "V") -> bool:
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
