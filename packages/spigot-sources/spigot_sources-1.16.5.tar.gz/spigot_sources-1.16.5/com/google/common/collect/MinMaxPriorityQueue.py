"""
Python module generated from Java source file com.google.common.collect.MinMaxPriorityQueue

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.common.math import IntMath
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import Weak
from com.google.j2objc.annotations import WeakOuter
from java.util import AbstractQueue
from java.util import ArrayDeque
from java.util import Collections
from java.util import Comparator
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import PriorityQueue
from java.util import Queue
from typing import Any, Callable, Iterable, Tuple


class MinMaxPriorityQueue(AbstractQueue):
    """
    A double-ended priority queue, which provides constant-time access to both
    its least element and its greatest element, as determined by the queue's
    specified comparator. If no comparator is given at creation time, the
    natural order of elements is used. If no maximum size is given at creation time,
    the queue is unbounded.
    
    Usage example: ```   `MinMaxPriorityQueue<User> users = MinMaxPriorityQueue.orderedBy(userComparator)
          .maximumSize(1000)
          .create();````
    
    As a Queue it functions exactly as a PriorityQueue: its
    head element -- the implicit target of the methods .peek(), .poll() and .remove() -- is defined as the *least* element in
    the queue according to the queue's comparator. But unlike a regular priority
    queue, the methods .peekLast, .pollLast and
    .removeLast are also provided, to act on the *greatest* element
    in the queue instead.
    
    A min-max priority queue can be configured with a maximum size. If so,
    each time the size of the queue exceeds that value, the queue automatically
    removes its greatest element according to its comparator (which might be the
    element that was just added). This is different from conventional bounded
    queues, which either block or reject new elements when full.
    
    This implementation is based on the
    <a href="http://portal.acm.org/citation.cfm?id=6621">min-max heap</a>
    developed by Atkinson, et al. Unlike many other double-ended priority queues,
    it stores elements in a single array, as compact as the traditional heap data
    structure used in PriorityQueue.
    
    This class is not thread-safe, and does not accept null elements.
    
    *Performance notes:*
    
    
    - If you only access one end of the queue, and do use a maximum size,
        this class will perform significantly worse than a `PriorityQueue`
        with manual eviction above the maximum size.  In many cases
        Ordering.leastOf may work for your use case with significantly
        improved (and asymptotically superior) performance.
    - The retrieval operations .peek, .peekFirst, .peekLast, .element, and .size are constant-time.
    - The enqueuing and dequeuing operations (.offer, .add, and
        all the forms of .poll and .remove()) run in `O(log n) time`.
    - The .remove(Object) and .contains operations require
        linear (`O(n)`) time.
    - If you only access one end of the queue, and don't use a maximum size,
        this class is functionally equivalent to PriorityQueue, but
        significantly slower.

    Author(s)
    - Torbjorn Gannholm

    Since
    - 8.0
    """

    @staticmethod
    def create() -> "MinMaxPriorityQueue"["E"]:
        """
        Creates a new min-max priority queue with default settings: natural order,
        no maximum size, no initial contents, and an initial expected size of 11.
        """
        ...


    @staticmethod
    def create(initialContents: Iterable["E"]) -> "MinMaxPriorityQueue"["E"]:
        """
        Creates a new min-max priority queue using natural order, no maximum size,
        and initially containing the given elements.
        """
        ...


    @staticmethod
    def orderedBy(comparator: "Comparator"["B"]) -> "Builder"["B"]:
        """
        Creates and returns a new builder, configured to build `MinMaxPriorityQueue` instances that use `comparator` to determine the
        least and greatest elements.
        """
        ...


    @staticmethod
    def expectedSize(expectedSize: int) -> "Builder"["Comparable"]:
        """
        Creates and returns a new builder, configured to build `MinMaxPriorityQueue` instances sized appropriately to hold `expectedSize` elements.
        """
        ...


    @staticmethod
    def maximumSize(maximumSize: int) -> "Builder"["Comparable"]:
        """
        Creates and returns a new builder, configured to build `MinMaxPriorityQueue` instances that are limited to `maximumSize`
        elements. Each time a queue grows beyond this bound, it immediately
        removes its greatest element (according to its comparator), which might be
        the element that was just added.
        """
        ...


    def size(self) -> int:
        ...


    def add(self, element: "E") -> bool:
        """
        Adds the given element to this queue. If this queue has a maximum size,
        after adding `element` the queue will automatically evict its
        greatest element (according to its comparator), which may be `element` itself.

        Returns
        - `True` always
        """
        ...


    def addAll(self, newElements: Iterable["E"]) -> bool:
        ...


    def offer(self, element: "E") -> bool:
        """
        Adds the given element to this queue. If this queue has a maximum size,
        after adding `element` the queue will automatically evict its
        greatest element (according to its comparator), which may be `element` itself.
        """
        ...


    def poll(self) -> "E":
        ...


    def peek(self) -> "E":
        ...


    def pollFirst(self) -> "E":
        """
        Removes and returns the least element of this queue, or returns `null` if the queue is empty.
        """
        ...


    def removeFirst(self) -> "E":
        """
        Removes and returns the least element of this queue.

        Raises
        - NoSuchElementException: if the queue is empty
        """
        ...


    def peekFirst(self) -> "E":
        """
        Retrieves, but does not remove, the least element of this queue, or returns
        `null` if the queue is empty.
        """
        ...


    def pollLast(self) -> "E":
        """
        Removes and returns the greatest element of this queue, or returns `null` if the queue is empty.
        """
        ...


    def removeLast(self) -> "E":
        """
        Removes and returns the greatest element of this queue.

        Raises
        - NoSuchElementException: if the queue is empty
        """
        ...


    def peekLast(self) -> "E":
        """
        Retrieves, but does not remove, the greatest element of this queue, or
        returns `null` if the queue is empty.
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements contained in this collection,
        *in no particular order*.
        
        The iterator is *fail-fast*: If the MinMaxPriorityQueue is modified
        at any time after the iterator is created, in any way except through the
        iterator's own remove method, the iterator will generally throw a
        ConcurrentModificationException. Thus, in the face of concurrent
        modification, the iterator fails quickly and cleanly, rather than risking
        arbitrary, non-deterministic behavior at an undetermined time in the
        future.
        
        Note that the fail-fast behavior of an iterator cannot be guaranteed
        as it is, generally speaking, impossible to make any hard guarantees in the
        presence of unsynchronized concurrent modification.  Fail-fast iterators
        throw `ConcurrentModificationException` on a best-effort basis.
        Therefore, it would be wrong to write a program that depended on this
        exception for its correctness: *the fail-fast behavior of iterators
        should be used only to detect bugs.*

        Returns
        - an iterator over the elements contained in this collection
        """
        ...


    def clear(self) -> None:
        ...


    def toArray(self) -> list["Object"]:
        ...


    def comparator(self) -> "Comparator"["E"]:
        """
        Returns the comparator used to order the elements in this queue. Obeys the
        general contract of PriorityQueue.comparator, but returns Ordering.natural instead of `null` to indicate natural ordering.
        """
        ...


    class Builder:
        """
        The builder class used in creation of min-max priority queues. Instead of
        constructing one directly, use MinMaxPriorityQueue.orderedBy(Comparator), MinMaxPriorityQueue.expectedSize(int) or MinMaxPriorityQueue.maximumSize(int).
        
        Type `<B>`: the upper bound on the eventual type that can be produced by
            this builder (for example, a `Builder<Number>` can produce a
            `Queue<Number>` or `Queue<Integer>` but not a `Queue<Object>`).

        Since
        - 8.0
        """

        def expectedSize(self, expectedSize: int) -> "Builder"["B"]:
            """
            Configures this builder to build min-max priority queues with an initial
            expected size of `expectedSize`.
            """
            ...


        def maximumSize(self, maximumSize: int) -> "Builder"["B"]:
            """
            Configures this builder to build `MinMaxPriorityQueue` instances
            that are limited to `maximumSize` elements. Each time a queue grows
            beyond this bound, it immediately removes its greatest element (according
            to its comparator), which might be the element that was just added.
            """
            ...


        def create(self) -> "MinMaxPriorityQueue"["T"]:
            """
            Builds a new min-max priority queue using the previously specified
            options, and having no initial contents.
            """
            ...


        def create(self, initialContents: Iterable["T"]) -> "MinMaxPriorityQueue"["T"]:
            """
            Builds a new min-max priority queue using the previously specified
            options, and having the given initial elements.
            """
            ...
