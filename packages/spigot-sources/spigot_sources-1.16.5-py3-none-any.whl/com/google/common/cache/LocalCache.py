"""
Python module generated from Java source file com.google.common.cache.LocalCache

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Equivalence
from com.google.common.base import Stopwatch
from com.google.common.base import Ticker
from com.google.common.cache import *
from com.google.common.cache.AbstractCache import SimpleStatsCounter
from com.google.common.cache.AbstractCache import StatsCounter
from com.google.common.cache.CacheBuilder import NullListener
from com.google.common.cache.CacheBuilder import OneWeigher
from com.google.common.cache.CacheLoader import InvalidCacheLoadException
from com.google.common.cache.CacheLoader import UnsupportedLoadingOperationException
from com.google.common.cache.LocalCache import AbstractCacheSet
from com.google.common.collect import AbstractSequentialIterator
from com.google.common.collect import ImmutableMap
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Iterators
from com.google.common.collect import Maps
from com.google.common.collect import Sets
from com.google.common.primitives import Ints
from com.google.common.util.concurrent import ExecutionError
from com.google.common.util.concurrent import Futures
from com.google.common.util.concurrent import ListenableFuture
from com.google.common.util.concurrent import SettableFuture
from com.google.common.util.concurrent import UncheckedExecutionException
from com.google.common.util.concurrent import Uninterruptibles
from com.google.j2objc.annotations import Weak
from com.google.j2objc.annotations import WeakOuter
from java.io import IOException
from java.io import ObjectInputStream
from java.io import Serializable
from java.lang.ref import Reference
from java.lang.ref import ReferenceQueue
from java.lang.ref import SoftReference
from java.lang.ref import WeakReference
from java.util import AbstractCollection
from java.util import AbstractQueue
from java.util import AbstractSet
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Queue
from java.util.concurrent import Callable
from java.util.concurrent import ConcurrentLinkedQueue
from java.util.concurrent import ConcurrentMap
from java.util.concurrent import ExecutionException
from java.util.concurrent import TimeUnit
from java.util.concurrent.atomic import AtomicInteger
from java.util.concurrent.atomic import AtomicReferenceArray
from java.util.concurrent.locks import ReentrantLock
from java.util.function import BiFunction
from java.util.function import BiPredicate
from java.util.function import Function
from java.util.function import Predicate
from javax.annotation import Nullable
from javax.annotation.concurrent import GuardedBy
from typing import Any, Callable, Iterable, Tuple


class LocalCache(AbstractMap, ConcurrentMap):
    """
    The concurrent hash map implementation built by CacheBuilder.
    
    This implementation is heavily derived from revision 1.96 of
    <a href="http://tinyurl.com/ConcurrentHashMap">ConcurrentHashMap.java</a>.

    Author(s)
    - Doug Lea (`ConcurrentHashMap`)
    """

    def cleanUp(self) -> None:
        ...


    def isEmpty(self) -> bool:
        ...


    def size(self) -> int:
        ...


    def get(self, key: "Object") -> "V":
        ...


    def getIfPresent(self, key: "Object") -> "V":
        ...


    def getOrDefault(self, key: "Object", defaultValue: "V") -> "V":
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def put(self, key: "K", value: "V") -> "V":
        ...


    def putIfAbsent(self, key: "K", value: "V") -> "V":
        ...


    def compute(self, key: "K", function: "BiFunction"["K", "V", "V"]) -> "V":
        ...


    def computeIfAbsent(self, key: "K", function: "Function"["K", "V"]) -> "V":
        ...


    def computeIfPresent(self, key: "K", function: "BiFunction"["K", "V", "V"]) -> "V":
        ...


    def merge(self, key: "K", newValue: "V", function: "BiFunction"["V", "V", "V"]) -> "V":
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
