"""
Python module generated from Java source file java.util.AbstractCollection

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from jdk.internal.util import ArraysSupport
from typing import Any, Callable, Iterable, Tuple


class AbstractCollection(Collection):

    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements contained in this collection.

        Returns
        - an iterator over the elements contained in this collection
        """
        ...


    def size(self) -> int:
        ...


    def isEmpty(self) -> bool:
        """
        Unknown Tags
        - This implementation returns `size() == 0`.
        """
        ...


    def contains(self, o: "Object") -> bool:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 

        Unknown Tags
        - This implementation iterates over the elements in the collection,
        checking each element in turn for equality with the specified element.
        """
        ...


    def toArray(self) -> list["Object"]:
        """
        Unknown Tags
        - This implementation returns an array containing all the elements
        returned by this collection's iterator, in the same order, stored in
        consecutive elements of the array, starting with index `0`.
        The length of the returned array is equal to the number of elements
        returned by the iterator, even if the size of this collection changes
        during iteration, as might happen if the collection permits
        concurrent modification during iteration.  The `size` method is
        called only as an optimization hint; the correct result is returned
        even if the iterator returns a different number of elements.
        
        This method is equivalent to:
        
         ``` `List<E> list = new ArrayList<E>(size());
        for (E e : this)
            list.add(e);
        return list.toArray();````
        """
        ...


    def toArray(self, a: list["T"]) -> list["T"]:
        """
        Raises
        - ArrayStoreException: 
        - NullPointerException: 

        Unknown Tags
        - This implementation returns an array containing all the elements
        returned by this collection's iterator in the same order, stored in
        consecutive elements of the array, starting with index `0`.
        If the number of elements returned by the iterator is too large to
        fit into the specified array, then the elements are returned in a
        newly allocated array with length equal to the number of elements
        returned by the iterator, even if the size of this collection
        changes during iteration, as might happen if the collection permits
        concurrent modification during iteration.  The `size` method is
        called only as an optimization hint; the correct result is returned
        even if the iterator returns a different number of elements.
        
        This method is equivalent to:
        
         ``` `List<E> list = new ArrayList<E>(size());
        for (E e : this)
            list.add(e);
        return list.toArray(a);````
        """
        ...


    def add(self, e: "E") -> bool:
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        - IllegalStateException: 

        Unknown Tags
        - This implementation always throws an
        `UnsupportedOperationException`.
        """
        ...


    def remove(self, o: "Object") -> bool:
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 

        Unknown Tags
        - This implementation iterates over the collection looking for the
        specified element.  If it finds the element, it removes the element
        from the collection using the iterator's remove method.
        
        Note that this implementation throws an
        `UnsupportedOperationException` if the iterator returned by this
        collection's iterator method does not implement the `remove`
        method and this collection contains the specified object.
        """
        ...


    def containsAll(self, c: Iterable[Any]) -> bool:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 

        See
        - .contains(Object)

        Unknown Tags
        - This implementation iterates over the specified collection,
        checking each element returned by the iterator in turn to see
        if it's contained in this collection.  If all elements are so
        contained `True` is returned, otherwise `False`.
        """
        ...


    def addAll(self, c: Iterable["E"]) -> bool:
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        - IllegalStateException: 

        See
        - .add(Object)

        Unknown Tags
        - This implementation iterates over the specified collection, and adds
        each object returned by the iterator to this collection, in turn.
        
        Note that this implementation will throw an
        `UnsupportedOperationException` unless `add` is
        overridden (assuming the specified collection is non-empty).
        """
        ...


    def removeAll(self, c: Iterable[Any]) -> bool:
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 

        See
        - .contains(Object)

        Unknown Tags
        - This implementation iterates over this collection, checking each
        element returned by the iterator in turn to see if it's contained
        in the specified collection.  If it's so contained, it's removed from
        this collection with the iterator's `remove` method.
        
        Note that this implementation will throw an
        `UnsupportedOperationException` if the iterator returned by the
        `iterator` method does not implement the `remove` method
        and this collection contains one or more elements in common with the
        specified collection.
        """
        ...


    def retainAll(self, c: Iterable[Any]) -> bool:
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 

        See
        - .contains(Object)

        Unknown Tags
        - This implementation iterates over this collection, checking each
        element returned by the iterator in turn to see if it's contained
        in the specified collection.  If it's not so contained, it's removed
        from this collection with the iterator's `remove` method.
        
        Note that this implementation will throw an
        `UnsupportedOperationException` if the iterator returned by the
        `iterator` method does not implement the `remove` method
        and this collection contains one or more elements not present in the
        specified collection.
        """
        ...


    def clear(self) -> None:
        """
        Raises
        - UnsupportedOperationException: 

        Unknown Tags
        - This implementation iterates over this collection, removing each
        element using the `Iterator.remove` operation.  Most
        implementations will probably choose to override this method for
        efficiency.
        
        Note that this implementation will throw an
        `UnsupportedOperationException` if the iterator returned by this
        collection's `iterator` method does not implement the
        `remove` method and this collection is non-empty.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this collection.  The string
        representation consists of a list of the collection's elements in the
        order they are returned by its iterator, enclosed in square brackets
        (`"[]"`).  Adjacent elements are separated by the characters
        `", "` (comma and space).  Elements are converted to strings as
        by String.valueOf(Object).

        Returns
        - a string representation of this collection
        """
        ...
