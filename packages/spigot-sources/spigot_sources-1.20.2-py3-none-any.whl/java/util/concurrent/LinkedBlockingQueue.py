"""
Python module generated from Java source file java.util.concurrent.LinkedBlockingQueue

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import AbstractQueue
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Objects
from java.util import Spliterator
from java.util.concurrent import *
from java.util.concurrent.atomic import AtomicInteger
from java.util.concurrent.locks import Condition
from java.util.concurrent.locks import ReentrantLock
from java.util.function import Consumer
from java.util.function import Predicate
from typing import Any, Callable, Iterable, Tuple


class LinkedBlockingQueue(AbstractQueue, BlockingQueue, Serializable):
    """
    An optionally-bounded BlockingQueue blocking queue based on
    linked nodes.
    This queue orders elements FIFO (first-in-first-out).
    The *head* of the queue is that element that has been on the
    queue the longest time.
    The *tail* of the queue is that element that has been on the
    queue the shortest time. New elements
    are inserted at the tail of the queue, and the queue retrieval
    operations obtain elements at the head of the queue.
    Linked queues typically have higher throughput than array-based queues but
    less predictable performance in most concurrent applications.
    
    The optional capacity bound constructor argument serves as a
    way to prevent excessive queue expansion. The capacity, if unspecified,
    is equal to Integer.MAX_VALUE.  Linked nodes are
    dynamically created upon each insertion unless this would bring the
    queue above capacity.
    
    This class and its iterator implement all of the *optional*
    methods of the Collection and Iterator interfaces.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this queue

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self):
        """
        Creates a `LinkedBlockingQueue` with a capacity of
        Integer.MAX_VALUE.
        """
        ...


    def __init__(self, capacity: int):
        """
        Creates a `LinkedBlockingQueue` with the given (fixed) capacity.

        Arguments
        - capacity: the capacity of this queue

        Raises
        - IllegalArgumentException: if `capacity` is not greater
                than zero
        """
        ...


    def __init__(self, c: Iterable["E"]):
        """
        Creates a `LinkedBlockingQueue` with a capacity of
        Integer.MAX_VALUE, initially containing the elements of the
        given collection,
        added in traversal order of the collection's iterator.

        Arguments
        - c: the collection of elements to initially contain

        Raises
        - NullPointerException: if the specified collection or any
                of its elements are null
        """
        ...


    def size(self) -> int:
        """
        Returns the number of elements in this queue.

        Returns
        - the number of elements in this queue
        """
        ...


    def remainingCapacity(self) -> int:
        """
        Returns the number of additional elements that this queue can ideally
        (in the absence of memory or resource constraints) accept without
        blocking. This is always equal to the initial capacity of this queue
        less the current `size` of this queue.
        
        Note that you *cannot* always tell if an attempt to insert
        an element will succeed by inspecting `remainingCapacity`
        because it may be the case that another thread is about to
        insert or remove an element.
        """
        ...


    def put(self, e: "E") -> None:
        """
        Inserts the specified element at the tail of this queue, waiting if
        necessary for space to become available.

        Raises
        - InterruptedException: 
        - NullPointerException: 
        """
        ...


    def offer(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Inserts the specified element at the tail of this queue, waiting if
        necessary up to the specified wait time for space to become available.

        Returns
        - `True` if successful, or `False` if
                the specified waiting time elapses before space is available

        Raises
        - InterruptedException: 
        - NullPointerException: 
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Inserts the specified element at the tail of this queue if it is
        possible to do so immediately without exceeding the queue's capacity,
        returning `True` upon success and `False` if this queue
        is full.
        When using a capacity-restricted queue, this method is generally
        preferable to method BlockingQueue.add add, which can fail to
        insert an element only by throwing an exception.

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def take(self) -> "E":
        ...


    def poll(self, timeout: int, unit: "TimeUnit") -> "E":
        ...


    def poll(self) -> "E":
        ...


    def peek(self) -> "E":
        ...


    def remove(self, o: "Object") -> bool:
        """
        Removes a single instance of the specified element from this queue,
        if it is present.  More formally, removes an element `e` such
        that `o.equals(e)`, if this queue contains one or more such
        elements.
        Returns `True` if this queue contained the specified element
        (or equivalently, if this queue changed as a result of the call).

        Arguments
        - o: element to be removed from this queue, if present

        Returns
        - `True` if this queue changed as a result of the call
        """
        ...


    def contains(self, o: "Object") -> bool:
        """
        Returns `True` if this queue contains the specified element.
        More formally, returns `True` if and only if this queue contains
        at least one element `e` such that `o.equals(e)`.

        Arguments
        - o: object to be checked for containment in this queue

        Returns
        - `True` if this queue contains the specified element
        """
        ...


    def toArray(self) -> list["Object"]:
        """
        Returns an array containing all of the elements in this queue, in
        proper sequence.
        
        The returned array will be "safe" in that no references to it are
        maintained by this queue.  (In other words, this method must allocate
        a new array).  The caller is thus free to modify the returned array.
        
        This method acts as bridge between array-based and collection-based
        APIs.

        Returns
        - an array containing all of the elements in this queue
        """
        ...


    def toArray(self, a: list["T"]) -> list["T"]:
        """
        Returns an array containing all of the elements in this queue, in
        proper sequence; the runtime type of the returned array is that of
        the specified array.  If the queue fits in the specified array, it
        is returned therein.  Otherwise, a new array is allocated with the
        runtime type of the specified array and the size of this queue.
        
        If this queue fits in the specified array with room to spare
        (i.e., the array has more elements than this queue), the element in
        the array immediately following the end of the queue is set to
        `null`.
        
        Like the .toArray() method, this method acts as bridge between
        array-based and collection-based APIs.  Further, this method allows
        precise control over the runtime type of the output array, and may,
        under certain circumstances, be used to save allocation costs.
        
        Suppose `x` is a queue known to contain only strings.
        The following code can be used to dump the queue into a newly
        allocated array of `String`:
        
        ``` `String[] y = x.toArray(new String[0]);````
        
        Note that `toArray(new Object[0])` is identical in function to
        `toArray()`.

        Arguments
        - a: the array into which the elements of the queue are to
                 be stored, if it is big enough; otherwise, a new array of the
                 same runtime type is allocated for this purpose

        Returns
        - an array containing all of the elements in this queue

        Raises
        - ArrayStoreException: if the runtime type of the specified array
                is not a supertype of the runtime type of every element in
                this queue
        - NullPointerException: if the specified array is null
        """
        ...


    def toString(self) -> str:
        ...


    def clear(self) -> None:
        """
        Atomically removes all of the elements from this queue.
        The queue will be empty after this call returns.
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


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this queue in proper sequence.
        The elements will be returned in order from first (head) to last (tail).
        
        The returned iterator is
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.

        Returns
        - an iterator over the elements in this queue in proper sequence
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Returns a Spliterator over the elements in this queue.
        
        The returned spliterator is
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        
        The `Spliterator` reports Spliterator.CONCURRENT,
        Spliterator.ORDERED, and Spliterator.NONNULL.

        Returns
        - a `Spliterator` over the elements in this queue

        Since
        - 1.8

        Unknown Tags
        - The `Spliterator` implements `trySplit` to permit limited
        parallelism.
        """
        ...


    def forEach(self, action: "Consumer"["E"]) -> None:
        """
        Raises
        - NullPointerException: 
        """
        ...


    def removeIf(self, filter: "Predicate"["E"]) -> bool:
        """
        Raises
        - NullPointerException: 
        """
        ...


    def removeAll(self, c: Iterable[Any]) -> bool:
        """
        Raises
        - NullPointerException: 
        """
        ...


    def retainAll(self, c: Iterable[Any]) -> bool:
        """
        Raises
        - NullPointerException: 
        """
        ...
