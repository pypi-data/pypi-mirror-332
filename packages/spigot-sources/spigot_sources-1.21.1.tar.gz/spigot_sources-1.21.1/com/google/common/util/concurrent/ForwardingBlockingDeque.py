"""
Python module generated from Java source file com.google.common.util.concurrent.ForwardingBlockingDeque

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.collect import ForwardingDeque
from com.google.common.util.concurrent import *
from java.util.concurrent import BlockingDeque
from java.util.concurrent import TimeUnit
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ForwardingBlockingDeque(ForwardingDeque, BlockingDeque):
    """
    A BlockingDeque which forwards all its method calls to another `BlockingDeque`.
    Subclasses should override one or more methods to modify the behavior of the backing deque as
    desired per the <a href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingBlockingDeque` forward **indiscriminately**
    to the methods of the delegate. For example, overriding .add alone **will not** change
    the behaviour of .offer which can lead to unexpected behaviour. In this case, you should
    override `offer` as well, either providing your own implementation, or delegating to the
    provided `standardOffer` method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingBlockingDeque`.
    
    The `standard` methods are not guaranteed to be thread-safe, even when all of the
    methods that they depend on are thread-safe.

    Author(s)
    - Emily Soldal

    Since
    - 21.0 (since 14.0 as com.google.common.collect.ForwardingBlockingDeque)
    """

    def remainingCapacity(self) -> int:
        ...


    def putFirst(self, e: "E") -> None:
        ...


    def putLast(self, e: "E") -> None:
        ...


    def offerFirst(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        ...


    def offerLast(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        ...


    def takeFirst(self) -> "E":
        ...


    def takeLast(self) -> "E":
        ...


    def pollFirst(self, timeout: int, unit: "TimeUnit") -> "E":
        ...


    def pollLast(self, timeout: int, unit: "TimeUnit") -> "E":
        ...


    def put(self, e: "E") -> None:
        ...


    def offer(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        ...


    def take(self) -> "E":
        ...


    def poll(self, timeout: int, unit: "TimeUnit") -> "E":
        ...


    def drainTo(self, c: Iterable["E"]) -> int:
        ...


    def drainTo(self, c: Iterable["E"], maxElements: int) -> int:
        ...
