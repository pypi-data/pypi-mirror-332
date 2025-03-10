"""
Python module generated from Java source file com.google.common.collect.UnmodifiableIterator

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotCall
from java.util import Iterator
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class UnmodifiableIterator(Iterator):
    """
    An iterator that does not support .remove.
    
    `UnmodifiableIterator` is used primarily in conjunction with implementations of ImmutableCollection, such as ImmutableList. You can, however, convert an existing
    iterator to an `UnmodifiableIterator` using Iterators.unmodifiableIterator.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    def remove(self) -> None:
        """
        Guaranteed to throw an exception and leave the underlying data unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...
