"""
Python module generated from Java source file com.google.common.collect.ImmutableSortedMapFauxverideShim

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotCall
from java.util.function import BinaryOperator
from java.util.function import Function
from java.util.stream import Collector
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableSortedMapFauxverideShim(ImmutableMap):
    """
    "Overrides" the ImmutableMap static methods that lack ImmutableSortedMap
    equivalents with deprecated, exception-throwing versions. See ImmutableSortedSetFauxverideShim for details.

    Author(s)
    - Chris Povirk
    """

    @staticmethod
    def toImmutableMap(keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"]) -> "Collector"["T", Any, "ImmutableMap"["K", "V"]]:
        """
        Not supported. Use ImmutableSortedMap.toImmutableSortedMap, which offers better
        type-safety, instead. This method exists only to hide ImmutableMap.toImmutableMap from
        consumers of `ImmutableSortedMap`.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Use ImmutableSortedMap.toImmutableSortedMap.
        """
        ...


    @staticmethod
    def toImmutableMap(keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"], mergeFunction: "BinaryOperator"["V"]) -> "Collector"["T", Any, "ImmutableMap"["K", "V"]]:
        """
        Not supported. Use ImmutableSortedMap.toImmutableSortedMap, which offers better
        type-safety, instead. This method exists only to hide ImmutableMap.toImmutableMap from
        consumers of `ImmutableSortedMap`.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Use ImmutableSortedMap.toImmutableSortedMap.
        """
        ...


    @staticmethod
    def builder() -> "ImmutableSortedMap.Builder"["K", "V"]:
        """
        Not supported. Use ImmutableSortedMap.naturalOrder, which offers better type-safety,
        instead. This method exists only to hide ImmutableMap.builder from consumers of `ImmutableSortedMap`.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Use ImmutableSortedMap.naturalOrder, which offers better type-safety.
        """
        ...


    @staticmethod
    def builderWithExpectedSize(expectedSize: int) -> "ImmutableSortedMap.Builder"["K", "V"]:
        """
        Not supported for ImmutableSortedMap.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Not supported for ImmutableSortedMap.
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain a non-`Comparable`
        key.** Proper calls will resolve to the version in `ImmutableSortedMap`, not this dummy
        version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass a key of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object).**
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain non-`Comparable`
        keys.** Proper calls will resolve to the version in `ImmutableSortedMap`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass keys of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object, Comparable, Object).**
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain non-`Comparable`
        keys.** Proper calls to will resolve to the version in `ImmutableSortedMap`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass keys of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object, Comparable, Object, Comparable, Object).**
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain non-`Comparable`
        keys.** Proper calls will resolve to the version in `ImmutableSortedMap`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass keys of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object, Comparable, Object, Comparable, Object,
            Comparable, Object).**
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain non-`Comparable`
        keys.** Proper calls will resolve to the version in `ImmutableSortedMap`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass keys of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object, Comparable, Object, Comparable, Object,
            Comparable, Object, Comparable, Object).**
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain non-`Comparable`
        keys.** Proper calls will resolve to the version in `ImmutableSortedMap`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass keys of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object, Comparable, Object, Comparable, Object,
            Comparable, Object, Comparable, Object).**
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain non-`Comparable`
        keys.** Proper calls will resolve to the version in `ImmutableSortedMap`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass keys of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object, Comparable, Object, Comparable, Object,
            Comparable, Object, Comparable, Object).**
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V", k8: "K", v8: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain non-`Comparable`
        keys.** Proper calls will resolve to the version in `ImmutableSortedMap`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass keys of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object, Comparable, Object, Comparable, Object,
            Comparable, Object, Comparable, Object).**
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V", k8: "K", v8: "V", k9: "K", v9: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain non-`Comparable`
        keys.** Proper calls will resolve to the version in `ImmutableSortedMap`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass keys of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object, Comparable, Object, Comparable, Object,
            Comparable, Object, Comparable, Object).**
        """
        ...


    @staticmethod
    def of(k1: "K", v1: "V", k2: "K", v2: "V", k3: "K", v3: "V", k4: "K", v4: "V", k5: "K", v5: "V", k6: "K", v6: "V", k7: "K", v7: "V", k8: "K", v8: "V", k9: "K", v9: "V", k10: "K", v10: "V") -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. **You are attempting to create a map that may contain non-`Comparable`
        keys.** Proper calls will resolve to the version in `ImmutableSortedMap`, not this
        dummy version.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - **Pass keys of type `Comparable` to use ImmutableSortedMap.of(Comparable, Object, Comparable, Object, Comparable, Object,
            Comparable, Object, Comparable, Object).**
        """
        ...


    @staticmethod
    def ofEntries(*entries: Tuple["Entry"["K", "V"], ...]) -> "ImmutableSortedMap"["K", "V"]:
        """
        Not supported. Use `ImmutableSortedMap.copyOf(ImmutableMap.ofEntries(...))`.

        Deprecated
        - Use `ImmutableSortedMap.copyOf(ImmutableMap.ofEntries(...))`.
        """
        ...
