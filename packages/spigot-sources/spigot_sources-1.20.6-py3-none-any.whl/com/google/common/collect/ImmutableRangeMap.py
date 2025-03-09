"""
Python module generated from Java source file com.google.common.collect.ImmutableRangeMap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from com.google.common.collect.SortedLists import KeyAbsentBehavior
from com.google.common.collect.SortedLists import KeyPresentBehavior
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from com.google.errorprone.annotations import DoNotMock
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.util import Collections
from java.util import NoSuchElementException
from java.util.function import BiFunction
from java.util.function import Function
from java.util.stream import Collector
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableRangeMap(RangeMap, Serializable):
    """
    A RangeMap whose contents will never change, with many other important properties
    detailed at ImmutableCollection.

    Author(s)
    - Louis Wasserman

    Since
    - 14.0
    """

    @staticmethod
    def toImmutableRangeMap(keyFunction: "Function"["T", "Range"["K"]], valueFunction: "Function"["T", "V"]) -> "Collector"["T", Any, "ImmutableRangeMap"["K", "V"]]:
        """
        Returns a `Collector` that accumulates the input elements into a new `ImmutableRangeMap`. As in Builder, overlapping ranges are not permitted.

        Since
        - 23.1
        """
        ...


    @staticmethod
    def of() -> "ImmutableRangeMap"["K", "V"]:
        """
        Returns an empty immutable range map.
        
        **Performance note:** the instance returned is a singleton.
        """
        ...


    @staticmethod
    def of(range: "Range"["K"], value: "V") -> "ImmutableRangeMap"["K", "V"]:
        """
        Returns an immutable range map mapping a single range to a single value.
        """
        ...


    @staticmethod
    def copyOf(rangeMap: "RangeMap"["K", "V"]) -> "ImmutableRangeMap"["K", "V"]:
        ...


    @staticmethod
    def builder() -> "Builder"["K", "V"]:
        """
        Returns a new builder for an immutable range map.
        """
        ...


    def get(self, key: "K") -> "V":
        ...


    def getEntry(self, key: "K") -> "Entry"["Range"["K"], "V"]:
        ...


    def span(self) -> "Range"["K"]:
        ...


    def put(self, range: "Range"["K"], value: "V") -> None:
        """
        Guaranteed to throw an exception and leave the `RangeMap` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def putCoalescing(self, range: "Range"["K"], value: "V") -> None:
        """
        Guaranteed to throw an exception and leave the `RangeMap` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def putAll(self, rangeMap: "RangeMap"["K", "V"]) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeMap` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def clear(self) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeMap` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def remove(self, range: "Range"["K"]) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeMap` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def merge(self, range: "Range"["K"], value: "V", remappingFunction: "BiFunction"["V", "V", "V"]) -> None:
        """
        Guaranteed to throw an exception and leave the `RangeMap` unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def asMapOfRanges(self) -> "ImmutableMap"["Range"["K"], "V"]:
        ...


    def asDescendingMapOfRanges(self) -> "ImmutableMap"["Range"["K"], "V"]:
        ...


    def subRangeMap(self, range: "Range"["K"]) -> "ImmutableRangeMap"["K", "V"]:
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...


    class Builder:
        """
        A builder for immutable range maps. Overlapping ranges are prohibited.

        Since
        - 14.0
        """

        def __init__(self):
            ...


        def put(self, range: "Range"["K"], value: "V") -> "Builder"["K", "V"]:
            """
            Associates the specified range with the specified value.

            Raises
            - IllegalArgumentException: if `range` is empty
            """
            ...


        def putAll(self, rangeMap: "RangeMap"["K", "V"]) -> "Builder"["K", "V"]:
            """
            Copies all associations from the specified range map into this builder.
            """
            ...


        def build(self) -> "ImmutableRangeMap"["K", "V"]:
            """
            Returns an `ImmutableRangeMap` containing the associations previously added to this
            builder.

            Raises
            - IllegalArgumentException: if any two ranges inserted into this builder overlap
            """
            ...
