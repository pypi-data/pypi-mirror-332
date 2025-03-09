"""
Python module generated from Java source file java.util.concurrent.ConcurrentLinkedQueue

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import MethodHandles
from java.lang.invoke import VarHandle
from java.util import AbstractQueue
from java.util import Arrays
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Objects
from java.util import Queue
from java.util import Spliterator
from java.util.concurrent import *
from java.util.function import Consumer
from java.util.function import Predicate
from typing import Any, Callable, Iterable, Tuple


class ConcurrentLinkedQueue(AbstractQueue, Queue, Serializable):
    """
    An unbounded thread-safe Queue queue based on linked nodes.
    This queue orders elements FIFO (first-in-first-out).
    The *head* of the queue is that element that has been on the
    queue the longest time.
    The *tail* of the queue is that element that has been on the
    queue the shortest time. New elements
    are inserted at the tail of the queue, and the queue retrieval
    operations obtain elements at the head of the queue.
    A `ConcurrentLinkedQueue` is an appropriate choice when
    many threads will share access to a common collection.
    Like most other concurrent collection implementations, this class
    does not permit the use of `null` elements.
    
    This implementation employs an efficient *non-blocking*
    algorithm based on one described in
    <a href="http://www.cs.rochester.edu/~scott/papers/1996_PODC_queues.pdf">
    Simple, Fast, and Practical Non-Blocking and Blocking Concurrent Queue
    Algorithms</a> by Maged M. Michael and Michael L. Scott.
    
    Iterators are *weakly consistent*, returning elements
    reflecting the state of the queue at some point at or since the
    creation of the iterator.  They do *not* throw java.util.ConcurrentModificationException, and may proceed concurrently
    with other operations.  Elements contained in the queue since the creation
    of the iterator will be returned exactly once.
    
    Beware that, unlike in most collections, the `size` method
    is *NOT* a constant-time operation. Because of the
    asynchronous nature of these queues, determining the current number
    of elements requires a traversal of the elements, and so may report
    inaccurate results if this collection is modified during traversal.
    
    Bulk operations that add, remove, or examine multiple elements,
    such as .addAll, .removeIf or .forEach,
    are *not* guaranteed to be performed atomically.
    For example, a `forEach` traversal concurrent with an `addAll` operation might observe only some of the added elements.
    
    This class and its iterator implement all of the *optional*
    methods of the Queue and Iterator interfaces.
    
    Memory consistency effects: As with other concurrent
    collections, actions in a thread prior to placing an object into a
    `ConcurrentLinkedQueue`
    <a href="package-summary.html#MemoryVisibility">*happen-before*</a>
    actions subsequent to the access or removal of that element from
    the `ConcurrentLinkedQueue` in another thread.
    
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
        Creates a `ConcurrentLinkedQueue` that is initially empty.
        """
        ...


    def __init__(self, c: Iterable["E"]):
        """
        Creates a `ConcurrentLinkedQueue`
        initially containing the elements of the given collection,
        added in traversal order of the collection's iterator.

        Arguments
        - c: the collection of elements to initially contain

        Raises
        - NullPointerException: if the specified collection or any
                of its elements are null
        """
        ...


    def add(self, e: "E") -> bool:
        """
        Inserts the specified element at the tail of this queue.
        As the queue is unbounded, this method will never throw
        IllegalStateException or return `False`.

        Returns
        - `True` (as specified by Collection.add)

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Inserts the specified element at the tail of this queue.
        As the queue is unbounded, this method will never return `False`.

        Returns
        - `True` (as specified by Queue.offer)

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def poll(self) -> "E":
        ...


    def peek(self) -> "E":
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if this queue contains no elements.

        Returns
        - `True` if this queue contains no elements
        """
        ...


    def size(self) -> int:
        """
        Returns the number of elements in this queue.  If this queue
        contains more than `Integer.MAX_VALUE` elements, returns
        `Integer.MAX_VALUE`.
        
        Beware that, unlike in most collections, this method is
        *NOT* a constant-time operation. Because of the
        asynchronous nature of these queues, determining the current
        number of elements requires an O(n) traversal.
        Additionally, if elements are added or removed during execution
        of this method, the returned result may be inaccurate.  Thus,
        this method is typically not very useful in concurrent
        applications.

        Returns
        - the number of elements in this queue
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


    def addAll(self, c: Iterable["E"]) -> bool:
        """
        Appends all of the elements in the specified collection to the end of
        this queue, in the order that they are returned by the specified
        collection's iterator.  Attempts to `addAll` of a queue to
        itself result in `IllegalArgumentException`.

        Arguments
        - c: the elements to be inserted into this queue

        Returns
        - `True` if this queue changed as a result of the call

        Raises
        - NullPointerException: if the specified collection or any
                of its elements are null
        - IllegalArgumentException: if the collection is this queue
        """
        ...


    def toString(self) -> str:
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


    def clear(self) -> None:
        ...


    def forEach(self, action: "Consumer"["E"]) -> None:
        """
        Raises
        - NullPointerException: 
        """
        ...
