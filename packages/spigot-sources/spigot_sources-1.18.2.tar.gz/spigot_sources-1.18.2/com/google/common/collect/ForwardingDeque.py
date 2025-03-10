"""
Python module generated from Java source file com.google.common.collect.ForwardingDeque

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Deque
from java.util import Iterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingDeque(ForwardingQueue, Deque):
    """
    A deque which forwards all its method calls to another deque. Subclasses should override one or
    more methods to modify the behavior of the backing deque as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingDeque` forward **indiscriminately** to the
    methods of the delegate. For example, overriding .add alone **will not** change the
    behavior of .offer which can lead to unexpected behavior. In this case, you should
    override `offer` as well.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingDeque`.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 12.0
    """

    def addFirst(self, e: "E") -> None:
        ...


    def addLast(self, e: "E") -> None:
        ...


    def descendingIterator(self) -> Iterator["E"]:
        ...


    def getFirst(self) -> "E":
        ...


    def getLast(self) -> "E":
        ...


    def offerFirst(self, e: "E") -> bool:
        ...


    def offerLast(self, e: "E") -> bool:
        ...


    def peekFirst(self) -> "E":
        ...


    def peekLast(self) -> "E":
        ...


    def pollFirst(self) -> "E":
        ...


    def pollLast(self) -> "E":
        ...


    def pop(self) -> "E":
        ...


    def push(self, e: "E") -> None:
        ...


    def removeFirst(self) -> "E":
        ...


    def removeLast(self) -> "E":
        ...


    def removeFirstOccurrence(self, o: "Object") -> bool:
        ...


    def removeLastOccurrence(self, o: "Object") -> bool:
        ...
