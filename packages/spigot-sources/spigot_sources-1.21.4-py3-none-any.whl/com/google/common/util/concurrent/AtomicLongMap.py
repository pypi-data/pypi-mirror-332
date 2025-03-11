"""
Python module generated from Java source file com.google.common.util.concurrent.AtomicLongMap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from java.io import Serializable
from java.util import Collections
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent.atomic import AtomicBoolean
from java.util.concurrent.atomic import AtomicLong
from java.util.function import LongBinaryOperator
from java.util.function import LongUnaryOperator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AtomicLongMap(Serializable):
    """
    A map containing `long` values that can be atomically updated. While writes to a
    traditional `Map` rely on `put(K, V)`, the typical mechanism for writing to this map
    is `addAndGet(K, long)`, which adds a `long` to the value currently associated with
    `K`. If a key has not yet been associated with a value, its implicit value is zero.
    
    Most methods in this class treat absent values and zero values identically, as individually
    documented. Exceptions to this are .containsKey, .size, .isEmpty, .asMap, and .toString.
    
    Instances of this class may be used by multiple threads concurrently. All operations are
    atomic unless otherwise noted.
    
    Instances of this class are serializable if the keys are serializable.
    
    **Note:** If your values are always positive and less than 2^31, you may wish to use a
    com.google.common.collect.Multiset such as com.google.common.collect.ConcurrentHashMultiset instead.
    
    **Warning:** Unlike `Multiset`, entries whose values are zero are not automatically
    removed from the map. Instead they must be removed manually with .removeAllZeros.

    Author(s)
    - Charles Fry

    Since
    - 11.0
    """

    @staticmethod
    def create() -> "AtomicLongMap"["K"]:
        """
        Creates an `AtomicLongMap`.
        """
        ...


    @staticmethod
    def create(m: dict["K", "Long"]) -> "AtomicLongMap"["K"]:
        """
        Creates an `AtomicLongMap` with the same mappings as the specified `Map`.
        """
        ...


    def get(self, key: "K") -> int:
        """
        Returns the value associated with `key`, or zero if there is no value associated with
        `key`.
        """
        ...


    def incrementAndGet(self, key: "K") -> int:
        """
        Increments by one the value currently associated with `key`, and returns the new value.
        """
        ...


    def decrementAndGet(self, key: "K") -> int:
        """
        Decrements by one the value currently associated with `key`, and returns the new value.
        """
        ...


    def addAndGet(self, key: "K", delta: int) -> int:
        """
        Adds `delta` to the value currently associated with `key`, and returns the new
        value.
        """
        ...


    def getAndIncrement(self, key: "K") -> int:
        """
        Increments by one the value currently associated with `key`, and returns the old value.
        """
        ...


    def getAndDecrement(self, key: "K") -> int:
        """
        Decrements by one the value currently associated with `key`, and returns the old value.
        """
        ...


    def getAndAdd(self, key: "K", delta: int) -> int:
        """
        Adds `delta` to the value currently associated with `key`, and returns the old
        value.
        """
        ...


    def updateAndGet(self, key: "K", updaterFunction: "LongUnaryOperator") -> int:
        """
        Updates the value currently associated with `key` with the specified function, and
        returns the new value. If there is not currently a value associated with `key`, the
        function is applied to `0L`.

        Since
        - 21.0
        """
        ...


    def getAndUpdate(self, key: "K", updaterFunction: "LongUnaryOperator") -> int:
        """
        Updates the value currently associated with `key` with the specified function, and
        returns the old value. If there is not currently a value associated with `key`, the
        function is applied to `0L`.

        Since
        - 21.0
        """
        ...


    def accumulateAndGet(self, key: "K", x: int, accumulatorFunction: "LongBinaryOperator") -> int:
        """
        Updates the value currently associated with `key` by combining it with `x` via the
        specified accumulator function, returning the new value. The previous value associated with
        `key` (or zero, if there is none) is passed as the first argument to `accumulatorFunction`, and `x` is passed as the second argument.

        Since
        - 21.0
        """
        ...


    def getAndAccumulate(self, key: "K", x: int, accumulatorFunction: "LongBinaryOperator") -> int:
        """
        Updates the value currently associated with `key` by combining it with `x` via the
        specified accumulator function, returning the old value. The previous value associated with
        `key` (or zero, if there is none) is passed as the first argument to `accumulatorFunction`, and `x` is passed as the second argument.

        Since
        - 21.0
        """
        ...


    def put(self, key: "K", newValue: int) -> int:
        """
        Associates `newValue` with `key` in this map, and returns the value previously
        associated with `key`, or zero if there was no such value.
        """
        ...


    def putAll(self, m: dict["K", "Long"]) -> None:
        """
        Copies all of the mappings from the specified map to this map. The effect of this call is
        equivalent to that of calling `put(k, v)` on this map once for each mapping from key
        `k` to value `v` in the specified map. The behavior of this operation is undefined
        if the specified map is modified while the operation is in progress.
        """
        ...


    def remove(self, key: "K") -> int:
        """
        Removes and returns the value associated with `key`. If `key` is not in the map,
        this method has no effect and returns zero.
        """
        ...


    def removeIfZero(self, key: "K") -> bool:
        """
        Atomically remove `key` from the map iff its associated value is 0.

        Since
        - 20.0
        """
        ...


    def removeAllZeros(self) -> None:
        """
        Removes all mappings from this map whose values are zero.
        
        This method is not atomic: the map may be visible in intermediate states, where some of the
        zero values have been removed and others have not.
        """
        ...


    def sum(self) -> int:
        """
        Returns the sum of all values in this map.
        
        This method is not atomic: the sum may or may not include other concurrent operations.
        """
        ...


    def asMap(self) -> dict["K", "Long"]:
        """
        Returns a live, read-only view of the map backing this `AtomicLongMap`.
        """
        ...


    def containsKey(self, key: "Object") -> bool:
        """
        Returns True if this map contains a mapping for the specified key.
        """
        ...


    def size(self) -> int:
        """
        Returns the number of key-value mappings in this map. If the map contains more than `Integer.MAX_VALUE` elements, returns `Integer.MAX_VALUE`.
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if this map contains no key-value mappings.
        """
        ...


    def clear(self) -> None:
        """
        Removes all of the mappings from this map. The map will be empty after this call returns.
        
        This method is not atomic: the map may not be empty after returning if there were concurrent
        writes.
        """
        ...


    def toString(self) -> str:
        ...
