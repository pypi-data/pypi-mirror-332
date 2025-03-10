"""
Python module generated from Java source file com.google.common.collect.ImmutableBiMapFauxverideShim

Java source file obtained from artifact guava version 31.0.1-jre

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


class ImmutableBiMapFauxverideShim(ImmutableMap):
    """
    "Overrides" the ImmutableMap static methods that lack ImmutableBiMap equivalents
    with deprecated, exception-throwing versions. See ImmutableSortedSetFauxverideShim for
    details.

    Author(s)
    - Louis Wasserman
    """

    @staticmethod
    def toImmutableMap(keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"]) -> "Collector"["T", Any, "ImmutableMap"["K", "V"]]:
        """
        Not supported. Use ImmutableBiMap.toImmutableBiMap instead. This method exists only to
        hide ImmutableMap.toImmutableMap(Function, Function) from consumers of `ImmutableBiMap`.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Use ImmutableBiMap.toImmutableBiMap.
        """
        ...


    @staticmethod
    def toImmutableMap(keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"], mergeFunction: "BinaryOperator"["V"]) -> "Collector"["T", Any, "ImmutableMap"["K", "V"]]:
        """
        Not supported. This method does not make sense for `BiMap`. This method exists only to
        hide ImmutableMap.toImmutableMap(Function, Function, BinaryOperator) from consumers of
        `ImmutableBiMap`.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - 
        """
        ...
