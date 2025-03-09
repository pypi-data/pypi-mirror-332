"""
Python module generated from Java source file java.util.Deque

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class Deque(Queue):
    """
    A linear collection that supports element insertion and removal at
    both ends.  The name *deque* is short for "double ended queue"
    and is usually pronounced "deck".  Most `Deque`
    implementations place no fixed limits on the number of elements
    they may contain, but this interface supports capacity-restricted
    deques as well as those with no fixed size limit.
    
    This interface defines methods to access the elements at both
    ends of the deque.  Methods are provided to insert, remove, and
    examine the element.  Each of these methods exists in two forms:
    one throws an exception if the operation fails, the other returns a
    special value (either `null` or `False`, depending on
    the operation).  The latter form of the insert operation is
    designed specifically for use with capacity-restricted
    `Deque` implementations; in most implementations, insert
    operations cannot fail.
    
    The twelve methods described above are summarized in the
    following table:
    
    <table class="striped">
    <caption>Summary of Deque methods</caption>
     <thead>
     <tr>
       <td rowspan="2"></td>
       <th scope="col" colspan="2"> First Element (Head)</th>
       <th scope="col" colspan="2"> Last Element (Tail)</th>
     </tr>
     <tr>
       <th scope="col" style="font-weight:normal; font-style:italic">Throws exception</th>
       <th scope="col" style="font-weight:normal; font-style:italic">Special value</th>
       <th scope="col" style="font-weight:normal; font-style:italic">Throws exception</th>
       <th scope="col" style="font-weight:normal; font-style:italic">Special value</th>
     </tr>
     </thead>
     <tbody>
     <tr>
       <th scope="row">Insert</th>
       <td>.addFirst(Object) addFirst(e)</td>
       <td>.offerFirst(Object) offerFirst(e)</td>
       <td>.addLast(Object) addLast(e)</td>
       <td>.offerLast(Object) offerLast(e)</td>
     </tr>
     <tr>
       <th scope="row">Remove</th>
       <td>.removeFirst() removeFirst()</td>
       <td>.pollFirst() pollFirst()</td>
       <td>.removeLast() removeLast()</td>
       <td>.pollLast() pollLast()</td>
     </tr>
     <tr>
       <th scope="row">Examine</th>
       <td>.getFirst() getFirst()</td>
       <td>.peekFirst() peekFirst()</td>
       <td>.getLast() getLast()</td>
       <td>.peekLast() peekLast()</td>
     </tr>
     </tbody>
    </table>
    
    This interface extends the Queue interface.  When a deque is
    used as a queue, FIFO (First-In-First-Out) behavior results.  Elements are
    added at the end of the deque and removed from the beginning.  The methods
    inherited from the `Queue` interface are precisely equivalent to
    `Deque` methods as indicated in the following table:
    
    <table class="striped">
    <caption>Comparison of Queue and Deque methods</caption>
     <thead>
     <tr>
       <th scope="col"> `Queue` Method</th>
       <th scope="col"> Equivalent `Deque` Method</th>
     </tr>
     </thead>
     <tbody>
     <tr>
       <th scope="row">.add(Object) add(e)</th>
       <td>.addLast(Object) addLast(e)</td>
     </tr>
     <tr>
       <th scope="row">.offer(Object) offer(e)</th>
       <td>.offerLast(Object) offerLast(e)</td>
     </tr>
     <tr>
       <th scope="row">.remove() remove()</th>
       <td>.removeFirst() removeFirst()</td>
     </tr>
     <tr>
       <th scope="row">.poll() poll()</th>
       <td>.pollFirst() pollFirst()</td>
     </tr>
     <tr>
       <th scope="row">.element() element()</th>
       <td>.getFirst() getFirst()</td>
     </tr>
     <tr>
       <th scope="row">.peek() peek()</th>
       <td>.peekFirst() peekFirst()</td>
     </tr>
     </tbody>
    </table>
    
    Deques can also be used as LIFO (Last-In-First-Out) stacks.  This
    interface should be used in preference to the legacy Stack class.
    When a deque is used as a stack, elements are pushed and popped from the
    beginning of the deque.  Stack methods are equivalent to `Deque`
    methods as indicated in the table below:
    
    <table class="striped">
    <caption>Comparison of Stack and Deque methods</caption>
     <thead>
     <tr>
       <th scope="col"> Stack Method</th>
       <th scope="col"> Equivalent `Deque` Method</th>
     </tr>
     </thead>
     <tbody>
     <tr>
       <th scope="row">.push(Object) push(e)</th>
       <td>.addFirst(Object) addFirst(e)</td>
     </tr>
     <tr>
       <th scope="row">.pop() pop()</th>
       <td>.removeFirst() removeFirst()</td>
     </tr>
     <tr>
       <th scope="row">.peek() peek()</th>
       <td>.getFirst() getFirst()</td>
     </tr>
     </tbody>
    </table>
    
    Note that the .peek peek method works equally well when
    a deque is used as a queue or a stack; in either case, elements are
    drawn from the beginning of the deque.
    
    This interface provides two methods to remove interior
    elements, .removeFirstOccurrence removeFirstOccurrence and
    .removeLastOccurrence removeLastOccurrence.
    
    Unlike the List interface, this interface does not
    provide support for indexed access to elements.
    
    While `Deque` implementations are not strictly required
    to prohibit the insertion of null elements, they are strongly
    encouraged to do so.  Users of any `Deque` implementations
    that do allow null elements are strongly encouraged *not* to
    take advantage of the ability to insert nulls.  This is so because
    `null` is used as a special return value by various methods
    to indicate that the deque is empty.
    
    `Deque` implementations generally do not define
    element-based versions of the `equals` and `hashCode`
    methods, but instead inherit the identity-based versions from class
    `Object`.
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this deque

    Author(s)
    - Josh Bloch

    Since
    - 1.6
    """

    def addFirst(self, e: "E") -> None:
        """
        Inserts the specified element at the front of this deque if it is
        possible to do so immediately without violating capacity restrictions,
        throwing an `IllegalStateException` if no space is currently
        available.  When using a capacity-restricted deque, it is generally
        preferable to use method .offerFirst.

        Arguments
        - e: the element to add

        Raises
        - IllegalStateException: if the element cannot be added at this
                time due to capacity restrictions
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def addLast(self, e: "E") -> None:
        """
        Inserts the specified element at the end of this deque if it is
        possible to do so immediately without violating capacity restrictions,
        throwing an `IllegalStateException` if no space is currently
        available.  When using a capacity-restricted deque, it is generally
        preferable to use method .offerLast.
        
        This method is equivalent to .add.

        Arguments
        - e: the element to add

        Raises
        - IllegalStateException: if the element cannot be added at this
                time due to capacity restrictions
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def offerFirst(self, e: "E") -> bool:
        """
        Inserts the specified element at the front of this deque unless it would
        violate capacity restrictions.  When using a capacity-restricted deque,
        this method is generally preferable to the .addFirst method,
        which can fail to insert an element only by throwing an exception.

        Arguments
        - e: the element to add

        Returns
        - `True` if the element was added to this deque, else
                `False`

        Raises
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def offerLast(self, e: "E") -> bool:
        """
        Inserts the specified element at the end of this deque unless it would
        violate capacity restrictions.  When using a capacity-restricted deque,
        this method is generally preferable to the .addLast method,
        which can fail to insert an element only by throwing an exception.

        Arguments
        - e: the element to add

        Returns
        - `True` if the element was added to this deque, else
                `False`

        Raises
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def removeFirst(self) -> "E":
        """
        Retrieves and removes the first element of this deque.  This method
        differs from .pollFirst pollFirst only in that it throws an
        exception if this deque is empty.

        Returns
        - the head of this deque

        Raises
        - NoSuchElementException: if this deque is empty
        """
        ...


    def removeLast(self) -> "E":
        """
        Retrieves and removes the last element of this deque.  This method
        differs from .pollLast pollLast only in that it throws an
        exception if this deque is empty.

        Returns
        - the tail of this deque

        Raises
        - NoSuchElementException: if this deque is empty
        """
        ...


    def pollFirst(self) -> "E":
        """
        Retrieves and removes the first element of this deque,
        or returns `null` if this deque is empty.

        Returns
        - the head of this deque, or `null` if this deque is empty
        """
        ...


    def pollLast(self) -> "E":
        """
        Retrieves and removes the last element of this deque,
        or returns `null` if this deque is empty.

        Returns
        - the tail of this deque, or `null` if this deque is empty
        """
        ...


    def getFirst(self) -> "E":
        """
        Retrieves, but does not remove, the first element of this deque.
        
        This method differs from .peekFirst peekFirst only in that it
        throws an exception if this deque is empty.

        Returns
        - the head of this deque

        Raises
        - NoSuchElementException: if this deque is empty
        """
        ...


    def getLast(self) -> "E":
        """
        Retrieves, but does not remove, the last element of this deque.
        This method differs from .peekLast peekLast only in that it
        throws an exception if this deque is empty.

        Returns
        - the tail of this deque

        Raises
        - NoSuchElementException: if this deque is empty
        """
        ...


    def peekFirst(self) -> "E":
        """
        Retrieves, but does not remove, the first element of this deque,
        or returns `null` if this deque is empty.

        Returns
        - the head of this deque, or `null` if this deque is empty
        """
        ...


    def peekLast(self) -> "E":
        """
        Retrieves, but does not remove, the last element of this deque,
        or returns `null` if this deque is empty.

        Returns
        - the tail of this deque, or `null` if this deque is empty
        """
        ...


    def removeFirstOccurrence(self, o: "Object") -> bool:
        """
        Removes the first occurrence of the specified element from this deque.
        If the deque does not contain the element, it is unchanged.
        More formally, removes the first element `e` such that
        `Objects.equals(o, e)` (if such an element exists).
        Returns `True` if this deque contained the specified element
        (or equivalently, if this deque changed as a result of the call).

        Arguments
        - o: element to be removed from this deque, if present

        Returns
        - `True` if an element was removed as a result of this call

        Raises
        - ClassCastException: if the class of the specified element
                is incompatible with this deque
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        """
        ...


    def removeLastOccurrence(self, o: "Object") -> bool:
        """
        Removes the last occurrence of the specified element from this deque.
        If the deque does not contain the element, it is unchanged.
        More formally, removes the last element `e` such that
        `Objects.equals(o, e)` (if such an element exists).
        Returns `True` if this deque contained the specified element
        (or equivalently, if this deque changed as a result of the call).

        Arguments
        - o: element to be removed from this deque, if present

        Returns
        - `True` if an element was removed as a result of this call

        Raises
        - ClassCastException: if the class of the specified element
                is incompatible with this deque
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        """
        ...


    def add(self, e: "E") -> bool:
        """
        Inserts the specified element into the queue represented by this deque
        (in other words, at the tail of this deque) if it is possible to do so
        immediately without violating capacity restrictions, returning
        `True` upon success and throwing an
        `IllegalStateException` if no space is currently available.
        When using a capacity-restricted deque, it is generally preferable to
        use .offer(Object) offer.
        
        This method is equivalent to .addLast.

        Arguments
        - e: the element to add

        Returns
        - `True` (as specified by Collection.add)

        Raises
        - IllegalStateException: if the element cannot be added at this
                time due to capacity restrictions
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Inserts the specified element into the queue represented by this deque
        (in other words, at the tail of this deque) if it is possible to do so
        immediately without violating capacity restrictions, returning
        `True` upon success and `False` if no space is currently
        available.  When using a capacity-restricted deque, this method is
        generally preferable to the .add method, which can fail to
        insert an element only by throwing an exception.
        
        This method is equivalent to .offerLast.

        Arguments
        - e: the element to add

        Returns
        - `True` if the element was added to this deque, else
                `False`

        Raises
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def remove(self) -> "E":
        """
        Retrieves and removes the head of the queue represented by this deque
        (in other words, the first element of this deque).
        This method differs from .poll() poll() only in that it
        throws an exception if this deque is empty.
        
        This method is equivalent to .removeFirst().

        Returns
        - the head of the queue represented by this deque

        Raises
        - NoSuchElementException: if this deque is empty
        """
        ...


    def poll(self) -> "E":
        """
        Retrieves and removes the head of the queue represented by this deque
        (in other words, the first element of this deque), or returns
        `null` if this deque is empty.
        
        This method is equivalent to .pollFirst().

        Returns
        - the first element of this deque, or `null` if
                this deque is empty
        """
        ...


    def element(self) -> "E":
        """
        Retrieves, but does not remove, the head of the queue represented by
        this deque (in other words, the first element of this deque).
        This method differs from .peek peek only in that it throws an
        exception if this deque is empty.
        
        This method is equivalent to .getFirst().

        Returns
        - the head of the queue represented by this deque

        Raises
        - NoSuchElementException: if this deque is empty
        """
        ...


    def peek(self) -> "E":
        """
        Retrieves, but does not remove, the head of the queue represented by
        this deque (in other words, the first element of this deque), or
        returns `null` if this deque is empty.
        
        This method is equivalent to .peekFirst().

        Returns
        - the head of the queue represented by this deque, or
                `null` if this deque is empty
        """
        ...


    def addAll(self, c: Iterable["E"]) -> bool:
        """
        Adds all of the elements in the specified collection at the end
        of this deque, as if by calling .addLast on each one,
        in the order that they are returned by the collection's iterator.
        
        When using a capacity-restricted deque, it is generally preferable
        to call .offer(Object) offer separately on each element.
        
        An exception encountered while trying to add an element may result
        in only some of the elements having been successfully added when
        the associated exception is thrown.

        Arguments
        - c: the elements to be inserted into this deque

        Returns
        - `True` if this deque changed as a result of the call

        Raises
        - IllegalStateException: if not all the elements can be added at
                this time due to insertion restrictions
        - ClassCastException: if the class of an element of the specified
                collection prevents it from being added to this deque
        - NullPointerException: if the specified collection contains a
                null element and this deque does not permit null elements,
                or if the specified collection is null
        - IllegalArgumentException: if some property of an element of the
                specified collection prevents it from being added to this deque
        """
        ...


    def push(self, e: "E") -> None:
        """
        Pushes an element onto the stack represented by this deque (in other
        words, at the head of this deque) if it is possible to do so
        immediately without violating capacity restrictions, throwing an
        `IllegalStateException` if no space is currently available.
        
        This method is equivalent to .addFirst.

        Arguments
        - e: the element to push

        Raises
        - IllegalStateException: if the element cannot be added at this
                time due to capacity restrictions
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
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
        - NoSuchElementException: if this deque is empty
        """
        ...


    def remove(self, o: "Object") -> bool:
        """
        Removes the first occurrence of the specified element from this deque.
        If the deque does not contain the element, it is unchanged.
        More formally, removes the first element `e` such that
        `Objects.equals(o, e)` (if such an element exists).
        Returns `True` if this deque contained the specified element
        (or equivalently, if this deque changed as a result of the call).
        
        This method is equivalent to .removeFirstOccurrence(Object).

        Arguments
        - o: element to be removed from this deque, if present

        Returns
        - `True` if an element was removed as a result of this call

        Raises
        - ClassCastException: if the class of the specified element
                is incompatible with this deque
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        """
        ...


    def contains(self, o: "Object") -> bool:
        """
        Returns `True` if this deque contains the specified element.
        More formally, returns `True` if and only if this deque contains
        at least one element `e` such that `Objects.equals(o, e)`.

        Arguments
        - o: element whose presence in this deque is to be tested

        Returns
        - `True` if this deque contains the specified element

        Raises
        - ClassCastException: if the class of the specified element
                is incompatible with this deque
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if the specified element is null and this
                deque does not permit null elements
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        """
        ...


    def size(self) -> int:
        """
        Returns the number of elements in this deque.

        Returns
        - the number of elements in this deque
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this deque in proper sequence.
        The elements will be returned in order from first (head) to last (tail).

        Returns
        - an iterator over the elements in this deque in proper sequence
        """
        ...


    def descendingIterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this deque in reverse
        sequential order.  The elements will be returned in order from
        last (tail) to first (head).

        Returns
        - an iterator over the elements in this deque in reverse
        sequence
        """
        ...
