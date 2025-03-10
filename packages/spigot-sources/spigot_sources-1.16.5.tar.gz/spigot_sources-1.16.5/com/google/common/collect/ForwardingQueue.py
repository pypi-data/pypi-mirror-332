"""
Python module generated from Java source file com.google.common.collect.ForwardingQueue

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import NoSuchElementException
from java.util import Queue
from typing import Any, Callable, Iterable, Tuple


class ForwardingQueue(ForwardingCollection, Queue):
    """
    A queue which forwards all its method calls to another queue. Subclasses
    should override one or more methods to modify the behavior of the backing
    queue as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingQueue` forward
    **indiscriminately** to the methods of the delegate. For example,
    overriding .add alone **will not** change the behavior of .offer which can lead to unexpected behavior. In this case, you should
    override `offer` as well, either providing your own implementation, or
    delegating to the provided `standardOffer` method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingQueue`.
    
    The `standard` methods are not guaranteed to be thread-safe, even
    when all of the methods that they depend on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    def offer(self, o: "E") -> bool:
        ...


    def poll(self) -> "E":
        ...


    def remove(self) -> "E":
        ...


    def peek(self) -> "E":
        ...


    def element(self) -> "E":
        ...
