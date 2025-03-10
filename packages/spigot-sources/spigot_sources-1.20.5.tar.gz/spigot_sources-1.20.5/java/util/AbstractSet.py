"""
Python module generated from Java source file java.util.AbstractSet

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class AbstractSet(AbstractCollection, Set):

    def equals(self, o: "Object") -> bool:
        """
        Compares the specified object with this set for equality.  Returns
        `True` if the given object is also a set, the two sets have
        the same size, and every member of the given set is contained in
        this set.  This ensures that the `equals` method works
        properly across different implementations of the `Set`
        interface.
        
        This implementation first checks if the specified object is this
        set; if so it returns `True`.  Then, it checks if the
        specified object is a set whose size is identical to the size of
        this set; if not, it returns False.  If so, it returns
        `containsAll((Collection) o)`.

        Arguments
        - o: object to be compared for equality with this set

        Returns
        - `True` if the specified object is equal to this set
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this set.  The hash code of a set is
        defined to be the sum of the hash codes of the elements in the set,
        where the hash code of a `null` element is defined to be zero.
        This ensures that `s1.equals(s2)` implies that
        `s1.hashCode()==s2.hashCode()` for any two sets `s1`
        and `s2`, as required by the general contract of
        Object.hashCode.
        
        This implementation iterates over the set, calling the
        `hashCode` method on each element in the set, and adding up
        the results.

        Returns
        - the hash code value for this set

        See
        - Set.equals(Object)
        """
        ...


    def removeAll(self, c: Iterable[Any]) -> bool:
        """
        Removes from this set all of its elements that are contained in the
        specified collection (optional operation).  If the specified
        collection is also a set, this operation effectively modifies this
        set so that its value is the *asymmetric set difference* of
        the two sets.
        
        This implementation determines which is the smaller of this set
        and the specified collection, by invoking the `size`
        method on each.  If this set has fewer elements, then the
        implementation iterates over this set, checking each element
        returned by the iterator in turn to see if it is contained in
        the specified collection.  If it is so contained, it is removed
        from this set with the iterator's `remove` method.  If
        the specified collection has fewer elements, then the
        implementation iterates over the specified collection, removing
        from this set each element returned by the iterator, using this
        set's `remove` method.
        
        Note that this implementation will throw an
        `UnsupportedOperationException` if the iterator returned by the
        `iterator` method does not implement the `remove` method.

        Arguments
        - c: collection containing elements to be removed from this set

        Returns
        - `True` if this set changed as a result of the call

        Raises
        - UnsupportedOperationException: if the `removeAll` operation
                is not supported by this set
        - ClassCastException: if the class of an element of this set
                is incompatible with the specified collection
        (<a href="Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if this set contains a null element and the
                specified collection does not permit null elements
        (<a href="Collection.html#optional-restrictions">optional</a>),
                or if the specified collection is null

        See
        - .contains(Object)
        """
        ...
