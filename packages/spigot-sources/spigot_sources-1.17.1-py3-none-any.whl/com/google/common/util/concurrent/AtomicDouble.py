"""
Python module generated from Java source file com.google.common.util.concurrent.AtomicDouble

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent.atomic import AtomicLongFieldUpdater
from typing import Any, Callable, Iterable, Tuple


class AtomicDouble(Number, Serializable):
    """
    A `double` value that may be updated atomically. See the java.util.concurrent.atomic package specification for description of the properties of atomic
    variables. An `AtomicDouble` is used in applications such as atomic accumulation, and
    cannot be used as a replacement for a Double. However, this class does extend `Number` to allow uniform access by tools and utilities that deal with numerically-based classes.
    
    <a name="bitEquals"></a>This class compares primitive `double` values in methods such as
    .compareAndSet by comparing their bitwise representation using Double.doubleToRawLongBits, which differs from both the primitive double `==` operator and
    from Double.equals, as if implemented by:
    
    ````static boolean bitEquals(double x, double y) {
      long xBits = Double.doubleToRawLongBits(x);
      long yBits = Double.doubleToRawLongBits(y);
      return xBits == yBits;`
    }```
    
    It is possible to write a more scalable updater, at the cost of giving up strict atomicity.
    See for example <a
    href="http://gee.cs.oswego.edu/dl/jsr166/dist/jsr166edocs/jsr166e/DoubleAdder.html">
    DoubleAdder</a> and <a
    href="http://gee.cs.oswego.edu/dl/jsr166/dist/jsr166edocs/jsr166e/DoubleMaxUpdater.html">
    DoubleMaxUpdater</a>.

    Author(s)
    - Martin Buchholz

    Since
    - 11.0
    """

    def __init__(self, initialValue: float):
        """
        Creates a new `AtomicDouble` with the given initial value.

        Arguments
        - initialValue: the initial value
        """
        ...


    def __init__(self):
        """
        Creates a new `AtomicDouble` with initial value `0.0`.
        """
        ...


    def get(self) -> float:
        """
        Gets the current value.

        Returns
        - the current value
        """
        ...


    def set(self, newValue: float) -> None:
        """
        Sets to the given value.

        Arguments
        - newValue: the new value
        """
        ...


    def lazySet(self, newValue: float) -> None:
        """
        Eventually sets to the given value.

        Arguments
        - newValue: the new value
        """
        ...


    def getAndSet(self, newValue: float) -> float:
        """
        Atomically sets to the given value and returns the old value.

        Arguments
        - newValue: the new value

        Returns
        - the previous value
        """
        ...


    def compareAndSet(self, expect: float, update: float) -> bool:
        """
        Atomically sets the value to the given updated value
        if the current value is <a href="#bitEquals">bitwise equal</a>
        to the expected value.

        Arguments
        - expect: the expected value
        - update: the new value

        Returns
        - `True` if successful. False return indicates that
        the actual value was not bitwise equal to the expected value.
        """
        ...


    def weakCompareAndSet(self, expect: float, update: float) -> bool:
        """
        Atomically sets the value to the given updated value
        if the current value is <a href="#bitEquals">bitwise equal</a>
        to the expected value.
        
        May <a
        href="http://download.oracle.com/javase/7/docs/api/java/util/concurrent/atomic/package-summary.html#Spurious">
        fail spuriously</a>
        and does not provide ordering guarantees, so is only rarely an
        appropriate alternative to `compareAndSet`.

        Arguments
        - expect: the expected value
        - update: the new value

        Returns
        - `True` if successful
        """
        ...


    def getAndAdd(self, delta: float) -> float:
        """
        Atomically adds the given value to the current value.

        Arguments
        - delta: the value to add

        Returns
        - the previous value
        """
        ...


    def addAndGet(self, delta: float) -> float:
        """
        Atomically adds the given value to the current value.

        Arguments
        - delta: the value to add

        Returns
        - the updated value
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
        Returns the value of this `AtomicDouble` as an `int`
        after a narrowing primitive conversion.
        """
        ...


    def longValue(self) -> int:
        """
        Returns the value of this `AtomicDouble` as a `long`
        after a narrowing primitive conversion.
        """
        ...


    def floatValue(self) -> float:
        """
        Returns the value of this `AtomicDouble` as a `float`
        after a narrowing primitive conversion.
        """
        ...


    def doubleValue(self) -> float:
        """
        Returns the value of this `AtomicDouble` as a `double`.
        """
        ...
