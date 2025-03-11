"""
Python module generated from Java source file com.google.common.collect.AbstractSequentialIterator

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import NoSuchElementException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class AbstractSequentialIterator(UnmodifiableIterator):
    """
    This class provides a skeletal implementation of the `Iterator` interface for sequences
    whose next element can always be derived from the previous element. Null elements are not
    supported, nor is the .remove() method.
    
    Example:
    
    ````Iterator<Integer> powersOfTwo =
        new AbstractSequentialIterator<Integer>(1) {
          protected Integer computeNext(Integer previous) {
            return (previous == 1 << 30) ? null : previous * 2;`
        };
    }```

    Author(s)
    - Chris Povirk

    Since
    - 12.0 (in Guava as `AbstractLinkedIterator` since 8.0)
    """

    def hasNext(self) -> bool:
        ...


    def next(self) -> "T":
        ...
