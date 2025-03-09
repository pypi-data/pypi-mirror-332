"""
Python module generated from Java source file com.google.common.collect.AbstractIndexedListIterator

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import ListIterator
from java.util import NoSuchElementException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractIndexedListIterator(UnmodifiableListIterator):
    """
    This class provides a skeletal implementation of the ListIterator interface across a
    fixed number of elements that may be retrieved by position. It does not support .remove,
    .set, or .add.

    Author(s)
    - Jared Levy
    """

    def hasNext(self) -> bool:
        ...


    def next(self) -> "E":
        ...


    def nextIndex(self) -> int:
        ...


    def hasPrevious(self) -> bool:
        ...


    def previous(self) -> "E":
        ...


    def previousIndex(self) -> int:
        ...
