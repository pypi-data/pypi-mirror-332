"""
Python module generated from Java source file java.util.ArrayDeque

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import Serializable
from java.util import *
from java.util.function import Consumer
from java.util.function import Predicate
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class ArrayDeque(AbstractCollection, Deque, Cloneable, Serializable):
    """
    Resizable-array implementation of the Deque interface.  Array
    deques have no capacity restrictions; they grow as necessary to support
    usage.  They are not thread-safe; in the absence of external
    synchronization, they do not support concurrent access by multiple threads.
    Null elements are prohibited.  This class is likely to be faster than
    Stack when used as a stack, and faster than LinkedList
    when used as a queue.
    
    Most `ArrayDeque` operations run in amortized constant time.
    Exceptions include
    .remove(Object) remove,
    .removeFirstOccurrence removeFirstOccurrence,
    .removeLastOccurrence removeLastOccurrence,
    .contains contains,
    .iterator iterator.remove(),
    and the bulk operations, all of which run in linear time.
    
    The iterators returned by this class's .iterator() iterator
    method are *fail-fast*: If the deque is modified at any time after
    the iterator is created, in any way except through the iterator's own
    `remove` method, the iterator will generally throw a ConcurrentModificationException.  Thus, in the face of concurrent
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
    
    This class and its iterator implement all of the
    *optional* methods of the Collection and Iterator interfaces.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this deque

    Author(s)
    - Josh Bloch and Doug Lea

    Since
    - 1.6
    """

    def __init__(self):
        """
        Constructs an empty array deque with an initial capacity
        sufficient to hold 16 elements.
        """
        ...


    def __init__(self, numElements: int):
        """
        Constructs an empty array deque with an initial capacity
        sufficient to hold the specified number of elements.

        Arguments
        - numElements: lower bound on initial capacity of the deque
        """
        ...


    def __init__(self, c: Iterable["E"]):
        """
        Constructs a deque containing the elements of the specified
        collection, in the order they are returned by the collection's
        iterator.  (The first element returned by the collection's
        iterator becomes the first element, or *front* of the
        deque.)

        Arguments
        - c: the collection whose elements are to be placed into the deque

        Raises
        - NullPointerException: if the specified collection is null
        """
        ...


    def addFirst(self, e: "E") -> None:
        """
        Inserts the specified element at the front of this deque.

        Arguments
        - e: the element to add

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def addLast(self, e: "E") -> None:
        """
        Inserts the specified element at the end of this deque.
        
        This method is equivalent to .add.

        Arguments
        - e: the element to add

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def addAll(self, c: Iterable["E"]) -> bool:
        """
        Adds all of the elements in the specified collection at the end
        of this deque, as if by calling .addLast on each one,
        in the order that they are returned by the collection's iterator.

        Arguments
        - c: the elements to be inserted into this deque

        Returns
        - `True` if this deque changed as a result of the call

        Raises
        - NullPointerException: if the specified collection or any
                of its elements are null
        """
        ...


    def offerFirst(self, e: "E") -> bool:
        """
        Inserts the specified element at the front of this deque.

        Arguments
        - e: the element to add

        Returns
        - `True` (as specified by Deque.offerFirst)

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def offerLast(self, e: "E") -> bool:
        """
        Inserts the specified element at the end of this deque.

        Arguments
        - e: the element to add

        Returns
        - `True` (as specified by Deque.offerLast)

        Raises
        - NullPointerException: if the specified element is null
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
        """
        Removes the first occurrence of the specified element in this
        deque (when traversing the deque from head to tail).
        If the deque does not contain the element, it is unchanged.
        More formally, removes the first element `e` such that
        `o.equals(e)` (if such an element exists).
        Returns `True` if this deque contained the specified element
        (or equivalently, if this deque changed as a result of the call).

        Arguments
        - o: element to be removed from this deque, if present

        Returns
        - `True` if the deque contained the specified element
        """
        ...


    def removeLastOccurrence(self, o: "Object") -> bool:
        """
        Removes the last occurrence of the specified element in this
        deque (when traversing the deque from head to tail).
        If the deque does not contain the element, it is unchanged.
        More formally, removes the last element `e` such that
        `o.equals(e)` (if such an element exists).
        Returns `True` if this deque contained the specified element
        (or equivalently, if this deque changed as a result of the call).

        Arguments
        - o: element to be removed from this deque, if present

        Returns
        - `True` if the deque contained the specified element
        """
        ...


    def add(self, e: "E") -> bool:
        """
        Inserts the specified element at the end of this deque.
        
        This method is equivalent to .addLast.

        Arguments
        - e: the element to add

        Returns
        - `True` (as specified by Collection.add)

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Inserts the specified element at the end of this deque.
        
        This method is equivalent to .offerLast.

        Arguments
        - e: the element to add

        Returns
        - `True` (as specified by Queue.offer)

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def remove(self) -> "E":
        """
        Retrieves and removes the head of the queue represented by this deque.
        
        This method differs from .poll() poll() only in that it
        throws an exception if this deque is empty.
        
        This method is equivalent to .removeFirst.

        Returns
        - the head of the queue represented by this deque

        Raises
        - NoSuchElementException: 
        """
        ...


    def poll(self) -> "E":
        """
        Retrieves and removes the head of the queue represented by this deque
        (in other words, the first element of this deque), or returns
        `null` if this deque is empty.
        
        This method is equivalent to .pollFirst.

        Returns
        - the head of the queue represented by this deque, or
                `null` if this deque is empty
        """
        ...


    def element(self) -> "E":
        """
        Retrieves, but does not remove, the head of the queue represented by
        this deque.  This method differs from .peek peek only in
        that it throws an exception if this deque is empty.
        
        This method is equivalent to .getFirst.

        Returns
        - the head of the queue represented by this deque

        Raises
        - NoSuchElementException: 
        """
        ...


    def peek(self) -> "E":
        """
        Retrieves, but does not remove, the head of the queue represented by
        this deque, or returns `null` if this deque is empty.
        
        This method is equivalent to .peekFirst.

        Returns
        - the head of the queue represented by this deque, or
                `null` if this deque is empty
        """
        ...


    def push(self, e: "E") -> None:
        """
        Pushes an element onto the stack represented by this deque.  In other
        words, inserts the element at the front of this deque.
        
        This method is equivalent to .addFirst.

        Arguments
        - e: the element to push

        Raises
        - NullPointerException: if the specified element is null
        """
        ...


    def pop(self) -> "E":
        """
        Pops an element from the stack represented by this deque.  In other
        words, removes and returns the first element of this deque.
        
        This method is equivalent to .removeFirst().

        Returns
        - the element at the front of this deque (which is the top
                of the stack represented by this deque)

        Raises
        - NoSuchElementException: 
        """
        ...


    def size(self) -> int:
        """
        Returns the number of elements in this deque.

        Returns
        - the number of elements in this deque
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if this deque contains no elements.

        Returns
        - `True` if this deque contains no elements
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this deque.  The elements
        will be ordered from first (head) to last (tail).  This is the same
        order that elements would be dequeued (via successive calls to
        .remove or popped (via successive calls to .pop).

        Returns
        - an iterator over the elements in this deque
        """
        ...


    def descendingIterator(self) -> Iterator["E"]:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Creates a *<a href="Spliterator.html#binding">late-binding</a>*
        and *fail-fast* Spliterator over the elements in this
        deque.
        
        The `Spliterator` reports Spliterator.SIZED,
        Spliterator.SUBSIZED, Spliterator.ORDERED, and
        Spliterator.NONNULL.  Overriding implementations should document
        the reporting of additional characteristic values.

        Returns
        - a `Spliterator` over the elements in this deque

        Since
        - 1.8
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


    def remove(self, o: "Object") -> bool:
        """
        Removes a single instance of the specified element from this deque.
        If the deque does not contain the element, it is unchanged.
        More formally, removes the first element `e` such that
        `o.equals(e)` (if such an element exists).
        Returns `True` if this deque contained the specified element
        (or equivalently, if this deque changed as a result of the call).
        
        This method is equivalent to .removeFirstOccurrence(Object).

        Arguments
        - o: element to be removed from this deque, if present

        Returns
        - `True` if this deque contained the specified element
        """
        ...


    def clear(self) -> None:
        """
        Removes all of the elements from this deque.
        The deque will be empty after this call returns.
        """
        ...


    def toArray(self) -> list["Object"]:
        """
        Returns an array containing all of the elements in this deque
        in proper sequence (from first to last element).
        
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
        Returns an array containing all of the elements in this deque in
        proper sequence (from first to last element); the runtime type of the
        returned array is that of the specified array.  If the deque fits in
        the specified array, it is returned therein.  Otherwise, a new array
        is allocated with the runtime type of the specified array and the
        size of this deque.
        
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


    def clone(self) -> "ArrayDeque"["E"]:
        """
        Returns a copy of this deque.

        Returns
        - a copy of this deque
        """
        ...
