"""
Python module generated from Java source file java.util.concurrent.LinkedBlockingDeque

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
from java.util.concurrent.locks import Condition
from java.util.concurrent.locks import ReentrantLock
from java.util.function import Consumer
from java.util.function import Predicate
from typing import Any, Callable, Iterable, Tuple


class LinkedBlockingDeque(AbstractQueue, BlockingDeque, Serializable):
    """
    An optionally-bounded BlockingDeque blocking deque based on
    linked nodes.
    
    The optional capacity bound constructor argument serves as a
    way to prevent excessive expansion. The capacity, if unspecified,
    is equal to Integer.MAX_VALUE.  Linked nodes are
    dynamically created upon each insertion unless this would bring the
    deque above capacity.
    
    Most operations run in constant time (ignoring time spent
    blocking).  Exceptions include .remove(Object) remove,
    .removeFirstOccurrence removeFirstOccurrence, .removeLastOccurrence removeLastOccurrence, .contains
    contains, .iterator iterator.remove(), and the bulk
    operations, all of which run in linear time.
    
    This class and its iterator implement all of the *optional*
    methods of the Collection and Iterator interfaces.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this deque

    Author(s)
    - Doug Lea

    Since
    - 1.6
    """

    def __init__(self):
        """
        Creates a `LinkedBlockingDeque` with a capacity of
        Integer.MAX_VALUE.
        """
        ...


    def __init__(self, capacity: int):
        """
        Creates a `LinkedBlockingDeque` with the given (fixed) capacity.

        Arguments
        - capacity: the capacity of this deque

        Raises
        - IllegalArgumentException: if `capacity` is less than 1
        """
        ...


    def __init__(self, c: Iterable["E"]):
        """
        Creates a `LinkedBlockingDeque` with a capacity of
        Integer.MAX_VALUE, initially containing the elements of
        the given collection, added in traversal order of the
        collection's iterator.

        Arguments
        - c: the collection of elements to initially contain

        Raises
        - NullPointerException: if the specified collection or any
                of its elements are null
        """
        ...


    def addFirst(self, e: "E") -> None:
        """
        Raises
        - IllegalStateException: if this deque is full
        - NullPointerException: 
        """
        ...


    def addLast(self, e: "E") -> None:
        """
        Raises
        - IllegalStateException: if this deque is full
        - NullPointerException: 
        """
        ...


    def offerFirst(self, e: "E") -> bool:
        """
        Raises
        - NullPointerException: 
        """
        ...


    def offerLast(self, e: "E") -> bool:
        """
        Raises
        - NullPointerException: 
        """
        ...


    def putFirst(self, e: "E") -> None:
        """
        Raises
        - NullPointerException: 
        - InterruptedException: 
        """
        ...


    def putLast(self, e: "E") -> None:
        """
        Raises
        - NullPointerException: 
        - InterruptedException: 
        """
        ...


    def offerFirst(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Raises
        - NullPointerException: 
        - InterruptedException: 
        """
        ...


    def offerLast(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Raises
        - NullPointerException: 
        - InterruptedException: 
        """
        ...


    def removeFirst(self) -> "E":
        """
        Raises
        - NoSuchElementException: 
        """
        ...


    def removeLast(self) -> "E":
        """
        Raises
        - NoSuchElementException: 
        """
        ...


    def pollFirst(self) -> "E":
        ...


    def pollLast(self) -> "E":
        ...


    def takeFirst(self) -> "E":
        ...


    def takeLast(self) -> "E":
        ...


    def pollFirst(self, timeout: int, unit: "TimeUnit") -> "E":
        ...


    def pollLast(self, timeout: int, unit: "TimeUnit") -> "E":
        ...


    def getFirst(self) -> "E":
        """
        Raises
        - NoSuchElementException: 
        """
        ...


    def getLast(self) -> "E":
        """
        Raises
        - NoSuchElementException: 
        """
        ...


    def peekFirst(self) -> "E":
        ...


    def peekLast(self) -> "E":
        ...


    def removeFirstOccurrence(self, o: "Object") -> bool:
        ...


    def removeLastOccurrence(self, o: "Object") -> bool:
        ...


    def add(self, e: "E") -> bool:
        """
        Inserts the specified element at the end of this deque unless it would
        violate capacity restrictions.  When using a capacity-restricted deque,
        it is generally preferable to use method .offer(Object) offer.
        
        This method is equivalent to .addLast.

        Raises
        - IllegalStateException: if this deque is full
        - NullPointerException: if the specified element is null
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def put(self, e: "E") -> None:
        """
        Raises
        - NullPointerException: 
        - InterruptedException: 
        """
        ...


    def offer(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Raises
        - NullPointerException: 
        - InterruptedException: 
        """
        ...


    def remove(self) -> "E":
        """
        Retrieves and removes the head of the queue represented by this deque.
        This method differs from .poll() poll() only in that it throws an
        exception if this deque is empty.
        
        This method is equivalent to .removeFirst() removeFirst.

        Returns
        - the head of the queue represented by this deque

        Raises
        - NoSuchElementException: if this deque is empty
        """
        ...


    def poll(self) -> "E":
        ...


    def take(self) -> "E":
        ...


    def poll(self, timeout: int, unit: "TimeUnit") -> "E":
        ...


    def element(self) -> "E":
        """
        Retrieves, but does not remove, the head of the queue represented by
        this deque.  This method differs from .peek() peek() only in that
        it throws an exception if this deque is empty.
        
        This method is equivalent to .getFirst() getFirst.

        Returns
        - the head of the queue represented by this deque

        Raises
        - NoSuchElementException: if this deque is empty
        """
        ...


    def peek(self) -> "E":
        ...


    def remainingCapacity(self) -> int:
        """
        Returns the number of additional elements that this deque can ideally
        (in the absence of memory or resource constraints) accept without
        blocking. This is always equal to the initial capacity of this deque
        less the current `size` of this deque.
        
        Note that you *cannot* always tell if an attempt to insert
        an element will succeed by inspecting `remainingCapacity`
        because it may be the case that another thread is about to
        insert or remove an element.
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


    def push(self, e: "E") -> None:
        """
        Raises
        - IllegalStateException: if this deque is full
        - NullPointerException: 
        """
        ...


    def pop(self) -> "E":
        """
        Raises
        - NoSuchElementException: 
        """
        ...


    def remove(self, o: "Object") -> bool:
        """
        Removes the first occurrence of the specified element from this deque.
        If the deque does not contain the element, it is unchanged.
        More formally, removes the first element `e` such that
        `o.equals(e)` (if such an element exists).
        Returns `True` if this deque contained the specified element
        (or equivalently, if this deque changed as a result of the call).
        
        This method is equivalent to
        .removeFirstOccurrence(Object) removeFirstOccurrence.

        Arguments
        - o: element to be removed from this deque, if present

        Returns
        - `True` if this deque changed as a result of the call
        """
        ...


    def size(self) -> int:
        """
        Returns the number of elements in this deque.

        Returns
        - the number of elements in this deque
        """
        ...


    def contains(self, o: "Object") -> bool:
        """
        Returns `True` if this deque contains the specified element.
        More formally, returns `True` if and only if this deque contains
        at least one element `e` such that `o.equals(e)`.

        Arguments
        - o: object to be checked for containment in this deque

        Returns
        - `True` if this deque contains the specified element
        """
        ...


    def addAll(self, c: Iterable["E"]) -> bool:
        """
        Appends all of the elements in the specified collection to the end of
        this deque, in the order that they are returned by the specified
        collection's iterator.  Attempts to `addAll` of a deque to
        itself result in `IllegalArgumentException`.

        Arguments
        - c: the elements to be inserted into this deque

        Returns
        - `True` if this deque changed as a result of the call

        Raises
        - NullPointerException: if the specified collection or any
                of its elements are null
        - IllegalArgumentException: if the collection is this deque
        - IllegalStateException: if this deque is full

        See
        - .add(Object)
        """
        ...


    def toArray(self) -> list["Object"]:
        """
        Returns an array containing all of the elements in this deque, in
        proper sequence (from first to last element).
        
        The returned array will be "safe" in that no references to it are
        maintained by this deque.  (In other words, this method must allocate
        a new array).  The caller is thus free to modify the returned array.
        
        This method acts as bridge between array-based and collection-based
        APIs.

        Returns
        - an array containing all of the elements in this deque
        """
        ...


    def toArray(self, a: list["T"]) -> list["T"]:
        """
        Returns an array containing all of the elements in this deque, in
        proper sequence; the runtime type of the returned array is that of
        the specified array.  If the deque fits in the specified array, it
        is returned therein.  Otherwise, a new array is allocated with the
        runtime type of the specified array and the size of this deque.
        
        If this deque fits in the specified array with room to spare
        (i.e., the array has more elements than this deque), the element in
        the array immediately following the end of the deque is set to
        `null`.
        
        Like the .toArray() method, this method acts as bridge between
        array-based and collection-based APIs.  Further, this method allows
        precise control over the runtime type of the output array, and may,
        under certain circumstances, be used to save allocation costs.
        
        Suppose `x` is a deque known to contain only strings.
        The following code can be used to dump the deque into a newly
        allocated array of `String`:
        
        ``` `String[] y = x.toArray(new String[0]);````
        
        Note that `toArray(new Object[0])` is identical in function to
        `toArray()`.

        Arguments
        - a: the array into which the elements of the deque are to
                 be stored, if it is big enough; otherwise, a new array of the
                 same runtime type is allocated for this purpose

        Returns
        - an array containing all of the elements in this deque

        Raises
        - ArrayStoreException: if the runtime type of the specified array
                is not a supertype of the runtime type of every element in
                this deque
        - NullPointerException: if the specified array is null
        """
        ...


    def toString(self) -> str:
        ...


    def clear(self) -> None:
        """
        Atomically removes all of the elements from this deque.
        The deque will be empty after this call returns.
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this deque in proper sequence.
        The elements will be returned in order from first (head) to last (tail).
        
        The returned iterator is
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.

        Returns
        - an iterator over the elements in this deque in proper sequence
        """
        ...


    def descendingIterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this deque in reverse
        sequential order.  The elements will be returned in order from
        last (tail) to first (head).
        
        The returned iterator is
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.

        Returns
        - an iterator over the elements in this deque in reverse order
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Returns a Spliterator over the elements in this deque.
        
        The returned spliterator is
        <a href="package-summary.html#Weakly">*weakly consistent*</a>.
        
        The `Spliterator` reports Spliterator.CONCURRENT,
        Spliterator.ORDERED, and Spliterator.NONNULL.

        Returns
        - a `Spliterator` over the elements in this deque

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
