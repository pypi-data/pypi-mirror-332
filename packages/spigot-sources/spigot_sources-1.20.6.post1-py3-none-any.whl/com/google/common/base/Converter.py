"""
Python module generated from Java source file com.google.common.base.Converter

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from com.google.errorprone.annotations import CheckReturnValue
from com.google.errorprone.annotations import ForOverride
from com.google.errorprone.annotations import InlineMe
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import RetainedWith
from java.io import Serializable
from java.util import Iterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Converter(Function):
    """
    A function from `A` to `B` with an associated *reverse* function from `B`
    to `A`; used for converting back and forth between *different representations of the same
    information*.
    
    <h3>Invertibility</h3>
    
    The reverse operation **may** be a strict *inverse* (meaning that `converter.reverse().convert(converter.convert(a)).equals(a)` is always True). However, it is very
    common (perhaps *more* common) for round-trip conversion to be *lossy*. Consider an
    example round-trip using com.google.common.primitives.Doubles.stringConverter:
    
    <ol>
      - `stringConverter().convert("1.00")` returns the `Double` value `1.0`
      - `stringConverter().reverse().convert(1.0)` returns the string `"1.0"` --
          *not* the same string (`"1.00"`) we started with
    </ol>
    
    Note that it should still be the case that the round-tripped and original objects are
    *similar*.
    
    <h3>Nullability</h3>
    
    A converter always converts `null` to `null` and non-null references to non-null
    references. It would not make sense to consider `null` and a non-null reference to be
    "different representations of the same information", since one is distinguishable from
    *missing* information and the other is not. The .convert method handles this null
    behavior for all converters; implementations of .doForward and .doBackward are
    guaranteed to never be passed `null`, and must never return `null`.
    
    <h3>Common ways to use</h3>
    
    Getting a converter:
    
    
      - Use a provided converter implementation, such as Enums.stringConverter, com.google.common.primitives.Ints.stringConverter Ints.stringConverter or the .reverse reverse views of these.
      - Convert between specific preset values using com.google.common.collect.Maps.asConverter Maps.asConverter. For example, use this to
          create a "fake" converter for a unit test. It is unnecessary (and confusing) to *mock*
          the `Converter` type using a mocking framework.
      - Extend this class and implement its .doForward and .doBackward methods.
      - **Java 8 users:** you may prefer to pass two lambda expressions or method references to
          the .from from factory method.
    
    
    Using a converter:
    
    
      - Convert one instance in the "forward" direction using `converter.convert(a)`.
      - Convert multiple instances "forward" using `converter.convertAll(as)`.
      - Convert in the "backward" direction using `converter.reverse().convert(b)` or `converter.reverse().convertAll(bs)`.
      - Use `converter` or `converter.reverse()` anywhere a java.util.function.Function is accepted (for example java.util.stream.Stream.map
          Stream.map).
      - **Do not** call .doForward or .doBackward directly; these exist only to
          be overridden.
    
    
    <h3>Example</h3>
    
    ```
      return new Converter&lt;Integer, String&gt;() {
        protected String doForward(Integer i) {
          return Integer.toHexString(i);
        }
    
        protected Integer doBackward(String s) {
          return parseUnsignedInt(s, 16);
        }
      };```
    
    An alternative using Java 8:
    
    ````return Converter.from(
        Integer::toHexString,
        s -> parseUnsignedInt(s, 16));````

    Author(s)
    - Gregory Kick

    Since
    - 16.0
    """

    def convert(self, a: "A") -> "B":
        """
        Returns a representation of `a` as an instance of type `B`.

        Returns
        - the converted value; is null *if and only if* `a` is null
        """
        ...


    def convertAll(self, fromIterable: Iterable["A"]) -> Iterable["B"]:
        ...


    def reverse(self) -> "Converter"["B", "A"]:
        """
        Returns the reversed view of this converter, which converts `this.convert(a)` back to a
        value roughly equivalent to `a`.
        
        The returned converter is serializable if `this` converter is.
        
        **Note:** you should not override this method. It is non-final for legacy reasons.
        """
        ...


    def andThen(self, secondConverter: "Converter"["B", "C"]) -> "Converter"["A", "C"]:
        """
        Returns a converter whose `convert` method applies `secondConverter` to the result
        of this converter. Its `reverse` method applies the converters in reverse order.
        
        The returned converter is serializable if `this` converter and `secondConverter`
        are.
        """
        ...


    def apply(self, a: "A") -> "B":
        """
        Deprecated
        - Provided to satisfy the `Function` interface; use .convert instead.
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Indicates whether another object is equal to this converter.
        
        Most implementations will have no reason to override the behavior of Object.equals.
        However, an implementation may also choose to return `True` whenever `object` is a
        Converter that it considers *interchangeable* with this one. "Interchangeable"
        *typically* means that `Objects.equal(this.convert(a), that.convert(a))` is True for
        all `a` of type `A` (and similarly for `reverse`). Note that a `False`
        result from this method does not imply that the converters are known *not* to be
        interchangeable.
        """
        ...


    @staticmethod
    def from(forwardFunction: "Function"["A", "B"], backwardFunction: "Function"["B", "A"]) -> "Converter"["A", "B"]:
        """
        Returns a converter based on separate forward and backward functions. This is useful if the
        function instances already exist, or so that you can supply lambda expressions. If those
        circumstances don't apply, you probably don't need to use this; subclass `Converter` and
        implement its .doForward and .doBackward methods directly.
        
        These functions will never be passed `null` and must not under any circumstances
        return `null`. If a value cannot be converted, the function should throw an unchecked
        exception (typically, but not necessarily, IllegalArgumentException).
        
        The returned converter is serializable if both provided functions are.

        Since
        - 17.0
        """
        ...


    @staticmethod
    def identity() -> "Converter"["T", "T"]:
        """
        Returns a serializable converter that always converts or reverses an object to itself.
        """
        ...
