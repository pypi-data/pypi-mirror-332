"""
Python module generated from Java source file com.google.common.base.Predicates

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import *
from java.io import Serializable
from java.util import Arrays
from java.util.regex import Pattern
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Predicates:
    """
    Static utility methods pertaining to `Predicate` instances.
    
    All methods return serializable predicates as long as they're given serializable parameters.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/FunctionalExplained">the use of `Predicate`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    @staticmethod
    def alwaysTrue() -> "Predicate"["T"]:
        """
        Returns a predicate that always evaluates to `True`.
        """
        ...


    @staticmethod
    def alwaysFalse() -> "Predicate"["T"]:
        """
        Returns a predicate that always evaluates to `False`.
        """
        ...


    @staticmethod
    def isNull() -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if the object reference being tested is
        null.
        """
        ...


    @staticmethod
    def notNull() -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if the object reference being tested is not
        null.
        """
        ...


    @staticmethod
    def not(predicate: "Predicate"["T"]) -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if the given predicate evaluates to `False`.
        """
        ...


    @staticmethod
    def and(components: Iterable["Predicate"["T"]]) -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if each of its components evaluates to
        `True`. The components are evaluated in order, and evaluation will be "short-circuited"
        as soon as a False predicate is found. It defensively copies the iterable passed in, so future
        changes to it won't alter the behavior of this predicate. If `components` is empty, the
        returned predicate will always evaluate to `True`.
        """
        ...


    @staticmethod
    def and(*components: Tuple["Predicate"["T"], ...]) -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if each of its components evaluates to
        `True`. The components are evaluated in order, and evaluation will be "short-circuited"
        as soon as a False predicate is found. It defensively copies the array passed in, so future
        changes to it won't alter the behavior of this predicate. If `components` is empty, the
        returned predicate will always evaluate to `True`.
        """
        ...


    @staticmethod
    def and(first: "Predicate"["T"], second: "Predicate"["T"]) -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if both of its components evaluate to `True`. The components are evaluated in order, and evaluation will be "short-circuited" as soon
        as a False predicate is found.
        """
        ...


    @staticmethod
    def or(components: Iterable["Predicate"["T"]]) -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if any one of its components evaluates to
        `True`. The components are evaluated in order, and evaluation will be "short-circuited"
        as soon as a True predicate is found. It defensively copies the iterable passed in, so future
        changes to it won't alter the behavior of this predicate. If `components` is empty, the
        returned predicate will always evaluate to `False`.
        """
        ...


    @staticmethod
    def or(*components: Tuple["Predicate"["T"], ...]) -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if any one of its components evaluates to
        `True`. The components are evaluated in order, and evaluation will be "short-circuited"
        as soon as a True predicate is found. It defensively copies the array passed in, so future
        changes to it won't alter the behavior of this predicate. If `components` is empty, the
        returned predicate will always evaluate to `False`.
        """
        ...


    @staticmethod
    def or(first: "Predicate"["T"], second: "Predicate"["T"]) -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if either of its components evaluates to
        `True`. The components are evaluated in order, and evaluation will be "short-circuited"
        as soon as a True predicate is found.
        """
        ...


    @staticmethod
    def equalTo(target: "T") -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if the object being tested `equals()`
        the given target or both are null.
        """
        ...


    @staticmethod
    def instanceOf(clazz: type[Any]) -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if the object being tested is an instance of
        the given class. If the object being tested is `null` this predicate evaluates to `False`.
        
        If you want to filter an `Iterable` to narrow its type, consider using com.google.common.collect.Iterables.filter(Iterable, Class) in preference.
        
        **Warning:** contrary to the typical assumptions about predicates (as documented at
        Predicate.apply), the returned predicate may not be *consistent with equals*. For
        example, `instanceOf(ArrayList.class)` will yield different results for the two equal
        instances `Lists.newArrayList(1)` and `Arrays.asList(1)`.
        """
        ...


    @staticmethod
    def subtypeOf(clazz: type[Any]) -> "Predicate"[type[Any]]:
        """
        Returns a predicate that evaluates to `True` if the class being tested is assignable to
        (is a subtype of) `clazz`. Example:
        
        ````List<Class<?>> classes = Arrays.asList(
            Object.class, String.class, Number.class, Long.class);
        return Iterables.filter(classes, subtypeOf(Number.class));````
        
        The code above returns an iterable containing `Number.class` and `Long.class`.

        Since
        - 20.0 (since 10.0 under the incorrect name `assignableFrom`)
        """
        ...


    @staticmethod
    def in(target: Iterable["T"]) -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to `True` if the object reference being tested is a
        member of the given collection. It does not defensively copy the collection passed in, so
        future changes to it will alter the behavior of the predicate.
        
        This method can technically accept any `Collection<?>`, but using a typed collection
        helps prevent bugs. This approach doesn't block any potential users since it is always possible
        to use `Predicates.<Object>in()`.

        Arguments
        - target: the collection that may contain the function input
        """
        ...


    @staticmethod
    def compose(predicate: "Predicate"["B"], function: "Function"["A", "B"]) -> "Predicate"["A"]:
        """
        Returns the composition of a function and a predicate. For every `x`, the generated
        predicate returns `predicate(function(x))`.

        Returns
        - the composition of the provided function and predicate
        """
        ...


    @staticmethod
    def containsPattern(pattern: str) -> "Predicate"["CharSequence"]:
        """
        Returns a predicate that evaluates to `True` if the `CharSequence` being tested
        contains any match for the given regular expression pattern. The test used is equivalent to
        `Pattern.compile(pattern).matcher(arg).find()`

        Raises
        - IllegalArgumentException: if the pattern is invalid

        Since
        - 3.0
        """
        ...


    @staticmethod
    def contains(pattern: "Pattern") -> "Predicate"["CharSequence"]:
        """
        Returns a predicate that evaluates to `True` if the `CharSequence` being tested
        contains any match for the given regular expression pattern. The test used is equivalent to
        `pattern.matcher(arg).find()`

        Since
        - 3.0
        """
        ...
