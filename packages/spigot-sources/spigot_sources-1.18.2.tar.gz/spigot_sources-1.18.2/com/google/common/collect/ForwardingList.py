"""
Python module generated from Java source file com.google.common.collect.ForwardingList

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Iterator
from java.util import ListIterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingList(ForwardingCollection, List):
    """
    A list which forwards all its method calls to another list. Subclasses should override one or
    more methods to modify the behavior of the backing list as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    This class does not implement java.util.RandomAccess. If the delegate supports random
    access, the `ForwardingList` subclass should implement the `RandomAccess` interface.
    
    **Warning:** The methods of `ForwardingList` forward **indiscriminately** to the
    methods of the delegate. For example, overriding .add alone **will not** change the
    behavior of .addAll, which can lead to unexpected behavior. In this case, you should
    override `addAll` as well, either providing your own implementation, or delegating to the
    provided `standardAddAll` method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingList`.
    
    The `standard` methods and any collection views they return are not guaranteed to be
    thread-safe, even when all of the methods that they depend on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    def add(self, index: int, element: "E") -> None:
        ...


    def addAll(self, index: int, elements: Iterable["E"]) -> bool:
        ...


    def get(self, index: int) -> "E":
        ...


    def indexOf(self, element: "Object") -> int:
        ...


    def lastIndexOf(self, element: "Object") -> int:
        ...


    def listIterator(self) -> "ListIterator"["E"]:
        ...


    def listIterator(self, index: int) -> "ListIterator"["E"]:
        ...


    def remove(self, index: int) -> "E":
        ...


    def set(self, index: int, element: "E") -> "E":
        ...


    def subList(self, fromIndex: int, toIndex: int) -> list["E"]:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
