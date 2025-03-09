"""
Python module generated from Java source file java.util.concurrent.PriorityBlockingQueue

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import MethodHandles
from java.lang.invoke import VarHandle
from java.util import AbstractQueue
from java.util import Arrays
from java.util import Comparator
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Objects
from java.util import PriorityQueue
from java.util import Queue
from java.util import SortedSet
from java.util import Spliterator
from java.util.concurrent import *
from java.util.concurrent.locks import Condition
from java.util.concurrent.locks import ReentrantLock
from java.util.function import Consumer
from java.util.function import Predicate
from jdk.internal.access import SharedSecrets
from jdk.internal.util import ArraysSupport
from typing import Any, Callable, Iterable, Tuple


class PriorityBlockingQueue(AbstractQueue, BlockingQueue, Serializable):
    """
    An unbounded BlockingQueue blocking queue that uses
    the same ordering rules as class PriorityQueue and supplies
    blocking retrieval operations.  While this queue is logically
    unbounded, attempted additions may fail due to resource exhaustion
    (causing `OutOfMemoryError`). This class does not permit
    `null` elements.  A priority queue relying on Comparable natural ordering also does not permit insertion of
    non-comparable objects (doing so results in
    `ClassCastException`).
    
    This class and its iterator implement all of the *optional*
    methods of the Collection and Iterator interfaces.
    The Iterator provided in method .iterator() and the
    Spliterator provided in method .spliterator() are *not*
    guaranteed to traverse the elements of the PriorityBlockingQueue in
    any particular order. If you need ordered traversal, consider using
    `Arrays.sort(pq.toArray())`.  Also, method `drainTo` can
    be used to *remove* some or all elements in priority order and
    place them in another collection.
    
    Operations on this class make no guarantees about the ordering
    of elements with equal priority. If you need to enforce an
    ordering, you can define custom classes or comparators that use a
    secondary key to break ties in primary priority values.  For
    example, here is a class that applies first-in-first-out
    tie-breaking to comparable elements. To use it, you would insert a
    `new FIFOEntry(anEntry)` instead of a plain entry object.
    
    ``` `class FIFOEntry<E extends Comparable<? super E>>
        implements Comparable<FIFOEntry<E>> {
      static final AtomicLong seq = new AtomicLong();
      final long seqNum;
      final E entry;
      public FIFOEntry(E entry) {
        seqNum = seq.getAndIncrement();
        this.entry = entry;`
      public E getEntry() { return entry; }
      public int compareTo(FIFOEntry<E> other) {
        int res = entry.compareTo(other.entry);
        if (res == 0 && other.entry != this.entry)
          res = (seqNum < other.seqNum ? -1 : 1);
        return res;
      }
    }}```
    
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
        Creates a `PriorityBlockingQueue` with the default
        initial capacity (11) that orders its elements according to
        their Comparable natural ordering.
        """
        ...


    def __init__(self, initialCapacity: int):
        """
        Creates a `PriorityBlockingQueue` with the specified
        initial capacity that orders its elements according to their
        Comparable natural ordering.

        Arguments
        - initialCapacity: the initial capacity for this priority queue

        Raises
        - IllegalArgumentException: if `initialCapacity` is less
                than 1
        """
        ...


    def __init__(self, initialCapacity: int, comparator: "Comparator"["E"]):
        """
        Creates a `PriorityBlockingQueue` with the specified initial
        capacity that orders its elements according to the specified
        comparator.

        Arguments
        - initialCapacity: the initial capacity for this priority queue
        - comparator: the comparator that will be used to order this
                priority queue.  If `null`, the Comparable
                natural ordering of the elements will be used.

        Raises
        - IllegalArgumentException: if `initialCapacity` is less
                than 1
        """
        ...


    def __init__(self, c: Iterable["E"]):
        """
        Creates a `PriorityBlockingQueue` containing the elements
        in the specified collection.  If the specified collection is a
        SortedSet or a PriorityBlockingQueue, this
        priority queue will be ordered according to the same ordering.
        Otherwise, this priority queue will be ordered according to the
        Comparable natural ordering of its elements.

        Arguments
        - c: the collection whose elements are to be placed
                into this priority queue

        Raises
        - ClassCastException: if elements of the specified collection
                cannot be compared to one another according to the priority
                queue's ordering
        - NullPointerException: if the specified collection or any
                of its elements are null
        """
        ...


    def add(self, e: "E") -> bool:
        """
        Inserts the specified element into this priority queue.

        Arguments
        - e: the element to add

        Returns
        - `True` (as specified by Collection.add)

        Raises
        - ClassCastException: if the specified element cannot be compared
                with elements currently in the priority queue according to the
                priority queue's ordering
        - NullPointerException: if the specified element is null
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Inserts the specified element into this priority queue.
        As the queue is unbounded, this method will never return `False`.

        Arguments
        - e: the element to add

        Returns
        - `True` (as specified by Queue.offer)

        Raises
        - ClassCastException: if the specified element cannot be compared
                with elements currently in the priority queue according to the
                priority queue's ordering
        - NullPointerException: if the specified element is null
        """
        ...


    def put(self, e: "E") -> None:
        """
        Inserts the specified element into this priority queue.
        As the queue is unbounded, this method will never block.

        Arguments
        - e: the element to add

        Raises
        - ClassCastException: if the specified element cannot be compared
                with elements currently in the priority queue according to the
                priority queue's ordering
        - NullPointerException: if the specified element is null
        """
        ...


    def offer(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Inserts the specified element into this priority queue.
        As the queue is unbounded, this method will never block or
        return `False`.

        Arguments
        - e: the element to add
        - timeout: This parameter is ignored as the method never blocks
        - unit: This parameter is ignored as the method never blocks

        Returns
        - `True` (as specified by
         BlockingQueue.offer(Object,long,TimeUnit) BlockingQueue.offer)

        Raises
        - ClassCastException: if the specified element cannot be compared
                with elements currently in the priority queue according to the
                priority queue's ordering
        - NullPointerException: if the specified element is null
        """
        ...


    def poll(self) -> "E":
        ...


    def take(self) -> "E":
        ...


    def poll(self, timeout: int, unit: "TimeUnit") -> "E":
        ...


    def peek(self) -> "E":
        ...


    def comparator(self) -> "Comparator"["E"]:
        """
        Returns the comparator used to order the elements in this queue,
        or `null` if this queue uses the Comparable
        natural ordering of its elements.

        Returns
        - the comparator used to order the elements in this queue,
                or `null` if this queue uses the natural
                ordering of its elements
        """
        ...


    def size(self) -> int:
        ...


    def remainingCapacity(self) -> int:
        """
        Always returns `Integer.MAX_VALUE` because
        a `PriorityBlockingQueue` is not capacity constrained.

        Returns
        - `Integer.MAX_VALUE` always
        """
        ...


    def remove(self, o: "Object") -> bool:
        """
        Removes a single instance of the specified element from this queue,
        if it is present.  More formally, removes an element `e` such
        that `o.equals(e)`, if this queue contains one or more such
        elements.  Returns `True` if and only if this queue contained
        the specified element (or equivalently, if this queue changed as a
        result of the call).

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


    def toString(self) -> str:
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


    def clear(self) -> None:
        """
        Atomically removes all of the elements from this queue.
        The queue will be empty after this call returns.
        """
        ...


    def toArray(self) -> list["Object"]:
        """
        Returns an array containing all of the elements in this queue.
        The returned array elements are in no particular order.
        
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
        Returns an array containing all of the elements in this queue; the
        runtime type of the returned array is that of the specified array.
        The returned array elements are in no particular order.
        If the queue fits in the specified array, it is returned therein.
        Otherwise, a new array is allocated with the runtime type of the
        specified array and the size of this queue.
        
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
        Returns an iterator over the elements in this queue. The
        iterator does not return the elements in any particular order.
        
        The returned iterator is
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.

        Returns
        - an iterator over the elements in this queue
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Returns a Spliterator over the elements in this queue.
        The spliterator does not traverse elements in any particular order
        (the Spliterator.ORDERED ORDERED characteristic is not reported).
        
        The returned spliterator is
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        
        The `Spliterator` reports Spliterator.SIZED and
        Spliterator.NONNULL.

        Returns
        - a `Spliterator` over the elements in this queue

        Since
        - 1.8

        Unknown Tags
        - The `Spliterator` additionally reports Spliterator.SUBSIZED.
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


    def forEach(self, action: "Consumer"["E"]) -> None:
        """
        Raises
        - NullPointerException: 
        """
        ...
