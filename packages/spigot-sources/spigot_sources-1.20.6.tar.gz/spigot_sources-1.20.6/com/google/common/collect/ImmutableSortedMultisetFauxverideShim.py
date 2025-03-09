"""
Python module generated from Java source file com.google.common.collect.ImmutableSortedMultisetFauxverideShim

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotCall
from java.util.function import Function
from java.util.function import ToIntFunction
from java.util.stream import Collector
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableSortedMultisetFauxverideShim(ImmutableMultiset):
    """
    "Overrides" the ImmutableMultiset static methods that lack ImmutableSortedMultiset equivalents with deprecated, exception-throwing versions. This prevents
    accidents like the following:
    
    ````List<Object> objects = ...;
    // Sort them:
    Set<Object> sorted = ImmutableSortedMultiset.copyOf(objects);
    // BAD CODE! The returned multiset is actually an unsorted ImmutableMultiset!````
    
    While we could put the overrides in ImmutableSortedMultiset itself, it seems clearer
    to separate these "do not call" methods from those intended for normal use.

    Author(s)
    - Louis Wasserman
    """

    @staticmethod
    def toImmutableMultiset() -> "Collector"["E", Any, "ImmutableMultiset"["E"]]:
        """
        Not supported. Use ImmutableSortedMultiset.toImmutableSortedMultiset instead. This
        method exists only to hide ImmutableMultiset.toImmutableMultiset from consumers of
        `ImmutableSortedMultiset`.

        Raises
        - UnsupportedOperationException: always

        Since
        - 21.0

        Deprecated
        - Use ImmutableSortedMultiset.toImmutableSortedMultiset.
        """
        ...


    @staticmethod
    def toImmutableMultiset(elementFunction: "Function"["T", "E"], countFunction: "ToIntFunction"["T"]) -> "Collector"["T", Any, "ImmutableMultiset"["E"]]:
        """
        Not supported. Use ImmutableSortedMultiset.toImmutableSortedMultiset instead. This
        method exists only to hide ImmutableMultiset.toImmutableMultiset from consumers of
        `ImmutableSortedMultiset`.

        Raises
        - UnsupportedOperationException: always

        Since
        - 22.0

        Deprecated
        - Use ImmutableSortedMultiset.toImmutableSortedMultiset.
        """
        ...


    @staticmethod
    def builder() -> "ImmutableSortedMultiset.Builder"["E"]:
        """
        Not supported. Use ImmutableSortedMultiset.naturalOrder, which offers better
        type-safety, instead. This method exists only to hide ImmutableMultiset.builder from
        consumers of `ImmutableSortedMultiset`.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Use ImmutableSortedMultiset.naturalOrder, which offers better type-safety.
        """
        ...


    @staticmethod
    def of(element: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Not supported. **You are attempting to create a multiset that may contain a non-`Comparable` element.** Proper calls will resolve to the version in `ImmutableSortedMultiset`, not this dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass a parameter of type `Comparable` to use ImmutableSortedMultiset.of(Comparable).**
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Not supported. **You are attempting to create a multiset that may contain a non-`Comparable` element.** Proper calls will resolve to the version in `ImmutableSortedMultiset`, not this dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedMultiset.of(Comparable, Comparable).**
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Not supported. **You are attempting to create a multiset that may contain a non-`Comparable` element.** Proper calls will resolve to the version in `ImmutableSortedMultiset`, not this dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedMultiset.of(Comparable, Comparable, Comparable).**
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Not supported. **You are attempting to create a multiset that may contain a non-`Comparable` element.** Proper calls will resolve to the version in `ImmutableSortedMultiset`, not this dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedMultiset.of(Comparable, Comparable, Comparable, Comparable). **
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E") -> "ImmutableSortedMultiset"["E"]:
        """
        Not supported. **You are attempting to create a multiset that may contain a non-`Comparable` element.** Proper calls will resolve to the version in `ImmutableSortedMultiset`, not this dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedMultiset.of(Comparable, Comparable, Comparable, Comparable, Comparable) .
            **
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", *remaining: Tuple["E", ...]) -> "ImmutableSortedMultiset"["E"]:
        """
        Not supported. **You are attempting to create a multiset that may contain a non-`Comparable` element.** Proper calls will resolve to the version in `ImmutableSortedMultiset`, not this dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass the parameters of type `Comparable` to use ImmutableSortedMultiset.of(Comparable, Comparable, Comparable, Comparable, Comparable,
            Comparable, Comparable...) . **
        """
        ...


    @staticmethod
    def copyOf(elements: list["E"]) -> "ImmutableSortedMultiset"["E"]:
        """
        Not supported. **You are attempting to create a multiset that may contain non-`Comparable` elements.** Proper calls will resolve to the version in `ImmutableSortedMultiset`, not this dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass parameters of type `Comparable` to use ImmutableSortedMultiset.copyOf(Comparable[]).**
        """
        ...
