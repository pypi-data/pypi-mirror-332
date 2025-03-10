"""
Python module generated from Java source file java.util.concurrent.atomic.AtomicBoolean

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import MethodHandles
from java.lang.invoke import VarHandle
from java.util.concurrent.atomic import *
from typing import Any, Callable, Iterable, Tuple


class AtomicBoolean(Serializable):
    """
    A `boolean` value that may be updated atomically. See the
    VarHandle specification for descriptions of the properties
    of atomic accesses. An `AtomicBoolean` is used in
    applications such as atomically updated flags, and cannot be used
    as a replacement for a java.lang.Boolean.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self, initialValue: bool):
        """
        Creates a new `AtomicBoolean` with the given initial value.

        Arguments
        - initialValue: the initial value
        """
        ...


    def __init__(self):
        """
        Creates a new `AtomicBoolean` with initial value `False`.
        """
        ...


    def get(self) -> bool:
        """
        Returns the current value,
        with memory effects as specified by VarHandle.getVolatile.

        Returns
        - the current value
        """
        ...


    def compareAndSet(self, expectedValue: bool, newValue: bool) -> bool:
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


    def weakCompareAndSet(self, expectedValue: bool, newValue: bool) -> bool:
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


    def weakCompareAndSetPlain(self, expectedValue: bool, newValue: bool) -> bool:
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


    def set(self, newValue: bool) -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setVolatile.

        Arguments
        - newValue: the new value
        """
        ...


    def lazySet(self, newValue: bool) -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setRelease.

        Arguments
        - newValue: the new value

        Since
        - 1.6
        """
        ...


    def getAndSet(self, newValue: bool) -> bool:
        """
        Atomically sets the value to `newValue` and returns the old value,
        with memory effects as specified by VarHandle.getAndSet.

        Arguments
        - newValue: the new value

        Returns
        - the previous value
        """
        ...


    def toString(self) -> str:
        """
        Returns the String representation of the current value.

        Returns
        - the String representation of the current value
        """
        ...


    def getPlain(self) -> bool:
        """
        Returns the current value, with memory semantics of reading as
        if the variable was declared non-`volatile`.

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setPlain(self, newValue: bool) -> None:
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


    def getOpaque(self) -> bool:
        """
        Returns the current value,
        with memory effects as specified by VarHandle.getOpaque.

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setOpaque(self, newValue: bool) -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setOpaque.

        Arguments
        - newValue: the new value

        Since
        - 9
        """
        ...


    def getAcquire(self) -> bool:
        """
        Returns the current value,
        with memory effects as specified by VarHandle.getAcquire.

        Returns
        - the value

        Since
        - 9
        """
        ...


    def setRelease(self, newValue: bool) -> None:
        """
        Sets the value to `newValue`,
        with memory effects as specified by VarHandle.setRelease.

        Arguments
        - newValue: the new value

        Since
        - 9
        """
        ...


    def compareAndExchange(self, expectedValue: bool, newValue: bool) -> bool:
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


    def compareAndExchangeAcquire(self, expectedValue: bool, newValue: bool) -> bool:
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


    def compareAndExchangeRelease(self, expectedValue: bool, newValue: bool) -> bool:
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


    def weakCompareAndSetVolatile(self, expectedValue: bool, newValue: bool) -> bool:
        """
        Possibly atomically sets the value to `newValue` if the current
        value `== expectedValue`,
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


    def weakCompareAndSetAcquire(self, expectedValue: bool, newValue: bool) -> bool:
        """
        Possibly atomically sets the value to `newValue` if the current
        value `== expectedValue`,
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


    def weakCompareAndSetRelease(self, expectedValue: bool, newValue: bool) -> bool:
        """
        Possibly atomically sets the value to `newValue` if the current
        value `== expectedValue`,
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
