"""
Python module generated from Java source file com.google.common.base.AbstractIterator

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Iterator
from java.util import NoSuchElementException
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractIterator(Iterator):
    """
    Note this class is a copy of com.google.common.collect.AbstractIterator (for dependency
    reasons).
    """

    def hasNext(self) -> bool:
        ...


    def next(self) -> "T":
        ...


    def remove(self) -> None:
        ...
