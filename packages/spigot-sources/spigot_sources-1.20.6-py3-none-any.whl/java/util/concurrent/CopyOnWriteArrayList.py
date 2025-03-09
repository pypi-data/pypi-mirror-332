"""
Python module generated from Java source file java.util.concurrent.CopyOnWriteArrayList

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import VarHandle
from java.lang.reflect import Field
from java.util import Arrays
from java.util import Comparator
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util import ListIterator
from java.util import NoSuchElementException
from java.util import Objects
from java.util import RandomAccess
from java.util import Spliterator
from java.util.concurrent import *
from java.util.function import Consumer
from java.util.function import Predicate
from java.util.function import UnaryOperator
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class CopyOnWriteArrayList(List, RandomAccess, Cloneable, Serializable):
    """
    A thread-safe variant of java.util.ArrayList in which all mutative
    operations (`add`, `set`, and so on) are implemented by
    making a fresh copy of the underlying array.
    
    This is ordinarily too costly, but may be *more* efficient
    than alternatives when traversal operations vastly outnumber
    mutations, and is useful when you cannot or don't want to
    synchronize traversals, yet need to preclude interference among
    concurrent threads.  The "snapshot" style iterator method uses a
    reference to the state of the array at the point that the iterator
    was created. This array never changes during the lifetime of the
    iterator, so interference is impossible and the iterator is
    guaranteed not to throw `ConcurrentModificationException`.
    The iterator will not reflect additions, removals, or changes to
    the list since the iterator was created.  Element-changing
    operations on iterators themselves (`remove`, `set`, and
    `add`) are not supported. These methods throw
    `UnsupportedOperationException`.
    
    All elements are permitted, including `null`.
    
    Memory consistency effects: As with other concurrent
    collections, actions in a thread prior to placing an object into a
    `CopyOnWriteArrayList`
    <a href="package-summary.html#MemoryVisibility">*happen-before*</a>
    actions subsequent to the access or removal of that element from
    the `CopyOnWriteArrayList` in another thread.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this list

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self):
        """
        Creates an empty list.
        """
        ...


    def __init__(self, c: Iterable["E"]):
        """
        Creates a list containing the elements of the specified
        collection, in the order they are returned by the collection's
        iterator.

        Arguments
        - c: the collection of initially held elements

        Raises
        - NullPointerException: if the specified collection is null
        """
        ...


    def __init__(self, toCopyIn: list["E"]):
        """
        Creates a list holding a copy of the given array.

        Arguments
        - toCopyIn: the array (a copy of this array is used as the
               internal array)

        Raises
        - NullPointerException: if the specified array is null
        """
        ...


    def size(self) -> int:
        """
        Returns the number of elements in this list.

        Returns
        - the number of elements in this list
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if this list contains no elements.

        Returns
        - `True` if this list contains no elements
        """
        ...


    def contains(self, o: "Object") -> bool:
        """
        Returns `True` if this list contains the specified element.
        More formally, returns `True` if and only if this list contains
        at least one element `e` such that `Objects.equals(o, e)`.

        Arguments
        - o: element whose presence in this list is to be tested

        Returns
        - `True` if this list contains the specified element
        """
        ...


    def indexOf(self, o: "Object") -> int:
        """

        """
        ...


    def indexOf(self, e: "E", index: int) -> int:
        """
        Returns the index of the first occurrence of the specified element in
        this list, searching forwards from `index`, or returns -1 if
        the element is not found.
        More formally, returns the lowest index `i` such that
        `i >= index && Objects.equals(get(i), e)`,
        or -1 if there is no such index.

        Arguments
        - e: element to search for
        - index: index to start searching from

        Returns
        - the index of the first occurrence of the element in
                this list at position `index` or later in the list;
                `-1` if the element is not found.

        Raises
        - IndexOutOfBoundsException: if the specified index is negative
        """
        ...


    def lastIndexOf(self, o: "Object") -> int:
        """

        """
        ...


    def lastIndexOf(self, e: "E", index: int) -> int:
        """
        Returns the index of the last occurrence of the specified element in
        this list, searching backwards from `index`, or returns -1 if
        the element is not found.
        More formally, returns the highest index `i` such that
        `i <= index && Objects.equals(get(i), e)`,
        or -1 if there is no such index.

        Arguments
        - e: element to search for
        - index: index to start searching backwards from

        Returns
        - the index of the last occurrence of the element at position
                less than or equal to `index` in this list;
                -1 if the element is not found.

        Raises
        - IndexOutOfBoundsException: if the specified index is greater
                than or equal to the current size of this list
        """
        ...


    def clone(self) -> "Object":
        """
        Returns a shallow copy of this list.  (The elements themselves
        are not copied.)

        Returns
        - a clone of this list
        """
        ...


    def toArray(self) -> list["Object"]:
        """
        Returns an array containing all of the elements in this list
        in proper sequence (from first to last element).
        
        The returned array will be "safe" in that no references to it are
        maintained by this list.  (In other words, this method must allocate
        a new array).  The caller is thus free to modify the returned array.
        
        This method acts as bridge between array-based and collection-based
        APIs.

        Returns
        - an array containing all the elements in this list
        """
        ...


    def toArray(self, a: list["T"]) -> list["T"]:
        """
        Returns an array containing all of the elements in this list in
        proper sequence (from first to last element); the runtime type of
        the returned array is that of the specified array.  If the list fits
        in the specified array, it is returned therein.  Otherwise, a new
        array is allocated with the runtime type of the specified array and
        the size of this list.
        
        If this list fits in the specified array with room to spare
        (i.e., the array has more elements than this list), the element in
        the array immediately following the end of the list is set to
        `null`.  (This is useful in determining the length of this
        list *only* if the caller knows that this list does not contain
        any null elements.)
        
        Like the .toArray() method, this method acts as bridge between
        array-based and collection-based APIs.  Further, this method allows
        precise control over the runtime type of the output array, and may,
        under certain circumstances, be used to save allocation costs.
        
        Suppose `x` is a list known to contain only strings.
        The following code can be used to dump the list into a newly
        allocated array of `String`:
        
        ``` `String[] y = x.toArray(new String[0]);````
        
        Note that `toArray(new Object[0])` is identical in function to
        `toArray()`.

        Arguments
        - a: the array into which the elements of the list are to
                 be stored, if it is big enough; otherwise, a new array of the
                 same runtime type is allocated for this purpose.

        Returns
        - an array containing all the elements in this list

        Raises
        - ArrayStoreException: if the runtime type of the specified array
                is not a supertype of the runtime type of every element in
                this list
        - NullPointerException: if the specified array is null
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
        Replaces the element at the specified position in this list with the
        specified element.

        Raises
        - IndexOutOfBoundsException: 
        """
        ...


    def add(self, e: "E") -> bool:
        """
        Appends the specified element to the end of this list.

        Arguments
        - e: element to be appended to this list

        Returns
        - `True` (as specified by Collection.add)
        """
        ...


    def add(self, index: int, element: "E") -> None:
        """
        Inserts the specified element at the specified position in this
        list. Shifts the element currently at that position (if any) and
        any subsequent elements to the right (adds one to their indices).

        Raises
        - IndexOutOfBoundsException: 
        """
        ...


    def remove(self, index: int) -> "E":
        """
        Removes the element at the specified position in this list.
        Shifts any subsequent elements to the left (subtracts one from their
        indices).  Returns the element that was removed from the list.

        Raises
        - IndexOutOfBoundsException: 
        """
        ...


    def remove(self, o: "Object") -> bool:
        """
        Removes the first occurrence of the specified element from this list,
        if it is present.  If this list does not contain the element, it is
        unchanged.  More formally, removes the element with the lowest index
        `i` such that `Objects.equals(o, get(i))`
        (if such an element exists).  Returns `True` if this list
        contained the specified element (or equivalently, if this list
        changed as a result of the call).

        Arguments
        - o: element to be removed from this list, if present

        Returns
        - `True` if this list contained the specified element
        """
        ...


    def addIfAbsent(self, e: "E") -> bool:
        """
        Appends the element, if not present.

        Arguments
        - e: element to be added to this list, if absent

        Returns
        - `True` if the element was added
        """
        ...


    def containsAll(self, c: Iterable[Any]) -> bool:
        """
        Returns `True` if this list contains all of the elements of the
        specified collection.

        Arguments
        - c: collection to be checked for containment in this list

        Returns
        - `True` if this list contains all of the elements of the
                specified collection

        Raises
        - NullPointerException: if the specified collection is null

        See
        - .contains(Object)
        """
        ...


    def removeAll(self, c: Iterable[Any]) -> bool:
        """
        Removes from this list all of its elements that are contained in
        the specified collection. This is a particularly expensive operation
        in this class because of the need for an internal temporary array.

        Arguments
        - c: collection containing elements to be removed from this list

        Returns
        - `True` if this list changed as a result of the call

        Raises
        - ClassCastException: if the class of an element of this list
                is incompatible with the specified collection
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if this list contains a null element and the
                specified collection does not permit null elements
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>),
                or if the specified collection is null

        See
        - .remove(Object)
        """
        ...


    def retainAll(self, c: Iterable[Any]) -> bool:
        """
        Retains only the elements in this list that are contained in the
        specified collection.  In other words, removes from this list all of
        its elements that are not contained in the specified collection.

        Arguments
        - c: collection containing elements to be retained in this list

        Returns
        - `True` if this list changed as a result of the call

        Raises
        - ClassCastException: if the class of an element of this list
                is incompatible with the specified collection
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if this list contains a null element and the
                specified collection does not permit null elements
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>),
                or if the specified collection is null

        See
        - .remove(Object)
        """
        ...


    def addAllAbsent(self, c: Iterable["E"]) -> int:
        """
        Appends all of the elements in the specified collection that
        are not already contained in this list, to the end of
        this list, in the order that they are returned by the
        specified collection's iterator.

        Arguments
        - c: collection containing elements to be added to this list

        Returns
        - the number of elements added

        Raises
        - NullPointerException: if the specified collection is null

        See
        - .addIfAbsent(Object)
        """
        ...


    def clear(self) -> None:
        """
        Removes all of the elements from this list.
        The list will be empty after this call returns.
        """
        ...


    def addAll(self, c: Iterable["E"]) -> bool:
        """
        Appends all of the elements in the specified collection to the end
        of this list, in the order that they are returned by the specified
        collection's iterator.

        Arguments
        - c: collection containing elements to be added to this list

        Returns
        - `True` if this list changed as a result of the call

        Raises
        - NullPointerException: if the specified collection is null

        See
        - .add(Object)
        """
        ...


    def addAll(self, index: int, c: Iterable["E"]) -> bool:
        """
        Inserts all of the elements in the specified collection into this
        list, starting at the specified position.  Shifts the element
        currently at that position (if any) and any subsequent elements to
        the right (increases their indices).  The new elements will appear
        in this list in the order that they are returned by the
        specified collection's iterator.

        Arguments
        - index: index at which to insert the first element
               from the specified collection
        - c: collection containing elements to be added to this list

        Returns
        - `True` if this list changed as a result of the call

        Raises
        - IndexOutOfBoundsException: 
        - NullPointerException: if the specified collection is null

        See
        - .add(int,Object)
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


    def replaceAll(self, operator: "UnaryOperator"["E"]) -> None:
        ...


    def sort(self, c: "Comparator"["E"]) -> None:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this list.  The string
        representation consists of the string representations of the list's
        elements in the order they are returned by its iterator, enclosed in
        square brackets (`"[]"`).  Adjacent elements are separated by
        the characters `", "` (comma and space).  Elements are
        converted to strings as by String.valueOf(Object).

        Returns
        - a string representation of this list
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Compares the specified object with this list for equality.
        Returns `True` if the specified object is the same object
        as this object, or if it is also a List and the sequence
        of elements returned by an List.iterator() iterator
        over the specified list is the same as the sequence returned by
        an iterator over this list.  The two sequences are considered to
        be the same if they have the same length and corresponding
        elements at the same position in the sequence are *equal*.
        Two elements `e1` and `e2` are considered
        *equal* if `Objects.equals(e1, e2)`.

        Arguments
        - o: the object to be compared for equality with this list

        Returns
        - `True` if the specified object is equal to this list
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this list.
        
        This implementation uses the definition in List.hashCode.

        Returns
        - the hash code value for this list
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this list in proper sequence.
        
        The returned iterator provides a snapshot of the state of the list
        when the iterator was constructed. No synchronization is needed while
        traversing the iterator. The iterator does *NOT* support the
        `remove` method.

        Returns
        - an iterator over the elements in this list in proper sequence
        """
        ...


    def listIterator(self) -> "ListIterator"["E"]:
        """
        
        
        The returned iterator provides a snapshot of the state of the list
        when the iterator was constructed. No synchronization is needed while
        traversing the iterator. The iterator does *NOT* support the
        `remove`, `set` or `add` methods.
        """
        ...


    def listIterator(self, index: int) -> "ListIterator"["E"]:
        """
        
        
        The returned iterator provides a snapshot of the state of the list
        when the iterator was constructed. No synchronization is needed while
        traversing the iterator. The iterator does *NOT* support the
        `remove`, `set` or `add` methods.

        Raises
        - IndexOutOfBoundsException: 
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Returns a Spliterator over the elements in this list.
        
        The `Spliterator` reports Spliterator.IMMUTABLE,
        Spliterator.ORDERED, Spliterator.SIZED, and
        Spliterator.SUBSIZED.
        
        The spliterator provides a snapshot of the state of the list
        when the spliterator was constructed. No synchronization is needed while
        operating on the spliterator.

        Returns
        - a `Spliterator` over the elements in this list

        Since
        - 1.8
        """
        ...


    def subList(self, fromIndex: int, toIndex: int) -> list["E"]:
        """
        Returns a view of the portion of this list between
        `fromIndex`, inclusive, and `toIndex`, exclusive.
        The returned list is backed by this list, so changes in the
        returned list are reflected in this list.
        
        The semantics of the list returned by this method become
        undefined if the backing list (i.e., this list) is modified in
        any way other than via the returned list.

        Arguments
        - fromIndex: low endpoint (inclusive) of the subList
        - toIndex: high endpoint (exclusive) of the subList

        Returns
        - a view of the specified range within this list

        Raises
        - IndexOutOfBoundsException: 
        """
        ...
