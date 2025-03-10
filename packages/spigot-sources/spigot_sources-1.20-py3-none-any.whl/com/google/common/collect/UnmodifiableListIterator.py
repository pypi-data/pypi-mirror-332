"""
Python module generated from Java source file com.google.common.collect.UnmodifiableListIterator

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotCall
from java.util import ListIterator
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class UnmodifiableListIterator(UnmodifiableIterator, ListIterator):
    """
    A list iterator that does not support .remove, .add, or .set.

    Author(s)
    - Louis Wasserman

    Since
    - 7.0
    """

    def add(self, e: "E") -> None:
        """
        Guaranteed to throw an exception and leave the underlying data unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def set(self, e: "E") -> None:
        """
        Guaranteed to throw an exception and leave the underlying data unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...
