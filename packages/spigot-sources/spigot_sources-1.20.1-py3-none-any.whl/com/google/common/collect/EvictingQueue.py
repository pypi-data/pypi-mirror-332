"""
Python module generated from Java source file com.google.common.collect.EvictingQueue

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import Serializable
from java.util import ArrayDeque
from java.util import Queue
from typing import Any, Callable, Iterable, Tuple


class EvictingQueue(ForwardingQueue, Serializable):
    """
    A non-blocking queue which automatically evicts elements from the head of the queue when
    attempting to add new elements onto the queue and it is full. This queue orders elements FIFO
    (first-in-first-out). This data structure is logically equivalent to a circular buffer (i.e.,
    cyclic buffer or ring buffer).
    
    An evicting queue must be configured with a maximum size. Each time an element is added to a
    full queue, the queue automatically removes its head element. This is different from conventional
    bounded queues, which either block or reject new elements when full.
    
    This class is not thread-safe, and does not accept null elements.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 15.0
    """

    @staticmethod
    def create(maxSize: int) -> "EvictingQueue"["E"]:
        """
        Creates and returns a new evicting queue that will hold up to `maxSize` elements.
        
        When `maxSize` is zero, elements will be evicted immediately after being added to the
        queue.
        """
        ...


    def remainingCapacity(self) -> int:
        """
        Returns the number of additional elements that this queue can accept without evicting; zero if
        the queue is currently full.

        Since
        - 16.0
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Adds the given element to this queue. If the queue is currently full, the element at the head
        of the queue is evicted to make room.

        Returns
        - `True` always
        """
        ...


    def add(self, e: "E") -> bool:
        """
        Adds the given element to this queue. If the queue is currently full, the element at the head
        of the queue is evicted to make room.

        Returns
        - `True` always
        """
        ...


    def addAll(self, collection: Iterable["E"]) -> bool:
        ...


    def toArray(self) -> list["Object"]:
        ...
