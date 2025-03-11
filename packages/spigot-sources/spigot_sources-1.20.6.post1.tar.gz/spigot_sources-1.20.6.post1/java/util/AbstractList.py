"""
Python module generated from Java source file java.util.AbstractList

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from java.util.function import Consumer
from typing import Any, Callable, Iterable, Tuple


class AbstractList(AbstractCollection, List):

    def add(self, e: "E") -> bool:
        """
        Appends the specified element to the end of this list (optional
        operation).
        
        Lists that support this operation may place limitations on what
        elements may be added to this list.  In particular, some
        lists will refuse to add null elements, and others will impose
        restrictions on the type of elements that may be added.  List
        classes should clearly specify in their documentation any restrictions
        on what elements may be added.

        Arguments
        - e: element to be appended to this list

        Returns
        - `True` (as specified by Collection.add)

        Raises
        - UnsupportedOperationException: if the `add` operation
                is not supported by this list
        - ClassCastException: if the class of the specified element
                prevents it from being added to this list
        - NullPointerException: if the specified element is null and this
                list does not permit null elements
        - IllegalArgumentException: if some property of this element
                prevents it from being added to this list

        Unknown Tags
        - This implementation calls `add(size(), e)`.
        
        Note that this implementation throws an
        `UnsupportedOperationException` unless
        .add(int, Object) add(int, E) is overridden.
        """
        ...


    def get(self, index: int) -> "E":
        """
        Raises
        - IndexOutOfBoundsException: 
        """
        ...


    def set(self, index: int, element: "E") -> "E":
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        - IndexOutOfBoundsException: 

        Unknown Tags
        - This implementation always throws an
        `UnsupportedOperationException`.
        """
        ...


    def add(self, index: int, element: "E") -> None:
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        - IndexOutOfBoundsException: 

        Unknown Tags
        - This implementation always throws an
        `UnsupportedOperationException`.
        """
        ...


    def remove(self, index: int) -> "E":
        """
        Raises
        - UnsupportedOperationException: 
        - IndexOutOfBoundsException: 

        Unknown Tags
        - This implementation always throws an
        `UnsupportedOperationException`.
        """
        ...


    def indexOf(self, o: "Object") -> int:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 

        Unknown Tags
        - This implementation first gets a list iterator (with
        `listIterator()`).  Then, it iterates over the list until the
        specified element is found or the end of the list is reached.
        """
        ...


    def lastIndexOf(self, o: "Object") -> int:
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 

        Unknown Tags
        - This implementation first gets a list iterator that points to the end
        of the list (with `listIterator(size())`).  Then, it iterates
        backwards over the list until the specified element is found, or the
        beginning of the list is reached.
        """
        ...


    def clear(self) -> None:
        """
        Removes all of the elements from this list (optional operation).
        The list will be empty after this call returns.

        Raises
        - UnsupportedOperationException: if the `clear` operation
                is not supported by this list

        Unknown Tags
        - This implementation calls `removeRange(0, size())`.
        
        Note that this implementation throws an
        `UnsupportedOperationException` unless `remove(int
        index)` or `removeRange(int fromIndex, int toIndex)` is
        overridden.
        """
        ...


    def addAll(self, index: int, c: Iterable["E"]) -> bool:
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        - IndexOutOfBoundsException: 

        Unknown Tags
        - This implementation gets an iterator over the specified collection
        and iterates over it, inserting the elements obtained from the
        iterator into this list at the appropriate position, one at a time,
        using `add(int, E)`.
        Many implementations will override this method for efficiency.
        
        Note that this implementation throws an
        `UnsupportedOperationException` unless
        .add(int, Object) add(int, E) is overridden.
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this list in proper sequence.

        Returns
        - an iterator over the elements in this list in proper sequence

        Unknown Tags
        - This implementation returns a straightforward implementation of the
        iterator interface, relying on the backing list's `size()`,
        `get(int)`, and `remove(int)` methods.
        
        Note that the iterator returned by this method will throw an
        UnsupportedOperationException in response to its
        `remove` method unless the list's `remove(int)` method is
        overridden.
        
        This implementation can be made to throw runtime exceptions in the
        face of concurrent modification, as described in the specification
        for the (protected) .modCount field.
        """
        ...


    def listIterator(self) -> "ListIterator"["E"]:
        """
        See
        - .listIterator(int)

        Unknown Tags
        - This implementation returns `listIterator(0)`.
        """
        ...


    def listIterator(self, index: int) -> "ListIterator"["E"]:
        """
        Raises
        - IndexOutOfBoundsException: 

        Unknown Tags
        - This implementation returns a straightforward implementation of the
        `ListIterator` interface that extends the implementation of the
        `Iterator` interface returned by the `iterator()` method.
        The `ListIterator` implementation relies on the backing list's
        `get(int)`, `set(int, E)`, `add(int, E)`
        and `remove(int)` methods.
        
        Note that the list iterator returned by this implementation will
        throw an UnsupportedOperationException in response to its
        `remove`, `set` and `add` methods unless the
        list's `remove(int)`, `set(int, E)`, and
        `add(int, E)` methods are overridden.
        
        This implementation can be made to throw runtime exceptions in the
        face of concurrent modification, as described in the specification for
        the (protected) .modCount field.
        """
        ...


    def subList(self, fromIndex: int, toIndex: int) -> list["E"]:
        """
        Raises
        - IndexOutOfBoundsException: if an endpoint index value is out of range
                `(fromIndex < 0 || toIndex > size)`
        - IllegalArgumentException: if the endpoint indices are out of order
                `(fromIndex > toIndex)`

        Unknown Tags
        - This implementation returns a list that subclasses
        `AbstractList`.  The subclass stores, in private fields, the
        size of the subList (which can change over its lifetime), and the
        expected `modCount` value of the backing list.  There are two
        variants of the subclass, one of which implements `RandomAccess`.
        If this list implements `RandomAccess` the returned list will
        be an instance of the subclass that implements `RandomAccess`.
        
        The subclass's `set(int, E)`, `get(int)`,
        `add(int, E)`, `remove(int)`, `addAll(int,
        Collection)` and `removeRange(int, int)` methods all
        delegate to the corresponding methods on the backing abstract list,
        after bounds-checking the index and adjusting for the offset.  The
        `addAll(Collection c)` method merely returns `addAll(size,
        c)`.
        
        The `listIterator(int)` method returns a "wrapper object"
        over a list iterator on the backing list, which is created with the
        corresponding method on the backing list.  The `iterator` method
        merely returns `listIterator()`, and the `size` method
        merely returns the subclass's `size` field.
        
        All methods first check to see if the actual `modCount` of
        the backing list is equal to its expected value, and throw a
        `ConcurrentModificationException` if it is not.
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Compares the specified object with this list for equality.  Returns
        `True` if and only if the specified object is also a list, both
        lists have the same size, and all corresponding pairs of elements in
        the two lists are *equal*.  (Two elements `e1` and
        `e2` are *equal* if `(e1==null ? e2==null :
        e1.equals(e2))`.)  In other words, two lists are defined to be
        equal if they contain the same elements in the same order.

        Arguments
        - o: the object to be compared for equality with this list

        Returns
        - `True` if the specified object is equal to this list

        Unknown Tags
        - This implementation first checks if the specified object is this
        list. If so, it returns `True`; if not, it checks if the
        specified object is a list. If not, it returns `False`; if so,
        it iterates over both lists, comparing corresponding pairs of elements.
        If any comparison returns `False`, this method returns
        `False`.  If either iterator runs out of elements before the
        other it returns `False` (as the lists are of unequal length);
        otherwise it returns `True` when the iterations complete.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this list.

        Returns
        - the hash code value for this list

        Unknown Tags
        - This implementation uses exactly the code that is used to define the
        list hash function in the documentation for the List.hashCode
        method.
        """
        ...
