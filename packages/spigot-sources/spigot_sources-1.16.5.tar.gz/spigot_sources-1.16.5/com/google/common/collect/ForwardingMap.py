"""
Python module generated from Java source file com.google.common.collect.ForwardingMap

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


class ForwardingMap(ForwardingObject, Map):
    """
    A map which forwards all its method calls to another map. Subclasses should
    override one or more methods to modify the behavior of the backing map as
    desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingMap` forward
    *indiscriminately* to the methods of the delegate. For example,
    overriding .put alone *will not* change the behavior of .putAll, which can lead to unexpected behavior. In this case, you should
    override `putAll` as well, either providing your own implementation, or
    delegating to the provided `standardPutAll` method.
    
    **`default` method warning:** This class does *not* forward calls to `default` methods. Instead, it inherits their default implementations. When those implementations
    invoke methods, they invoke methods on the `ForwardingMap`.
    
    Each of the `standard` methods, where appropriate, use Objects.equal to test equality for both keys and values. This may not be
    the desired behavior for map implementations that use non-standard notions of
    key equality, such as a `SortedMap` whose comparator is not consistent
    with `equals`.
    
    The `standard` methods and the collection views they return are not
    guaranteed to be thread-safe, even when all of the methods that they depend
    on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    def size(self) -> int:
        ...


    def isEmpty(self) -> bool:
        ...


    def remove(self, object: "Object") -> "V":
        ...


    def clear(self) -> None:
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def containsValue(self, value: "Object") -> bool:
        ...


    def get(self, key: "Object") -> "V":
        ...


    def put(self, key: "K", value: "V") -> "V":
        ...


    def putAll(self, map: dict["K", "V"]) -> None:
        ...


    def keySet(self) -> set["K"]:
        ...


    def values(self) -> Iterable["V"]:
        ...


    def entrySet(self) -> set["Entry"["K", "V"]]:
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
