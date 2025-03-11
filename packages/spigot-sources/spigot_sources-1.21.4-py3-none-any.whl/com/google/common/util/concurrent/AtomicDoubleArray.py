"""
Python module generated from Java source file com.google.common.util.concurrent.AtomicDoubleArray

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.primitives import ImmutableLongArray
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util.concurrent.atomic import AtomicLongArray
from java.util.function import DoubleBinaryOperator
from java.util.function import DoubleUnaryOperator
from typing import Any, Callable, Iterable, Tuple


class AtomicDoubleArray(Serializable):
    """
    A `double` array in which elements may be updated atomically. See the java.util.concurrent.atomic package specification for description of the properties of atomic
    variables.
    
    <a id="bitEquals"></a>This class compares primitive `double` values in methods such as
    .compareAndSet by comparing their bitwise representation using Double.doubleToRawLongBits, which differs from both the primitive double `==` operator and
    from Double.equals, as if implemented by:
    
    ````static boolean bitEquals(double x, double y) {
      long xBits = Double.doubleToRawLongBits(x);
      long yBits = Double.doubleToRawLongBits(y);
      return xBits == yBits;`
    }```

    Author(s)
    - Martin Buchholz

    Since
    - 11.0
    """

    def __init__(self, length: int):
        """
        Creates a new `AtomicDoubleArray` of the given length, with all elements initially zero.

        Arguments
        - length: the length of the array
        """
        ...


    def __init__(self, array: list[float]):
        """
        Creates a new `AtomicDoubleArray` with the same length as, and all elements copied from,
        the given array.

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


    def get(self, i: int) -> float:
        """
        Gets the current value at position `i`.

        Arguments
        - i: the index

        Returns
        - the current value
        """
        ...


    def set(self, i: int, newValue: float) -> None:
        """
        Atomically sets the element at position `i` to the given value.

        Arguments
        - i: the index
        - newValue: the new value
        """
        ...


    def lazySet(self, i: int, newValue: float) -> None:
        """
        Eventually sets the element at position `i` to the given value.

        Arguments
        - i: the index
        - newValue: the new value
        """
        ...


    def getAndSet(self, i: int, newValue: float) -> float:
        """
        Atomically sets the element at position `i` to the given value and returns the old value.

        Arguments
        - i: the index
        - newValue: the new value

        Returns
        - the previous value
        """
        ...


    def compareAndSet(self, i: int, expect: float, update: float) -> bool:
        """
        Atomically sets the element at position `i` to the given updated value if the current
        value is <a href="#bitEquals">bitwise equal</a> to the expected value.

        Arguments
        - i: the index
        - expect: the expected value
        - update: the new value

        Returns
        - True if successful. False return indicates that the actual value was not equal to the
            expected value.
        """
        ...


    def weakCompareAndSet(self, i: int, expect: float, update: float) -> bool:
        """
        Atomically sets the element at position `i` to the given updated value if the current
        value is <a href="#bitEquals">bitwise equal</a> to the expected value.
        
        May <a
        href="http://download.oracle.com/javase/7/docs/api/java/util/concurrent/atomic/package-summary.html#Spurious">
        fail spuriously</a> and does not provide ordering guarantees, so is only rarely an appropriate
        alternative to `compareAndSet`.

        Arguments
        - i: the index
        - expect: the expected value
        - update: the new value

        Returns
        - True if successful
        """
        ...


    def getAndAdd(self, i: int, delta: float) -> float:
        """
        Atomically adds the given value to the element at index `i`.

        Arguments
        - i: the index
        - delta: the value to add

        Returns
        - the previous value
        """
        ...


    def addAndGet(self, i: int, delta: float) -> float:
        """
        Atomically adds the given value to the element at index `i`.

        Arguments
        - i: the index
        - delta: the value to add

        Returns
        - the updated value
        """
        ...


    def getAndAccumulate(self, i: int, x: float, accumulatorFunction: "DoubleBinaryOperator") -> float:
        """
        Atomically updates the element at index `i` with the results of applying the given
        function to the current and given values.

        Arguments
        - i: the index to update
        - x: the update value
        - accumulatorFunction: the accumulator function

        Returns
        - the previous value

        Since
        - 31.1
        """
        ...


    def accumulateAndGet(self, i: int, x: float, accumulatorFunction: "DoubleBinaryOperator") -> float:
        """
        Atomically updates the element at index `i` with the results of applying the given
        function to the current and given values.

        Arguments
        - i: the index to update
        - x: the update value
        - accumulatorFunction: the accumulator function

        Returns
        - the updated value

        Since
        - 31.1
        """
        ...


    def getAndUpdate(self, i: int, updaterFunction: "DoubleUnaryOperator") -> float:
        """
        Atomically updates the element at index `i` with the results of applying the given
        function to the current value.

        Arguments
        - i: the index to update
        - updaterFunction: the update function

        Returns
        - the previous value

        Since
        - 31.1
        """
        ...


    def updateAndGet(self, i: int, updaterFunction: "DoubleUnaryOperator") -> float:
        """
        Atomically updates the element at index `i` with the results of applying the given
        function to the current value.

        Arguments
        - i: the index to update
        - updaterFunction: the update function

        Returns
        - the updated value

        Since
        - 31.1
        """
        ...


    def toString(self) -> str:
        """
        Returns the String representation of the current values of array.

        Returns
        - the String representation of the current values of array
        """
        ...
