"""
Python module generated from Java source file com.google.common.collect.AbstractIterator

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import NoSuchElementException
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractIterator(UnmodifiableIterator):

    def hasNext(self) -> bool:
        ...


    def next(self) -> "T":
        ...


    def peek(self) -> "T":
        """
        Returns the next element in the iteration without advancing the iteration, according to the
        contract of PeekingIterator.peek().
        
        Implementations of `AbstractIterator` that wish to expose this functionality should
        implement `PeekingIterator`.
        """
        ...
