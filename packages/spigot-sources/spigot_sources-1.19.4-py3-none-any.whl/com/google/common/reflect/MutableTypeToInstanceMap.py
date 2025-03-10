"""
Python module generated from Java source file com.google.common.reflect.MutableTypeToInstanceMap

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ForwardingMap
from com.google.common.collect import ForwardingMapEntry
from com.google.common.collect import ForwardingSet
from com.google.common.collect import Iterators
from com.google.common.collect import Maps
from com.google.common.reflect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from java.util import Iterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class MutableTypeToInstanceMap(ForwardingMap, TypeToInstanceMap):
    """
    A mutable type-to-instance map. See also ImmutableTypeToInstanceMap.
    
    This implementation *does* support null values, despite how it is annotated; see
    discussion at TypeToInstanceMap.

    Author(s)
    - Ben Yu

    Since
    - 13.0
    """

    def getInstance(self, type: type["T"]) -> "T":
        ...


    def getInstance(self, type: "TypeToken"["T"]) -> "T":
        ...


    def putInstance(self, type: type["T"], value: "T") -> "T":
        ...


    def putInstance(self, type: "TypeToken"["T"], value: "T") -> "T":
        ...


    def put(self, key: "TypeToken"["B"], value: "B") -> "B":
        """
        Not supported. Use .putInstance instead.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - unsupported operation
        """
        ...


    def putAll(self, map: dict["TypeToken"["B"], "B"]) -> None:
        """
        Not supported. Use .putInstance instead.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - unsupported operation
        """
        ...


    def entrySet(self) -> set["Entry"["TypeToken"["B"], "B"]]:
        ...
