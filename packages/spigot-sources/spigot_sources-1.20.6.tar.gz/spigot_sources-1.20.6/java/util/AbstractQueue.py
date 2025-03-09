"""
Python module generated from Java source file java.util.AbstractQueue

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class AbstractQueue(AbstractCollection, Queue):
    """
    This class provides skeletal implementations of some Queue
    operations. The implementations in this class are appropriate when
    the base implementation does *not* allow `null`
    elements.  Methods .add add, .remove remove, and
    .element element are based on .offer offer, .poll poll, and .peek peek, respectively, but throw
    exceptions instead of indicating failure via `False` or
    `null` returns.
    
    A `Queue` implementation that extends this class must
    minimally define a method Queue.offer which does not permit
    insertion of `null` elements, along with methods Queue.peek, Queue.poll, Collection.size, and
    Collection.iterator.  Typically, additional methods will be
    overridden as well.  If these requirements cannot be met, consider
    instead subclassing AbstractCollection.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this queue

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def add(self, e: "E") -> bool:
        """
        Inserts the specified element into this queue if it is possible to do so
        immediately without violating capacity restrictions, returning
        `True` upon success and throwing an `IllegalStateException`
        if no space is currently available.
        
        This implementation returns `True` if `offer` succeeds,
        else throws an `IllegalStateException`.

        Arguments
        - e: the element to add

        Returns
        - `True` (as specified by Collection.add)

        Raises
        - IllegalStateException: if the element cannot be added at this
                time due to capacity restrictions
        - ClassCastException: if the class of the specified element
                prevents it from being added to this queue
        - NullPointerException: if the specified element is null and
                this queue does not permit null elements
        - IllegalArgumentException: if some property of this element
                prevents it from being added to this queue
        """
        ...


    def remove(self) -> "E":
        """
        Retrieves and removes the head of this queue.  This method differs
        from .poll poll only in that it throws an exception if this
        queue is empty.
        
        This implementation returns the result of `poll`
        unless the queue is empty.

        Returns
        - the head of this queue

        Raises
        - NoSuchElementException: if this queue is empty
        """
        ...


    def element(self) -> "E":
        """
        Retrieves, but does not remove, the head of this queue.  This method
        differs from .peek peek only in that it throws an exception if
        this queue is empty.
        
        This implementation returns the result of `peek`
        unless the queue is empty.

        Returns
        - the head of this queue

        Raises
        - NoSuchElementException: if this queue is empty
        """
        ...


    def clear(self) -> None:
        """
        Removes all of the elements from this queue.
        The queue will be empty after this call returns.
        
        This implementation repeatedly invokes .poll poll until it
        returns `null`.
        """
        ...


    def addAll(self, c: Iterable["E"]) -> bool:
        """
        Adds all of the elements in the specified collection to this
        queue.  Attempts to addAll of a queue to itself result in
        `IllegalArgumentException`. Further, the behavior of
        this operation is undefined if the specified collection is
        modified while the operation is in progress.
        
        This implementation iterates over the specified collection,
        and adds each element returned by the iterator to this
        queue, in turn.  A runtime exception encountered while
        trying to add an element (including, in particular, a
        `null` element) may result in only some of the elements
        having been successfully added when the associated exception is
        thrown.

        Arguments
        - c: collection containing elements to be added to this queue

        Returns
        - `True` if this queue changed as a result of the call

        Raises
        - ClassCastException: if the class of an element of the specified
                collection prevents it from being added to this queue
        - NullPointerException: if the specified collection contains a
                null element and this queue does not permit null elements,
                or if the specified collection is null
        - IllegalArgumentException: if some property of an element of the
                specified collection prevents it from being added to this
                queue, or if the specified collection is this queue
        - IllegalStateException: if not all the elements can be added at
                this time due to insertion restrictions

        See
        - .add(Object)
        """
        ...
