"""
Python module generated from Java source file java.util.ListIterator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class ListIterator(Iterator):
    """
    An iterator for lists that allows the programmer
    to traverse the list in either direction, modify
    the list during iteration, and obtain the iterator's
    current position in the list. A `ListIterator`
    has no current element; its <I>cursor position</I> always
    lies between the element that would be returned by a call
    to `previous()` and the element that would be
    returned by a call to `next()`.
    An iterator for a list of length `n` has `n+1` possible
    cursor positions, as illustrated by the carets (`^`) below:
    <PRE>
                         Element(0)   Element(1)   Element(2)   ... Element(n-1)
    cursor positions:  ^            ^            ^            ^                  ^
    </PRE>
    Note that the .remove and .set(Object) methods are
    *not* defined in terms of the cursor position;  they are defined to
    operate on the last element returned by a call to .next or
    .previous().
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.

    Author(s)
    - Josh Bloch

    See
    - List.listIterator()

    Since
    - 1.2
    """

    def hasNext(self) -> bool:
        """
        Returns `True` if this list iterator has more elements when
        traversing the list in the forward direction. (In other words,
        returns `True` if .next would return an element rather
        than throwing an exception.)

        Returns
        - `True` if the list iterator has more elements when
                traversing the list in the forward direction
        """
        ...


    def next(self) -> "E":
        """
        Returns the next element in the list and advances the cursor position.
        This method may be called repeatedly to iterate through the list,
        or intermixed with calls to .previous to go back and forth.
        (Note that alternating calls to `next` and `previous`
        will return the same element repeatedly.)

        Returns
        - the next element in the list

        Raises
        - NoSuchElementException: if the iteration has no next element
        """
        ...


    def hasPrevious(self) -> bool:
        """
        Returns `True` if this list iterator has more elements when
        traversing the list in the reverse direction.  (In other words,
        returns `True` if .previous would return an element
        rather than throwing an exception.)

        Returns
        - `True` if the list iterator has more elements when
                traversing the list in the reverse direction
        """
        ...


    def previous(self) -> "E":
        """
        Returns the previous element in the list and moves the cursor
        position backwards.  This method may be called repeatedly to
        iterate through the list backwards, or intermixed with calls to
        .next to go back and forth.  (Note that alternating calls
        to `next` and `previous` will return the same
        element repeatedly.)

        Returns
        - the previous element in the list

        Raises
        - NoSuchElementException: if the iteration has no previous
                element
        """
        ...


    def nextIndex(self) -> int:
        """
        Returns the index of the element that would be returned by a
        subsequent call to .next. (Returns list size if the list
        iterator is at the end of the list.)

        Returns
        - the index of the element that would be returned by a
                subsequent call to `next`, or list size if the list
                iterator is at the end of the list
        """
        ...


    def previousIndex(self) -> int:
        """
        Returns the index of the element that would be returned by a
        subsequent call to .previous. (Returns -1 if the list
        iterator is at the beginning of the list.)

        Returns
        - the index of the element that would be returned by a
                subsequent call to `previous`, or -1 if the list
                iterator is at the beginning of the list
        """
        ...


    def remove(self) -> None:
        """
        Removes from the list the last element that was returned by .next or .previous (optional operation).  This call can
        only be made once per call to `next` or `previous`.
        It can be made only if .add has not been
        called after the last call to `next` or `previous`.

        Raises
        - UnsupportedOperationException: if the `remove`
                operation is not supported by this list iterator
        - IllegalStateException: if neither `next` nor
                `previous` have been called, or `remove` or
                `add` have been called after the last call to
                `next` or `previous`
        """
        ...


    def set(self, e: "E") -> None:
        """
        Replaces the last element returned by .next or
        .previous with the specified element (optional operation).
        This call can be made only if neither .remove nor .add have been called after the last call to `next` or
        `previous`.

        Arguments
        - e: the element with which to replace the last element returned by
                 `next` or `previous`

        Raises
        - UnsupportedOperationException: if the `set` operation
                is not supported by this list iterator
        - ClassCastException: if the class of the specified element
                prevents it from being added to this list
        - IllegalArgumentException: if some aspect of the specified
                element prevents it from being added to this list
        - IllegalStateException: if neither `next` nor
                `previous` have been called, or `remove` or
                `add` have been called after the last call to
                `next` or `previous`
        """
        ...


    def add(self, e: "E") -> None:
        """
        Inserts the specified element into the list (optional operation).
        The element is inserted immediately before the element that
        would be returned by .next, if any, and after the element
        that would be returned by .previous, if any.  (If the
        list contains no elements, the new element becomes the sole element
        on the list.)  The new element is inserted before the implicit
        cursor: a subsequent call to `next` would be unaffected, and a
        subsequent call to `previous` would return the new element.
        (This call increases by one the value that would be returned by a
        call to `nextIndex` or `previousIndex`.)

        Arguments
        - e: the element to insert

        Raises
        - UnsupportedOperationException: if the `add` method is
                not supported by this list iterator
        - ClassCastException: if the class of the specified element
                prevents it from being added to this list
        - IllegalArgumentException: if some aspect of this element
                prevents it from being added to this list
        """
        ...
