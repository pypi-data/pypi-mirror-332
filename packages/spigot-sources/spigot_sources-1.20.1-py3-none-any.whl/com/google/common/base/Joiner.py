"""
Python module generated from Java source file com.google.common.base.Joiner

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from java.util import AbstractList
from java.util import Arrays
from java.util import Iterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Joiner:
    """
    An object which joins pieces of text (specified as an array, Iterable, varargs or even a
    Map) with a separator. It either appends the results to an Appendable or returns
    them as a String. Example:
    
    ````Joiner joiner = Joiner.on("; ").skipNulls();
     . . .
    return joiner.join("Harry", null, "Ron", "Hermione");````
    
    This returns the string `"Harry; Ron; Hermione"`. Note that all input elements are
    converted to strings using Object.toString() before being appended.
    
    If neither .skipNulls() nor .useForNull(String) is specified, the joining
    methods will throw NullPointerException if any given element is null.
    
    **Warning: joiner instances are always immutable**; a configuration method such as `useForNull` has no effect on the instance it is invoked on! You must store and use the new joiner
    instance returned by the method. This makes joiners thread-safe, and safe to store as `static final` constants.
    
    ````// Bad! Do not do this!
    Joiner joiner = Joiner.on(',');
    joiner.skipNulls(); // does nothing!
    return joiner.join("wrong", null, "wrong");````
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/StringsExplained#joiner">`Joiner`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    @staticmethod
    def on(separator: str) -> "Joiner":
        """
        Returns a joiner which automatically places `separator` between consecutive elements.
        """
        ...


    @staticmethod
    def on(separator: str) -> "Joiner":
        """
        Returns a joiner which automatically places `separator` between consecutive elements.
        """
        ...


    def appendTo(self, appendable: "A", parts: Iterable["Object"]) -> "A":
        """
        Appends the string representation of each of `parts`, using the previously configured
        separator between each, to `appendable`.
        """
        ...


    def appendTo(self, appendable: "A", parts: Iterator["Object"]) -> "A":
        """
        Appends the string representation of each of `parts`, using the previously configured
        separator between each, to `appendable`.

        Since
        - 11.0
        """
        ...


    def appendTo(self, appendable: "A", parts: list["Object"]) -> "A":
        """
        Appends the string representation of each of `parts`, using the previously configured
        separator between each, to `appendable`.
        """
        ...


    def appendTo(self, appendable: "A", first: "Object", second: "Object", *rest: Tuple["Object", ...]) -> "A":
        """
        Appends to `appendable` the string representation of each of the remaining arguments.
        """
        ...


    def appendTo(self, builder: "StringBuilder", parts: Iterable["Object"]) -> "StringBuilder":
        """
        Appends the string representation of each of `parts`, using the previously configured
        separator between each, to `builder`. Identical to .appendTo(Appendable,
        Iterable), except that it does not throw IOException.
        """
        ...


    def appendTo(self, builder: "StringBuilder", parts: Iterator["Object"]) -> "StringBuilder":
        """
        Appends the string representation of each of `parts`, using the previously configured
        separator between each, to `builder`. Identical to .appendTo(Appendable,
        Iterable), except that it does not throw IOException.

        Since
        - 11.0
        """
        ...


    def appendTo(self, builder: "StringBuilder", parts: list["Object"]) -> "StringBuilder":
        """
        Appends the string representation of each of `parts`, using the previously configured
        separator between each, to `builder`. Identical to .appendTo(Appendable,
        Iterable), except that it does not throw IOException.
        """
        ...


    def appendTo(self, builder: "StringBuilder", first: "Object", second: "Object", *rest: Tuple["Object", ...]) -> "StringBuilder":
        """
        Appends to `builder` the string representation of each of the remaining arguments.
        Identical to .appendTo(Appendable, Object, Object, Object...), except that it does not
        throw IOException.
        """
        ...


    def join(self, parts: Iterable["Object"]) -> str:
        """
        Returns a string containing the string representation of each of `parts`, using the
        previously configured separator between each.
        """
        ...


    def join(self, parts: Iterator["Object"]) -> str:
        """
        Returns a string containing the string representation of each of `parts`, using the
        previously configured separator between each.

        Since
        - 11.0
        """
        ...


    def join(self, parts: list["Object"]) -> str:
        """
        Returns a string containing the string representation of each of `parts`, using the
        previously configured separator between each.
        """
        ...


    def join(self, first: "Object", second: "Object", *rest: Tuple["Object", ...]) -> str:
        """
        Returns a string containing the string representation of each argument, using the previously
        configured separator between each.
        """
        ...


    def useForNull(self, nullText: str) -> "Joiner":
        """
        Returns a joiner with the same behavior as this one, except automatically substituting `nullText` for any provided null elements.
        """
        ...


    def skipNulls(self) -> "Joiner":
        """
        Returns a joiner with the same behavior as this joiner, except automatically skipping over any
        provided null elements.
        """
        ...


    def withKeyValueSeparator(self, keyValueSeparator: str) -> "MapJoiner":
        """
        Returns a `MapJoiner` using the given key-value separator, and the same configuration as
        this `Joiner` otherwise.

        Since
        - 20.0
        """
        ...


    def withKeyValueSeparator(self, keyValueSeparator: str) -> "MapJoiner":
        """
        Returns a `MapJoiner` using the given key-value separator, and the same configuration as
        this `Joiner` otherwise.
        """
        ...


    class MapJoiner:
        """
        An object that joins map entries in the same manner as `Joiner` joins iterables and
        arrays. Like `Joiner`, it is thread-safe and immutable.
        
        In addition to operating on `Map` instances, `MapJoiner` can operate on `Multimap` entries in two distinct modes:
        
        
          - To output a separate entry for each key-value pair, pass `multimap.entries()` to a
              `MapJoiner` method that accepts entries as input, and receive output of the form
              `key1=A&key1=B&key2=C`.
          - To output a single entry for each key, pass `multimap.asMap()` to a `MapJoiner` method that accepts a map as input, and receive output of the form `key1=[A, B]&key2=C`.

        Since
        - 2.0
        """

        def appendTo(self, appendable: "A", map: dict[Any, Any]) -> "A":
            """
            Appends the string representation of each entry of `map`, using the previously
            configured separator and key-value separator, to `appendable`.
            """
            ...


        def appendTo(self, builder: "StringBuilder", map: dict[Any, Any]) -> "StringBuilder":
            """
            Appends the string representation of each entry of `map`, using the previously
            configured separator and key-value separator, to `builder`. Identical to .appendTo(Appendable, Map), except that it does not throw IOException.
            """
            ...


        def appendTo(self, appendable: "A", entries: Iterable["Entry"[Any, Any]]) -> "A":
            """
            Appends the string representation of each entry in `entries`, using the previously
            configured separator and key-value separator, to `appendable`.

            Since
            - 10.0
            """
            ...


        def appendTo(self, appendable: "A", parts: Iterator["Entry"[Any, Any]]) -> "A":
            """
            Appends the string representation of each entry in `entries`, using the previously
            configured separator and key-value separator, to `appendable`.

            Since
            - 11.0
            """
            ...


        def appendTo(self, builder: "StringBuilder", entries: Iterable["Entry"[Any, Any]]) -> "StringBuilder":
            """
            Appends the string representation of each entry in `entries`, using the previously
            configured separator and key-value separator, to `builder`. Identical to .appendTo(Appendable, Iterable), except that it does not throw IOException.

            Since
            - 10.0
            """
            ...


        def appendTo(self, builder: "StringBuilder", entries: Iterator["Entry"[Any, Any]]) -> "StringBuilder":
            """
            Appends the string representation of each entry in `entries`, using the previously
            configured separator and key-value separator, to `builder`. Identical to .appendTo(Appendable, Iterable), except that it does not throw IOException.

            Since
            - 11.0
            """
            ...


        def join(self, map: dict[Any, Any]) -> str:
            """
            Returns a string containing the string representation of each entry of `map`, using the
            previously configured separator and key-value separator.
            """
            ...


        def join(self, entries: Iterable["Entry"[Any, Any]]) -> str:
            """
            Returns a string containing the string representation of each entry in `entries`, using
            the previously configured separator and key-value separator.

            Since
            - 10.0
            """
            ...


        def join(self, entries: Iterator["Entry"[Any, Any]]) -> str:
            """
            Returns a string containing the string representation of each entry in `entries`, using
            the previously configured separator and key-value separator.

            Since
            - 11.0
            """
            ...


        def useForNull(self, nullText: str) -> "MapJoiner":
            """
            Returns a map joiner with the same behavior as this one, except automatically substituting
            `nullText` for any provided null keys or values.
            """
            ...
