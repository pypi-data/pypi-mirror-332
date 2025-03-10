"""
Python module generated from Java source file com.google.common.collect.TransformedIterator

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import Iterator
from typing import Any, Callable, Iterable, Tuple


class TransformedIterator(Iterator):
    """
    An iterator that transforms a backing iterator; for internal use. This avoids
    the object overhead of constructing a Function for internal methods.

    Author(s)
    - Louis Wasserman
    """

    def hasNext(self) -> bool:
        ...


    def next(self) -> "T":
        ...


    def remove(self) -> None:
        ...
