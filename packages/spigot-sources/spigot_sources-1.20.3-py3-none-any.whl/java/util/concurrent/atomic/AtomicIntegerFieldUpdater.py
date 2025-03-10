"""
Python module generated from Java source file java.util.concurrent.atomic.AtomicIntegerFieldUpdater

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import VarHandle
from java.lang.reflect import Field
from java.lang.reflect import Modifier
from java.security import AccessController
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.util.concurrent.atomic import *
from java.util.function import IntBinaryOperator
from java.util.function import IntUnaryOperator
from jdk.internal.misc import Unsafe
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import Reflection
from typing import Any, Callable, Iterable, Tuple


class AtomicIntegerFieldUpdater:
    """
    A reflection-based utility that enables atomic updates to
    designated `volatile int` fields of designated classes.
    This class is designed for use in atomic data structures in which
    several fields of the same node are independently subject to atomic
    updates.
    
    Note that the guarantees of the `compareAndSet`
    method in this class are weaker than in other atomic classes.
    Because this class cannot ensure that all uses of the field
    are appropriate for purposes of atomic access, it can
    guarantee atomicity only with respect to other invocations of
    `compareAndSet` and `set` on the same updater.
    
    Object arguments for parameters of type `T` that are not
    instances of the class passed to .newUpdater will result in
    a ClassCastException being thrown.
    
    Type `<T>`: The type of the object holding the updatable field

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    @staticmethod
    def newUpdater(tclass: type["U"], fieldName: str) -> "AtomicIntegerFieldUpdater"["U"]:
        """
        Creates and returns an updater for objects with the given field.
        The Class argument is needed to check that reflective types and
        generic types match.
        
        Type `<U>`: the type of instances of tclass

        Arguments
        - tclass: the class of the objects holding the field
        - fieldName: the name of the field to be updated

        Returns
        - the updater

        Raises
        - IllegalArgumentException: if the field is not a
        volatile integer type
        - RuntimeException: with a nested reflection-based
        exception if the class does not hold field or is the wrong type,
        or the field is inaccessible to the caller according to Java language
        access control
        """
        ...


    def compareAndSet(self, obj: "T", expect: int, update: int) -> bool:
        """
        Atomically sets the field of the given object managed by this updater
        to the given updated value if the current value `==` the
        expected value. This method is guaranteed to be atomic with respect to
        other calls to `compareAndSet` and `set`, but not
        necessarily with respect to other changes in the field.

        Arguments
        - obj: An object whose field to conditionally set
        - expect: the expected value
        - update: the new value

        Returns
        - `True` if successful
        """
        ...


    def weakCompareAndSet(self, obj: "T", expect: int, update: int) -> bool:
        """
        Atomically sets the field of the given object managed by this updater
        to the given updated value if the current value `==` the
        expected value. This method is guaranteed to be atomic with respect to
        other calls to `compareAndSet` and `set`, but not
        necessarily with respect to other changes in the field.
        
        This operation may fail spuriously and does not provide
        ordering guarantees, so is only rarely an appropriate
        alternative to `compareAndSet`.

        Arguments
        - obj: An object whose field to conditionally set
        - expect: the expected value
        - update: the new value

        Returns
        - `True` if successful
        """
        ...


    def set(self, obj: "T", newValue: int) -> None:
        """
        Sets the field of the given object managed by this updater to the
        given updated value. This operation is guaranteed to act as a volatile
        store with respect to subsequent invocations of `compareAndSet`.

        Arguments
        - obj: An object whose field to set
        - newValue: the new value
        """
        ...


    def lazySet(self, obj: "T", newValue: int) -> None:
        """
        Eventually sets the field of the given object managed by this
        updater to the given updated value.

        Arguments
        - obj: An object whose field to set
        - newValue: the new value

        Since
        - 1.6
        """
        ...


    def get(self, obj: "T") -> int:
        """
        Returns the current value held in the field of the given object
        managed by this updater.

        Arguments
        - obj: An object whose field to get

        Returns
        - the current value
        """
        ...


    def getAndSet(self, obj: "T", newValue: int) -> int:
        """
        Atomically sets the field of the given object managed by this updater
        to the given value and returns the old value.

        Arguments
        - obj: An object whose field to get and set
        - newValue: the new value

        Returns
        - the previous value
        """
        ...


    def getAndIncrement(self, obj: "T") -> int:
        """
        Atomically increments by one the current value of the field of the
        given object managed by this updater.

        Arguments
        - obj: An object whose field to get and set

        Returns
        - the previous value
        """
        ...


    def getAndDecrement(self, obj: "T") -> int:
        """
        Atomically decrements by one the current value of the field of the
        given object managed by this updater.

        Arguments
        - obj: An object whose field to get and set

        Returns
        - the previous value
        """
        ...


    def getAndAdd(self, obj: "T", delta: int) -> int:
        """
        Atomically adds the given value to the current value of the field of
        the given object managed by this updater.

        Arguments
        - obj: An object whose field to get and set
        - delta: the value to add

        Returns
        - the previous value
        """
        ...


    def incrementAndGet(self, obj: "T") -> int:
        """
        Atomically increments by one the current value of the field of the
        given object managed by this updater.

        Arguments
        - obj: An object whose field to get and set

        Returns
        - the updated value
        """
        ...


    def decrementAndGet(self, obj: "T") -> int:
        """
        Atomically decrements by one the current value of the field of the
        given object managed by this updater.

        Arguments
        - obj: An object whose field to get and set

        Returns
        - the updated value
        """
        ...


    def addAndGet(self, obj: "T", delta: int) -> int:
        """
        Atomically adds the given value to the current value of the field of
        the given object managed by this updater.

        Arguments
        - obj: An object whose field to get and set
        - delta: the value to add

        Returns
        - the updated value
        """
        ...


    def getAndUpdate(self, obj: "T", updateFunction: "IntUnaryOperator") -> int:
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the field of the given object managed
        by this updater with the results of applying the given
        function, returning the previous value. The function should be
        side-effect-free, since it may be re-applied when attempted
        updates fail due to contention among threads.

        Arguments
        - obj: An object whose field to get and set
        - updateFunction: a side-effect-free function

        Returns
        - the previous value

        Since
        - 1.8
        """
        ...


    def updateAndGet(self, obj: "T", updateFunction: "IntUnaryOperator") -> int:
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the field of the given object managed
        by this updater with the results of applying the given
        function, returning the updated value. The function should be
        side-effect-free, since it may be re-applied when attempted
        updates fail due to contention among threads.

        Arguments
        - obj: An object whose field to get and set
        - updateFunction: a side-effect-free function

        Returns
        - the updated value

        Since
        - 1.8
        """
        ...


    def getAndAccumulate(self, obj: "T", x: int, accumulatorFunction: "IntBinaryOperator") -> int:
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the field of the given object managed
        by this updater with the results of applying the given function
        to the current and given values, returning the previous value.
        The function should be side-effect-free, since it may be
        re-applied when attempted updates fail due to contention among
        threads.  The function is applied with the current value as its
        first argument, and the given update as the second argument.

        Arguments
        - obj: An object whose field to get and set
        - x: the update value
        - accumulatorFunction: a side-effect-free function of two arguments

        Returns
        - the previous value

        Since
        - 1.8
        """
        ...


    def accumulateAndGet(self, obj: "T", x: int, accumulatorFunction: "IntBinaryOperator") -> int:
        """
        Atomically updates (with memory effects as specified by VarHandle.compareAndSet) the field of the given object managed
        by this updater with the results of applying the given function
        to the current and given values, returning the updated value.
        The function should be side-effect-free, since it may be
        re-applied when attempted updates fail due to contention among
        threads.  The function is applied with the current value as its
        first argument, and the given update as the second argument.

        Arguments
        - obj: An object whose field to get and set
        - x: the update value
        - accumulatorFunction: a side-effect-free function of two arguments

        Returns
        - the updated value

        Since
        - 1.8
        """
        ...
