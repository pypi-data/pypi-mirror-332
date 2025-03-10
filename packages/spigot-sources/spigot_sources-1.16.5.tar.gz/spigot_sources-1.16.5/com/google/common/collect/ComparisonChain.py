"""
Python module generated from Java source file com.google.common.collect.ComparisonChain

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.common.primitives import Booleans
from com.google.common.primitives import Ints
from com.google.common.primitives import Longs
from java.util import Comparator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ComparisonChain:
    """
    A utility for performing a chained comparison statement. For example:
    ```   `public int compareTo(Foo that) {
        return ComparisonChain.start()
            .compare(this.aString, that.aString)
            .compare(this.anInt, that.anInt)
            .compare(this.anEnum, that.anEnum, Ordering.natural().nullsLast())
            .result();`}```
    
    The value of this expression will have the same sign as the *first
    nonzero* comparison result in the chain, or will be zero if every
    comparison result was zero.
    
    **Note:** `ComparisonChain` instances are **immutable**. For
    this utility to work correctly, calls must be chained as illustrated above.
    
    Performance note: Even though the `ComparisonChain` caller always
    invokes its `compare` methods unconditionally, the `ComparisonChain` implementation stops calling its inputs' Comparable.compareTo compareTo and Comparator.compare compare
    methods as soon as one of them returns a nonzero result. This optimization is
    typically important only in the presence of expensive `compareTo` and
    `compare` implementations.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/CommonObjectUtilitiesExplained#comparecompareto">
    `ComparisonChain`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    @staticmethod
    def start() -> "ComparisonChain":
        """
        Begins a new chained comparison statement. See example in the class
        documentation.
        """
        ...


    def compare(self, left: "Comparable"[Any], right: "Comparable"[Any]) -> "ComparisonChain":
        """
        Compares two comparable objects as specified by Comparable.compareTo, *if* the result of this comparison chain
        has not already been determined.
        """
        ...


    def compare(self, left: "T", right: "T", comparator: "Comparator"["T"]) -> "ComparisonChain":
        """
        Compares two objects using a comparator, *if* the result of this
        comparison chain has not already been determined.
        """
        ...


    def compare(self, left: int, right: int) -> "ComparisonChain":
        """
        Compares two `int` values as specified by Ints.compare,
        *if* the result of this comparison chain has not already been
        determined.
        """
        ...


    def compare(self, left: int, right: int) -> "ComparisonChain":
        """
        Compares two `long` values as specified by Longs.compare,
        *if* the result of this comparison chain has not already been
        determined.
        """
        ...


    def compare(self, left: float, right: float) -> "ComparisonChain":
        """
        Compares two `float` values as specified by Float.compare, *if* the result of this comparison chain has not
        already been determined.
        """
        ...


    def compare(self, left: float, right: float) -> "ComparisonChain":
        """
        Compares two `double` values as specified by Double.compare, *if* the result of this comparison chain has not
        already been determined.
        """
        ...


    def compare(self, left: "Boolean", right: "Boolean") -> "ComparisonChain":
        """
        Discouraged synonym for .compareFalseFirst.

        Since
        - 19.0

        Deprecated
        - Use .compareFalseFirst; or, if the parameters passed
            are being either negated or reversed, undo the negation or reversal and
            use .compareTrueFirst.
        """
        ...


    def compareTrueFirst(self, left: bool, right: bool) -> "ComparisonChain":
        """
        Compares two `boolean` values, considering `True` to be less
        than `False`, *if* the result of this comparison chain has not
        already been determined.

        Since
        - 12.0
        """
        ...


    def compareFalseFirst(self, left: bool, right: bool) -> "ComparisonChain":
        """
        Compares two `boolean` values, considering `False` to be less
        than `True`, *if* the result of this comparison chain has not
        already been determined.

        Since
        - 12.0 (present as `compare` since 2.0)
        """
        ...


    def result(self) -> int:
        """
        Ends this comparison chain and returns its result: a value having the
        same sign as the first nonzero comparison result in the chain, or zero if
        every result was zero.
        """
        ...
