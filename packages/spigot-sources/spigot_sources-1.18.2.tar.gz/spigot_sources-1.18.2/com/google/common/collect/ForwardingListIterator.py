"""
Python module generated from Java source file com.google.common.collect.ForwardingListIterator

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import ListIterator
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingListIterator(ForwardingIterator, ListIterator):
    """
    A list iterator which forwards all its method calls to another list iterator. Subclasses should
    override one or more methods to modify the behavior of the backing iterator as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **`default` method warning:** This class forwards calls to *only some* `default` methods. Specifically, it forwards calls only for methods that existed <a
    href="https://docs.oracle.com/javase/7/docs/api/java/util/ListIterator.html">before `default` methods were introduced</a>. For newer methods, like `forEachRemaining`, it
    inherits their default implementations. When those implementations invoke methods, they invoke
    methods on the `ForwardingListIterator`.

    Author(s)
    - Mike Bostock

    Since
    - 2.0
    """

    def add(self, element: "E") -> None:
        ...


    def hasPrevious(self) -> bool:
        ...


    def nextIndex(self) -> int:
        ...


    def previous(self) -> "E":
        ...


    def previousIndex(self) -> int:
        ...


    def set(self, element: "E") -> None:
        ...
