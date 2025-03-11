"""
Python module generated from Java source file com.google.common.collect.MutableClassToInstanceMap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import *
from com.google.common.primitives import Primitives
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.util import Iterator
from java.util import Spliterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import NonNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class MutableClassToInstanceMap(ForwardingMap, ClassToInstanceMap, Serializable):
    """
    A mutable class-to-instance map backed by an arbitrary user-provided map. See also ImmutableClassToInstanceMap.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#classtoinstancemap">`ClassToInstanceMap`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    @staticmethod
    def create() -> "MutableClassToInstanceMap"["B"]:
        """
        Returns a new `MutableClassToInstanceMap` instance backed by a HashMap using the
        default initial capacity and load factor.
        """
        ...


    @staticmethod
    def create(backingMap: dict[type["B"], "B"]) -> "MutableClassToInstanceMap"["B"]:
        """
        Returns a new `MutableClassToInstanceMap` instance backed by a given empty `backingMap`. The caller surrenders control of the backing map, and thus should not allow any
        direct references to it to remain accessible.
        """
        ...


    def entrySet(self) -> set["Entry"[type["B"], "B"]]:
        ...


    def put(self, key: type["B"], value: "B") -> "B":
        ...


    def putAll(self, map: dict[type["B"], "B"]) -> None:
        ...


    def putInstance(self, type: type["T"], value: "T") -> "T":
        ...


    def getInstance(self, type: type["T"]) -> "T":
        ...
