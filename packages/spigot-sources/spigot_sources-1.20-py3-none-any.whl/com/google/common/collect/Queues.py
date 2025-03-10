"""
Python module generated from Java source file com.google.common.collect.Queues

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import ArrayDeque
from java.util import Deque
from java.util import PriorityQueue
from java.util import Queue
from java.util.concurrent import ArrayBlockingQueue
from java.util.concurrent import BlockingQueue
from java.util.concurrent import ConcurrentLinkedQueue
from java.util.concurrent import LinkedBlockingDeque
from java.util.concurrent import LinkedBlockingQueue
from java.util.concurrent import PriorityBlockingQueue
from java.util.concurrent import SynchronousQueue
from java.util.concurrent import TimeUnit
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Queues:
    """
    Static utility methods pertaining to Queue and Deque instances. Also see this
    class's counterparts Lists, Sets, and Maps.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 11.0
    """

    @staticmethod
    def newArrayBlockingQueue(capacity: int) -> "ArrayBlockingQueue"["E"]:
        """
        Creates an empty `ArrayBlockingQueue` with the given (fixed) capacity and nonfair access
        policy.
        """
        ...


    @staticmethod
    def newArrayDeque() -> "ArrayDeque"["E"]:
        """
        Creates an empty `ArrayDeque`.

        Since
        - 12.0
        """
        ...


    @staticmethod
    def newArrayDeque(elements: Iterable["E"]) -> "ArrayDeque"["E"]:
        """
        Creates an `ArrayDeque` containing the elements of the specified iterable, in the order
        they are returned by the iterable's iterator.

        Since
        - 12.0
        """
        ...


    @staticmethod
    def newConcurrentLinkedQueue() -> "ConcurrentLinkedQueue"["E"]:
        """
        Creates an empty `ConcurrentLinkedQueue`.
        """
        ...


    @staticmethod
    def newConcurrentLinkedQueue(elements: Iterable["E"]) -> "ConcurrentLinkedQueue"["E"]:
        """
        Creates a `ConcurrentLinkedQueue` containing the elements of the specified iterable, in
        the order they are returned by the iterable's iterator.
        """
        ...


    @staticmethod
    def newLinkedBlockingDeque() -> "LinkedBlockingDeque"["E"]:
        """
        Creates an empty `LinkedBlockingDeque` with a capacity of Integer.MAX_VALUE.

        Since
        - 12.0
        """
        ...


    @staticmethod
    def newLinkedBlockingDeque(capacity: int) -> "LinkedBlockingDeque"["E"]:
        """
        Creates an empty `LinkedBlockingDeque` with the given (fixed) capacity.

        Raises
        - IllegalArgumentException: if `capacity` is less than 1

        Since
        - 12.0
        """
        ...


    @staticmethod
    def newLinkedBlockingDeque(elements: Iterable["E"]) -> "LinkedBlockingDeque"["E"]:
        """
        Creates a `LinkedBlockingDeque` with a capacity of Integer.MAX_VALUE, containing
        the elements of the specified iterable, in the order they are returned by the iterable's
        iterator.

        Since
        - 12.0
        """
        ...


    @staticmethod
    def newLinkedBlockingQueue() -> "LinkedBlockingQueue"["E"]:
        """
        Creates an empty `LinkedBlockingQueue` with a capacity of Integer.MAX_VALUE.
        """
        ...


    @staticmethod
    def newLinkedBlockingQueue(capacity: int) -> "LinkedBlockingQueue"["E"]:
        """
        Creates an empty `LinkedBlockingQueue` with the given (fixed) capacity.

        Raises
        - IllegalArgumentException: if `capacity` is less than 1
        """
        ...


    @staticmethod
    def newLinkedBlockingQueue(elements: Iterable["E"]) -> "LinkedBlockingQueue"["E"]:
        """
        Creates a `LinkedBlockingQueue` with a capacity of Integer.MAX_VALUE, containing
        the elements of the specified iterable, in the order they are returned by the iterable's
        iterator.

        Arguments
        - elements: the elements that the queue should contain, in order

        Returns
        - a new `LinkedBlockingQueue` containing those elements
        """
        ...


    @staticmethod
    def newPriorityBlockingQueue() -> "PriorityBlockingQueue"["E"]:
        """
        Creates an empty `PriorityBlockingQueue` with the ordering given by its elements' natural
        ordering.

        Since
        - 11.0 (but the bound of `E` was changed from `Object` to `Comparable`
            in 15.0)
        """
        ...


    @staticmethod
    def newPriorityBlockingQueue(elements: Iterable["E"]) -> "PriorityBlockingQueue"["E"]:
        """
        Creates a `PriorityBlockingQueue` containing the given elements.
        
        **Note:** If the specified iterable is a `SortedSet` or a `PriorityQueue`,
        this priority queue will be ordered according to the same ordering.

        Since
        - 11.0 (but the bound of `E` was changed from `Object` to `Comparable`
            in 15.0)
        """
        ...


    @staticmethod
    def newPriorityQueue() -> "PriorityQueue"["E"]:
        """
        Creates an empty `PriorityQueue` with the ordering given by its elements' natural
        ordering.

        Since
        - 11.0 (but the bound of `E` was changed from `Object` to `Comparable`
            in 15.0)
        """
        ...


    @staticmethod
    def newPriorityQueue(elements: Iterable["E"]) -> "PriorityQueue"["E"]:
        """
        Creates a `PriorityQueue` containing the given elements.
        
        **Note:** If the specified iterable is a `SortedSet` or a `PriorityQueue`,
        this priority queue will be ordered according to the same ordering.

        Since
        - 11.0 (but the bound of `E` was changed from `Object` to `Comparable`
            in 15.0)
        """
        ...


    @staticmethod
    def newSynchronousQueue() -> "SynchronousQueue"["E"]:
        """
        Creates an empty `SynchronousQueue` with nonfair access policy.
        """
        ...


    @staticmethod
    def drain(q: "BlockingQueue"["E"], buffer: Iterable["E"], numElements: int, timeout: "java.time.Duration") -> int:
        """
        Drains the queue as BlockingQueue.drainTo(Collection, int), but if the requested `numElements` elements are not available, it will wait for them up to the specified timeout.

        Arguments
        - q: the blocking queue to be drained
        - buffer: where to add the transferred elements
        - numElements: the number of elements to be waited for
        - timeout: how long to wait before giving up

        Returns
        - the number of elements transferred

        Raises
        - InterruptedException: if interrupted while waiting

        Since
        - 28.0
        """
        ...


    @staticmethod
    def drain(q: "BlockingQueue"["E"], buffer: Iterable["E"], numElements: int, timeout: int, unit: "TimeUnit") -> int:
        """
        Drains the queue as BlockingQueue.drainTo(Collection, int), but if the requested `numElements` elements are not available, it will wait for them up to the specified timeout.

        Arguments
        - q: the blocking queue to be drained
        - buffer: where to add the transferred elements
        - numElements: the number of elements to be waited for
        - timeout: how long to wait before giving up, in units of `unit`
        - unit: a `TimeUnit` determining how to interpret the timeout parameter

        Returns
        - the number of elements transferred

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    @staticmethod
    def drainUninterruptibly(q: "BlockingQueue"["E"], buffer: Iterable["E"], numElements: int, timeout: "java.time.Duration") -> int:
        """
        Drains the queue as .drain(BlockingQueue, Collection, int, Duration), but with a
        different behavior in case it is interrupted while waiting. In that case, the operation will
        continue as usual, and in the end the thread's interruption status will be set (no `InterruptedException` is thrown).

        Arguments
        - q: the blocking queue to be drained
        - buffer: where to add the transferred elements
        - numElements: the number of elements to be waited for
        - timeout: how long to wait before giving up

        Returns
        - the number of elements transferred

        Since
        - 28.0
        """
        ...


    @staticmethod
    def drainUninterruptibly(q: "BlockingQueue"["E"], buffer: Iterable["E"], numElements: int, timeout: int, unit: "TimeUnit") -> int:
        """
        Drains the queue as .drain(BlockingQueue, Collection, int, long, TimeUnit), but
        with a different behavior in case it is interrupted while waiting. In that case, the operation
        will continue as usual, and in the end the thread's interruption status will be set (no `InterruptedException` is thrown).

        Arguments
        - q: the blocking queue to be drained
        - buffer: where to add the transferred elements
        - numElements: the number of elements to be waited for
        - timeout: how long to wait before giving up, in units of `unit`
        - unit: a `TimeUnit` determining how to interpret the timeout parameter

        Returns
        - the number of elements transferred
        """
        ...


    @staticmethod
    def synchronizedQueue(queue: "Queue"["E"]) -> "Queue"["E"]:
        """
        Returns a synchronized (thread-safe) queue backed by the specified queue. In order to guarantee
        serial access, it is critical that **all** access to the backing queue is accomplished
        through the returned queue.
        
        It is imperative that the user manually synchronize on the returned queue when accessing the
        queue's iterator:
        
        ````Queue<E> queue = Queues.synchronizedQueue(MinMaxPriorityQueue.<E>create());
        ...
        queue.add(element);  // Needn't be in synchronized block
        ...
        synchronized (queue) {  // Must synchronize on queue!
          Iterator<E> i = queue.iterator(); // Must be in synchronized block
          while (i.hasNext()) {
            foo(i.next());`
        }
        }```
        
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned queue will be serializable if the specified queue is serializable.

        Arguments
        - queue: the queue to be wrapped in a synchronized view

        Returns
        - a synchronized view of the specified queue

        Since
        - 14.0
        """
        ...


    @staticmethod
    def synchronizedDeque(deque: "Deque"["E"]) -> "Deque"["E"]:
        """
        Returns a synchronized (thread-safe) deque backed by the specified deque. In order to guarantee
        serial access, it is critical that **all** access to the backing deque is accomplished
        through the returned deque.
        
        It is imperative that the user manually synchronize on the returned deque when accessing any
        of the deque's iterators:
        
        ````Deque<E> deque = Queues.synchronizedDeque(Queues.<E>newArrayDeque());
        ...
        deque.add(element);  // Needn't be in synchronized block
        ...
        synchronized (deque) {  // Must synchronize on deque!
          Iterator<E> i = deque.iterator(); // Must be in synchronized block
          while (i.hasNext()) {
            foo(i.next());`
        }
        }```
        
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned deque will be serializable if the specified deque is serializable.

        Arguments
        - deque: the deque to be wrapped in a synchronized view

        Returns
        - a synchronized view of the specified deque

        Since
        - 15.0
        """
        ...
