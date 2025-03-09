"""
Python module generated from Java source file com.google.common.collect.ComparisonChain

Java source file obtained from artifact guava version 32.1.2-jre

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
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ComparisonChain:
    """
    A utility for performing a chained comparison statement. **Note:** Java 8+ users should
    generally prefer the methods in Comparator; see <a href="#java8">below</a>.
    
    Example usage of `ComparisonChain`:
    
    ````public int compareTo(Foo that) {
      return ComparisonChain.start()
          .compare(this.aString, that.aString)
          .compare(this.anInt, that.anInt)
          .compare(this.anEnum, that.anEnum, Ordering.natural().nullsLast())
          .result();`
    }```
    
    The value of this expression will have the same sign as the *first nonzero* comparison
    result in the chain, or will be zero if every comparison result was zero.
    
    **Note:** `ComparisonChain` instances are **immutable**. For this utility to work
    correctly, calls must be chained as illustrated above.
    
    Performance note: Even though the `ComparisonChain` caller always invokes its `compare` methods unconditionally, the `ComparisonChain` implementation stops calling its
    inputs' Comparable.compareTo compareTo and Comparator.compare compare methods as
    soon as one of them returns a nonzero result. This optimization is typically important only in
    the presence of expensive `compareTo` and `compare` implementations.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/CommonObjectUtilitiesExplained#comparecompareto">`ComparisonChain`</a>.
    
    <h4 id="java8">Java 8+ equivalents</h4>
    
    If you are using Java version 8 or greater, you should generally use the static methods in Comparator instead of `ComparisonChain`. The example above can be implemented like this:
    
    ````import static java.util.Comparator.comparing;
    import static java.util.Comparator.nullsLast;
    import static java.util.Comparator.naturalOrder;
    
    ...
      private static final Comparator<Foo> COMPARATOR =
          comparing((Foo foo) -> foo.aString)
              .thenComparing(foo -> foo.anInt)
              .thenComparing(foo -> foo.anEnum, nullsLast(naturalOrder()));`
    
      `@Override``public int compareTo(Foo that) {
        return COMPARATOR.compare(this, that);`
    }```
    
    With method references it is more succinct: `comparing(Foo::aString)` for example.
    
    Using Comparator avoids certain types of bugs, for example when you meant to write
    `.compare(a.foo, b.foo)` but you actually wrote `.compare(a.foo, a.foo)` or `.compare(a.foo, b.bar)`. `ComparisonChain` also has a potential performance problem that
    `Comparator` doesn't: it evaluates all the parameters of all the `.compare` calls,
    even when the result of the comparison is already known from previous `.compare` calls.
    That can be expensive.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    @staticmethod
    def start() -> "ComparisonChain":
        """
        Begins a new chained comparison statement. See example in the class documentation.
        """
        ...


    def compare(self, left: "Comparable"[Any], right: "Comparable"[Any]) -> "ComparisonChain":
        """
        Compares two comparable objects as specified by Comparable.compareTo, *if* the
        result of this comparison chain has not already been determined.
        
        This method is declared to accept any 2 `Comparable` objects, even if they are not <a
        href="https://docs.oracle.com/javase/tutorial/collections/interfaces/order.html">mutually
        comparable</a>. If you pass objects that are not mutually comparable, this method may throw an
        exception. (The reason for this decision is lost to time, but the reason *might* be that
        we wanted to support legacy classes that implement the raw type `Comparable` (instead of
        implementing `Comparable<Foo>`) without producing warnings. If so, we would prefer today
        to produce warnings in that case, and we may change this method to do so in the future. Support
        for raw `Comparable` types in Guava in general is tracked as <a
        href="https://github.com/google/guava/issues/989">#989</a>.)

        Raises
        - ClassCastException: if the parameters are not mutually comparable
        """
        ...


    def compare(self, left: "T", right: "T", comparator: "Comparator"["T"]) -> "ComparisonChain":
        """
        Compares two objects using a comparator, *if* the result of this comparison chain has not
        already been determined.
        """
        ...


    def compare(self, left: int, right: int) -> "ComparisonChain":
        """
        Compares two `int` values as specified by Ints.compare, *if* the result of
        this comparison chain has not already been determined.
        """
        ...


    def compare(self, left: int, right: int) -> "ComparisonChain":
        """
        Compares two `long` values as specified by Longs.compare, *if* the result of
        this comparison chain has not already been determined.
        """
        ...


    def compare(self, left: float, right: float) -> "ComparisonChain":
        """
        Compares two `float` values as specified by Float.compare, *if* the result
        of this comparison chain has not already been determined.
        """
        ...


    def compare(self, left: float, right: float) -> "ComparisonChain":
        """
        Compares two `double` values as specified by Double.compare, *if* the result
        of this comparison chain has not already been determined.
        """
        ...


    def compare(self, left: "Boolean", right: "Boolean") -> "ComparisonChain":
        """
        Discouraged synonym for .compareFalseFirst.

        Since
        - 19.0

        Deprecated
        - Use .compareFalseFirst; or, if the parameters passed are being either
            negated or reversed, undo the negation or reversal and use .compareTrueFirst.
        """
        ...


    def compareTrueFirst(self, left: bool, right: bool) -> "ComparisonChain":
        """
        Compares two `boolean` values, considering `True` to be less than `False`,
        *if* the result of this comparison chain has not already been determined.
        
        Java 8+ users: you can get the equivalent from Booleans.TrueFirst(). For example:
        
        ```
        Comparator.comparing(Foo::isBar, Booleans.TrueFirst())
        ```

        Since
        - 12.0
        """
        ...


    def compareFalseFirst(self, left: bool, right: bool) -> "ComparisonChain":
        """
        Compares two `boolean` values, considering `False` to be less than `True`,
        *if* the result of this comparison chain has not already been determined.
        
        Java 8+ users: you can get the equivalent from Booleans.FalseFirst(). For example:
        
        ```
        Comparator.comparing(Foo::isBar, Booleans.FalseFirst())
        ```

        Since
        - 12.0 (present as `compare` since 2.0)
        """
        ...


    def result(self) -> int:
        """
        Ends this comparison chain and returns its result: a value having the same sign as the first
        nonzero comparison result in the chain, or zero if every result was zero.
        """
        ...
