"""
Python module generated from Java source file com.google.common.collect.MapMakerInternalMap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Equivalence
from com.google.common.collect import *
from com.google.common.collect.MapMaker import Dummy
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import GuardedBy
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import Weak
from com.google.j2objc.annotations import WeakOuter
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.lang.ref import Reference
from java.lang.ref import ReferenceQueue
from java.lang.ref import WeakReference
from java.util import AbstractCollection
from java.util import AbstractSet
from java.util import Iterator
from java.util import NoSuchElementException
from java.util.concurrent import CancellationException
from java.util.concurrent import ConcurrentMap
from java.util.concurrent.atomic import AtomicInteger
from java.util.concurrent.atomic import AtomicReferenceArray
from java.util.concurrent.locks import ReentrantLock
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MapMakerInternalMap(AbstractMap, ConcurrentMap, Serializable):

    def isEmpty(self) -> bool:
        ...


    def size(self) -> int:
        ...


    def get(self, key: "Object") -> "V":
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def put(self, key: "K", value: "V") -> "V":
        ...


    def putIfAbsent(self, key: "K", value: "V") -> "V":
        ...


    def putAll(self, m: dict["K", "V"]) -> None:
        ...


    def remove(self, key: "Object") -> "V":
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        ...


    def replace(self, key: "K", oldValue: "V", newValue: "V") -> bool:
        ...


    def replace(self, key: "K", value: "V") -> "V":
        ...


    def clear(self) -> None:
        ...


    def keySet(self) -> set["K"]:
        ...


    def values(self) -> Iterable["V"]:
        ...


    def entrySet(self) -> set["Entry"["K", "V"]]:
        ...
