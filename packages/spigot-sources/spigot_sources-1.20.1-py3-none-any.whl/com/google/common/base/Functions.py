"""
Python module generated from Java source file com.google.common.base.Functions

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from java.io import Serializable
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Functions:
    """
    Static utility methods pertaining to `com.google.common.base.Function` instances; see that
    class for information about migrating to `java.util.function`.
    
    All methods return serializable functions as long as they're given serializable parameters.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/FunctionalExplained">the use of `Function`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def toStringFunction() -> "Function"["Object", str]:
        """
        A function equivalent to the method reference `Object::toString`, for users not yet using
        Java 8. The function simply invokes `toString` on its argument and returns the result. It
        throws a NullPointerException on null input.
        
        **Warning:** The returned function may not be *consistent with equals* (as
        documented at Function.apply). For example, this function yields different results for
        the two equal instances `ImmutableSet.of(1, 2)` and `ImmutableSet.of(2, 1)`.
        
        **Warning:** as with all function types in this package, avoid depending on the specific
        `equals`, `hashCode` or `toString` behavior of the returned function. A
        future migration to `java.util.function` will not preserve this behavior.
        
        **For Java 8 users:** use the method reference `Object::toString` instead. In the
        future, when this class requires Java 8, this method will be deprecated. See Function
        for more important information about the Java 8 transition.
        """
        ...


    @staticmethod
    def identity() -> "Function"["E", "E"]:
        ...


    @staticmethod
    def forMap(map: dict["K", "V"]) -> "Function"["K", "V"]:
        """
        Returns a function which performs a map lookup. The returned function throws an IllegalArgumentException if given a key that does not exist in the map. See also .forMap(Map, Object), which returns a default value in this case.
        
        Note: if `map` is a com.google.common.collect.BiMap BiMap (or can be one), you
        can use com.google.common.collect.Maps.asConverter Maps.asConverter instead to get a
        function that also supports reverse conversion.
        
        **Java 8 users:** if you are okay with `null` being returned for an unrecognized
        key (instead of an exception being thrown), you can use the method reference `map::get`
        instead.
        """
        ...


    @staticmethod
    def forMap(map: dict["K", "V"], defaultValue: "V") -> "Function"["K", "V"]:
        """
        Returns a function which performs a map lookup with a default value. The function created by
        this method returns `defaultValue` for all inputs that do not belong to the map's key
        set. See also .forMap(Map), which throws an exception in this case.
        
        **Java 8 users:** you can just write the lambda expression `k ->
        map.getOrDefault(k, defaultValue)` instead.

        Arguments
        - map: source map that determines the function behavior
        - defaultValue: the value to return for inputs that aren't map keys

        Returns
        - function that returns `map.get(a)` when `a` is a key, or `defaultValue` otherwise
        """
        ...


    @staticmethod
    def compose(g: "Function"["B", "C"], f: "Function"["A", "B"]) -> "Function"["A", "C"]:
        """
        Returns the composition of two functions. For `f: A->B` and `g: B->C`, composition
        is defined as the function h such that `h(a) == g(f(a))` for each `a`.
        
        **Java 8 users:** use `g.compose(f)` or (probably clearer) `f.andThen(g)`
        instead.

        Arguments
        - g: the second function to apply
        - f: the first function to apply

        Returns
        - the composition of `f` and `g`

        See
        - <a href="//en.wikipedia.org/wiki/Function_composition">function composition</a>
        """
        ...


    @staticmethod
    def forPredicate(predicate: "Predicate"["T"]) -> "Function"["T", "Boolean"]:
        """
        Creates a function that returns the same boolean output as the given predicate for all inputs.
        
        The returned function is *consistent with equals* (as documented at Function.apply) if and only if `predicate` is itself consistent with equals.
        
        **Java 8 users:** use the method reference `predicate::test` instead.
        """
        ...


    @staticmethod
    def constant(value: "E") -> "Function"["Object", "E"]:
        """
        Returns a function that ignores its input and always returns `value`.
        
        **Java 8 users:** use the lambda expression `o -> value` instead.

        Arguments
        - value: the constant value for the function to return

        Returns
        - a function that always returns `value`
        """
        ...


    @staticmethod
    def forSupplier(supplier: "Supplier"["T"]) -> "Function"["F", "T"]:
        """
        Returns a function that ignores its input and returns the result of `supplier.get()`.
        
        **Java 8 users:** use the lambda expression `o -> supplier.get()` instead.

        Since
        - 10.0
        """
        ...
