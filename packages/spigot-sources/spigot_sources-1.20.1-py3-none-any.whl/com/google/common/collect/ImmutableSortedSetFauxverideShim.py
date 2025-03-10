"""
Python module generated from Java source file com.google.common.collect.ImmutableSortedSetFauxverideShim

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotCall
from java.util.stream import Collector
from typing import Any, Callable, Iterable, Tuple


class ImmutableSortedSetFauxverideShim(CachingAsList):
    """
    "Overrides" the ImmutableSet static methods that lack ImmutableSortedSet
    equivalents with deprecated, exception-throwing versions. This prevents accidents like the
    following:
    
    ````List<Object> objects = ...;
    // Sort them:
    Set<Object> sorted = ImmutableSortedSet.copyOf(objects);
    // BAD CODE! The returned set is actually an unsorted ImmutableSet!````
    
    While we could put the overrides in ImmutableSortedSet itself, it seems clearer to
    separate these "do not call" methods from those intended for normal use.

    Author(s)
    - Chris Povirk
    """

    @staticmethod
    def toImmutableSet() -> "Collector"["E", Any, "ImmutableSet"["E"]]:
        """
        Not supported. Use ImmutableSortedSet.toImmutableSortedSet instead. This method exists
        only to hide ImmutableSet.toImmutableSet from consumers of `ImmutableSortedSet`.

        Raises
        - UnsupportedOperationException: always

        Since
        - 21.0

        Deprecated
        - Use ImmutableSortedSet.toImmutableSortedSet.
        """
        ...


    @staticmethod
    def builder() -> "ImmutableSortedSet.Builder"["E"]:
        """
        Not supported. Use ImmutableSortedSet.naturalOrder, which offers better type-safety,
        instead. This method exists only to hide ImmutableSet.builder from consumers of `ImmutableSortedSet`.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Use ImmutableSortedSet.naturalOrder, which offers better type-safety.
        """
        ...


    @staticmethod
    def builderWithExpectedSize(expectedSize: int) -> "ImmutableSortedSet.Builder"["E"]:
        """
        Not supported. This method exists only to hide ImmutableSet.builderWithExpectedSize
        from consumers of `ImmutableSortedSet`.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Not supported by ImmutableSortedSet.
        """
        ...


    @staticmethod
    def of(element: "E") -> "ImmutableSortedSet"["E"]:
        """
        Not supported. **You are attempting to create a set that may contain a non-`Comparable`
        element.** Proper calls will resolve to the version in `ImmutableSortedSet`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass a parameter of type `Comparable` to use ImmutableSortedSet.of(Comparable).**
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E") -> "ImmutableSortedSet"["E"]:
        """
        Not supported. **You are attempting to create a set that may contain a non-`Comparable`
        element.** Proper calls will resolve to the version in `ImmutableSortedSet`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedSet.of(Comparable, Comparable).**
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E") -> "ImmutableSortedSet"["E"]:
        """
        Not supported. **You are attempting to create a set that may contain a non-`Comparable`
        element.** Proper calls will resolve to the version in `ImmutableSortedSet`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedSet.of(Comparable, Comparable, Comparable).**
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E") -> "ImmutableSortedSet"["E"]:
        """
        Not supported. **You are attempting to create a set that may contain a non-`Comparable`
        element.** Proper calls will resolve to the version in `ImmutableSortedSet`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedSet.of(Comparable, Comparable, Comparable, Comparable). **
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E") -> "ImmutableSortedSet"["E"]:
        """
        Not supported. **You are attempting to create a set that may contain a non-`Comparable`
        element.** Proper calls will resolve to the version in `ImmutableSortedSet`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedSet.of( Comparable, Comparable, Comparable, Comparable, Comparable). **
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", *remaining: Tuple["E", ...]) -> "ImmutableSortedSet"["E"]:
        """
        Not supported. **You are attempting to create a set that may contain a non-`Comparable`
        element.** Proper calls will resolve to the version in `ImmutableSortedSet`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedSet.of(Comparable, Comparable, Comparable, Comparable, Comparable,
            Comparable, Comparable...). **
        """
        ...


    @staticmethod
    def copyOf(elements: list["E"]) -> "ImmutableSortedSet"["E"]:
        """
        Not supported. **You are attempting to create a set that may contain non-`Comparable`
        elements.** Proper calls will resolve to the version in `ImmutableSortedSet`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass parameters of type `Comparable` to use ImmutableSortedSet.copyOf(Comparable[]).**
        """
        ...
