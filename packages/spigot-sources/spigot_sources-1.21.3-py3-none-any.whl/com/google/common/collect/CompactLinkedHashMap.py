"""
Python module generated from Java source file com.google.common.collect.CompactLinkedHashMap

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import WeakOuter
from java.util import Arrays
from java.util import Spliterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CompactLinkedHashMap(CompactHashMap):
    """
    CompactLinkedHashMap is an implementation of a Map with insertion or LRU iteration order,
    maintained with a doubly linked list through the entries. All optional operations (put and
    remove) are supported. Null keys and values are supported.
    
    `containsKey(k)`, `put(k, v)` and `remove(k)` are all (expected and
    amortized) constant time operations. Expected in the hashtable sense (depends on the hash
    function doing a good job of distributing the elements to the buckets to a distribution not far
    from uniform), and amortized since some operations can trigger a hash table resize.
    
    As compared with java.util.LinkedHashMap, this structure places significantly reduced
    load on the garbage collector by only using a constant number of internal objects.
    
    This class should not be assumed to be universally superior to `java.util.LinkedHashMap`. Generally speaking, this class reduces object allocation and memory
    consumption at the price of moderately increased constant factors of CPU. Only use this class
    when there is a specific reason to prioritize memory over CPU.

    Author(s)
    - Louis Wasserman
    """

    @staticmethod
    def create() -> "CompactLinkedHashMap"["K", "V"]:
        """
        Creates an empty `CompactLinkedHashMap` instance.
        """
        ...


    @staticmethod
    def createWithExpectedSize(expectedSize: int) -> "CompactLinkedHashMap"["K", "V"]:
        """
        Creates a `CompactLinkedHashMap` instance, with a high enough "initial capacity" that it
        *should* hold `expectedSize` elements without rebuilding internal data structures.

        Arguments
        - expectedSize: the number of elements you expect to add to the returned set

        Returns
        - a new, empty `CompactLinkedHashMap` with enough capacity to hold `expectedSize` elements without resizing

        Raises
        - IllegalArgumentException: if `expectedSize` is negative
        """
        ...


    def clear(self) -> None:
        ...
