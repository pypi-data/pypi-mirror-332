"""
Python module generated from Java source file com.google.common.collect.MultitransformedIterator

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import Iterator
from java.util import NoSuchElementException
from typing import Any, Callable, Iterable, Tuple


class MultitransformedIterator(Iterator):
    """
    Similar to TransformedIterator, this iterator transforms a backing iterator.
    However, rather than enforcing a one-to-one mapping, each element in the backing iterator
    can be transformed into an arbitrary number of elements (i.e. a one-to-many mapping).

    Author(s)
    - James Sexton
    """

    def hasNext(self) -> bool:
        ...


    def next(self) -> "T":
        ...


    def remove(self) -> None:
        ...
