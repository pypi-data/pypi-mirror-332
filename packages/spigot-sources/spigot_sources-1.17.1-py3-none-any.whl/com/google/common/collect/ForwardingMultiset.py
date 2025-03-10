"""
Python module generated from Java source file com.google.common.collect.ForwardingMultiset

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Objects
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Iterator
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingMultiset(ForwardingCollection, Multiset):
    """
    A multiset which forwards all its method calls to another multiset.
    Subclasses should override one or more methods to modify the behavior of the
    backing multiset as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingMultiset` forward
    **indiscriminately** to the methods of the delegate. For example,
    overriding .add(Object, int) alone **will not** change the
    behavior of .add(Object), which can lead to unexpected behavior. In
    this case, you should override `add(Object)` as well, either providing
    your own implementation, or delegating to the provided `standardAdd`
    method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingMultiset`.
    
    The `standard` methods and any collection views they return are not
    guaranteed to be thread-safe, even when all of the methods that they depend
    on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    def count(self, element: "Object") -> int:
        ...


    def add(self, element: "E", occurrences: int) -> int:
        ...


    def remove(self, element: "Object", occurrences: int) -> int:
        ...


    def elementSet(self) -> set["E"]:
        ...


    def entrySet(self) -> set["Entry"["E"]]:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def setCount(self, element: "E", count: int) -> int:
        ...


    def setCount(self, element: "E", oldCount: int, newCount: int) -> bool:
        ...
