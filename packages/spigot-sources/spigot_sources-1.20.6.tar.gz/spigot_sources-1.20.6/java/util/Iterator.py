"""
Python module generated from Java source file java.util.Iterator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from java.util.function import Consumer
from typing import Any, Callable, Iterable, Tuple


class Iterator:
    """
    An iterator over a collection.  `Iterator` takes the place of
    Enumeration in the Java Collections Framework.  Iterators
    differ from enumerations in two ways:
    
    
         -  Iterators allow the caller to remove elements from the
              underlying collection during the iteration with well-defined
              semantics.
         -  Method names have been improved.
    
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements returned by this iterator

    Author(s)
    - Josh Bloch

    See
    - Iterable

    Since
    - 1.2

    Unknown Tags
    - An Enumeration can be converted into an `Iterator` by
    using the Enumeration.asIterator method.
    """

    def hasNext(self) -> bool:
        """
        Returns `True` if the iteration has more elements.
        (In other words, returns `True` if .next would
        return an element rather than throwing an exception.)

        Returns
        - `True` if the iteration has more elements
        """
        ...


    def next(self) -> "E":
        """
        Returns the next element in the iteration.

        Returns
        - the next element in the iteration

        Raises
        - NoSuchElementException: if the iteration has no more elements
        """
        ...


    def remove(self) -> None:
        """
        Removes from the underlying collection the last element returned
        by this iterator (optional operation).  This method can be called
        only once per call to .next.
        
        The behavior of an iterator is unspecified if the underlying collection
        is modified while the iteration is in progress in any way other than by
        calling this method, unless an overriding class has specified a
        concurrent modification policy.
        
        The behavior of an iterator is unspecified if this method is called
        after a call to the .forEachRemaining forEachRemaining method.

        Raises
        - UnsupportedOperationException: if the `remove`
                operation is not supported by this iterator
        - IllegalStateException: if the `next` method has not
                yet been called, or the `remove` method has already
                been called after the last call to the `next`
                method

        Unknown Tags
        - The default implementation throws an instance of
        UnsupportedOperationException and performs no other action.
        """
        ...


    def forEachRemaining(self, action: "Consumer"["E"]) -> None:
        """
        Performs the given action for each remaining element until all elements
        have been processed or the action throws an exception.  Actions are
        performed in the order of iteration, if that order is specified.
        Exceptions thrown by the action are relayed to the caller.
        
        The behavior of an iterator is unspecified if the action modifies the
        collection in any way (even by calling the .remove remove method
        or other mutator methods of `Iterator` subtypes),
        unless an overriding class has specified a concurrent modification policy.
        
        Subsequent behavior of an iterator is unspecified if the action throws an
        exception.

        Arguments
        - action: The action to be performed for each element

        Raises
        - NullPointerException: if the specified action is null

        Since
        - 1.8

        Unknown Tags
        - The default implementation behaves as if:
        ````while (hasNext())
                action.accept(next());````
        """
        ...
