"""
Python module generated from Java source file com.google.common.collect.PeekingIterator

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotMock
from java.util import Iterator
from java.util import NoSuchElementException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class PeekingIterator(Iterator):
    """
    An iterator that supports a one-element lookahead while iterating.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/CollectionHelpersExplained#peekingiterator">`PeekingIterator`</a>.

    Author(s)
    - Mick Killianey

    Since
    - 2.0
    """

    def peek(self) -> "E":
        """
        Returns the next element in the iteration, without advancing the iteration.
        
        Calls to `peek()` should not change the state of the iteration, except that it
        *may* prevent removal of the most recent element via .remove().

        Raises
        - NoSuchElementException: if the iteration has no more elements according to .hasNext()
        """
        ...


    def next(self) -> "E":
        """
        
        
        The objects returned by consecutive calls to .peek() then .next() are
        guaranteed to be equal to each other.
        """
        ...


    def remove(self) -> None:
        """
        
        
        Implementations may or may not support removal when a call to .peek() has occurred
        since the most recent call to .next().

        Raises
        - IllegalStateException: if there has been a call to .peek() since the most recent
            call to .next() and this implementation does not support this sequence of calls
            (optional)
        """
        ...
