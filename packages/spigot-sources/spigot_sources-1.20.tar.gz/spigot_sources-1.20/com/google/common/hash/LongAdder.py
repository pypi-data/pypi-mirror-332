"""
Python module generated from Java source file com.google.common.hash.LongAdder

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util.concurrent.atomic import AtomicLong
from typing import Any, Callable, Iterable, Tuple


class LongAdder(Striped64, Serializable, LongAddable):
    """
    One or more variables that together maintain an initially zero `long` sum. When updates
    (method .add) are contended across threads, the set of variables may grow dynamically to
    reduce contention. Method .sum (or, equivalently, .longValue) returns the current
    total combined across the variables maintaining the sum.
    
    This class is usually preferable to AtomicLong when multiple threads update a common
    sum that is used for purposes such as collecting statistics, not for fine-grained synchronization
    control. Under low update contention, the two classes have similar characteristics. But under
    high contention, expected throughput of this class is significantly higher, at the expense of
    higher space consumption.
    
    This class extends Number, but does *not* define methods such as `equals`, `hashCode` and `compareTo` because instances are expected to be mutated, and
    so are not useful as collection keys.
    
    *jsr166e note: This class is targeted to be placed in java.util.concurrent.atomic.*

    Author(s)
    - Doug Lea

    Since
    - 1.8
    """

    def __init__(self):
        """
        Creates a new adder with initial sum of zero.
        """
        ...


    def add(self, x: int) -> None:
        """
        Adds the given value.

        Arguments
        - x: the value to add
        """
        ...


    def increment(self) -> None:
        """
        Equivalent to `add(1)`.
        """
        ...


    def decrement(self) -> None:
        """
        Equivalent to `add(-1)`.
        """
        ...


    def sum(self) -> int:
        """
        Returns the current sum. The returned value is *NOT* an atomic snapshot; invocation in
        the absence of concurrent updates returns an accurate result, but concurrent updates that occur
        while the sum is being calculated might not be incorporated.

        Returns
        - the sum
        """
        ...


    def reset(self) -> None:
        """
        Resets variables maintaining the sum to zero. This method may be a useful alternative to
        creating a new adder, but is only effective if there are no concurrent updates. Because this
        method is intrinsically racy, it should only be used when it is known that no threads are
        concurrently updating.
        """
        ...


    def sumThenReset(self) -> int:
        """
        Equivalent in effect to .sum followed by .reset. This method may apply for
        example during quiescent points between multithreaded computations. If there are updates
        concurrent with this method, the returned value is *not* guaranteed to be the final
        value occurring before the reset.

        Returns
        - the sum
        """
        ...


    def toString(self) -> str:
        """
        Returns the String representation of the .sum.

        Returns
        - the String representation of the .sum
        """
        ...


    def longValue(self) -> int:
        """
        Equivalent to .sum.

        Returns
        - the sum
        """
        ...


    def intValue(self) -> int:
        """
        Returns the .sum as an `int` after a narrowing primitive conversion.
        """
        ...


    def floatValue(self) -> float:
        """
        Returns the .sum as a `float` after a widening primitive conversion.
        """
        ...


    def doubleValue(self) -> float:
        """
        Returns the .sum as a `double` after a widening primitive conversion.
        """
        ...
