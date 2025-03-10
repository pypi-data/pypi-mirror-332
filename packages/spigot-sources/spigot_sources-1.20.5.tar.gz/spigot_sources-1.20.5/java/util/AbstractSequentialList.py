"""
Python module generated from Java source file java.util.AbstractSequentialList

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class AbstractSequentialList(AbstractList):

    def get(self, index: int) -> "E":
        """
        Returns the element at the specified position in this list.
        
        This implementation first gets a list iterator pointing to the
        indexed element (with `listIterator(index)`).  Then, it gets
        the element using `ListIterator.next` and returns it.

        Raises
        - IndexOutOfBoundsException: 
        """
        ...


    def set(self, index: int, element: "E") -> "E":
        """
        Replaces the element at the specified position in this list with the
        specified element (optional operation).
        
        This implementation first gets a list iterator pointing to the
        indexed element (with `listIterator(index)`).  Then, it gets
        the current element using `ListIterator.next` and replaces it
        with `ListIterator.set`.
        
        Note that this implementation will throw an
        `UnsupportedOperationException` if the list iterator does not
        implement the `set` operation.

        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        - IndexOutOfBoundsException: 
        """
        ...


    def add(self, index: int, element: "E") -> None:
        """
        Inserts the specified element at the specified position in this list
        (optional operation).  Shifts the element currently at that position
        (if any) and any subsequent elements to the right (adds one to their
        indices).
        
        This implementation first gets a list iterator pointing to the
        indexed element (with `listIterator(index)`).  Then, it
        inserts the specified element with `ListIterator.add`.
        
        Note that this implementation will throw an
        `UnsupportedOperationException` if the list iterator does not
        implement the `add` operation.

        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        - IndexOutOfBoundsException: 
        """
        ...


    def remove(self, index: int) -> "E":
        """
        Removes the element at the specified position in this list (optional
        operation).  Shifts any subsequent elements to the left (subtracts one
        from their indices).  Returns the element that was removed from the
        list.
        
        This implementation first gets a list iterator pointing to the
        indexed element (with `listIterator(index)`).  Then, it removes
        the element with `ListIterator.remove`.
        
        Note that this implementation will throw an
        `UnsupportedOperationException` if the list iterator does not
        implement the `remove` operation.

        Raises
        - UnsupportedOperationException: 
        - IndexOutOfBoundsException: 
        """
        ...


    def addAll(self, index: int, c: Iterable["E"]) -> bool:
        """
        Inserts all of the elements in the specified collection into this
        list at the specified position (optional operation).  Shifts the
        element currently at that position (if any) and any subsequent
        elements to the right (increases their indices).  The new elements
        will appear in this list in the order that they are returned by the
        specified collection's iterator.  The behavior of this operation is
        undefined if the specified collection is modified while the
        operation is in progress.  (Note that this will occur if the specified
        collection is this list, and it's nonempty.)
        
        This implementation gets an iterator over the specified collection and
        a list iterator over this list pointing to the indexed element (with
        `listIterator(index)`).  Then, it iterates over the specified
        collection, inserting the elements obtained from the iterator into this
        list, one at a time, using `ListIterator.add` followed by
        `ListIterator.next` (to skip over the added element).
        
        Note that this implementation will throw an
        `UnsupportedOperationException` if the list iterator returned by
        the `listIterator` method does not implement the `add`
        operation.

        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        - IndexOutOfBoundsException: 
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this list (in proper
        sequence).
        
        This implementation merely returns a list iterator over the list.

        Returns
        - an iterator over the elements in this list (in proper sequence)
        """
        ...


    def listIterator(self, index: int) -> "ListIterator"["E"]:
        """
        Returns a list iterator over the elements in this list (in proper
        sequence).

        Arguments
        - index: index of first element to be returned from the list
                iterator (by a call to the `next` method)

        Returns
        - a list iterator over the elements in this list (in proper
                sequence)

        Raises
        - IndexOutOfBoundsException: 
        """
        ...
