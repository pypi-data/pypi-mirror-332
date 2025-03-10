"""
Python module generated from Java source file com.google.common.util.concurrent.Striped

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import MoreObjects
from com.google.common.base import Preconditions
from com.google.common.base import Supplier
from com.google.common.collect import ImmutableList
from com.google.common.collect import MapMaker
from com.google.common.math import IntMath
from com.google.common.primitives import Ints
from com.google.common.util.concurrent import *
from java.lang.ref import Reference
from java.lang.ref import ReferenceQueue
from java.lang.ref import WeakReference
from java.math import RoundingMode
from java.util import Arrays
from java.util import Collections
from java.util.concurrent import ConcurrentMap
from java.util.concurrent import Semaphore
from java.util.concurrent.atomic import AtomicReferenceArray
from java.util.concurrent.locks import Condition
from java.util.concurrent.locks import Lock
from java.util.concurrent.locks import ReadWriteLock
from java.util.concurrent.locks import ReentrantLock
from java.util.concurrent.locks import ReentrantReadWriteLock
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Striped:
    """
    A striped `Lock/Semaphore/ReadWriteLock`. This offers the underlying lock striping similar
    to that of `ConcurrentHashMap` in a reusable form, and extends it for semaphores and
    read-write locks. Conceptually, lock striping is the technique of dividing a lock into many
    *stripes*, increasing the granularity of a single lock and allowing independent operations
    to lock different stripes and proceed concurrently, instead of creating contention for a single
    lock.
    
    The guarantee provided by this class is that equal keys lead to the same lock (or semaphore),
    i.e. `if (key1.equals(key2))` then `striped.get(key1) == striped.get(key2)` (assuming
    Object.hashCode() is correctly implemented for the keys). Note that if `key1` is
    <strong>not</strong> equal to `key2`, it is <strong>not</strong> guaranteed that `striped.get(key1) != striped.get(key2)`; the elements might nevertheless be mapped to the same
    lock. The lower the number of stripes, the higher the probability of this happening.
    
    There are three flavors of this class: `Striped<Lock>`, `Striped<Semaphore>`, and
    `Striped<ReadWriteLock>`. For each type, two implementations are offered: .lock(int) strong and .lazyWeakLock(int) weak `Striped<Lock>`, .semaphore(int, int) strong and .lazyWeakSemaphore(int, int) weak `Striped<Semaphore>`, and .readWriteLock(int) strong and .lazyWeakReadWriteLock(int) weak `Striped<ReadWriteLock>`. *Strong* means that all
    stripes (locks/semaphores) are initialized eagerly, and are not reclaimed unless `Striped`
    itself is reclaimable. *Weak* means that locks/semaphores are created lazily, and they are
    allowed to be reclaimed if nobody is holding on to them. This is useful, for example, if one
    wants to create a `Striped<Lock>` of many locks, but worries that in most cases only a
    small portion of these would be in use.
    
    Prior to this class, one might be tempted to use `Map<K, Lock>`, where `K`
    represents the task. This maximizes concurrency by having each unique key mapped to a unique
    lock, but also maximizes memory footprint. On the other extreme, one could use a single lock for
    all tasks, which minimizes memory footprint but also minimizes concurrency. Instead of choosing
    either of these extremes, `Striped` allows the user to trade between required concurrency
    and memory footprint. For example, if a set of tasks are CPU-bound, one could easily create a
    very compact `Striped<Lock>` of `availableProcessors() * 4` stripes, instead of
    possibly thousands of locks which could be created in a `Map<K, Lock>` structure.

    Author(s)
    - Dimitris Andreou

    Since
    - 13.0
    """

    def get(self, key: "Object") -> "L":
        """
        Returns the stripe that corresponds to the passed key. It is always guaranteed that if `key1.equals(key2)`, then `get(key1) == get(key2)`.

        Arguments
        - key: an arbitrary, non-null key

        Returns
        - the stripe that the passed key corresponds to
        """
        ...


    def getAt(self, index: int) -> "L":
        """
        Returns the stripe at the specified index. Valid indexes are 0, inclusively, to `size()`,
        exclusively.

        Arguments
        - index: the index of the stripe to return; must be in `[0...size())`

        Returns
        - the stripe at the specified index
        """
        ...


    def size(self) -> int:
        """
        Returns the total number of stripes in this instance.
        """
        ...


    def bulkGet(self, keys: Iterable["Object"]) -> Iterable["L"]:
        """
        Returns the stripes that correspond to the passed objects, in ascending (as per .getAt(int)) order. Thus, threads that use the stripes in the order returned by this method
        are guaranteed to not deadlock each other.
        
        It should be noted that using a `Striped<L>` with relatively few stripes, and `bulkGet(keys)` with a relative large number of keys can cause an excessive number of shared
        stripes (much like the birthday paradox, where much fewer than anticipated birthdays are needed
        for a pair of them to match). Please consider carefully the implications of the number of
        stripes, the intended concurrency level, and the typical number of keys used in a `bulkGet(keys)` operation. See <a href="http://www.mathpages.com/home/kmath199.htm">Balls in
        Bins model</a> for mathematical formulas that can be used to estimate the probability of
        collisions.

        Arguments
        - keys: arbitrary non-null keys

        Returns
        - the stripes corresponding to the objects (one per each object, derived by delegating to
            .get(Object); may contain duplicates), in an increasing index order.
        """
        ...


    @staticmethod
    def lock(stripes: int) -> "Striped"["Lock"]:
        """
        Creates a `Striped<Lock>` with eagerly initialized, strongly referenced locks. Every lock
        is reentrant.

        Arguments
        - stripes: the minimum number of stripes (locks) required

        Returns
        - a new `Striped<Lock>`
        """
        ...


    @staticmethod
    def lazyWeakLock(stripes: int) -> "Striped"["Lock"]:
        """
        Creates a `Striped<Lock>` with lazily initialized, weakly referenced locks. Every lock is
        reentrant.

        Arguments
        - stripes: the minimum number of stripes (locks) required

        Returns
        - a new `Striped<Lock>`
        """
        ...


    @staticmethod
    def semaphore(stripes: int, permits: int) -> "Striped"["Semaphore"]:
        """
        Creates a `Striped<Semaphore>` with eagerly initialized, strongly referenced semaphores,
        with the specified number of permits.

        Arguments
        - stripes: the minimum number of stripes (semaphores) required
        - permits: the number of permits in each semaphore

        Returns
        - a new `Striped<Semaphore>`
        """
        ...


    @staticmethod
    def lazyWeakSemaphore(stripes: int, permits: int) -> "Striped"["Semaphore"]:
        """
        Creates a `Striped<Semaphore>` with lazily initialized, weakly referenced semaphores,
        with the specified number of permits.

        Arguments
        - stripes: the minimum number of stripes (semaphores) required
        - permits: the number of permits in each semaphore

        Returns
        - a new `Striped<Semaphore>`
        """
        ...


    @staticmethod
    def readWriteLock(stripes: int) -> "Striped"["ReadWriteLock"]:
        """
        Creates a `Striped<ReadWriteLock>` with eagerly initialized, strongly referenced
        read-write locks. Every lock is reentrant.

        Arguments
        - stripes: the minimum number of stripes (locks) required

        Returns
        - a new `Striped<ReadWriteLock>`
        """
        ...


    @staticmethod
    def lazyWeakReadWriteLock(stripes: int) -> "Striped"["ReadWriteLock"]:
        """
        Creates a `Striped<ReadWriteLock>` with lazily initialized, weakly referenced read-write
        locks. Every lock is reentrant.

        Arguments
        - stripes: the minimum number of stripes (locks) required

        Returns
        - a new `Striped<ReadWriteLock>`
        """
        ...
