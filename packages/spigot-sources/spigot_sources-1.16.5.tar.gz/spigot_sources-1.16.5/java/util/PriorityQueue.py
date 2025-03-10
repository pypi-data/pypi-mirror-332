"""
Python module generated from Java source file java.util.PriorityQueue

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from java.util.function import Consumer
from java.util.function import Predicate
from jdk.internal.access import SharedSecrets
from jdk.internal.util import ArraysSupport
from typing import Any, Callable, Iterable, Tuple


class PriorityQueue(AbstractQueue, Serializable):
    """
    An unbounded priority Queue queue based on a priority heap.
    The elements of the priority queue are ordered according to their
    Comparable natural ordering, or by a Comparator
    provided at queue construction time, depending on which constructor is
    used.  A priority queue does not permit `null` elements.
    A priority queue relying on natural ordering also does not permit
    insertion of non-comparable objects (doing so may result in
    `ClassCastException`).
    
    The *head* of this queue is the *least* element
    with respect to the specified ordering.  If multiple elements are
    tied for least value, the head is one of those elements -- ties are
    broken arbitrarily.  The queue retrieval operations `poll`,
    `remove`, `peek`, and `element` access the
    element at the head of the queue.
    
    A priority queue is unbounded, but has an internal
    *capacity* governing the size of an array used to store the
    elements on the queue.  It is always at least as large as the queue
    size.  As elements are added to a priority queue, its capacity
    grows automatically.  The details of the growth policy are not
    specified.
    
    This class and its iterator implement all of the
    *optional* methods of the Collection and Iterator interfaces.  The Iterator provided in method .iterator() and the Spliterator provided in method .spliterator()
    are *not* guaranteed to traverse the elements of
    the priority queue in any particular order. If you need ordered
    traversal, consider using `Arrays.sort(pq.toArray())`.
    
    <strong>Note that this implementation is not synchronized.</strong>
    Multiple threads should not access a `PriorityQueue`
    instance concurrently if any of the threads modifies the queue.
    Instead, use the thread-safe java.util.concurrent.PriorityBlockingQueue class.
    
    Implementation note: this implementation provides
    O(log(n)) time for the enqueuing and dequeuing methods
    (`offer`, `poll`, `remove()` and `add`);
    linear time for the `remove(Object)` and `contains(Object)`
    methods; and constant time for the retrieval methods
    (`peek`, `element`, and `size`).
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this queue

    Author(s)
    - Josh Bloch, Doug Lea

    Since
    - 1.5
    """

    def __init__(self):
        """
        Creates a `PriorityQueue` with the default initial
        capacity (11) that orders its elements according to their
        Comparable natural ordering.
        """
        ...


    def __init__(self, initialCapacity: int):
        """
        Creates a `PriorityQueue` with the specified initial
        capacity that orders its elements according to their
        Comparable natural ordering.

        Arguments
        - initialCapacity: the initial capacity for this priority queue

        Raises
        - IllegalArgumentException: if `initialCapacity` is less
                than 1
        """
        ...


    def __init__(self, comparator: "Comparator"["E"]):
        """
        Creates a `PriorityQueue` with the default initial capacity and
        whose elements are ordered according to the specified comparator.

        Arguments
        - comparator: the comparator that will be used to order this
                priority queue.  If `null`, the Comparable
                natural ordering of the elements will be used.

        Since
        - 1.8
        """
        ...


    def __init__(self, initialCapacity: int, comparator: "Comparator"["E"]):
        """
        Creates a `PriorityQueue` with the specified initial capacity
        that orders its elements according to the specified comparator.

        Arguments
        - initialCapacity: the initial capacity for this priority queue
        - comparator: the comparator that will be used to order this
                priority queue.  If `null`, the Comparable
                natural ordering of the elements will be used.

        Raises
        - IllegalArgumentException: if `initialCapacity` is
                less than 1
        """
        ...


    def __init__(self, c: Iterable["E"]):
        """
        Creates a `PriorityQueue` containing the elements in the
        specified collection.  If the specified collection is an instance of
        a SortedSet or is another `PriorityQueue`, this
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


    def __init__(self, c: "PriorityQueue"["E"]):
        """
        Creates a `PriorityQueue` containing the elements in the
        specified priority queue.  This priority queue will be
        ordered according to the same ordering as the given priority
        queue.

        Arguments
        - c: the priority queue whose elements are to be placed
                into this priority queue

        Raises
        - ClassCastException: if elements of `c` cannot be
                compared to one another according to `c`'s
                ordering
        - NullPointerException: if the specified priority queue or any
                of its elements are null
        """
        ...


    def __init__(self, c: "SortedSet"["E"]):
        """
        Creates a `PriorityQueue` containing the elements in the
        specified sorted set.   This priority queue will be ordered
        according to the same ordering as the given sorted set.

        Arguments
        - c: the sorted set whose elements are to be placed
                into this priority queue

        Raises
        - ClassCastException: if elements of the specified sorted
                set cannot be compared to one another according to the
                sorted set's ordering
        - NullPointerException: if the specified sorted set or any
                of its elements are null
        """
        ...


    def add(self, e: "E") -> bool:
        """
        Inserts the specified element into this priority queue.

        Returns
        - `True` (as specified by Collection.add)

        Raises
        - ClassCastException: if the specified element cannot be
                compared with elements currently in this priority queue
                according to the priority queue's ordering
        - NullPointerException: if the specified element is null
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Inserts the specified element into this priority queue.

        Returns
        - `True` (as specified by Queue.offer)

        Raises
        - ClassCastException: if the specified element cannot be
                compared with elements currently in this priority queue
                according to the priority queue's ordering
        - NullPointerException: if the specified element is null
        """
        ...


    def peek(self) -> "E":
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


    def toArray(self) -> list["Object"]:
        """
        Returns an array containing all of the elements in this queue.
        The elements are in no particular order.
        
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
        
        If the queue fits in the specified array with room to spare
        (i.e., the array has more elements than the queue), the element in
        the array immediately following the end of the collection is set to
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
                 same runtime type is allocated for this purpose.

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
        Returns an iterator over the elements in this queue. The iterator
        does not return the elements in any particular order.

        Returns
        - an iterator over the elements in this queue
        """
        ...


    def size(self) -> int:
        ...


    def clear(self) -> None:
        """
        Removes all of the elements from this priority queue.
        The queue will be empty after this call returns.
        """
        ...


    def poll(self) -> "E":
        ...


    def comparator(self) -> "Comparator"["E"]:
        """
        Returns the comparator used to order the elements in this
        queue, or `null` if this queue is sorted according to
        the Comparable natural ordering of its elements.

        Returns
        - the comparator used to order this queue, or
                `null` if this queue is sorted according to the
                natural ordering of its elements
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Creates a *<a href="Spliterator.html#binding">late-binding</a>*
        and *fail-fast* Spliterator over the elements in this
        queue. The spliterator does not traverse elements in any particular order
        (the Spliterator.ORDERED ORDERED characteristic is not reported).
        
        The `Spliterator` reports Spliterator.SIZED,
        Spliterator.SUBSIZED, and Spliterator.NONNULL.
        Overriding implementations should document the reporting of additional
        characteristic values.

        Returns
        - a `Spliterator` over the elements in this queue

        Since
        - 1.8
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
