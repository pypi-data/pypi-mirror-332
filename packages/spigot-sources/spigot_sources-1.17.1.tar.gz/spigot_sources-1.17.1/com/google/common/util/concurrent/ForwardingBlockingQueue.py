"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingBlockingQueue

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import ForwardingQueue
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import BlockingQueue
from java.util.concurrent import TimeUnit
from typing import Any, Callable, Iterable, Tuple


class ForwardingBlockingQueue(ForwardingQueue, BlockingQueue):
    """
    A BlockingQueue which forwards all its method calls to another BlockingQueue.
    Subclasses should override one or more methods to modify the behavior of the backing collection
    as desired per the <a href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator
    pattern</a>.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingBlockingQueue`.
    
    Type `<E>`: the type of elements held in this collection

    Author(s)
    - Raimundo Mirisola

    Since
    - 4.0
    """

    def drainTo(self, c: Iterable["E"], maxElements: int) -> int:
        ...


    def drainTo(self, c: Iterable["E"]) -> int:
        ...


    def offer(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        ...


    def poll(self, timeout: int, unit: "TimeUnit") -> "E":
        ...


    def put(self, e: "E") -> None:
        ...


    def remainingCapacity(self) -> int:
        ...


    def take(self) -> "E":
        ...
