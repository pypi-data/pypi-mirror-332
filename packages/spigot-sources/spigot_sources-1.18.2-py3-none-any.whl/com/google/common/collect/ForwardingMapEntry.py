"""
Python module generated from Java source file com.google.common.collect.ForwardingMapEntry

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Objects
from com.google.common.collect import *
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ForwardingMapEntry(ForwardingObject, Entry):
    """
    A map entry which forwards all its method calls to another map entry. Subclasses should override
    one or more methods to modify the behavior of the backing map entry as desired per the <a
    href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.
    
    **Warning:** The methods of `ForwardingMapEntry` forward *indiscriminately* to
    the methods of the delegate. For example, overriding .getValue alone *will not*
    change the behavior of .equals, which can lead to unexpected behavior. In this case, you
    should override `equals` as well, either providing your own implementation, or delegating
    to the provided `standardEquals` method.
    
    Each of the `standard` methods, where appropriate, use Objects.equal to test
    equality for both keys and values. This may not be the desired behavior for map implementations
    that use non-standard notions of key equality, such as the entry of a `SortedMap` whose
    comparator is not consistent with `equals`.
    
    The `standard` methods are not guaranteed to be thread-safe, even when all of the
    methods that they depend on are thread-safe.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    def getKey(self) -> "K":
        ...


    def getValue(self) -> "V":
        ...


    def setValue(self, value: "V") -> "V":
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
