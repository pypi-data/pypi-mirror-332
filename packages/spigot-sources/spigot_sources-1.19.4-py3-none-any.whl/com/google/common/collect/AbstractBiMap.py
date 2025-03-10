"""
Python module generated from Java source file com.google.common.collect.AbstractBiMap

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Objects
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import RetainedWith
from com.google.j2objc.annotations import WeakOuter
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util import Iterator
from java.util.function import BiFunction
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractBiMap(ForwardingMap, BiMap, Serializable):
    """
    A general-purpose bimap implementation using any two backing `Map` instances.
    
    Note that this class contains `equals()` calls that keep it from supporting `IdentityHashMap` backing maps.

    Author(s)
    - Mike Bostock
    """

    def containsValue(self, value: "Object") -> bool:
        ...


    def put(self, key: "K", value: "V") -> "V":
        ...


    def forcePut(self, key: "K", value: "V") -> "V":
        ...


    def remove(self, key: "Object") -> "V":
        ...


    def putAll(self, map: dict["K", "V"]) -> None:
        ...


    def replaceAll(self, function: "BiFunction"["K", "V", "V"]) -> None:
        ...


    def clear(self) -> None:
        ...


    def inverse(self) -> "BiMap"["V", "K"]:
        ...


    def keySet(self) -> set["K"]:
        ...


    def values(self) -> set["V"]:
        ...


    def entrySet(self) -> set["Entry"["K", "V"]]:
        ...
