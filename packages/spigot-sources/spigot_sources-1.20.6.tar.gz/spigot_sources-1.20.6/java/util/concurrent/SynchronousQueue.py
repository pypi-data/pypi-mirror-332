"""
Python module generated from Java source file java.util.concurrent.SynchronousQueue

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import MethodHandles
from java.lang.invoke import VarHandle
from java.util import AbstractQueue
from java.util import Collections
from java.util import Iterator
from java.util import Objects
from java.util import Spliterator
from java.util.concurrent import *
from java.util.concurrent.locks import LockSupport
from java.util.concurrent.locks import ReentrantLock
from typing import Any, Callable, Iterable, Tuple


class SynchronousQueue(AbstractQueue, BlockingQueue, Serializable):
    """
    A BlockingQueue blocking queue in which each insert
    operation must wait for a corresponding remove operation by another
    thread, and vice versa.  A synchronous queue does not have any
    internal capacity, not even a capacity of one.  You cannot
    `peek` at a synchronous queue because an element is only
    present when you try to remove it; you cannot insert an element
    (using any method) unless another thread is trying to remove it;
    you cannot iterate as there is nothing to iterate.  The
    *head* of the queue is the element that the first queued
    inserting thread is trying to add to the queue; if there is no such
    queued thread then no element is available for removal and
    `poll()` will return `null`.  For purposes of other
    `Collection` methods (for example `contains`), a
    `SynchronousQueue` acts as an empty collection.  This queue
    does not permit `null` elements.
    
    Synchronous queues are similar to rendezvous channels used in
    CSP and Ada. They are well suited for handoff designs, in which an
    object running in one thread must sync up with an object running
    in another thread in order to hand it some information, event, or
    task.
    
    This class supports an optional fairness policy for ordering
    waiting producer and consumer threads.  By default, this ordering
    is not guaranteed. However, a queue constructed with fairness set
    to `True` grants threads access in FIFO order.
    
    This class and its iterator implement all of the *optional*
    methods of the Collection and Iterator interfaces.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this queue

    Author(s)
    - Doug Lea and Bill Scherer and Michael Scott

    Since
    - 1.5
    """

    def __init__(self):
        """
        Creates a `SynchronousQueue` with nonfair access policy.
        """
        ...


    def __init__(self, fair: bool):
        """
        Creates a `SynchronousQueue` with the specified fairness policy.

        Arguments
        - fair: if True, waiting threads contend in FIFO order for
               access; otherwise the order is unspecified.
        """
        ...


    def put(self, e: "E") -> None:
        """
        Adds the specified element to this queue, waiting if necessary for
        another thread to receive it.

        Raises
        - InterruptedException: 
        - NullPointerException: 
        """
        ...


    def offer(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Inserts the specified element into this queue, waiting if necessary
        up to the specified wait time for another thread to receive it.

        Returns
        - `True` if successful, or `False` if the
                specified waiting time elapses before a consumer appears

        Raises
        - InterruptedException: 
        - NullPointerException: 
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Inserts the specified element into this queue, if another thread is
        waiting to receive it.

        Arguments
        - e: the element to add

        Returns
        - `True` if the element was added to this queue, else
                `False`

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def take(self) -> "E":
        """
        Retrieves and removes the head of this queue, waiting if necessary
        for another thread to insert it.

        Returns
        - the head of this queue

        Raises
        - InterruptedException: 
        """
        ...


    def poll(self, timeout: int, unit: "TimeUnit") -> "E":
        """
        Retrieves and removes the head of this queue, waiting
        if necessary up to the specified wait time, for another thread
        to insert it.

        Returns
        - the head of this queue, or `null` if the
                specified waiting time elapses before an element is present

        Raises
        - InterruptedException: 
        """
        ...


    def poll(self) -> "E":
        """
        Retrieves and removes the head of this queue, if another thread
        is currently making an element available.

        Returns
        - the head of this queue, or `null` if no
                element is available
        """
        ...


    def isEmpty(self) -> bool:
        """
        Always returns `True`.
        A `SynchronousQueue` has no internal capacity.

        Returns
        - `True`
        """
        ...


    def size(self) -> int:
        """
        Always returns zero.
        A `SynchronousQueue` has no internal capacity.

        Returns
        - zero
        """
        ...


    def remainingCapacity(self) -> int:
        """
        Always returns zero.
        A `SynchronousQueue` has no internal capacity.

        Returns
        - zero
        """
        ...


    def clear(self) -> None:
        """
        Does nothing.
        A `SynchronousQueue` has no internal capacity.
        """
        ...


    def contains(self, o: "Object") -> bool:
        """
        Always returns `False`.
        A `SynchronousQueue` has no internal capacity.

        Arguments
        - o: the element

        Returns
        - `False`
        """
        ...


    def remove(self, o: "Object") -> bool:
        """
        Always returns `False`.
        A `SynchronousQueue` has no internal capacity.

        Arguments
        - o: the element to remove

        Returns
        - `False`
        """
        ...


    def containsAll(self, c: Iterable[Any]) -> bool:
        """
        Returns `False` unless the given collection is empty.
        A `SynchronousQueue` has no internal capacity.

        Arguments
        - c: the collection

        Returns
        - `False` unless given collection is empty
        """
        ...


    def removeAll(self, c: Iterable[Any]) -> bool:
        """
        Always returns `False`.
        A `SynchronousQueue` has no internal capacity.

        Arguments
        - c: the collection

        Returns
        - `False`
        """
        ...


    def retainAll(self, c: Iterable[Any]) -> bool:
        """
        Always returns `False`.
        A `SynchronousQueue` has no internal capacity.

        Arguments
        - c: the collection

        Returns
        - `False`
        """
        ...


    def peek(self) -> "E":
        """
        Always returns `null`.
        A `SynchronousQueue` does not return elements
        unless actively waited on.

        Returns
        - `null`
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an empty iterator in which `hasNext` always returns
        `False`.

        Returns
        - an empty iterator
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Returns an empty spliterator in which calls to
        Spliterator.trySplit() trySplit always return `null`.

        Returns
        - an empty spliterator

        Since
        - 1.8
        """
        ...


    def toArray(self) -> list["Object"]:
        """
        Returns a zero-length array.

        Returns
        - a zero-length array
        """
        ...


    def toArray(self, a: list["T"]) -> list["T"]:
        """
        Sets the zeroth element of the specified array to `null`
        (if the array has non-zero length) and returns it.

        Arguments
        - a: the array

        Returns
        - the specified array

        Raises
        - NullPointerException: if the specified array is null
        """
        ...


    def toString(self) -> str:
        """
        Always returns `"[]"`.

        Returns
        - `"[]"`
        """
        ...


    def drainTo(self, c: Iterable["E"]) -> int:
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def drainTo(self, c: Iterable["E"], maxElements: int) -> int:
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...
