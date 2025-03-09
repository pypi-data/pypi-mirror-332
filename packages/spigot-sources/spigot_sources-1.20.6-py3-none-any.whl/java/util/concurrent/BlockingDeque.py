"""
Python module generated from Java source file java.util.concurrent.BlockingDeque

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Deque
from java.util import Iterator
from java.util import NoSuchElementException
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class BlockingDeque(BlockingQueue, Deque):
    """
    A Deque that additionally supports blocking operations that wait
    for the deque to become non-empty when retrieving an element, and wait for
    space to become available in the deque when storing an element.
    
    `BlockingDeque` methods come in four forms, with different ways
    of handling operations that cannot be satisfied immediately, but may be
    satisfied at some point in the future:
    one throws an exception, the second returns a special value (either
    `null` or `False`, depending on the operation), the third
    blocks the current thread indefinitely until the operation can succeed,
    and the fourth blocks for only a given maximum time limit before giving
    up.  These methods are summarized in the following table:
    
    <table class="plain">
    <caption>Summary of BlockingDeque methods</caption>
     <tr>
       <th id="First" colspan="5"> First Element (Head)</th>
     </tr>
     <tr>
       <td></td>
       <th id="FThrow" style="font-weight:normal; font-style: italic">Throws exception</th>
       <th id="FValue" style="font-weight:normal; font-style: italic">Special value</th>
       <th id="FBlock" style="font-weight:normal; font-style: italic">Blocks</th>
       <th id="FTimes" style="font-weight:normal; font-style: italic">Times out</th>
     </tr>
     <tr>
       <th id="FInsert" style="text-align:left">Insert</th>
       <td headers="First FInsert FThrow">.addFirst(Object) addFirst(e)</td>
       <td headers="First FInsert FValue">.offerFirst(Object) offerFirst(e)</td>
       <td headers="First FInsert FBlock">.putFirst(Object) putFirst(e)</td>
       <td headers="First FInsert FTimes">.offerFirst(Object, long, TimeUnit) offerFirst(e, time, unit)</td>
     </tr>
     <tr>
       <th id="FRemove" style="text-align:left">Remove</th>
       <td headers="First FRemove FThrow">.removeFirst() removeFirst()</td>
       <td headers="First FRemove FValue">.pollFirst() pollFirst()</td>
       <td headers="First FRemove FBlock">.takeFirst() takeFirst()</td>
       <td headers="First FRemove FTimes">.pollFirst(long, TimeUnit) pollFirst(time, unit)</td>
     </tr>
     <tr>
       <th id="FExamine" style="text-align:left">Examine</th>
       <td headers="First FExamine FThrow">.getFirst() getFirst()</td>
       <td headers="First FExamine FValue">.peekFirst() peekFirst()</td>
       <td headers="First FExamine FBlock" style="font-style:italic">not applicable</td>
       <td headers="First FExamine FTimes" style="font-style:italic">not applicable</td>
     </tr>
     <tr>
       <th id="Last" colspan="5"> Last Element (Tail)</th>
     </tr>
     <tr>
       <td></td>
       <th id="LThrow" style="font-weight:normal; font-style: italic">Throws exception</th>
       <th id="LValue" style="font-weight:normal; font-style: italic">Special value</th>
       <th id="LBlock" style="font-weight:normal; font-style: italic">Blocks</th>
       <th id="LTimes" style="font-weight:normal; font-style: italic">Times out</th>
     </tr>
     <tr>
       <th id="LInsert" style="text-align:left">Insert</th>
       <td headers="Last LInsert LThrow">.addLast(Object) addLast(e)</td>
       <td headers="Last LInsert LValue">.offerLast(Object) offerLast(e)</td>
       <td headers="Last LInsert LBlock">.putLast(Object) putLast(e)</td>
       <td headers="Last LInsert LTimes">.offerLast(Object, long, TimeUnit) offerLast(e, time, unit)</td>
     </tr>
     <tr>
       <th id="LRemove" style="text-align:left">Remove</th>
       <td headers="Last LRemove LThrow">.removeLast() removeLast()</td>
       <td headers="Last LRemove LValue">.pollLast() pollLast()</td>
       <td headers="Last LRemove LBlock">.takeLast() takeLast()</td>
       <td headers="Last LRemove LTimes">.pollLast(long, TimeUnit) pollLast(time, unit)</td>
     </tr>
     <tr>
       <th id="LExamine" style="text-align:left">Examine</th>
       <td headers="Last LExamine LThrow">.getLast() getLast()</td>
       <td headers="Last LExamine LValue">.peekLast() peekLast()</td>
       <td headers="Last LExamine LBlock" style="font-style:italic">not applicable</td>
       <td headers="Last LExamine LTimes" style="font-style:italic">not applicable</td>
     </tr>
    </table>
    
    Like any BlockingQueue, a `BlockingDeque` is thread safe,
    does not permit null elements, and may (or may not) be
    capacity-constrained.
    
    A `BlockingDeque` implementation may be used directly as a FIFO
    `BlockingQueue`. The methods inherited from the
    `BlockingQueue` interface are precisely equivalent to
    `BlockingDeque` methods as indicated in the following table:
    
    <table class="plain">
    <caption>Comparison of BlockingQueue and BlockingDeque methods</caption>
     <tr>
       <td></td>
       <th id="BQueue"> `BlockingQueue` Method</th>
       <th id="BDeque"> Equivalent `BlockingDeque` Method</th>
     </tr>
     <tr>
       <th id="Insert" rowspan="4" style="text-align:left; vertical-align:top">Insert</th>
       <th id="add" style="font-weight:normal; text-align:left">.add(Object) add(e)</th>
       <td headers="Insert BDeque add">.addLast(Object) addLast(e)</td>
     </tr>
     <tr>
       <th id="offer1" style="font-weight:normal; text-align:left">.offer(Object) offer(e)</th>
       <td headers="Insert BDeque offer1">.offerLast(Object) offerLast(e)</td>
     </tr>
     <tr>
       <th id="put" style="font-weight:normal; text-align:left">.put(Object) put(e)</th>
       <td headers="Insert BDeque put">.putLast(Object) putLast(e)</td>
     </tr>
     <tr>
       <th id="offer2" style="font-weight:normal; text-align:left">.offer(Object, long, TimeUnit) offer(e, time, unit)</th>
       <td headers="Insert BDeque offer2">.offerLast(Object, long, TimeUnit) offerLast(e, time, unit)</td>
     </tr>
     <tr>
       <th id="Remove" rowspan="4" style="text-align:left; vertical-align:top">Remove</th>
       <th id="remove" style="font-weight:normal; text-align:left">.remove() remove()</th>
       <td headers="Remove BDeque remove">.removeFirst() removeFirst()</td>
     </tr>
     <tr>
       <th id="poll1" style="font-weight:normal; text-align:left">.poll() poll()</th>
       <td headers="Remove BDeque poll1">.pollFirst() pollFirst()</td>
     </tr>
     <tr>
       <th id="take" style="font-weight:normal; text-align:left">.take() take()</th>
       <td headers="Remove BDeque take">.takeFirst() takeFirst()</td>
     </tr>
     <tr>
       <th id="poll2" style="font-weight:normal; text-align:left">.poll(long, TimeUnit) poll(time, unit)</th>
       <td headers="Remove BDeque poll2">.pollFirst(long, TimeUnit) pollFirst(time, unit)</td>
     </tr>
     <tr>
       <th id="Examine" rowspan="2" style="text-align:left; vertical-align:top">Examine</th>
       <th id="element" style="font-weight:normal; text-align:left">.element() element()</th>
       <td headers="Examine BDeque element">.getFirst() getFirst()</td>
     </tr>
     <tr>
       <th id="peek" style="font-weight:normal; text-align:left">.peek() peek()</th>
       <td headers="Examine BDeque peek">.peekFirst() peekFirst()</td>
     </tr>
    </table>
    
    Memory consistency effects: As with other concurrent
    collections, actions in a thread prior to placing an object into a
    `BlockingDeque`
    <a href="package-summary.html#MemoryVisibility">*happen-before*</a>
    actions subsequent to the access or removal of that element from
    the `BlockingDeque` in another thread.
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this deque

    Author(s)
    - Doug Lea

    Since
    - 1.6
    """

    def addFirst(self, e: "E") -> None:
        """
        Inserts the specified element at the front of this deque if it is
        possible to do so immediately without violating capacity restrictions,
        throwing an `IllegalStateException` if no space is currently
        available.  When using a capacity-restricted deque, it is generally
        preferable to use .offerFirst(Object) offerFirst.

        Arguments
        - e: the element to add

        Raises
        - IllegalStateException: 
        - ClassCastException: 
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: 
        """
        ...


    def addLast(self, e: "E") -> None:
        """
        Inserts the specified element at the end of this deque if it is
        possible to do so immediately without violating capacity restrictions,
        throwing an `IllegalStateException` if no space is currently
        available.  When using a capacity-restricted deque, it is generally
        preferable to use .offerLast(Object) offerLast.

        Arguments
        - e: the element to add

        Raises
        - IllegalStateException: 
        - ClassCastException: 
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: 
        """
        ...


    def offerFirst(self, e: "E") -> bool:
        """
        Inserts the specified element at the front of this deque if it is
        possible to do so immediately without violating capacity restrictions,
        returning `True` upon success and `False` if no space is
        currently available.
        When using a capacity-restricted deque, this method is generally
        preferable to the .addFirst(Object) addFirst method, which can
        fail to insert an element only by throwing an exception.

        Arguments
        - e: the element to add

        Raises
        - ClassCastException: 
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: 
        """
        ...


    def offerLast(self, e: "E") -> bool:
        """
        Inserts the specified element at the end of this deque if it is
        possible to do so immediately without violating capacity restrictions,
        returning `True` upon success and `False` if no space is
        currently available.
        When using a capacity-restricted deque, this method is generally
        preferable to the .addLast(Object) addLast method, which can
        fail to insert an element only by throwing an exception.

        Arguments
        - e: the element to add

        Raises
        - ClassCastException: 
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: 
        """
        ...


    def putFirst(self, e: "E") -> None:
        """
        Inserts the specified element at the front of this deque,
        waiting if necessary for space to become available.

        Arguments
        - e: the element to add

        Raises
        - InterruptedException: if interrupted while waiting
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def putLast(self, e: "E") -> None:
        """
        Inserts the specified element at the end of this deque,
        waiting if necessary for space to become available.

        Arguments
        - e: the element to add

        Raises
        - InterruptedException: if interrupted while waiting
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def offerFirst(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Inserts the specified element at the front of this deque,
        waiting up to the specified wait time if necessary for space to
        become available.

        Arguments
        - e: the element to add
        - timeout: how long to wait before giving up, in units of
               `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `timeout` parameter

        Returns
        - `True` if successful, or `False` if
                the specified waiting time elapses before space is available

        Raises
        - InterruptedException: if interrupted while waiting
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def offerLast(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Inserts the specified element at the end of this deque,
        waiting up to the specified wait time if necessary for space to
        become available.

        Arguments
        - e: the element to add
        - timeout: how long to wait before giving up, in units of
               `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `timeout` parameter

        Returns
        - `True` if successful, or `False` if
                the specified waiting time elapses before space is available

        Raises
        - InterruptedException: if interrupted while waiting
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def takeFirst(self) -> "E":
        """
        Retrieves and removes the first element of this deque, waiting
        if necessary until an element becomes available.

        Returns
        - the head of this deque

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def takeLast(self) -> "E":
        """
        Retrieves and removes the last element of this deque, waiting
        if necessary until an element becomes available.

        Returns
        - the tail of this deque

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def pollFirst(self, timeout: int, unit: "TimeUnit") -> "E":
        """
        Retrieves and removes the first element of this deque, waiting
        up to the specified wait time if necessary for an element to
        become available.

        Arguments
        - timeout: how long to wait before giving up, in units of
               `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `timeout` parameter

        Returns
        - the head of this deque, or `null` if the specified
                waiting time elapses before an element is available

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def pollLast(self, timeout: int, unit: "TimeUnit") -> "E":
        """
        Retrieves and removes the last element of this deque, waiting
        up to the specified wait time if necessary for an element to
        become available.

        Arguments
        - timeout: how long to wait before giving up, in units of
               `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `timeout` parameter

        Returns
        - the tail of this deque, or `null` if the specified
                waiting time elapses before an element is available

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def removeFirstOccurrence(self, o: "Object") -> bool:
        """
        Removes the first occurrence of the specified element from this deque.
        If the deque does not contain the element, it is unchanged.
        More formally, removes the first element `e` such that
        `o.equals(e)` (if such an element exists).
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
        - NullPointerException: if the specified element is null
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        """
        ...


    def removeLastOccurrence(self, o: "Object") -> bool:
        """
        Removes the last occurrence of the specified element from this deque.
        If the deque does not contain the element, it is unchanged.
        More formally, removes the last element `e` such that
        `o.equals(e)` (if such an element exists).
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
        - NullPointerException: if the specified element is null
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
        
        This method is equivalent to .addLast(Object) addLast.

        Arguments
        - e: the element to add

        Raises
        - IllegalStateException: 
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null
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
        
        This method is equivalent to .offerLast(Object) offerLast.

        Arguments
        - e: the element to add

        Raises
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def put(self, e: "E") -> None:
        """
        Inserts the specified element into the queue represented by this deque
        (in other words, at the tail of this deque), waiting if necessary for
        space to become available.
        
        This method is equivalent to .putLast(Object) putLast.

        Arguments
        - e: the element to add

        Raises
        - InterruptedException: 
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this deque
        """
        ...


    def offer(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Inserts the specified element into the queue represented by this deque
        (in other words, at the tail of this deque), waiting up to the
        specified wait time if necessary for space to become available.
        
        This method is equivalent to
        .offerLast(Object,long,TimeUnit) offerLast.

        Arguments
        - e: the element to add

        Returns
        - `True` if the element was added to this deque, else
                `False`

        Raises
        - InterruptedException: 
        - ClassCastException: if the class of the specified element
                prevents it from being added to this deque
        - NullPointerException: if the specified element is null
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
        
        This method is equivalent to .removeFirst() removeFirst.

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
        - the head of this deque, or `null` if this deque is empty
        """
        ...


    def take(self) -> "E":
        """
        Retrieves and removes the head of the queue represented by this deque
        (in other words, the first element of this deque), waiting if
        necessary until an element becomes available.
        
        This method is equivalent to .takeFirst() takeFirst.

        Returns
        - the head of this deque

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def poll(self, timeout: int, unit: "TimeUnit") -> "E":
        """
        Retrieves and removes the head of the queue represented by this deque
        (in other words, the first element of this deque), waiting up to the
        specified wait time if necessary for an element to become available.
        
        This method is equivalent to
        .pollFirst(long,TimeUnit) pollFirst.

        Returns
        - the head of this deque, or `null` if the
                specified waiting time elapses before an element is available

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def element(self) -> "E":
        """
        Retrieves, but does not remove, the head of the queue represented by
        this deque (in other words, the first element of this deque).
        This method differs from .peek() peek only in that it throws an
        exception if this deque is empty.
        
        This method is equivalent to .getFirst() getFirst.

        Returns
        - the head of this deque

        Raises
        - NoSuchElementException: if this deque is empty
        """
        ...


    def peek(self) -> "E":
        """
        Retrieves, but does not remove, the head of the queue represented by
        this deque (in other words, the first element of this deque), or
        returns `null` if this deque is empty.
        
        This method is equivalent to .peekFirst() peekFirst.

        Returns
        - the head of this deque, or `null` if this deque is empty
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

        Raises
        - ClassCastException: if the class of the specified element
                is incompatible with this deque
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if the specified element is null
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
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

        Raises
        - ClassCastException: if the class of the specified element
                is incompatible with this deque
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if the specified element is null
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


    def push(self, e: "E") -> None:
        """
        Pushes an element onto the stack represented by this deque (in other
        words, at the head of this deque) if it is possible to do so
        immediately without violating capacity restrictions, throwing an
        `IllegalStateException` if no space is currently available.
        
        This method is equivalent to .addFirst(Object) addFirst.

        Raises
        - IllegalStateException: 
        - ClassCastException: 
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: 
        """
        ...
